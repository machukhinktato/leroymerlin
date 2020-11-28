# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose


def convert_to_int(string):
    integer = int(string.replace(' ', ''))
    return integer

class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(convert_to_int), output_processor=TakeFirst())
    term = scrapy.Field(output_processor=TakeFirst())
    definition = scrapy.Field(output_processor=TakeFirst())
    _id = scrapy.Field()
    photo = scrapy.Field(input_proccesor=MapCompose())
    url = scrapy.Field(output_processor=TakeFirst())
    print()

