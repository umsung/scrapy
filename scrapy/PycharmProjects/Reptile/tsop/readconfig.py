# coding=utf-8
import configparser
import os

print(os.path.abspath('.'))
print(os.path.dirname(os.path.abspath('.')))


class TestReadConfig(object):
    def get_value(self):
        config_path = os.path.dirname(os.path.abspath('.')) + '\config\config.ini'
        print(config_path)

        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')

        browser = config.get('browserType', 'browserName')

        url = config.get('testServer', 'URL')

        return(browser, url)


testread = TestReadConfig()
print(testread.get_value())
