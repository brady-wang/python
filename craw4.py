# -*- coding: utf-8 -*-
import re_test
import urllib
import os.path


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html, p):
    reg = r'<img src="(http://img\.7160\.com.+\.jpg)" '
    imgre = re_test.compile(reg)
    imglist = re_test.findall(imgre, html)
    x = 0;
    for imgurl in imglist:
        print
        os.path.basename(imgurl)
        y = str(p) + '-' + str(x);
        urllib.urlretrieve(imgurl, './images/%s.jpg' % y)
        x += 1



for i in range(2, 36 + 1):
    url = "http://www.7160.com/meinv/38343/index_" + str(i) + ".html"
    html = getHtml(url)
    getImg(html, p=i)
