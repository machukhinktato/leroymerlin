import scrapy
from scrapy.http import HtmlResponse


class LmruSpider(scrapy.Spider):
    name = 'lmru'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/search/?q=%D0%BE%D0%B1%D0%BE%D0%B8&family=00b9b5a0-faeb-11e9-810b-878d0b27ea5b&suggest=true']

    def parse(self, response:HtmlResponse):
        print()
        pass
