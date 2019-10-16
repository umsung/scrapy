# -*- coding: utf-8 -*-
import scrapy


class YaozhiSpider(scrapy.Spider):
    name = 'yaozhi'
    allowed_domains = ['db.yaozh.com']
    url = 'https://db.yaozh.com/fangji/{num}.html'



    def start_requests(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'kztoken=nJail6zJp6iXaJqWl25maWVuaZOZ; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOS%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOZ%22%3B%7D; acw_tc=2f624a0b15547779373626962e2c454f3d12c9a51208a2d9d43b5811aad164; _ga=GA1.2.914088002.1554777939; MEIQIA_EXTRA_TRACK_ID=1Jby9OhcHRDm9UapjQCJf6v4k7q; _gid=GA1.2.1753007927.1554858488; UtzD_f52b_saltkey=KcT6zzbc; UtzD_f52b_lastvisit=1554854893; _ga=GA1.3.914088002.1554777939; bigdata_use_tips=1; UtzD_f52b_ulastactivity=1554775927%7C0; think_language=zh-CN; PHPSESSID=554uh18imjkus745n6barrf2n3; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D656992; UtzD_f52b_creditbase=0D0D4D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; MEIQIA_VISIT_ID=1JhRsmsBJRpXRK5aPLR1eYfaG3U; expire=1554962834212; UtzD_f52b_lastact=1554946013%09uc.php%09; yaozh_logintime=1554946364; yaozh_user=728478%09umsung; yaozh_userId=728478; yaozh_uidhas=1; yaozh_mylogin=1554946365; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1554946367; acw_tc=2f624a6715548584856626296e3d7bf5fd4df0e048c213322b156b89e54150; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1554858363%2C1554879242%2C1554945547%2C1554946367; kztoken=nJail6zJp6iXaJqWl25maWVuZ5qa; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZWV%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5qa%22%3B%7D',
            'Host': 'db.yaozh.com',
            'Referer': 'https://db.yaozh.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        Cookie = {'Cookie': 'kztoken=nJail6zJp6iXaJqWl25maWVuaZOZ; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOS%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOZ%22%3B%7D; acw_tc=2f624a0b15547779373626962e2c454f3d12c9a51208a2d9d43b5811aad164; _ga=GA1.2.914088002.1554777939; MEIQIA_EXTRA_TRACK_ID=1Jby9OhcHRDm9UapjQCJf6v4k7q; _gid=GA1.2.1753007927.1554858488; UtzD_f52b_saltkey=KcT6zzbc; UtzD_f52b_lastvisit=1554854893; _ga=GA1.3.914088002.1554777939; bigdata_use_tips=1; UtzD_f52b_ulastactivity=1554775927%7C0; think_language=zh-CN; PHPSESSID=554uh18imjkus745n6barrf2n3; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D656992; UtzD_f52b_creditbase=0D0D4D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; MEIQIA_VISIT_ID=1JhRsmsBJRpXRK5aPLR1eYfaG3U; expire=1554962834212; UtzD_f52b_lastact=1554946013%09uc.php%09; yaozh_logintime=1554946364; yaozh_user=728478%09umsung; yaozh_userId=728478; yaozh_uidhas=1; yaozh_mylogin=1554946365; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1554946367; acw_tc=2f624a6715548584856626296e3d7bf5fd4df0e048c213322b156b89e54150; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1554858363%2C1554879242%2C1554945547%2C1554946367; kztoken=nJail6zJp6iXaJqWl25maWVuZ5qa; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZWV%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5qa%22%3B%7D'

}

        for i in range(2, 3):
            num = 10000000 + i
            yield scrapy.Request(url=self.url.format(num=int(num)), callback=self.parse, cookies=Cookie, headers=headers)


    def parse(self, response):
        print(response.text)
