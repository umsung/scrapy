import time
from datetime import datetime

class GetTime(object):
    def get_system_time(self):
        print(time.time())
        now = time.strftime('%y-%m-%d %H:%M:%S', time.localtime())
        return now


gettime = GetTime()
print(gettime.get_system_time())