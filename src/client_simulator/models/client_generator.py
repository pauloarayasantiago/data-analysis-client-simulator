"""
Client Generator Module

This module handles the generation of client profiles and business problems.
"""

from ..utils.logger import DocumentationLogger
from .gemini_config import initialize_model, get_model_config
import google.generativeai as genai
import time
from typing import Optional, Tuple

class ClientGenerator:
    """Handles the generation of client profiles and business problems."""
    
    def __init__(self):
        """Initialize the client generator with the Gemini model."""
        self.model = initialize_model()
        self.max_retries = 3
        self.timeout = 30  # seconds
        self.scenario_prompt = """
    You are acting as a client representative directly addressing a team of data analysts in a business meeting. Speak in the first person ("I", "we", "us") *as the client representative*. Your goal is to present your company's data analysis project to the team, clearly and engagingly, as if you are in a real meeting.

    Present the scenario from *your* (the client representative's) perspective, explaining *your company's* challenges and needs.

    1. Start by introducing *your company* and yourself, describing your industry, size, and business type.
    2. Clearly explain *your company's* business problem and its impact.
    3. Describe the data sources *your company* can provide for analysis.
    4. Define what *you* need the data analysts to do and your expected outcomes.
    5. End with a brief closing statement.

    Use first-person pronouns consistently and maintain a professional tone. Make the scenario realistic but concise.
    """

        self.csv_prompt = """
    You are an expert in creating realistic synthetic datasets for data analysis practice. Your task is to generate a CSV dataset that directly corresponds to the data described in the scenario provided below.

    **Scenario Context:**
    {scenario}

    **Dataset Generation Goal:**
    Create a CSV dataset that is realistic, relevant, and useful for a data analyst to perform the tasks outlined in the "Analyst Task" section of the scenario and address the "Business Problem."

    **Specific Instructions for Dataset Generation:**

    1. **Identify Key Data Entities and Attributes:** Based on the "Data Provided" section of the scenario, identify the key entities (e.g., customers, products, transactions, website visits) and their attributes (characteristics or properties).  Think about what tables and columns would logically represent the data described.

    2. **Define CSV Columns (Schema Design):** Design a CSV schema (set of columns) that effectively represents the data entities and attributes identified in step 1.
        * **Column Names:** Choose clear, descriptive column names. Use snake_case (e.g., `customer_id`, `order_date`, `product_name`).
        * **Data Types:** Determine the appropriate data type for each column (e.g., integer, float, string, date, category).  Be realistic about the data types you would expect for each attribute.
        * **Column Descriptions:** For each column, briefly explain what it represents and its data type. This will help in understanding the dataset.

    3. **Generate Realistic Synthetic Data:** Populate the CSV dataset with synthetic data.
        * **Realism:**  The data should be plausible and reflect the real-world scenario described. Consider realistic ranges, distributions, and relationships between columns.
        * **Diversity:** Ensure variety in the data to make it interesting for analysis.
        * **Data Volume:** Generate a dataset with a reasonable number of rows (e.g., aim for around 50-200 rows for a practice dataset).
        * **Include Data Quality Issues:**  Real-world datasets are messy. Intentionally introduce some common data quality issues to make the dataset more realistic and challenging for analysis. Include:
            * **Missing Values (NaN or empty strings):**  Introduce missing values in some columns randomly.
            * **Outliers:**  Include a few outlier values that are significantly different from the typical range.
            * **Inconsistent Formatting:**  Vary the formatting in columns where it's plausible (e.g., dates in different formats, inconsistent capitalization in text fields, extra spaces).
            * **Inaccurate or Noisy Data (Optional):** If appropriate for the scenario, you can introduce some slightly inaccurate or noisy data points.

    4. **CSV Format Output:** Output the generated dataset strictly in CSV (Comma Separated Values) format.
        * **Header Row:** The first line MUST be the header row containing the column names, separated by commas.
        * **Data Rows:** Each subsequent line MUST be a data row, with values for each column separated by commas.
        * **Text Fields:** Enclose text fields that might contain commas or special characters in double quotes (").
        * **No Extra Lines or Text:**  The output should ONLY contain the CSV data. No introductory text, explanations, or code blocks before or after the CSV data itself.

    Your output should be ONLY the CSV data, starting with the header row and followed by the data rows, in valid CSV format. Do not include any explanations or descriptions *within* the output, just the raw CSV data.
    """

    def generate(self, logger: DocumentationLogger) -> Tuple[Optional[str], Optional[str]]:
        """
        Generate a new client profile and corresponding CSV dataset.
        
        Args:
            logger: DocumentationLogger instance for logging the generation process.
            
        Returns:
            Tuple[Optional[str], Optional[str]]: The generated client profile and CSV data, or None if generation fails.
        """
        attempt = 0
        while attempt < self.max_retries:
            try:
                logger.log_documentation(f"Attempt {attempt + 1}: Generating client and problem")
                
                # Use consistent generation parameters from config
                generation_config = genai.types.GenerationConfig(**get_model_config())
                
                # Generate scenario
                start_time = time.time()
                scenario_response = self.model.generate_content(
                    self.scenario_prompt,
                    generation_config=generation_config,
                )
                
                # Check if generation took too long
                if time.time() - start_time > self.timeout:
                    logger.log_documentation("Scenario generation timed out")
                    attempt += 1
                    time.sleep(1)  # Add delay before retry
                    continue
                
                if not scenario_response or not scenario_response.text:
                    logger.log_documentation("No scenario generated")
                    attempt += 1
                    time.sleep(1)  # Add delay before retry
                    continue

                # Generate CSV data based on scenario
                csv_prompt = self.csv_prompt.format(scenario=scenario_response.text)
                start_time = time.time()  # Reset timer for CSV generation
                csv_response = self.model.generate_content(
                    csv_prompt,
                    generation_config=generation_config,
                )

                # Check CSV generation timeout separately
                if time.time() - start_time > self.timeout:
                    logger.log_documentation("CSV generation timed out")
                    attempt += 1
                    time.sleep(1)  # Add delay before retry
                    continue

                if not csv_response or not csv_response.text:
                    logger.log_documentation("No CSV data generated")
                    attempt += 1
                    time.sleep(1)  # Add delay before retry
                    continue

                logger.log_documentation(f"Raw model responses:\nScenario:\n{scenario_response.text}\nCSV:\n{csv_response.text}")
                return scenario_response.text, csv_response.text
                
            except Exception as e:
                logger.log_documentation(f"Error during generation: {str(e)}")
                attempt += 1
                time.sleep(1)  # Wait before retrying
                
        logger.log_documentation("All generation attempts failed")
        return None, None 