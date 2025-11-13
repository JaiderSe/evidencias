from flask import Flask
from flask_mysqldb import MySQL
from app.config import Config

mysql = MySQL()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    mysql.init_app(app)
    
    # Registrar blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.menu_controller import menu_bp
    from app.controllers.order_controller import order_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(order_bp)
    
    return app