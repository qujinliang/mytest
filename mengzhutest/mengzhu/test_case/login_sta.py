#-*- coidng:utf-8 -*-
from time import sleep
import unittest,random ,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login 

class loginTest(myunit.MyTest):
	"""盟主登录测试"""

	#测试用户登录

	def user_login_verify(self,username="",password=""):
		login(self.driver).user_login(username,password)




	def test_login1(self):
		'''用户名、密码为空登录'''
		self.user_login_verify()
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(),"请输入您的手机号码")
		self.assertEqual(po.pawd_error_hint(),"请输入您的密码")
		function.insert_img(self.driver,"user_pawd_empty.jpg")


	def test_login2():
		'''用户名正确，密码为空登录'''
		self.user_login_verify(username='13700001231')
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(),"密码不能为空")
		function.insert_img(self.driver,"pawd_empty.jpg")

		#pass
	 
	def test_login3():
		'''用户名为空，密码正确'''
		self.user_login_verify(password='123456q')
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(),"账号不能为空")
		function.insert_img(self.driver,"user_empty.jpg")

		#pass

	def test_login4():
		'''用户名与密码不匹配'''
		#character = random.choice(1-9)
		username = "13718369579"
		self.user_login_verify(username=username,password="123456qjl")
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(),"密码与账号不匹配")
		function.insert_img(self.driver,"user_pawd_error.jpg")

	def test_login5(self):
		'''用户名、密码正确'''
		self.user_login_verify(username='13718369579',password='123456q')
		sleep(2)
		po = login(self.driver)
		#print(po.user_login_success()[0:4])
		self.assertEqual(po.user_login_success()[0:4],'test')
		function.insert_img(self.driver,"user_pawd_ture.jpg")
	

if __name__ == '__main__':
	unittest.main()

