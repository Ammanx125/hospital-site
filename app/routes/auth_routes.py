from flask import Blueprint, render_template, request, redirect, session, url_for

auth = Blueprint('auth', __name__)

# Dummy user database
users = {
    "reception1": {"password": "pass123", "role": "receptionist"},
    "doctor1": {"password": "docpass", "role": "doctor"}
}

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        user = users.get(username)
        if user and user['password'] == password and user['role'] == role:
            session['username'] = username
            session['role'] = role

            if role == 'receptionist':
                return redirect(url_for('main.receptionist_dashboard'))
            elif role == 'doctor':
                return redirect(url_for('main.doctor_dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
        
    return render_template('login.html')
