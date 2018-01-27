import string
import urllib.request
from urllib.parse import quote

#下载网页
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        url_ = quote(url, safe=string.printable)#去除特殊字符
        response = urllib.request.urlopen(url_)
        if response.getcode() != 200:
            return None

        return response.read()
