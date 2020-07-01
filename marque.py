import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import threading
import concurrent.futures
import subprocess

class Browse():
    def __init__(self,url,category):
        super().__init__()
        self.browser =  webdriver.Chrome()
        # self.cat_list = ["entertainment","sport","technology","www","news","politics",'business']
        self.category = category
        self.new_url = 'https://www.giftalworld.com/category/' + self.category

        self.url = url
        self.browse(self.url)
        # self.get_other()

    def browse(self,url):

        self.browser.get(url)
        # driver = By()
        time.sleep(2)
        username = 'username'
        password = 'password'
        time.sleep(2)
        credentials1 = self.browser.find_element_by_name('username').send_keys('IBTJ')
        time.sleep(1)
        credentials2 = self.browser.find_element_by_name('password').send_keys('172910249271Ade')

        submit_btn2 = self.browser.find_element_by_xpath("//button[@id='user_login_btn']")

        time.sleep(2)
        submit_btn2.click()


    def click_each_marquee(self):
            each_marques = self.browser.find_elements_by_xpath("//div[@class='js-marquee-wrapper']//div[@class='js-marquee']//artical[@class='news-post-title']//span[@class='news-post-img']//a[@class='attachment-post-thumbnail']")
            self.browser.execute_script("window.open('');")
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.get(self.new_url)

