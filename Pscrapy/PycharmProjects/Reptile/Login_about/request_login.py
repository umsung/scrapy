import requests
from lxml import etree
from urllib.parse import urlencode

def get_token(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://glidedsky.com/login',
        'Host': 'glidedsky.com',
        'Connection': 'keep - alive',
        'Origin': 'http: // glidedsky.com',
        'Upgrade - Insecure - Requests': '1',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Cookie': '_ga = GA1.2.1884163979.1558064145;Hm_lvt_020fbaad6104bcddd1db12d6b78812f6 = 1558064145, 1558515373, 1558666318, 1558927123;_gid = GA1.2.1932643421.1558927123;XSRF - TOKEN = eyJpdiI6IjhTUURhRm5odHlUZjFMenlKZzdRWEE9PSIsInZhbHVlIjoiNkVyNThDaDRDVG80cVwvREFTZjFoQ3NWUFwvSHRqODM3TWg5QkVOUFZjcXZ5eGZIbFVGNVZXU1p1YzY3UkkwQ1dTIiwibWFjIjoiMmIyODFjNTY2YTc2NDE4YjlhODNhZWM4ZTA0ODA5Nzg2OGZmZDU5NWYyOTU1Y2YwMTU0ODNjZTVjOTgxMzE1MyJ9;glidedsky_session = eyJpdiI6IlNsVHFCd2FxM0FWN0ZKK0h6cGx5WlE9PSIsInZhbHVlIjoiWVZlWXFGQm1JZ2k3NWY4cVNwNFJJK2lcL01LK1piV3JKNjg3VnViOFRVSThkU1F2WncwOUdhWUZzSWdmQXZld0EiLCJtYWMiOiI2MjhmNDYyN2IzMGFjZDhjNDgyMTMxMWI1YWZjY2YwMmUzMDgyNDY2NDI1NWVlZTBmN2ZhYzM1YjQyNzU4YWM2In0 % 3D;Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6 = 1558944558;_gat_gtag_UA_75859356_3 = 1'

    # 'Set - Cookie': 'XSRF - TOKEN = eyJpdiI6InRqam9cL1ZjcFJOMHpVWmMyemhkQm9BPT0iLCJ2YWx1ZSI6InFrU2QxeEtyS1NYV3N5SFgrbVZubVU1RlF6TmpsMDc5ZkNUbTBReFVwSjlXZ3BzS2VTd1wvUDlUam40Y09pc2lEIiwibWFjIjoiYzA0Yjg2ZDdhMWIwZDgwZjg3ZTE5ZGQ1YzdjMjk2MzRmYTEzNzUwODRmMzYwMTYyZGJhOGFlZjQwYjVkN2IxZCJ9;expires = Mon, 27 - May - 2019 08: 58:03 GMT; Max - Age = 7200;path ='

    }
    s = requests.session()
    resp1 = s.get(url, headers=headers)
    selector = etree.HTML(resp1.text)
    _token = selector.xpath('//*[@id="app"]/main/div/div/div/div/div[2]/form/input/@value')[0]
    cookies1 = resp1.cookies.get_dict()
    print(cookies1)
    print(_token)
    login(url, _token, s)


