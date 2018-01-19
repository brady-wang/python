import urllib.request

def save_file(data):
    path = "D:\\www\\spider\\02_douban.html"
    f = open(path,'wb')
    f.write(data)
    f.close()

url = "https://www.douban.com/"
headers = {'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
req = urllib.request.Request(url=url,headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

save_file(data)

data = data.decode('utf-8')

print(data)
print(res.geturl())
print(res.info())
print(res.getcode())