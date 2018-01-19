import urllib.request,socket,re_test,sys,os

targetPath = "D:\\www\\spider\\03_images"


def saveFile(path):
    # 检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

        # 设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos + 1:])
    return t


# 用if __name__ == '__main__'来判断是否是在直接运行该.py文件


# 网址
url = "https://tieba.baidu.com/p/5519982610"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
}

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

for link, t in set(re_test.findall(r'(http[s]?:[\S]*?(jpg|png|gif|webp))', str(data))):

    print(link)
    try:
        urllib.request.urlretrieve(link, saveFile(link))
    except:
        print('失败')