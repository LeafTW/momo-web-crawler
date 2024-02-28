import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from sxrapy_101.items import Sxrapy101Item

class MomoSpider(CrawlSpider):
    name = "momo"
    allowed_domains = ["m.momoshop.com.tw"]
    start_urls = [
        "https://m.momoshop.com.tw/category.momo?cn=4201500000&page=1"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'/html/body/div[2]/div[6]/dl/dd/a'),),
    )

    def parse_item(self, response):
        print("=============start==============")
        src = response.xpath('//*[@id="directory"]/div[2]/article[2]/ul/li/a/div/div/div[1]/img/@data-original')
        name = response.xpath('//*[@id="directory"]/div[2]/article[2]/ul/li/a/div[2]/h3/text()')
        price = response.xpath("(//span[@class='priceSymbol'])/b[@class='price']/text()")
        for number in range(0, len(name)):
            namep = name.extract()[number]
            srcp = src.extract()[number]
            pricep = price.extract()[number]
            print(namep + " " + pricep + " " + srcp)
            watch = Sxrapy101Item(name=namep, src=srcp, price=pricep)
            yield watch
        print("=============end==============")

    # allowed_domains = ['www.dushu.com']
    # start_urls = ['https://www.dushu.com/book/1188_1.html']
    #
    # rules = (
    #     Rule(LinkExtractor(allow=r'/book/1188_\d+.html'),
    #                        callback='parse_item',
    #                        follow=True),
    # )
    #
    # def parse_item(self, response):
    #
    #     img_list = response.xpath('//div[@class="bookslist"]//img')
    #
    #     for img in img_list:
    #         name = img.xpath('./@data-original').extract_first()
    #         src = img.xpath('./@alt').extract_first()
    #
    #         book = Sxrapy101Item(name=name,src=src)
    #         yield book