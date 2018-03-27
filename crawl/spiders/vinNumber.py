import scrapy
from selenium import webdriver
import time


class Facebookspider(scrapy.Spider):
    name = "vin"
    start_urls = [
        'http://randomvin.com/'
    ]


    def __init__(self):

        self.browser = webdriver.Chrome()


    def parse(self,response):
        self.browser.get('http://randomvin.com/')
        number = {}


        for i in range(1000):
            got = self.getNew()
            number[i]=got

        yield(number)


    def getNew(self):
        number = self.browser.execute_script("but= document.getElementById('button').click()")
        time.sleep(0.7)
        number = self.browser.execute_script("var dict= {};id=document.getElementById('Result');dict[1]= id.innerText ;return id.innerText")
        return number
