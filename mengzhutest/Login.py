#-*- coding = utf-8 -*-
from selenium import webdriver
import time

br = webdriver.Firefox()
url1 = 'https://u.mengzhu.tv/?ref=https://www.mengzhu.tv/'

br.get(url1)
br.maximize_window()

try:
    br.find_element_by_id("phoneNo").send_keys("13718369579")
    time.sleep(2)
    br.find_element_by_id("pwd_login").send_keys('123456q')
    time.sleep(2)
    
    br.find_element_by_css_selector("[tabindex='3']").click()
except BaseException:
    print("没找到元素")
    br.quit()

time.sleep(5)

br.quit()
