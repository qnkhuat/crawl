from selenium import webdriver
import scrapy


class OneWord(scrapy.Spider):
    name='oneword'
    start_urls=['http://www.dictionary.com/wordoftheday/2018/02/21']



    def parse(self,response):
        # link=response.xpath('//*[@class="tile-image"]/a/img/@src')

        # word = response.xpath('//*[@class="definition-header"]/h1/strong/text()').extract()

        # link,word=get()
        link=get_info()



        yield{
            'link':link
            # 'word':word
            # 'definitions':defs
        }


    def get_info(self):
        link = self.browser.execute_script('image=document.getElementsByClassName("tile-image");link=image[0].getElementsByTagName("img")[0].src;return link;')
