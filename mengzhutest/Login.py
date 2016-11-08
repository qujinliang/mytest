#-*- coding = utf-8 -*-
from selenium import webdriver
import time

br = webdriver.Firefox()
url1 = 'http://www.baidu.com'

br.get(url1)
br.maximize_window()

try:
    br.find_element_by_id("kw").send_keys("selenium")
    time.sleep(2)
    br.find_element_by_id("su").click()
except BaseException:
    print("没找到元素")
    br.quit()

time.sleep(5)

br.quit()
