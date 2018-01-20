import string
from urllib import request
from urllib.parse import quote

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        # Python 3.x中没有urllib2模块了，python3中是用urllib.request.urlopen()
        # 这里使用第三方库requests

        # response = requests.get(url, allow_redirects=False)
        # response.encoding = 'utf-8'
        # print(response.status_code)
        # if response.status_code != 200:   # 页面请求的状态值常用的有：200请求成功404文件未找到、500服务器错误
        #    return None
        # return response.text()

        url_ = quote(url, safe=string.printable)
        response = request.urlopen(url_)

        if response.getcode() != 200:
            return None

        return response.read()

