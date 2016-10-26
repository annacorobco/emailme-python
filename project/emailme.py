import smtplib
from email.mime.text import MIMEText

try:
    from project.settings import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, \
        MAIL_PASSWORD, MAIL_SENDER
except ImportError:
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 20
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_SENDER = 'noreply'

class EmailMe:
    def __init__(self):
        self.server = MAIL_SERVER
        self.port = MAIL_PORT
        self.username = MAIL_USERNAME
        self.password = MAIL_PASSWORD
        self.sender = MAIL_SENDER

    def send(self, text, recipient):
        """ Send email using SMTP
        :param text: string
        :param recipient: string
        :return:
        """
        msg = self.generate_msg(text=text, recipient=recipient)
        s = smtplib.SMTP(self.server)
        s.send_message(msg)
        s.quit()

    def generate_msg(self, text, recipient):
        """ Generate message and set necessary headers
        :param text: string
        :param recipient: string
        :return: MIMEText
        """
        msg = MIMEText(text)
        msg['Subject'] = 'The contents of'
        msg['From'] = self.sender
        msg['To'] = recipient
        return msg
