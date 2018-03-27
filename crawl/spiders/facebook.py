import scrapy
from selenium import webdriver
import time


class Facebookspider(scrapy.Spider):
    name = "facebooks"
    start_urls = [
        'https://www.brainyquote.com/authors'
    ]


    def __init__(self):

        self.browser = webdriver.Chrome()


    def delay(self,times=3):
        time.sleep(times)

    def parse(self,response):
        links={}
        self.login()
        self.cancleWindow()
        self.to_friend()
        self.scroll(7)
        links = self.browser.execute_script("a=document.getElementsByClassName('fcb');var dict = {};for (i = 0; i < a.length; i++) {link=a[i].firstElementChild.getAttribute('href');dict[i]=link;}; return dict;")
        self.delay(1)

        yield(links)

    def cancleWindow(self):
        self.browser.execute_script("document.getElementsByClassName('layerCancel')[0].click();;")
        self.delay()


    def scroll(self,n):
        for i in range(n):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.delay()
    def login(self):
        EMAIL = 'qn.khuat'
        PASSWORD = 'Qnkhuat.qnkhuat98fb'
        self.browser.get('http://facebook.com')
        time.sleep(1)
        username = self.browser.find_element_by_id("email")
        password = self.browser.find_element_by_id("pass")
        username.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        login_attempt = self.browser.find_element_by_xpath("//*[@id='loginbutton']/input")
        login_attempt.submit()
        self.delay()

    def to_friend(self):
        self.browser.get('https://www.facebook.com/trung.hongoc/friends')
        self.delay()
