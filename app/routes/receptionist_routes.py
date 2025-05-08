from flask import Blueprint, render_template, request, redirect, url_for, current_app
from ..routes.auth_routes import login_required

receptionist_bp = Blueprint('receptionist', __name__)

# Dummy database for patients
patients = []

@receptionist_bp.route('/receptionist_dashboard')
@login_required('receptionist')
def receptionist_dashboard():
    appointments = current_app.config['APPOINTMENTS']
    return render_template('receptionist/dashboard.html', patients=patients, appointments=appointments)

@receptionist_bp.route('/register_patient', methods=['POST'])
def register_patient():
    name = request.form['patient_name']
    age = request.form['patient_age']
    contact = request.form['patient_contact']
    
    # Register patient in the dummy database
    patients.append({
        'name': name,
        'age': age,
        'contact': contact
    })
    
    return redirect(url_for('receptionist.receptionist_dashboard'))
