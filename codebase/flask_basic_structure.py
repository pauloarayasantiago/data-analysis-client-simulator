# flask_basic_structure.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    """
    View function for the root URL.

    Returns:
        str: The "Hello, World!" message.
    """
    return 'Hello, World!'

# Run the application if this file is executed directly
if __name__ == '__main__':
    # Start the Flask development server
    # debug=True enables debugging mode, providing helpful error messages
    # use_reloader=False is important for running within Jupyter Notebooks to avoid conflicts
    app.run(debug=True, use_reloader=False)