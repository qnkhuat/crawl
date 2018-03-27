import scrapy
from urllib.parse import urljoin
from crawl.items import CrawlItem
class QuotesSpider(scrapy.Spider):
    name = "image"

    def start_requests(self):
        urls = [
            'https://www.brainyquote.com/authors'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):

        for link in response.css('.bqLn a::attr(href)'):
            yield response.follow(link, callback=self.scrape)

    def scrape(self,response):
        preLink='https://www.brainyquote.com'
        for src in response.css('.bqpht::attr(src)').extract():
            item= CrawlItem()
            item['image_urls']=[urljoin(response.url,preLink+src )]
            yield item
