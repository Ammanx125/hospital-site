from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    # Initialize shared list if not present
    messages = current_app.config.setdefault('MESSAGES', [])
    
    if request.method == 'POST':
        sender = request.form.get('sender', '').strip()
        text = request.form.get('text', '').strip()

        if not sender or not text:
            flash('Both name and message are required.', 'error')
            return redirect(url_for('chat.chat'))
        
        # Append the new message to the list
        messages.append({
            'sender': sender,
            'text': text
        })
        
        return redirect(url_for('chat.chat'))  # Redirect to avoid form resubmission

    return render_template('chat/chat.html', messages=messages)

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    message_text = request.form['message_text']

    # You can add this message as needed, for example, adding it to the current messages list
    messages = current_app.config.setdefault('MESSAGES', [])
    messages.append({'sender': 'Receptionist', 'text': message_text})

    return redirect(url_for('chat.chat'))
