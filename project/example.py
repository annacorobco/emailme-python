# TODO: Incorrect
import sys
sys.path.append("..")


from project.emailme import EmailMe


email_server = EmailMe()
email_server.send("Hello, world", 'anna-test@example.com')
