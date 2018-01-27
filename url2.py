import json
from urllib import parse, request

url = r"http://wang.com/python/test_python.php"
headers = {
    'User-Agent':r'ozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    'Referer':r'http://www.tps138.brady1125/',
    'Connection':'keep-alive'
}
data = {
    'first':True,
    'pn':1,
    'kd':'Python'
}
try:
    data = parse.urlencode(data).encode('utf-8');
    req = request.Request(url, headers=headers, data=data)
    response = request.urlopen(req)

    content = response.read()
    obj = json.loads(content)
    print(obj['first'])
except Exception as e:
    print(e)

