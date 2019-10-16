from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlwt
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

resp=requests.get('https://movie.douban.com/cinema/nowplaying/hangzhou/',headers = headers).text
print(resp)
soup=BeautifulSoup(resp,'html.parser')
list=soup.select('.list-item')
n_list=[]
for i in list: 
    n_dict={}
    name=i.get('data-title')
    id=i['id']
    n_dict['id']=id
    n_dict['name']=name
    n_list.append(n_dict)
print(n_list)