# app/routes/auth.py 
from flask import Blueprint 
 
auth_bp = Blueprint('auth', __name__) 
 
@auth_bp.route('/') 
def home(): 
    return "Bienvenido al sistema de repostería"