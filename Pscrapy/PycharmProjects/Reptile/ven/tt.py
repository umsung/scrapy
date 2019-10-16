import requests

url = 'http://mall.wine-world.com/'

s = requests.session()
r = s.get(url)
# print(r.content.decode('utf-8'))
print(r.headers)