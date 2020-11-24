import scrapy
from scrapy.http import HtmlResponse
from pprint import pprint
from scrapy.loader import ItemLoader


class LmruSpider(scrapy.Spider):
    name = 'lmru'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/search/?q=%D0%BA%D1%83%D0%B2%D0%B0%D0%BB%D0%B4%D0%B0']

    def parse(self, response:HtmlResponse):
        links = response.xpath("//a[@slot='name']/@href")
        for link in links:
            yield response.follow(link, callback=self.parse_leroy)
        print()
        pass

    def parse_leroy(self, response:HtmlResponse):
        name = response.xpath("//h1/text()").extract_first()
        params = response.xpath("//dl[@class='def-list']")
        print()