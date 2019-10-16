# coding:utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import formataddr

sender = '********'@163.com'
receivers = '********'@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEMultipart()
message['From'] = formataddr(["来自简书作者的问候", sender])  # 发送者
message['To'] = formataddr(["来自简书作者董小贱的问候", receivers])  # 接收者

subject = '这是一封正常正常邮件， 并不是异常的！'
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText('这是邮件的正文内容', 'plain', 'utf-8 '))  # 邮件的正文内容
att1 = MIMEText(open('dongxiaojian.txt').read(), 'base64', 'utf-8')  # 构建邮件附件
att1["Content-Disposition"] = 'attachment;filename="dongxiaojian.txt"'  # 这里的filename就是收到附件的名字
message.attach(att1)

# 以附件的形式添加图片
f = open('timg.jpeg', 'rb')
att2 = MIMEImage(f.read())
f.close()
att2["Content-Disposition"] = 'attachment;filename="danding.jpeg"'  # 这里的filename就是收到附件图片的的名字
message.attach(att2)

smtpObj = smtplib.SMTP('smtp.163.com', port=25)
smtpObj.login(user=sender, password='********'')
smtpObj.sendmail(sender, receivers, message.as_string())
