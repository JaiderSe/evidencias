# app/controllers/main_controller.py
from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

