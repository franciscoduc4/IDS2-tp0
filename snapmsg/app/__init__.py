from flask import Flask
from .config import DevelopmentConfig, ProductionConfig, TestingConfig

def create_app(config_class=DevelopmentConfig):
    """Factory pattern for creating the Flask app."""
    app = Flask(__name__)
    
    # Cargar la configuración
    app.config.from_object(config_class)
    
    # Registro de Blueprints (rutas)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # BDD
    # from .models import db
    # db.init_app(app)

    # Inicializar otras extensiones, middleware, etc.
    
    return app
