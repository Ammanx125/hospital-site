from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app

general_bp = Blueprint('general', __name__)

@general_bp.route('/about')
def about():
    team = [
        {"name": "Aman", "role": "Backend & UI", "image": "aman.jpg"},
        {"name": "Hani", "role": "Page Designer", "image": "hani.jpg"},
        {"name": "Rhode", "role": "Page Designer", "image": "rod.jpg"},
        {"name": "Yeabsira", "role": "Frontend Dev", "image": "yaba.jpg"},
        {"name": "Nuhamin", "role": "Proposal Writing", "image": "nuha.jpg"},
        {"name": "Ruth", "role": "Proposal Writing", "image": "ruth.jpg"},
    ]
    return render_template('about.html', team=team)

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

appointments = []

@general_bp.route('/handle_appointment', methods=['POST'])
def handle_appointment():
    full_name = request.form['full_name']
    reason = request.form['reason']
    time = request.form.get('time')

    if not time:
        flash("Time is required, my guy 👀", "error")
        return redirect(url_for('general.make_appointment'))

    new_appointment = {
        'full_name': full_name,
        'reason': reason,
        'time': time
    }

    current_app.config['APPOINTMENTS'].append(new_appointment)
    flash('Appointment booked successfully!', 'success')
    return redirect(url_for('general.make_appointment'))
