from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from functools import wraps

auth_bp = Blueprint('auth', __name__)

# Dummy user store; in production use a real database
users = {
    "abc": {"password": "123", "role": "receptionist"},
    "abcd": {"password": "123", "role": "doctor"}
}

def login_required(role=None):
    """
    Decorator to protect routes by login and role.
    Usage:
      @login_required()             # any logged-in user
      @login_required('doctor')     # only doctors
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'username' not in session:
                flash('Please log in to access this page.', 'error')
                return redirect(url_for('auth.login'))
            if role and session.get('role') != role:
                flash('You do not have permission to view this page.', 'error')
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return wrapped
    return decorator

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.args.get('next')  # for redirects like /chat

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        role     = request.form.get('role')

        user = users.get(username)

        if not user or user['password'] != password or user['role'] != role:
            flash('Invalid credentials, try again.', 'error')
            return render_template('login.html')

        # Successful login
        session.clear()
        session['username'] = username
        session['role'] = role
        flash(f'Welcome, {username}!', 'success')

        # Redirect priority: custom next_page > role dashboard
        if next_page:
            return redirect(next_page)

        if role == 'receptionist':
            return redirect(url_for('receptionist.receptionist_dashboard'))
        elif role == 'doctor':
            return redirect(url_for('doctor.doctor_dashboard'))

        # fallback if role doesn't match known dashboards
        return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))
