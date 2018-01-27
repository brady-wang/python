import urllib.request
import re
from bs4 import BeautifulSoup

url = "http://www.cnblogs.com/php-linux/default.html?page=1"
url_origin = "http://www.cnblogs.com/php-linux/default.html?page=";

try:
    res = urllib.request.urlopen(url)
    if(res.getcode() == 200) :
        soup = BeautifulSoup(res,'lxml')
        page = soup.find(id="stats_post_count")
        pages = page.string
        pattern = re.compile('\d+')
        a = re.search(pattern,str(pages))
        total_page = int(a.group()) // 10
        for i in range(1,total_page + 1):
            url1 = url_origin + str(i)
            print(url1)

except Exception as e:
    print(e)