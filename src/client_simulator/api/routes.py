"""
API Routes Module

This module defines the Flask routes for the client simulator API.
"""

from flask import Blueprint, jsonify, render_template
from ..models.client_generator import ClientGenerator
from ..utils.logger import DocumentationLogger
from ..utils.file_handler import FileHandler
from ..utils.name_extractor import extract_client_name

# Create blueprint for client simulator routes
client_sim = Blueprint('client_sim', __name__)

# Initialize components
generator = ClientGenerator()
file_handler = FileHandler()

@client_sim.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@client_sim.route('/generate', methods=['POST'])
def generate():
    """Generate a new client profile and problem."""
    logger = DocumentationLogger()
    logger.log_documentation("Starting new client generation")
    
    try:
        # Generate client and problem
        client_data, csv_data = generator.generate(logger)
        
        if client_data is None or csv_data is None:
            raise Exception("Failed to generate client data or CSV data")
        
        return jsonify({
            'status': 'success',
            'client_data': client_data,
            'csv_data': csv_data,
            'logs': logger.log
        })
    
    except Exception as e:
        logger.log_documentation(f"Error occurred: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e),
            'logs': logger.log
        }), 500 