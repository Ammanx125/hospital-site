from flask import Blueprint, render_template, request, redirect, url_for

chat_bp = Blueprint('chat', __name__)

messages = {
    'sender':'Doctor',
    'text':'Hello receptionist, how are the patients today',
}

@chat_bp.route('/chat')
def chat():
    return render_template('chat.html', messages=messages)

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    message_text = request.form['message_text']

    messages.append({'sender': 'reseptionist', 'text': message_text})

    return redirect(url_for('chat.chat'))