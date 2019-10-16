import os
import time

import yaml
from selenium import webdriver

print(os.path.abspath(__file__))
print(os.path.abspath('.'))

basepath = os.path.join(os.path.join(os.path.abspath('.'), 'pageelement'), 'desired_caps.yaml')
print(basepath)

def get_desired_caps(deviceName=''):
    '''
       t = {"token": value}
       with open(ypath, "w", encoding="utf-8") as f:
           yaml.dump(t, f, Dumper=yaml.RoundTripDumper)
       '''

    f = open(basepath, 'r', encoding='utf-8')
    a = f.read()
    dict_content = yaml.load(a)
    print(dict_content)
    for i in dict_content:
        if deviceName in i['desc']:
            strat_appium_server(i['port'], i['desired_caps']['uuid'])
            return i['desired_caps'], i['port']


def strat_appium_server(port='', uuid=''):
    r = os.popen('netstat -ano | findstr "%s" ' % port)
    time.sleep()
    result = r.read()
    if 'LISTENING' in result:
        print('appium服务已启动')
    else:
        os.system('appium -a 127.0.0.1 -p %s -u %s --no-reset' % (port, uuid))


def run_app(deviceName):
    desired_caps = get_desired_caps(deviceName)[0]
    driver = webdriver.Remote('https://127.0.0.1:%s/wd/hub', desired_caps)
    driver.find_element_by_id('').click()
    driver.find_element_by_xpath('').send_keys('')


if __name__ == '__main__':
    run_app('夜神')