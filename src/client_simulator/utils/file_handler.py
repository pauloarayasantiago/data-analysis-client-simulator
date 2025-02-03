"""
File Handler Module

This module handles file operations for the client simulator.
"""

import os
import re
from .logger import DocumentationLogger

class FileHandler:
    """Handles file operations for client data and documentation."""
    
    def __init__(self, base_dir: str = "trials"):
        """
        Initialize the file handler.
        
        Args:
            base_dir: Base directory for storing trials.
        """
        self.base_dir = base_dir

    def save_client_data(self, client_data: str, client_name: str, logger: DocumentationLogger) -> dict:
        """
        Save client data and documentation to files.
        
        Args:
            client_data: The generated client profile and problem.
            client_name: The name of the client.
            logger: DocumentationLogger instance.
            
        Returns:
            dict: Paths to the saved files.
        """
        # Create base directory if it doesn't exist
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        
        # Get the next trial number
        trial_number = len([d for d in os.listdir(self.base_dir) 
                          if os.path.isdir(os.path.join(self.base_dir, d))]) + 1
        
        # Create trial directory
        trial_dir = os.path.join(self.base_dir, f"trial_{trial_number}")
        os.makedirs(trial_dir)
        
        # Sanitize client name for filename
        sanitized_name = re.sub(r'[^\w\s-]', '', client_name)
        sanitized_name = re.sub(r'\s+', '_', sanitized_name).strip()
        
        # Save client data
        client_file = os.path.join(trial_dir, f"{sanitized_name}.txt")
        doc_file = os.path.join(trial_dir, f"{sanitized_name}_documentation.txt")
        
        with open(client_file, "w") as f:
            f.write(client_data)
        
        with open(doc_file, "w") as f:
            f.write(logger.log)
        
        return {
            "client_file": client_file,
            "doc_file": doc_file
        } 