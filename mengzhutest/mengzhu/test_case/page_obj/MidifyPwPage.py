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
	midify_password_loc = (By.CSS_SELECTOR,"[data-reactid = '.0.0.1.0.0.0.1.$0.1.$1']")

	#Action
	def mengzhu_midify(self):
		login(self.driver).user_login()
		sleep(2)
		self.find_element(*self.midify_password_loc).click()


	login_password_loc = (By.CSS_SELECTOR,"[name = 'password']")
	new_password_loc = (By.CSS_SELECTOR,"[name = 'repassword_1']")
	confirm_password_loc = (By.CSS_SELECTOR,"[name = 'repassword_2']")
	confirm_button_loc = (By.CSS_SELECTOR,"[data-reactid = '.0.0.1.0.0.1.0.2']")

	#登录密码
	def login_password(self,login_password):
		self.find_element(*self.login_password_loc).send_keys(login_password)


	#新密码
	def new_password(self,new_password):
		self.find_element(*self.new_password_loc).send_keys(new_password)

	#确认密码
	def confirm_password(self,confirm_password):
		self.find_element(*self.confirm_password_loc).send_keys(confirm_password)


	def confirm_button(self):
		self.find_element(*self.confirm_button_loc).click()

	def user_confirm_password(self,loginpwd="",newpwd="",confirmpwd=""):

		self.login_password(loginpwd)
		sleep(1)
		self.new_password(newpwd)
		sleep(1)
		self.confirm_password(confirmpwd)
		sleep(1)
		self.confirm_button()
		sleep(1)

	confirm_password_success_loc = (By.CSS_SELECTOR,"[data-reactid = '.1.1.$dialog.0.2.0']")

	#修改密码成功
	def confirm_password_success(self):
		return self.find_element(*self.confirm_password_success_loc).text





	


