"""
Run Script

This script starts the Flask development server.
"""

from src.client_simulator.app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 