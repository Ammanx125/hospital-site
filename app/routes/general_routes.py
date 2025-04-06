from flask import Blueprint, render_template, redirect, url_for

general_bp = Blueprint('general', __name__)

@general_bp.route('/about')
def about():
    return render_template('about.html')

@general_bp.route('/')
def home():
    return render_template('home.html')

@general_bp.route('/contact')
def contact():
    return render_template('contact.html')

@general_bp.route('/doctor_dashboard')
def redirect_to_doctor():
    return redirect(url_for('doctor.doctor_dashboard'))

@general_bp.route('/receptionist_dashboard')
def redirect_to_receptionist():
    return redirect(url_for('receptionist.receptionist_dashboard'))

@general_bp.route('/chat')
def redirect_to_chat():
    return redirect(url_for('chat.chat'))

@general_bp.route('/make_appointment')
def make_appointment():
    return render_template('appointment/make_appointment.html')