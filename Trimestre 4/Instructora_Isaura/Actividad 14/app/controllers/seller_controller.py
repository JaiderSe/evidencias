# app/controllers/seller_controller.py
from flask import Blueprint, render_template

seller_bp = Blueprint('seller_bp', __name__)

@seller_bp.route('/seller/dashboard')
def seller_dashboard():
    return render_template('seller_dashboard.html')

