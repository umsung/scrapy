from tsop.classA import *
import time, os

class ClassB(ClassA):


    def test_inherit(self):
        self.open_baidu()


classb = ClassB()
classb.test_inherit()