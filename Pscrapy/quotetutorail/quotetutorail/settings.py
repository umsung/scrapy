# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
# Scrapy settings for quotetutorail project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# scrapy 分布式爬虫配置， 用scrapy_redis
# # 替换scrapy调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 添加去重的class,指纹判断
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # 添加pipeline
# # 如果添加这行配置，每次爬取的数据
# # 也都会入到redis数据库中，所以一般这里不做这个配置
# ITEM_PIPELINES = {
# 'scrapy_redis.pipelines.RedisPipeline': 300
# }
#
# # 共享的爬取队列，这里用需要redis的连接信息
# # 这里的user:pass表示用户名和密码，如果没有则为空就可以
REDIS_URL = 'redis://localhost:6379'
#
# # 设置为为True则不会清空redis里的dupefilter和requests队列
# # 这样设置后指纹和请求队列则会一直保存在redis数据库中，默认为False，一般不进行设置
#
# SCHEDULER_PERSIST = True
#
# # 设置重启爬虫时是否清空爬取队列
# # 这样每次重启爬虫都会清空指纹和请求队列,一般设置为False
# SCHEDULER_FLUSH_ON_START=True

# ----------------------------------------------------------

# 使用scrapy_mongodb， 无需链接和配置mongodb数据库，可直接把数据存入mongodb数据库
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'spider_world'
MONGODB_COLLECTION = 'dytt8'

# -------------------------------------------------------------

# 代理池和cookies链接
PROXY_POOL_URL = 'http://localhost:5000/GET'
COOKIES_POOL_URL = 'http://localhost:5000/weibo/random'

BOT_NAME = 'quotetutorail'

SPIDER_MODULES = ['quotetutorail.spiders']
NEWSPIDER_MODULE = 'quotetutorail.spiders'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'quotetutorail'

# HTTPERROR_ALLOWED_CODES = [400]
FEED_EXPORT_ENCODING = 'utf-8'

# scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：
# 默认json
# scrapy crawl weather -o spider.json

# json lines格式，默认为Unicode编码
# scrapy crawl weather -o spider..jl

# csv 逗号表达式，可用Excel打开
# scrapy crawl weather -o spider..csv

# xml格式
# scrapy crawl weather -o spider..xml

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'quotetutorail (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False



# HTTPERROR_ALLOWED_CODES = [403, 430]


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',

    'Cookie': 'kztoken=nJail6zJp6iXaJqWl25maWVuaZOZ; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOS%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuaZOZ%22%3B%7D; acw_tc=2f624a0b15547779373626962e2c454f3d12c9a51208a2d9d43b5811aad164; _ga=GA1.2.914088002.1554777939; MEIQIA_EXTRA_TRACK_ID=1Jby9OhcHRDm9UapjQCJf6v4k7q; _gid=GA1.2.1753007927.1554858488; UtzD_f52b_saltkey=KcT6zzbc; UtzD_f52b_lastvisit=1554854893; _ga=GA1.3.914088002.1554777939; bigdata_use_tips=1; UtzD_f52b_ulastactivity=1554775927%7C0; think_language=zh-CN; PHPSESSID=554uh18imjkus745n6barrf2n3; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D656992; UtzD_f52b_creditbase=0D0D4D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; MEIQIA_VISIT_ID=1JhRsmsBJRpXRK5aPLR1eYfaG3U; expire=1554962834212; UtzD_f52b_lastact=1554946013%09uc.php%09; yaozh_logintime=1554946364; yaozh_user=728478%09umsung; yaozh_userId=728478; yaozh_uidhas=1; yaozh_mylogin=1554946365; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1554946367; acw_tc=2f624a6715548584856626296e3d7bf5fd4df0e048c213322b156b89e54150; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1554858363%2C1554879242%2C1554945547%2C1554946367; kztoken=nJail6zJp6iXaJqWl25maWVuZ5qa; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZWV%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZeT%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZZuZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpaW%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpeS%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpqW%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuT%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZpuY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5OT%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl25maWVuZ5qa%22%3B%7D'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'quotetutorail.middlewares.QuotetutorailSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   # 'quotetutorail.middlewares.QuotetutorailDownloaderMiddleware': None,
   # 'quotetutorail.middlewares.PayLoadRequestMiddleware': None,
   'quotetutorail.middlewares.RandomUserAgentMiddleware': 500,
   # 'quotetutorail.middlewares.ProxyMiddleWare': 543,
   # 'quotetutorail.middlewares.JSPageMiddleware': 555,

}



# 随机更换如下ip,ip池
IPPOOL=[
        {"ipaddr": "111.225.8.231:9999"},
        {"ipaddr": "114.95.226.232:8118"},
        {"ipaddr": "119.31.210.170:7777"},
        {"ipaddr": "219.131.240.118:9797"},
        {"ipaddr": "219.159.38.200:56210"},
        {"ipaddr": "163.142.67.46:9000"},
        {"ipaddr": "27.46.21.20:888"}
]


# 随机更换userAgent
RANDOM_UA_TYPE = 'random'

# 设置用户代理池
UPPOOL = ["Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
]




# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'quotetutorail.pipelines.QuotetPipeline': 300,
   # 'quotetutorail.pipelines.ImgSavePipeline': 400,
   # 'quotetutorail.pipelines.JsonWriterPipeline': 500,
   #  'quotetutorail.pipelines.MysqlPipeline': 600,
    'quotetutorail.pipelines.MongoPipeline': 700,
   # 'quotetutorail.pipelines.TestPanadsPipline': 800,
   # 'quotetutorail.pipelines.ExcelPipline': 900,
   # 'quotetutorail.pipelines.EntePipline': 900,
   # 'scrapy_redis.pipelines.RedisPipeline': 300
   #  'scrapy_mongodb.MongoDBPipeline': 300   # 数据库存储 这里介绍一下scrapy-mongodb，也是超级好用，省去了自己链接和配置的麻烦，没有下载的童鞋，可以pip安装下，然后写入mongodb配置即可
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



