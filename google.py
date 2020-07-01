import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import threading
import concurrent.futures
import subprocess
import random

class Browse():
    def __init__(self,url):
        super().__init__()
        self.browser =  webdriver.Chrome()
        self.cat_list = ["entertainment","sport","technology","www","news","politics",'business']
        self.new_url = 'https://www.giftalworld.com/category/'

        self.url = url

        self.browse(self.url)
        self.to_new_window()
        self.get_other()

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
        for i in range(len(self.cat_list)):
            new_url = self.new_url + self.cat_list[i]

            #s <a href="https://www.giftalworld.com/revival-of-ajaokuta-steel-will-save-nigeria-billions-of-dollars/" class="more-link">Read More</a>
            # # Open a new window
            new_window = self.browser.execute_script("window.open('');")
            # # # Switch to the new window and open URL B
            self.browser.switch_to.window(self.browser.window_handles[i])
            self.browser.get(new_url)
    
    def to_new_window(self):
        

        for count in range(len(self.cat_list)):
            new_url = self.new_url + self.cat_list[count]
            # # # Switch to the new window and open URL B
            self.browser.switch_to.window(self.browser.window_handles[count])
            self.browser.get(new_url)
            nav_feature = self.browser.find_elements_by_xpath("//p//a[@class='more-link'][contains(text(),'Read More')]")
            if nav_feature != []:
                nav_feature[1].click()
            else:
                return super(Browse,self).__init__(self.url)
                
    def get_other(self):
        try:
            while self.browser.current_url in self.url:
                time.sleep(3)
                if self.browser.find_element_by_xpath("//div/a[@rel='prev']"):
                    time.sleep(2)
                    self.browser.find_element_by_xpath("//div/a[@rel='prev']").click()
                else:
                    return super(Browse,self).__init__(self.url)
        except:
            return super(Browse,self).__init__(self.url)


# cat_list = ["entertainment","sports","technology","www","news","politics","news"]
url = 'https://www.giftalworld.com/login/'
Browse(url)