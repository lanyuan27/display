# -*- coding:utf-8 -*-
'''
@version: 23.3.2016
@author: yndots
'''
from Selenium2Library import Selenium2Library
from Selenium2Library.keywords import *
import time
from time import sleep

class _Basic(Selenium2Library):
    
    def __init__(self):
#         self.s2l=Selenium2Library()
        Selenium2Library.__init__(self)
    def my_open_browser(self):
        #自己的打开浏览器方法
        self.open_browser("https://10.138.19.6:8080", "ff")
        driver = self._current_browser()
        return driver
    def test_login(self):
        driver=self.my_open_browser()
        self.set_selenium_implicit_wait(10)
        
        self.input_text("id=username","admin")
        self.input_password("id=password","readwrite")
        self.click_button("id=submit")
        time.sleep(6)
        self.click_element("//*[@id='webui_nav_list']/li[3]/div")
        self.click_element("//a[contains(@href,'/network/controller')]")

        # time.sleep(3)      
        # driver.get("https://10.138.19.6:8080")
        # driver.find_element_by_name("email").clear()
        # driver.find_element_by_id("username").send_keys("admin")
        # driver.find_element_by_name("password").clear()
        # driver.find_element_by_id("password").send_keys("readwrite")
        # driver.find_element_by_id("submit").click()
        # driver.find_element_by_xpath("//*[@id='webui_nav_list']/li[3]/div").click()
        # driver.find_element_by_xpath("//a[@href='/dashboard/#gatewaywirelesscontroller']").click()
        # driver.find_element_by_xpath("//a[@href='/network/controller']").click()
if __name__ == '__main__':
    _Basic().test_login()