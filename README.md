# Data Analyst Client Simulator (DACS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.13.1-blue.svg)
![Flask Version](https://img.shields.io/badge/Flask-3.0.3-blue.svg)
## Overview
The Data Analyst Client Simulator (DACS) is a web application designed to provide aspiring data analysts with a realistic environment to practice their skills. It generates simulated client interactions and corresponding datasets, allowing users to engage in practical data analysis tasks.
**Purpose:** To offer a dynamic and challenging environment for improving data analysis skills, building portfolios, and developing communication abilities through realistic scenarios.
**Value Proposition:** DACS bridges the gap between theoretical knowledge and real-world application, providing aspiring data analysts with the practical experience needed for professional roles.
**Target Audience:** Aspiring and entry-level data analysts, data science students, and individuals building a data analysis portfolio.
**Key Features:**
* Scenario Generation: Generates realistic business scenarios with client profiles, business problems, and descriptions of available data, powered by the Google Gemini API.
* Dataset Generation: Creates corresponding datasets with diverse data types and realistic data quality issues (missing values, outliers, inconsistent formatting).
* Basic Web UI: Provides a simple interface to generate and download scenarios and datasets.
**Future Enhancements:**
* Interactive AI client for guidance and context.
* AI-powered feedback on analysis approaches.
* Portfolio building tools.
## Getting Started
### Prerequisites
* **Conda:** We recommend using Conda for environment management. If you don't have it, you can download it from https://docs.conda.io/en/latest/miniconda.html.
* **Git:** Required for cloning the repository. Download it from https://git-scm.com/.
* **Google Cloud API Key:** You will need a Google Cloud API key to use the Gemini API. See the [Gemini API Integration](#gemini-api-integration) section for details.
### Installation
1. **Clone the repository:**
```bash
git clone https://github.com/pauloarayasantiago/data-analysis-client-simulator.git
cd data-analysis-client-simulator
```
2. **Create and activate the Conda environment:**
```bash
conda env create --file environment.yml
conda activate dacs
```
*(Alternatively, if you don't have the `environment.yml` file or prefer to create it manually):*
```bash
conda create --name dacs python=3.13 flask google-generativeai pandas faker jupyter ipywidgets grpcio
conda activate dacs
```
### Configuration
1. **Set up the Google Cloud API Key:**
* Obtain a Google Cloud API key from the Google Cloud Console.
* Set the API key as an environment variable named `GOOGLE_API_KEY`. For example, on Linux/macOS:
```bash
export GOOGLE_API_KEY="YOUR_API_KEY"
```
Or on Windows:
```bash
set GOOGLE_API_KEY="YOUR_API_KEY"
```
* **Important:** For production environments, consider using more secure methods like service accounts and Workload Identity Federation as mentioned in the [Gemini API Integration](#gemini-api-integration) section.
## Usage
### Running the Flask Application
To start the DACS web application, execute the following command from the project root directory:
```bash
python flask_basic_structure.py
```
This will start the Flask development server. You can then access the application in your web browser, typically at http://127.0.0.1:5000/.
### Interacting with the Application
* **Generate Scenario:** Click the "Generate Scenario" button on the web interface.
* **View Scenario:** The generated scenario will be displayed on the page, including a client profile, a business problem, and a description of the available data.
* **Download Dataset:** Click the provided link to download the generated dataset in CSV format.
## Project Structure
```plaintext
data-analysis-client-simulator/
├── flask_basic_structure.py    # Core Flask application
├── templates/                 # HTML templates
│   └── index.html
├── static/                    # Static files (CSS, JS, images)
├── .git/                      # Git repository files
├── README.md                  # This file
└── environment.yml            # Conda environment definition
```
### Key Components
* **flask_basic_structure.py:** The main Python file containing the Flask application logic. It handles:
* Initializing the Flask application (`app = Flask(__name__)`).
* Defining routes and views (e.g., `@app.route('/')` for the homepage).
* Running the development server (`app.run(debug=True, use_reloader=False)`).
* **templates/:** Contains HTML templates used by Flask to render the user interface. `index.html` is the main page for generating scenarios and downloading data.
* **static/:** Holds static files such as CSS stylesheets, JavaScript files, and images.
## Git Repository Initialization
This project uses Git for version control, hosted on GitHub.
Repository URL: https://github.com/pauloarayasantiago/data-analysis-client-simulator
Main Branch: main
### Setting up the Repository:
#### Using the Command Line:
```bash
git clone https://github.com/pauloarayasantiago/data-analysis-client-simulator.git
cd data-analysis-client-simulator
```
#### Using GitHub Desktop:
* **Clone a Repository:** In GitHub Desktop, go to "File" > "Clone repository..." and enter the repository URL.
* **Initial Commit:** After making changes, stage them, write a commit message, and click "Commit to main".
* **Push to Remote:** Click the "Push origin" button to synchronize your local changes with the remote repository.
## Gemini API Integration
This application leverages the Google Gemini API (`google-generativeai` library) for generating realistic client interaction scenarios and datasets.
* **API Key:** A Google Cloud API key is required and must be set as an OS environment variable named `GOOGLE_API_KEY`. For production deployments, using a service account with Workload Identity Federation is strongly recommended for enhanced security.
* **Model:** The `gemini-1.5-pro-latest` model is utilized for text generation.
* **Key Endpoint:** `client.models.generate_content`:
* Used for all text generation tasks.
* The `contents` parameter accepts both text and multimedia inputs for generating diverse scenarios.
* The `config` parameter allows fine-tuning the output, including setting the temperature for creativity, `max_output_tokens` for length control, and adding safety filters.
* The generated text is accessible via the `response.text` property of the API response.
* **File Upload:** For handling larger multimedia or text files, the API requires uploading them first using `client.files.upload`. The returned URI can then be used in the `generate_content` method.
* **Error Handling:** The application incorporates robust error handling using try-catch blocks and logging to manage potential issues with the Gemini API, such as rate limiting, authentication problems, or invalid requests.
## Contributing
We welcome contributions to the DACS project! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Write clear and concise commit messages.
5. Submit a pull request.
Please adhere to the existing code style and ensure your changes include appropriate tests.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Contact
For questions or issues, please open an issue on the GitHub repository.
## Acknowledgements
We would like to acknowledge the following libraries and resources that were essential for the development of this project:
* Flask: For the web application framework.
* Google Generative AI Python SDK: For accessing the Gemini API.
* Pandas: For data manipulation and analysis.
* Faker: For generating realistic fake data (used internally for testing and potential future features).

