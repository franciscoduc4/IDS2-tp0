# app/logging_config.py

import logging

def setup_logging():
    """
    Configure the basic logging settings for the application.

    This function sets up the logging configuration with the following parameters:
    - Log level: INFO
    - Log format: timestamp - logger name - log level - message

    The configured format provides detailed information for each log entry,
    making it easier to track and debug issues in the application.

    Usage:
        Call this function at the start of your application to initialize
        the logging system with these settings.

    Example:
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Application started")
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
