import scrapy
import argparse
import urllib

parser=argparse.ArgumentParser()
parser.add_argument('-l')
args= parser.parse_args()

class QuotesSpider(scrapy.Spider):
    name = "udemy"
    def start_requests(self):
        start_urls = []
        iterations=1000000
        url=args.l


        yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)

    def parse(self,response):
        boxes=response.css('.course-image--card--left-col--1_8cb')
        for box in boxes:

            yield{
                'vin': response.css('.input::attr(value)').extract()[0]
            }
