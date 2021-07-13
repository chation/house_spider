import scrapy

from house_need.items import HouseNeedItem

class HouseSpider(scrapy.Spider):
    name = "house"
    start_urls = [
        'https://wh.58.com/zufang/sub/l89/s3741/j2/',
    ]

    def parse(self, response):
        item = HouseNeedItem()
        house_div = response.xpath("//li[@class='house-cell realverify']")

        for each in house_div :
            item['title'] = each.xpath(".//div[@class='des']//h2//a/text()").extract()[0].strip()
            item['far'] = each.xpath(".//div[@class='des']//p[@class='infor']/text()").extract()[3].strip()
            item['name'] = each.xpath(".//div[@class='des']//p[@class='infor']//a/text()").extract()[1].strip()
            item['area'] = each.xpath(".//div[@class='des']//p[@class='infor']//a/text()").extract()[0].strip()
            item['money'] = each.xpath(".//div[@class='list-li-right']//div[@class='money']//b/text()").extract()[0].strip()
            
            print(item)
        pass

