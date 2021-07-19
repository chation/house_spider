import scrapy

from house_need.items import HouseNeedItem

class HouseAnjuke(scrapy.Spider):
    name = "anjuke"
    start_urls = [
        # 2号线 杨家湾 两室 整租
        'https://wh.zu.anjuke.com/ditie/dt89-s3741-x1-fx2/',
    ]

    def parse(self, response):
        item = HouseNeedItem()
        house_div = response.xpath("//div[@class='zu-itemmod']")

        for each in house_div :
            item['source']= 2
            item['title'] = each.xpath(".//div[@class='zu-info']//h3//a//b/text()").extract()[0].strip()
            item['far']   = each.xpath(".//div[@class='zu-info']//p[@class='details-item bot-tag']//span[last()]/text()").extract()[0].strip()
            item['name']  = each.xpath(".//div[@class='zu-info']//address[@class='details-item']//a/text()").extract()[0].strip()
            item['area']  = each.xpath(".//div[@class='zu-info']//address[@class='details-item']/text()").extract()[1].strip()
            item['money'] = each.xpath(".//div[@class='zu-side']//p//strong//b/text()").extract()[0].strip()
            
            print(item)
            yield item

