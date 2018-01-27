import urllib.request
from bs4 import BeautifulSoup
import re


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

url = "https://tieba.baidu.com/p/5407739329?see_lz=1"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

soup = BeautifulSoup(response,'lxml')

try:
    #获取总页数
    a = soup.find(text=re.compile("回复贴"))
    total_page = a.find_next_sibling('span').string
    total_page = int(total_page)

    if total_page > 0 :
        for j in range(1,int(total_page) + 1):
            url = "https://tieba.baidu.com/p/5407739329?see_lz=1&pn="+str(j)
            request1 = urllib.request.Request(url)
            response1 = urllib.request.urlopen(request1)
            soup1 = BeautifulSoup(response1, 'lxml')
            title = soup1.title.string
            link = soup1.find_all('img',class_="BDE_Image")
            i = 1
            for li in link :
                print(li.get('src'))
                file_name = "D:/www/spider/" + validateTitle(title) + str(j) +"-"+ str(i) + ".jpg"
                print(file_name)
                urllib.request.urlretrieve(li.get('src'),file_name)
                i = i + 1
except Exception as e:
    print(e)
