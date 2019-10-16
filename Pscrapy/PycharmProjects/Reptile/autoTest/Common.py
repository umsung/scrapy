from datetime import datetime
''' 公共模块'''

def driverPath():
    return r'C:\Users\xua\Downloads\chromedriver_win32\chromedriver.exe'


def baseUrl():
    return "https:xxxxxxxx"


def getCurrentTime():
    format = '%a %b %d %H:%M:%S %Y'
    return datetime.now().strftime(format)


def timeOff(startime, endtime):
    format = '%a %b %d %H:%M:%S %Y'
    return datetime.strptime(endtime,format) - datetime.strptime(startime, format)