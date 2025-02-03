import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(app, log_dir='logs'):
    """Configure application logging with both file and console handlers."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'dacs_app.log')
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file, maxBytes=1024 * 1024, backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Configure app logger
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    # Log startup message
    app.logger.info('Logger initialized successfully') 