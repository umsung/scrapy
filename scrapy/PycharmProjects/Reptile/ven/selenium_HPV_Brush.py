from selenium import webdriver
import time
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

option = webdriver.ChromeOptions()
# chrome_options = Options()
# 无头模式启动
option.add_argument('--headless')
# 谷歌文档提到需要加上这个属性来规避bug
option.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=option)
driver.get('http://www.kwh.org.mo/')


def hpv_parse():
    html = driver.page_source
    selector = etree.HTML(html)
    out_stock = selector.xpath('//a[contains(./font/b/text()[2], "暫未有貨")]/font/b/text()')
    in_stock = selector.xpath('//a[contains(./font/b/text()[2], "已有少量貨源")]/font/b/text()')
    print('少量貨源的内容是：', in_stock)
    print('暫未有貨的内容是：', out_stock)
    if len(in_stock):
        print('有货，当前时间是: {},开始发送邮件'.format(str(datetime.datetime.now()).split('.')[0]))
        send_mail(subject=s, content=c)
        time.sleep(2)
        driver.quit()
    else:
        print('无货, 当前时间是: {}'.format(str(datetime.datetime.now()).split('.')[0]))
        driver.refresh()
        time.sleep(5)
        return hpv_parse()


def send_mail(subject='subject', content='content'):
    # mail server
    mail_host = 'smtp.163.com'
    mail_port = 25
    mail_user = 'qq1516442017@163.com'     # 账号
    mail_pwd = 'qq545699233'       #

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


if __name__ == '__main__':
    s = 'HPV疫苗预约'
    c = '''姓名：龙洋
性别：女
证件号：430521199401133323
联系电话：15211186524
邮箱地址：qq1516442017@163.com
首针日期：7月12日、7月19日、7月26日
'''
    hpv_parse()