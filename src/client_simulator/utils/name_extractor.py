"""
Name Extractor Module

This module handles the extraction of client names from generated text.
"""

import re
from .logger import DocumentationLogger

def extract_client_name(text: str, logger: DocumentationLogger) -> str:
    """
    Extract the client name from the generated text.
    
    Args:
        text: The generated text containing the client profile.
        logger: DocumentationLogger instance.
        
    Returns:
        str: The extracted client name or 'Unknown_Client' if not found.
    """
    logger.log_documentation("Extracting client name")
    logger.log_documentation(f"Text passed to name extraction: \n{text}")
    
    name_match = re.search(r"^(.+?):", text)
    if name_match:
        name = name_match.group(1).strip()
        logger.log_documentation(f"Extracted name: {name}")
        return name
    else:
        logger.log_documentation("Could not extract name")
        return "Unknown_Client" 