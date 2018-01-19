import urllib.request
#urllib learning
request = urllib.request.Request(r"http://www.baidu.com")

response = urllib.request.urlopen(request)

html = response.read()

html = html.decode("utf8")
print(html)