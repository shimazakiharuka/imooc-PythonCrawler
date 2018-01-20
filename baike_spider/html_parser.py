import re
import urllib

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):   # html_cont即下载器返回的response.text
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data

    def get_new_urls(self, page_url, soup):
        new_urls = set()   # 找到新的url放入set中
        links = soup.find_all('a', href=re.compile(r"/item/"))   # 网址有变，表达式做了调整
        for link in links:
            new_url = link['href']   # link是一个字典，link["herf"]就是找到“herf”的键值
            # 使用urljoin通过url拼接从相对路径获取绝对路径,
            # Py3中用到的模块名称变为urllib.parse
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            # print('url拼接：', page_url, new_url, new_full_url)   # 查看如何拼接
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):   # 获取标题title和简介summary作为我们要抓取的数据
        res_data = {}   # 一个字典,即键值对存放数据
        # url
        res_data['url'] = page_url

        # 审查元素获得title为 <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is not None:
            res_data['summary'] = summary_node.get_text()

        return res_data
