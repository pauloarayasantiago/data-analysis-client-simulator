"""
Gemini AI Model Configuration

This module handles the configuration and setup of the Gemini AI model.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Dict

# Load environment variables
load_dotenv()

def get_model_config() -> Dict:
    """Get the generation configuration for the Gemini model."""
    return {
        'temperature': 0.7,  # Lower temperature for more focused outputs
        'top_p': 0.9,
        'top_k': 40,
        'max_output_tokens': 4096,  # Increased for the flash model
        'candidate_count': 1,
    }

def get_safety_settings():
    """Get the safety settings for the model."""
    return [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

def initialize_model():
    """Initialize and configure the Gemini model.
    
    Returns:
        The configured Gemini model instance.
        
    Raises:
        ValueError: If the API key is not set or invalid.
    """
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY environment variable is not set. "
            "Please set it with your Google API key."
        )
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Configure safety settings
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
        
        model.safety_settings = safety_settings
        return model
        
    except Exception as e:
        raise ValueError(f"Failed to initialize Gemini model: {str(e)}") 