#-*- coidng:utf-8 -*-
from time import sleep
import unittest,random ,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.midifyPwPage import midify



class midifyTest(myunit.MyTest):


	def confirm_pawd_verify(self,loginpwd='',newpwd='',confirmpwd=''):
		midify(self.driver).user_confirm_password(loginpwd,newpwd,confirmpwd)


	def confirm_longin(self):
		midify(self.driver).mengzhu_midify()

	def test_midify1(self):
		self.confirm_longin()

		self.confirm_pawd_verify()
		po = midify(self.driver)
		self.assertEqual(po.login_password_error_hint(),'密码不能为空')
		self.assertEqual(po.new_password_error_hint(),'新密码不能为空')
		self.assertEqual(po.confirm_password_error_hint(),'确认新密码不能为空')
		function.insert_img(self.driver,"confirm_pawd_empty.jpg")




	def test_midify5(self):
		self.confirm_longin()

		self.confirm_pawd_verify(loginpwd='123456q',newpwd='123456789q',confirmpwd='123456789q')
		sleep(2)
		po = midify(self.driver)
		#print (po.confirm_password_success())
		self.assertEqual(po.confirm_password_success(),'密码修改成功')
		po.confirm_password_button()
		function.insert_img(self.driver,"confirm_pawd_ture.jpg")
		sleep(1)
		self.confirm_pawd_verify(loginpwd = '123456789q', newpwd = '123456q', confirmpwd = '123456q')
		po.confirm_password_button()







if __name__ == '__main__':
	unittest.main()