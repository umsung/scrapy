# *-* coding:utf-8 *-*
import requests
import urllib.request


proxies = {
    "http": "http://127.0.0.1:9999",
    "https": "https://93.91.80.6:443"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
response = requests.get("https://mojim.com/cn104083x3.htm", headers=headers, proxies=proxies)
print(response.text)



# 如果代理需要设置账户名和密码,只需要将字典更改为如下：
# proxies = {
# "http":"http://user:password@127.0.0.1:9999"
# }
# 如果你的代理是通过sokces这种方式则需要pip install "requests[socks]"
# proxies= {
# "http":"socks5://127.0.0.1:9999",
# "https":"sockes5://127.0.0.1:8888"
# }





# # 调用ProxyHandler  代理IP的形式是字典
# # 付费的代理
# # money_proxy = {'协议':'username:pwd@IP:port'}
# px = urllib.request.ProxyHandler({'http': '93.91.80.6:443'})
# # 用build_opener()来构建一个opener对象
# opener = urllib.request.build_opener(px)
#
# # 然后调用构建好的opener对象里面的open方法来发生请求。
# # 实际上urlopen也是类似这样使用内部定义好的opener.open()，这里就相当于我们自己重写。
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
# res = urllib.request.Request('http://mojim.com/cn104083x3.htm', headers=headers)
# response = opener.open(res, timeout=3)
# print(response)
# re = response.read().decode('gbk')
# print(re)




# import requests
#
# response = requests.get("http://www.baidu.com")
# print(response.cookies)
# print(response.cookies.get_dict())
#
# for key,value in response.cookies.items():
#     print(key+"="+value)