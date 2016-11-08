#-*- coding=utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''

    url = '/'

    #Action
    mengzhu_login_user_loc = (

