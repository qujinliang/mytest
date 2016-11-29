#-*- coding=utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''

    url = '/?ref=https%3A%2F%2Fb.mengzhu.tv%2F%23%2Faccount'

    #Action
    mengzhu_login_user_loc = (By.ID,'phoneNo')
    mengzhu_login_button_loc = (By.CLASS_NAME,"border-reg-c fl")

    '''
    def mengzhu_login(self):
        self.find_element(*mengzhu_login_user_loc).click()
        sleep(1)
        self.find_element(*mengzhu_login_button_loc).click()

    '''

    login_username_loc = (By.ID,"phoneNo")
    login_password_loc = (By.ID,"pwd_login")
    login_tutton_loc = (By.CSS_SELECTOR,"[tabindex='3']")

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录用密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_tutton_loc).click()

    #定义统一登录入口
    def user_login(self,username="13718369579",password="123456q"):
        """获取的用户名密码登录"""
        self.open()
        self.login_username(username)
        sleep(1)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.CSS_SELECTOR,"[class = 'error_username errors']")
    pawd_error_hint_loc = (By.CSS_SELECTOR,"[class = 'error_pwd errors']")
    user_login_success_loc = (By.CSS_SELECTOR,"[data-reactid='.0.0.0.0.2.0.1']")


    #用户名密码错误
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text


    #登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
