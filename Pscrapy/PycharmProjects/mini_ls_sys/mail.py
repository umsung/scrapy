import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


class Mail(object):
    def __init__(self,server='',from_addr='',to_addr=''):
        self._server = server
        self._from_addr = from_addr
        self._to_addr = to_addr
        self._mail_title = 'mail_title'
        self._mail_content = 'mail_content'

    @property
    def mail_title(self):
        return self._mail_title

    @mail_title.setter
    def mail_title(self,title):
        self._mail_title = title

    @property
    def mail_content(self):
        return self._mail_content

    @mail_content.setter
    def mail_content(self,content):
        self._mail_content = content


    def send_mail(self):
        cur_time = time.strftime('%y%m%d',time.localtime())
        msg = MIMEText(self.mail_content, 'plain', 'utf-8')
        msg['Subject']= cur_time + ' ' + self.mail_title
        msg['from']= self._from_addr
        msg['to']= self._to_addr
        self._server.sendmail(msg['From'], msg['To'], msg.as_string())
        self._server.close()
