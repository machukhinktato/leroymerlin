# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import Join

banana = []

def convert_to_int(string):
    integer = int(string.replace(' ', ''))
    return integer


def text_beautify(string):
    string = string.replace('\n', '').replace(' ', '')
    # banana.append(string)
    # print()
    # return banana
    return string


class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(convert_to_int), output_processor=TakeFirst())
    term = scrapy.Field(input_processor=MapCompose(text_beautify))
    definition = scrapy.Field(input_processor=MapCompose(text_beautify))
    _id = scrapy.Field()
    photo = scrapy.Field(input_proccesor=MapCompose())
    url = scrapy.Field(output_processor=TakeFirst())
    # banana = scrapy.Field(input_proccesor=MapCompose(text_beautify))
    print()
