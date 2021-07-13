import scrapy

class QuotesSpider(scrapy.Spider):
    name = "house"
    start_urls = [
        'https://wh.58.com/chuzu/sub/l89/s3741/',
    ]

    def parse(self, response):
        pass

