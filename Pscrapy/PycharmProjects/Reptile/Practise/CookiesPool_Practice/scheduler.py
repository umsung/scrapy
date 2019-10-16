from db import *
from tester import *
from generator import *
from api import *
import time
from multiprocessing import Process

class Scheduler(object):
    def __init__(self):
        pass

    def run_generator(self):
        while True:
            try:
                for k,v in GENERATOR_MAP.items():
                    generator = v + '(name="' + k + '")'
                    generator.run()
                    print('Generator Finished')
                    generator.close()
                    print('Generator Closed')
                    time.sleep(CYCLE)
            except Exception as e:
                print('Error', e.args)

    def tester(self):
        while True:
            try:
                for k,v in TESTER_MAP.items():
                    tester = v + '(name="' + k + '")'
                    tester.run()
                    print('Tester Finished')
                    del tester
                    time.sleep(CYCLE)
            except Exception as e:
                print(e.args)
    
    def api(self):
        app.run()

    def run(self):
        if GENERATOR_PROCESS:
            generator_process = Process(target=self.run_generator)
            generator_process.start()
            

        if TESTER_PROCESS:
            tester_process = Process(target=self.tester)
            tester_process.start()
            

        if API_PROCESS:
            api_process = Process(target=self.api)
            api_process.start()
            