"""
Application Factory Module

This module creates and configures the Flask application.
"""

from flask import Flask
from .api.routes import client_sim

def create_app(config=None):
    """
    Create and configure the Flask application.
    
    Args:
        config: Configuration dictionary or object.
        
    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    
    # Apply configuration
    if config:
        app.config.update(config)
    
    # Register blueprints
    app.register_blueprint(client_sim)
    
    return app 