import os

class Config:
    """Base configuration."""
    # Variables generales
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8080))
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

    # Configuraciones relacionadas con la base de datos
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = int(os.getenv('DATABASE_PORT', 5432))
    DATABASE_USER = os.getenv('DATABASE_USER', 'user')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'snapmsg_db')

    # Configuración adicional que podrías necesitar
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']
    TESTING = os.getenv('TESTING', 'False').lower() in ['true', '1', 't']

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'snapmsg_test_db')
