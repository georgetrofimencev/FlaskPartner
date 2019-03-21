from flask import current_app
from flask_mail import Message
from main import mail
from core.utils.async_def import async_def


class EmailSender:
    def __init__(self, msg=None):
        self.msg = msg

    def create_message(self, subject, email, body):
        self.msg = Message(subject, recipients=[email, ], body=body)

    @async_def
    def send_email_async(self, app):
        with app.app_context():
            mail.send(self.msg)

    def send_email_sync(self):
        with current_app.app_context():
            mail.send(self.msg)
