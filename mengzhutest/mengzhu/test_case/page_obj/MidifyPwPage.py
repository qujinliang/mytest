#-*- coding=utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from .loginPage import login
from time import sleep

class midify(Page):

	'''
	   登录
	'''
	url = "/"

	#获取修改密码链接元素
	midify_password_loc = (By.CSS_SELECTOR,"[class = 'home-cur']")

	#Action
	def mengzhu_midify(self):
		self.find_element(*self.midify_password_loc).click()


	login_password_loc = (By.CSS_SELECTOR,"[name = 'password']")
	new_password_loc = (By.CSS_SELECTOR,"[name = 'repassword_1']")
	confirm_password_loc = (By.CSS_SELECTOR,"[name = 'repassword_2']")

	#登录密码
	def login_password(self,login_password):
		self.find_element(*self.login_password_loc).send_keys(login_password)


	#新密码
	def new_password(self,new_password):
		self.find_element(*self.new_password_loc).send_keys(new_password)

	#确认密码
	def confirm_password(self,confirm_password):
		self.find_element(*self.confirm_password).send_keys(confirm_password)




	


