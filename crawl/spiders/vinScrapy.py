
import scrapy
import argparse

class QuotesSpider(scrapy.Spider):
    name = "vins"



    def start_requests(self):
        start_urls = []

        iterations=10

        vin='http://randomvin.com/getvin.php?type=real'
        [start_urls.append(vin) for i in range(iterations)]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)


    def parse(self,response):
        for code in response.css('p::text'):
            yield{
                'vin': code.extract(),
            }
