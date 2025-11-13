from flask_mysqldb import MySQL
from app import mysql

def get_db_connection():
    return mysql.connection