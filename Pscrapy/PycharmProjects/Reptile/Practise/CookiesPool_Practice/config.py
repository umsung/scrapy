# redis数据库配置
HOST = 'localhost'
PORT = 6379
PASSWORD = ''

# generator
BROWSER_TYPE = 'Chrome'

# api
API_HOST = ''
API_PORT = ''

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'tet': 'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'tet': 'TestValidCookie'
}

# scheduler
CYCLE = 1
GENERATOR_PROCESS = False
TESTER_PROCESS = False
API_PROCESS =  True