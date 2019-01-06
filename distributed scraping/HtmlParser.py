# coding:utf-8
import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        bdzd_content = soup.find("div", class_="content-wrapper")
        # print(bdzd_content)
        links = bdzd_content.find_all('a', href=re.compile(r'/item/[%..]+[/\d+]?'), limit=3)
        for link in links:
            # print(link)
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        if summary is None:
            data['summary'] = None
        else:
            data['summary'] = summary.get_text()
        # print(data)
        return data
