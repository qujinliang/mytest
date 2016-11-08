from selenium import webdriver

dr = webdriver.Firefox()
dr.get("https://www.mengzhu.tv/")


cookie = dr.get_cookies()
#name = dr.get_cookies(name)

print(cookie)
#print(name)
