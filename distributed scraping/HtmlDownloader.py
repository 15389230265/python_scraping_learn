# coding:utf-8
import requests
from requests import exceptions


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            print("url is None!")
            return None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'user-Agent': user_agent}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                r.encoding = 'utf-8'
                return r.text
        except exceptions.Timeout:
            print("请求超时")
            pass
        except exceptions.ConnectionError:
            print("发生连接错误")
            pass

        print("cannot connect {}!".format(url))
        return None