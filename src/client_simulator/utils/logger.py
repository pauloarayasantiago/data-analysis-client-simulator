"""
Logger Module

This module provides logging functionality for the client simulator.
"""

from datetime import datetime

class DocumentationLogger:
    """Handles logging of the client generation process."""
    
    def __init__(self):
        """Initialize an empty log."""
        self.log = ""

    def log_documentation(self, text: str) -> str:
        """
        Add a new log entry with timestamp.
        
        Args:
            text: The text to log.
            
        Returns:
            str: The formatted log entry.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}]: {text}\n"
        self.log += log_entry
        return log_entry 