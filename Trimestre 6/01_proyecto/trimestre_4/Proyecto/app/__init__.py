from flask import Flask
import pymysql.cursors
from flask_bcrypt import Bcrypt
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(Config)

    # Inicializar Bcrypt
    bcrypt = Bcrypt(app)
    app.bcrypt = bcrypt  # Hacer bcrypt disponible en la app

    # Conexión a la base de datos MySQL
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )
    app.connection = connection

    # Registrar Blueprints (importar aquí para evitar dependencias circulares)
    from app.controllers.main_controller import main_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.admin_controller import admin_bp
    from app.controllers.menu_controller import menu_bp
    from app.controllers.mesas_controller import mesas_bp
    from app.controllers.pedidos_controller import pedidos_bp
    from app.controllers.platillos_controller import platillos_bp
    from app.controllers.chef_controller import chef_bp
    from app.controllers.inventario_controller import inventario_bp
    from app.controllers.mesero_controller import mesero_bp
    
    
    
    
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(mesas_bp)
    app.register_blueprint(pedidos_bp)
    app.register_blueprint(platillos_bp)
    app.register_blueprint(chef_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(mesero_bp)
    
    
    
    @app.template_filter('datetimeformat')
    def datetimeformat(value, format='%d/%m/%Y %H:%M'):
        if value is None:
            return ""
        return value.strftime(format)

    return app