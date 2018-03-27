import scrapy

class QuotesSpider(scrapy.Spider):
    name = "brainy"
    start_urls = [
        'https://www.brainyquote.com/authors',
    ]


    def parse(self,response):

        for link in response.css('.bqLn a::attr(href)'):
            yield response.follow(link, callback=self.scrape)


    def scrape(self,response):

        for quote in response.css('.m-brick'):
            yield{
                'quote': quote.css('.b-qt::text').extract(),
                'author': quote.css('.bq-aut::text').extract()
            }
