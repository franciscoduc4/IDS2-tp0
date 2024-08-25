import os

class Config:
    """
    Configuration class for the application.

    This class uses environment variables to set configuration values,
    with fallback default values if the environment variables are not set.
    """

    # Application environment (e.g., development, production)
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

    # Host address for the application to bind to
    HOST = os.getenv('HOST', '0.0.0.0')

    # Port number for the application to listen on
    PORT = int(os.getenv('PORT', 8080))

    # Database connection URL
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./app.db')