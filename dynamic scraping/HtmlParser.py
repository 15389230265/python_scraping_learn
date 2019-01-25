# coding:utf-8
import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser_url(self, page_url, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls is not None:
            return list(set(urls))
        else:
            return None

    # def parser_json(self, page_url, response):

