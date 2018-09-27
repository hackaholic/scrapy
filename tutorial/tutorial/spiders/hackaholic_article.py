import scrapy

class HackaholicSpider(scrapy.Spider):
    name = "hackaholic"

    def start_requests(self):
        urls = ['http://hackaholic.info']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.xpath('//article'):
            yield {
                    'title': article.xpath(".//h2[@class='entry-title']/a/text()").extract()[0],
                    'published_date': article.xpath(".//div[@class='entry-meta']/span/time[@class='onDate date published']/a/text()").extract()[0]
                   }
