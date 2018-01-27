from urllib import request, parse

try:
    data = {'id': 'name', 'age': "11", 'sex': 'man'}
    proxy = request.ProxyHandler({'http': '39.134.240.135:8080'})
    opener = request.build_opener(proxy)
    request.install_opener(opener=opener)
    data = parse.urlencode(data).encode('utf-8')
    url = r"https://www.baidu.com/"
    response = opener.open(url, data)
    content = response.read()
    print(content.decode('utf-8'))
except Exception as e:
    print(e)
