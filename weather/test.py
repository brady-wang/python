from urllib import request,parse

import re
from bs4 import BeautifulSoup

url = "http://www.weather.com.cn/weather/101280601.shtml"
headers = {
    'User-Agent' : r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer':'http://www.weather.com.cn/weather/101280601.shtml',
    'Connection':'keep-alive'
}


try:
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    res = resp.read()
    soup = BeautifulSoup(res, 'lxml')
    print(soup.prettify())
    uls = soup.find('ul', class_='t clearfix')
    weather = []
    if uls is not None:
        lis = uls.find_all('li')
        i = 0
        for li in lis:
            day = li.h1.string.replace(r'\n','')
            wea = li.find('p',class_='wea').string.replace('\n','')
            tem = li.find('p',class_='tem').get_text().replace('\n','')
            win = li.find('p',class_='win').get_text().replace('\n','')
            weather.append({'day':day,'wea':wea,'tem':tem,'win':win})
        print(weather)
    else:
        print("未请求到数据")
except Exception as e:
    print(e)



