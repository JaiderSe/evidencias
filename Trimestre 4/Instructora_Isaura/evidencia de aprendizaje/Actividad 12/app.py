from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def home():
   #app.logger.debug('Iniciando el debug')
   #app.logger.info('Iniciando info')
   #app.logger.warning('Iniciando a nivel warning')
   #app.logger.error('Iniciando a nivel de error')
   app.logger.info(f'Solicitud en la ruta {request.path}')
   return "<p>Hello, World! desde pycharm</p>"


@app.route("/saludar/<nombre>")
def saludar(nombre):
   app.logger.info(f'Solicitud en la ruta {request.path}')
   return f"Hola {nombre}"

@app.route("/edad/<edad>")
def edad(edad):
   app.logger.info(f'Solicitud en la ruta {request.path}')
   return f"tu edad es {edad}"

@app.route("/saludo/<nombre>/<edad>")
def saludo(nombre, edad):
   app.logger.info(f'Solicitud en la ruta {request.path}')
   return f"hola {nombre} tu edad es {edad}"

@app.route("/productos", methods=['GET'])
def listarproductos():
   return ("Listado de productos")
    
@app.route("/productos/crear/<nombre>/<valor>", methods=['POST'])
def crearproductos():
    
    nombre=request.form['nombre']
    valor=request.form['valor']
    return ("Se creo el producto")

