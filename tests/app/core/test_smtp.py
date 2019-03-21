import unittest

from flask_mail import Mail
from betronic import create_app
from core.smtp.sender import EmailSender


class EmailSenderTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("default")
        self.mail = Mail()
        self.mail.init_app(self.app)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_send_email(self):
        email_sender = EmailSender()
        email_sender.create_message(
            "Hello World!",
            "george98trofimencev@gmail.com",
            body='test'
        )
        email_sender.send_email_sync()
