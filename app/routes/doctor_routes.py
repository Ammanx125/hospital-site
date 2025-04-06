from flask import Blueprint, render_template, request, redirect, url_for

doctor_bp = Blueprint('doctor', __name__)

# Dummy patient data (same as receptionist for now)
patients = [
    {'name': 'Yeabsira Debebe', 'age': 30, 'contact': '09********', 'notes': ''},
    {'name': 'Ruth Teshome', 'age': 25, 'contact': '09********', 'notes': ''}
]

@doctor_bp.route('/doctor_dashboard')
def doctor_dashboard():
    return render_template('doctor/dashboard.html', patients=patients)

@doctor_bp.route('/update_patient/<int:index>', methods=['POST'])
def update_patient(index):
    notes = request.form['notes']
    
    # Update patient's notes
    patients[index - 1]['notes'] = notes  # Adjusting index since loop starts from 1
    
    return redirect(url_for('doctor.doctor_dashboard'))
