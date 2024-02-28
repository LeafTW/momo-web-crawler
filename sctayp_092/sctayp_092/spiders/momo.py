import scrapy
from sctayp_092.items import Sctayp092Item
from scrapy.utils.project import get_project_settings

class MomoSpider(scrapy.Spider):
    name = "momo"
    allowed_domains = ["m.momoshop.com.tw"]
    start_urls = ["https://m.momoshop.com.tw/category.momo?cn=4201500000&page=1&sortType=6&imgSH=itemizedType&brandName=GARMIN&brandNoList=20160808155724727"]

    # 下一頁關鍵字
    nextKeyword='page='
    # 當前頁數Xpath位置
    haveNextXpath="//dd[@class='selected']/a/text()"
    # 抓取產品名稱位置
    getNameXpath='//*[@id="directory"]/div[2]/article[2]/ul/li/a/div[2]/h3/text()'

    # crawl 即執行
    def parse(self, response):
        print("responseURL"+response.url)
        if self.have_next(response):
            yield from self.scrape(response)
            nextUrl = self.processURL(response)
            yield scrapy.Request(nextUrl, callback=self.parse)
        else:
            print("==========run stop==============")
            return None

    # 判斷是否有下一行
    def have_next(self,response):
        print("have_next_STR===="+response.url)
        value=response.xpath(self.getNameXpath).get()
        if value != None:
            return True
        print("next is  None")
        return False

    # 處理url轉換下一頁網址
    def processURL(self,response):
        oldPageNumber=response.xpath(self.haveNextXpath).get()
        NewNextKeyword=(str)((int)(oldPageNumber)+1)
        print(self.nextKeyword+oldPageNumber+"  "+self.nextKeyword+NewNextKeyword)
        haveNextUrl=response.url.replace(self.nextKeyword+oldPageNumber,self.nextKeyword+NewNextKeyword)
        return haveNextUrl

    # 執行爬取
    def scrape(self,response):
        src=response.xpath('//*[@id="directory"]/div[2]/article[2]/ul/li/a/div/div/div[1]/img/@data-original')
        name=response.xpath(self.getNameXpath)
        price=response.xpath("(//span[@class='priceSymbol'])/b[@class='price']/text()")

        for number in range(0,len(name)):
            namep=name.extract()[number]
            srcp=src.extract()[number]
            pricep=price.extract()[number]
        #     print(namep +" "+ pricep +" "+srcp)
            watch=Sctayp092Item(name=namep,src=srcp,price=pricep)
            yield watch