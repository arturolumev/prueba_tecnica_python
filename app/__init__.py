from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Inicialización de las extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializamos las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Importar y registrar las rutas después de crear la app
    from .routes import init_routes
    init_routes(app)  # Registramos las rutas aquí
    
    return app
