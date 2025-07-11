from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def obtener_conexion():
    return mysql.connector.connect(
        host='127.0.0.1',      # Cambia por tu host si es necesario
        user='root',     # Cambia por tu usuario de MySQL
        password='', # Cambia por tu contraseña de MySQL
        database='coleccion_musical' # Cambia por el nombre de tu base de datos
    )

@app.route('/')
def inicio():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("Show tables")  # Cambia por el nombre de tu tabla
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('index.html', datos=resultados)

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    artista = request.form['artista']
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO canciones (nombre, artista) VALUES (%s, %s)", (nombre, artista))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
