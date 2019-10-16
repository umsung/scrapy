import requests
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'

  }


def hpv_parse():
    resp = requests.get('http://www.kwh.org.mo/', headers=headers)
    resp.encoding = 'utf-8'

    if resp.status_code == 200:
        selector = etree.HTML(resp.text)
        # in_stock = selector.xpath('//a[contains(./font/b/text()[2], "暫未有貨")]/font/b/text()')
        in_stock = selector.xpath('//a[contains(./font/b/text()[2], "已有少量貨源")]/font/b/text()')
        print('in_stock的内容是：', in_stock)
        if len(in_stock):
            print('有货，开始发送邮件')
            send_mail(subject=s, content=c)
        else:
            print('无货, 当前时间是: {}'.format(str(datetime.datetime.now()).split('.')[0]))
            time.sleep(60)
            return hpv_parse()


def send_mail(subject='subject', content='content'):
    # mail server
    mail_host = 'smtp.163.com'
    mail_port = 25
    mail_user = 'qq1516442017@163.com'     # 账号
    mail_pwd = '******'       # 密码

    # mail message
    # 三个参数：第一个为邮件正文文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8').encode()  # 邮件的主题
    message['From'] = 'qq1516442017@163.com'   # 发送者    填写发送邮箱者地址
    message['To'] = 'health@kwh.org.mo'   # 接收者      填写接收邮箱者地址
    # send mail
    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, mail_port)    # SMTP协议默认端口是25
        smtp_obj.login(mail_user, mail_pwd)
        smtp_obj.sendmail(message['From'], message['To'], message.as_string())
        print('邮件发送成功')
        smtp_obj.quit()
    except smtplib.SMTPException as e:
        print(e, '无法发送邮件')


# def main(h, m):
#     while True:
#         now = datetime.datetime.now()
#         if now.hour == h and now.minute in m:
#             hpv_parse()
#
#         time.sleep(60)


if __name__ == '__main__':
    s = 'HPV疫苗预约'
    c = '''姓名：龙洋
性别：女
证件号：430521199401133323
联系电话：15211186524
邮箱地址：qq1516442017@163.com
首针日期：6月6日、6月14日、6月21日
'''
    hpv_parse()

