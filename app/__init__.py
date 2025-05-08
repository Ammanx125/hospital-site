from flask import Flask
from .utils import format_time

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super_secret_key'
    app.config['APPOINTMENTS'] = []
    app.config.setdefault('MESSAGES', [])
    app.jinja_env.filters['format_time'] = format_time

    from .routes.auth_routes import auth_bp
    from .routes.receptionist_routes import receptionist_bp
    from .routes.doctor_routes import doctor_bp
    from .routes.chat_routes import chat_bp
    from .routes.general_routes import general_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(receptionist_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(general_bp)

    return app
