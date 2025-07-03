# app/controllers/baker_controller.py
from flask import Blueprint, render_template

baker_bp = Blueprint('baker_bp', __name__)

@baker_bp.route('/baker/dashboard')
def baker_dashboard():
    return render_template('baker_dashboard.html')

