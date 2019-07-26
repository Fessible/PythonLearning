# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector.unified import SelectorList


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        print('=' * 20)
        duanzi_list = response.xpath("//div[@id='content-left']/div")
        for duanzi in duanzi_list:
            author = duanzi.xpath(".//h2/text()").get()
            content = duanzi.xpath(".//div[@class='content']//text()").getall()
            print(author)
            print(''.join(content).strip())
            print('-' * 30)

            yield {'author': author, 'content': content}

        print('=' * 20)
