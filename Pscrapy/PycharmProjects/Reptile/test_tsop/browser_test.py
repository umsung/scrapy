from tsop.browser_engine import BrowserEngine


class TestBrowser(object):
    def test_open_browser(self):
        browserengine = BrowserEngine(self)
        browserengine.get_browser()


testbrowser = TestBrowser()
testbrowser.test_open_browser()