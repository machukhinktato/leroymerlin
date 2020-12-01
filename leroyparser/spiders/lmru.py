import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroyparser.items import LeroyparserItem


class LmruSpider(scrapy.Spider):
    name = 'lmru'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://leroymerlin.ru/search/?sortby=8&tab=products&q=%D1%83%D0%BD%D0%B8%D1%82%D0%B0%D0%B7']

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@slot='name']/@href")
        next_page = response.xpath("//div[contains(@class, 'next-pag')]//@href").extract_first()
        for link in links:
            yield response.follow(link, callback=self.parse_leroy)
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_leroy(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyparserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('photo', "//img[@alt='product image']/@src")
        loader.add_xpath('desc', "//dl//dt/text()")
        loader.add_xpath('desc', "//dl//dd/text()")
        loader.add_value('url', response.url)
        yield loader.load_item()
