import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(subject='subject', content='content'):
    # mail server
    mail_host = 'smtp.sina.com'
    mail_port = 25
    mail_user = ''     # 账号
    mail_pwd = ''       # 密码

    # mail message
    # email模块 负责构造邮件
    # 三个参数：第一个为邮件正文文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = subject  # 邮件的主题
    message['From'] = ''   # 发送者    填写发送邮箱者地址
    message['To'] = ''   # 接收者      填写接收邮箱者地址, #收件人为多个收件人,通过join将列表转换为以;为间隔的字符串

    # send mail
    # smtplib模块负责发送邮件，是一个发送邮件的动作
    try:
        # 实例化SMTP()
        smtp_obj = smtplib.SMTP()

        # 实例化SMTP(),连接邮箱服务器, mail_host是邮箱服务器地址，mail_port是端口，
        # 新浪邮箱：smtp.sina.com,
        # 新浪VIP：smtp.vip.sina.com,
        # 搜狐邮箱：smtp.sohu.com，
        # 126邮箱：smtp.126.com,
        # 139邮箱：smtp.139.com,
        # 163网易邮箱：smtp.163.com。
        smtp_obj.connect(mail_host, mail_port)  # SMTP协议默认端口是25
        smtp_obj.login(mail_user, mail_pwd)
        # as_string()message(MIMEText对象或者MIMEMultipart对象)变为str
        smtp_obj.sendmail(message['From'], message['To'], message.as_string())
        smtp_obj.quit()
    except smtplib.SMTPException as e:
        print(e)


s = 'Please study hard'
c = 'My name is Teacher hou, I teach python'
send_mail(subject=s, content=c)
