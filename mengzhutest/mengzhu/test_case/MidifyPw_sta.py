#-*- coidng:utf-8 -*-
from time import sleep
import unittest,random ,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.MidifyPwPage import midify



class midifyTest(myunit.MyTest):

	def test_midify1(self):
		login(self.driver).user_login()
		




if __name__ == '__main__':
	unittest.main()