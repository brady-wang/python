import urllib.request

def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def saveHtml(file_name,file_content):
    with open(file_name.replace('/','_')+'.html','wb') as f:
        f.write(file_content)

for i in range(1,20):
    html = getHtml("http://tieba.baidu.com/p/3439301111?pn="+ str(i))
    saveHtml("test"+ str(i),html)
    print("下载成功"+"test"+ str(i))
print("结束")