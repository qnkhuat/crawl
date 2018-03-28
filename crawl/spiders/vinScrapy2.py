
import scrapy
import argparse

class QuotesSpider(scrapy.Spider):
    name = "vins2"
    def start_requests(self):
        start_urls = []
        iterations=1000000
        vin='https://vingenerator.org/'
        [start_urls.append(vin) for i in range(iterations)]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)


    def parse(self,response):
        yield{
            'vin': response.css('.input::attr(value)').extract()[0]
        }
