# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseNeedItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    room = scrapy.Field()
    size = scrapy.Field()
    far = scrapy.Field()
    name = scrapy.Field()
    area = scrapy.Field()
    pic = scrapy.Field()
    money = scrapy.Field()
