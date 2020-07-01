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
        self.to_new_window()
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
           
    def to_new_window(self):    
        # # # Switch to the new window and open URL B
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(self.new_url)

        self.forward_back()

        
        # if nav_feature != []:0124967712
        #     nav_feature[1].click() 22321955410
    def forward_back(self):
        for count in range(1,10):
            nav_feature1 = self.browser.find_elements_by_xpath("//p//a[@class='more-link'][contains(text(),'Read More')]")
            for i in range(1,len(nav_feature1)):
                nav_feature = self.browser.find_elements_by_xpath("//p//a[@class='more-link'][contains(text(),'Read More')]")

                nav_feature[i].click()
                time.sleep(2)
                self.browser.back()
            self.browser.get('https://www.giftalworld.com/category/' + self.category + '/page/' + str(count+1))
            print(count)

        # self.browser.execute_script("window.history.go(-1)")
        return self.forward_back()
    def click_each_marquee(self):
        each_marques = self.browser.find_elements_by_xpath("//div[@class='js-marquee-wrapper']//div[@class='js-marquee']//artical[@class='news-post-title']//span[@class='news-post-img']//a[@class='attachment-post-thumbnail']")
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(self.new_url)



                            
    def get_other(self):
        try:
            while self.browser.current_url in self.url:
                time.sleep(3)
                if self.browser.find_element_by_xpath("//div/a[@rel='prev']"):
                    time.sleep(2)
                    self.browser.find_element_by_xpath("//div/a[@rel='prev']").click()
                else:
                    return self.browse(url)
        except:
            return self.browse(url)
# cat_list = ["entertaicnment","sports","technology","www","news","politics","news"]
url = 'https://www.giftalworld.com/login/'
Browse(url,'politics')