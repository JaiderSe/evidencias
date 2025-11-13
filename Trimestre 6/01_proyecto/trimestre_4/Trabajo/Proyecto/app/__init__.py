from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.config import Config  # Adjust the import path if your Config is elsewhere

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    Bootstrap(app)
    
    # Registrar blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.menu_controller import menu_bp
    from app.controllers.order_controller import order_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(order_bp)
    
    # Crear tablas de la base de datos
    with app.app_context():
        db.create_all()
    
    return app