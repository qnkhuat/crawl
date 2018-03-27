import scrapy
# from selenium import webdriver
import time


class Facebookspider(scrapy.Spider):
    name = "scroll"
    start_urls = [
        'https://www.brainyquote.com/authors/martin_luther_king_jr'
    ]

    def __init__(self):
        self.browser = webdriver.Chrome()

        self.browser.get('https://www.brainyquote.com/authors/martin_luther_king_jr')
        self.scroll(3)

    def parse(self,response):
        yield('hello')

    def delay(self,times=3):
        time.sleep(times)

    def scroll(self,n):
        for i in range(n):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.delay(3)
