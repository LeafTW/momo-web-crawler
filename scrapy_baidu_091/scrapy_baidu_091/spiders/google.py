import scrapy


class BaiduSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["www.google.com"]
    start_urls = ["http://www.google.com"]

    def parse(self, response):
        print("+0")
