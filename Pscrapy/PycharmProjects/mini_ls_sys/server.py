import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Server(object):
    def __init__(self,mail_host,mail_port,mail_user,mail_pwd):
        self.mail_host = mail_host
        self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_pwd = mail_pwd
        self.smtp_obj = smtplib.SMTP()

    def connect(self):
        try:
            self.smtp_obj.connect(self.mail_host, self.mail_port)  # SMTP协议默认端口是25
            self.smtp_obj.login(self.mail_user, self.mail_pwd)
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False

    def close(self):
        self.smtp_obj.quit()