def login(baseurl, token, s):
    data = {

        '_token': token,
        'email': '3238321252@qq.com',
        'password': '821874169'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://glidedsky.com/login',
        'Host': 'glidedsky.com',
        'Connection': 'keep - alive',
        'Origin': 'http: // glidedsky.com',
        'Upgrade - Insecure - Requests': '1',
        'Content - Type': 'application / x - www - form - urlencoded',
        # 'Cookie': '_ga = GA1.2.1884163979.1558064145;Hm_lvt_020fbaad6104bcddd1db12d6b78812f6 = 1558064145, 1558515373, 1558666318, 1558927123;_gid = GA1.2.1932643421.1558927123;XSRF - TOKEN = eyJpdiI6IjhTUURhRm5odHlUZjFMenlKZzdRWEE9PSIsInZhbHVlIjoiNkVyNThDaDRDVG80cVwvREFTZjFoQ3NWUFwvSHRqODM3TWg5QkVOUFZjcXZ5eGZIbFVGNVZXU1p1YzY3UkkwQ1dTIiwibWFjIjoiMmIyODFjNTY2YTc2NDE4YjlhODNhZWM4ZTA0ODA5Nzg2OGZmZDU5NWYyOTU1Y2YwMTU0ODNjZTVjOTgxMzE1MyJ9;glidedsky_session = eyJpdiI6IlNsVHFCd2FxM0FWN0ZKK0h6cGx5WlE9PSIsInZhbHVlIjoiWVZlWXFGQm1JZ2k3NWY4cVNwNFJJK2lcL01LK1piV3JKNjg3VnViOFRVSThkU1F2WncwOUdhWUZzSWdmQXZld0EiLCJtYWMiOiI2MjhmNDYyN2IzMGFjZDhjNDgyMTMxMWI1YWZjY2YwMmUzMDgyNDY2NDI1NWVlZTBmN2ZhYzM1YjQyNzU4YWM2In0 % 3D;Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6 = 1558944558;_gat_gtag_UA_75859356_3 = 1'

    # 'Set - Cookie': 'XSRF - TOKEN = eyJpdiI6InRqam9cL1ZjcFJOMHpVWmMyemhkQm9BPT0iLCJ2YWx1ZSI6InFrU2QxeEtyS1NYV3N5SFgrbVZubVU1RlF6TmpsMDc5ZkNUbTBReFVwSjlXZ3BzS2VTd1wvUDlUam40Y09pc2lEIiwibWFjIjoiYzA0Yjg2ZDdhMWIwZDgwZjg3ZTE5ZGQ1YzdjMjk2MzRmYTEzNzUwODRmMzYwMTYyZGJhOGFlZjQwYjVkN2IxZCJ9;expires = Mon, 27 - May - 2019 08: 58:03 GMT; Max - Age = 7200;path ='
    }

    # s = requests.session()
    resp2 = s.post(baseurl, data=data, headers=headers, verify=False, allow_redirects=False)
    print(resp2.status_code)
    print(resp2.headers)
    cookies2 = resp2.cookies.get_dict()
    print(cookies2)
    print(resp2.text)


    resp3 = s.get(resp2.headers['Location'], headers=headers,  cookies=cookies2)
    print(resp3.text)

    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://glidedsky.com/level/web/crawler-javascript-obfuscation-1?page=7',
        'Host': 'glidedsky.com',
        'Proxy-Connection': 'keep - alive',
        'X - Requested - With': 'XMLHttpRequest'
        # 'Cookie': '_ga = GA1.2.1884163979.1558064145;Hm_lvt_020fbaad6104bcddd1db12d6b78812f6 = 1558064145, 1558515373, 1558666318, 1558927123;_gid = GA1.2.1932643421.1558927123;XSRF - TOKEN = eyJpdiI6IjhTUURhRm5odHlUZjFMenlKZzdRWEE9PSIsInZhbHVlIjoiNkVyNThDaDRDVG80cVwvREFTZjFoQ3NWUFwvSHRqODM3TWg5QkVOUFZjcXZ5eGZIbFVGNVZXU1p1YzY3UkkwQ1dTIiwibWFjIjoiMmIyODFjNTY2YTc2NDE4YjlhODNhZWM4ZTA0ODA5Nzg2OGZmZDU5NWYyOTU1Y2YwMTU0ODNjZTVjOTgxMzE1MyJ9;glidedsky_session = eyJpdiI6IlNsVHFCd2FxM0FWN0ZKK0h6cGx5WlE9PSIsInZhbHVlIjoiWVZlWXFGQm1JZ2k3NWY4cVNwNFJJK2lcL01LK1piV3JKNjg3VnViOFRVSThkU1F2WncwOUdhWUZzSWdmQXZld0EiLCJtYWMiOiI2MjhmNDYyN2IzMGFjZDhjNDgyMTMxMWI1YWZjY2YwMmUzMDgyNDY2NDI1NWVlZTBmN2ZhYzM1YjQyNzU4YWM2In0 % 3D;Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6 = 1558944558;_gat_gtag_UA_75859356_3 = 1'

    # 'Set - Cookie': 'XSRF - TOKEN = eyJpdiI6InRqam9cL1ZjcFJOMHpVWmMyemhkQm9BPT0iLCJ2YWx1ZSI6InFrU2QxeEtyS1NYV3N5SFgrbVZubVU1RlF6TmpsMDc5ZkNUbTBReFVwSjlXZ3BzS2VTd1wvUDlUam40Y09pc2lEIiwibWFjIjoiYzA0Yjg2ZDdhMWIwZDgwZjg3ZTE5ZGQ1YzdjMjk2MzRmYTEzNzUwODRmMzYwMTYyZGJhOGFlZjQwYjVkN2IxZCJ9;expires = Mon, 27 - May - 2019 08: 58:03 GMT; Max - Age = 7200;path ='

    }

    params = {
        'page': '7',
        't': '1558946047',
        'sign': 'c50cd70cea6e71f1a7f138379fde86cf10756669'
    }

    resp4 = s.get('http://glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?' + urlencode(params), headers=headers2,  cookies=cookies2)
    print(resp4.text, resp4.status_code)

url = 'http://glidedsky.com/login'

get_token('http://glidedsky.com/login')