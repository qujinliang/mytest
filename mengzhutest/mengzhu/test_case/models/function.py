from selenium import webdriver
import os

#截图函数
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.mengzhu.tv")
    insert_img(driver,'baidu.jpg')
    driver.quit()
