import scrapy

class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'https://www.brainyquote.com/authors/a_a_milne',
    ]

    def parse(self,response):
        for quote in response.css('.m-brick'):
            yield{
                'quote': quote.css('.b-qt::text').extract(),
                'author': quote.css('.bq-aut::text').extract()
            }
