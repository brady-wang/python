from urllib import request

response = request.urlopen(r'http://www.baidu.com')
page = response.read()
page = page.decode('utf-8')
print(response.getcode())
print(response.info())
print(response.reason)
print(response.geturl())