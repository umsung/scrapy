import os
import unittest
import time
from testsuits.mainland import MainLand
# from testsuits.baidu_search import BaiduSearch
# from testsuits.test_get_page_title import GetPageTitle
# from testsuits import *
import HtmlTestRunner
# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTitle('test_get_title'))


suite = unittest.TestSuite(unittest.makeSuite(MainLand))

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
sj = time.strftime('%y%m%d%H%M%S', time.localtime())
# HTMLFile = report_path + sj + 'HTMLTemplate.html'
# fp = open(HTMLFile, 'w')

# testsuits_path = os.path.dirname(os.path.abspath('.')) + '/testsuits/'
# suite = unittest.TestLoader().discover(testsuits_path)

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output=report_path, report_title="TestReport", descriptions="巡检测试")
    # runner = HtmlTestRunner.HTMLTestRunner(stream=fp, report_title='测试标题', descriptions='描述')
    # runner = unittest.TextTestRunner()
    runner.run(suite)