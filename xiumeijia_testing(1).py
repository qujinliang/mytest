#coding=utf-8
import unittest
import time,os, re
from selenium.common.exceptions import NoSuchElementException
import HTMLTestRunner

from selenium import webdriver

driver  = webdriver.Chrome()
wait_time = 15


h5_base_url = "http://m.quxiu8.com"		#H5地址
web_base_url = "http://dianpu.quxiu8.com"		#web商铺后台地址
user_name = "18811169392"
user_pass = "123456"
store_name ="秀美甲自动测试店"
search_store_name="@@秀美甲自动测试店"
store_red_packet_id = '15240'

#支付宝账户
account = '18811169392'
accout_login_password = 'duan528'
accout_pay_password = '150528'

class Coupons(unittest.TestCase):
	"""1.团购h5下单0.01元; 2.商铺后台验证消费码"""

	def setUp(self):
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_coupons_pay_order_1(self):
		"""1.h5购买团购,并验证订单状态和价格显示"""
		h5_login()
		time.sleep(wait_time)
		driver.find_element_by_link_text("抢便宜").click()
		time.sleep(wait_time)
		driver.find_element_by_xpath("//input[@class='search-input']").send_keys(search_store_name)
		driver.find_element_by_link_text("搜索").click()
		time.sleep(wait_time)
		driver.find_element_by_xpath("//div[@class='text-memo']/p[span='￥0.01']").click()
		time.sleep(wait_time)
		driver.find_element_by_link_text("立即抢购").click()
		time.sleep(wait_time)
		driver.find_element_by_id("btn_submit").click()
		time.sleep(wait_time)
		driver.find_element_by_id("btn_submit").click()
		time.sleep(wait_time)
		driver.find_element_by_id("logon_id").send_keys(account)
		driver.find_element_by_id("pwd_unencrypt").send_keys(accout_pay_password)
		driver.find_element_by_xpath("//div[button='登录']").click()
		time.sleep(wait_time)
		driver.find_element_by_xpath("//div[button='确认付款']").click()
		time.sleep(wait_time)
		driver.find_element_by_link_text("返回商户").click()
		time.sleep(wait_time)

		Subscribe_home_service.order_number = ''
		Subscribe_home_service.order_number = driver.find_element_by_xpath("//div[@class='main-content']/p[@class='memo']/strong").text
		driver.find_element_by_link_text("查看我的团购").click()
		time.sleep(wait_time)

		#验证我的团购中的支付信息是否正确
		real_total_price = ''
		real_total_price = driver.find_element_by_xpath("//div[@class='dt-info']/p[span='总价：']").text
		expect_total_price = '总价：0.01元'
		self.assertEqual(real_total_price,expect_total_price)

		real_off_price = ''
		real_off_price = driver.find_element_by_xpath("//div[@class='dt-info']/p[span='优惠：']").text
		expect_off_price = '优惠：0元'
		self.assertEqual(real_off_price,expect_off_price)

		real_payed_price = ''
		real_payed_price = driver.find_element_by_xpath("//div[@class='dt-info']/p[span='实付：']").text
		expect_payed_price = '实付：0.01元'
		self.assertEqual(real_payed_price,expect_payed_price)

		#获取支付消费码
		Subscribe_home_service.consumption_code = ''
		Subscribe_home_service.consumption_code = driver.find_element_by_xpath("//div[@class='vouchers']/p[span='消费密码：']").text
		Subscribe_home_service.consumption_code = Subscribe_home_service.consumption_code[5:17]
		h5_logout()

	def test_coupons_pay_order_2(self):
		"""2.商铺后台验证团购消费码,并查看状态和金额 """
		web_login()
		driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='交易验证']").click()
		time.sleep(wait_time)
		driver.find_element_by_id("subcheckManagement").find_element_by_id("Voucher_children2").click()
		time.sleep(wait_time)

		driver.find_element_by_id("txtPwd").send_keys(Subscribe_home_service.consumption_code)
		driver.find_element_by_link_text("获取详情").click()
		time.sleep(wait_time)
		#验证团购名称和价格
		real_coupons_name = ''
		real_coupons_name = driver.find_element_by_class_name("dt-details").find_element_by_class_name("dt-title").text
		expect_coupons_name = '团购名称：5元可使用红包款式'
		self.assertEqual(real_coupons_name,expect_coupons_name)

		real_coupons_price = ''
		real_coupons_price = driver.find_element_by_xpath("//div[@class='dt-right']/div[@class='dt-text1']/span").text
		expect_coupons_price = '￥0.01元'
		self.assertEqual(real_coupons_price,expect_coupons_price)
		#使用消费码
		driver.find_element_by_id("btn-use").click()
		time.sleep(wait_time)
		alert = driver.switch_to_alert()
		time.sleep(wait_time)
		alert.accept()
		time.sleep(wait_time)
		#验证消费码已消费
		real_coupons_status = ''
		real_coupons_status = driver.find_element_by_id("state").text
		expect_coupons_status = '已使用'
		self.assertEqual(real_coupons_status,expect_coupons_status)
		time.sleep(wait_time)
		web_logout()

	def tearDown(self):
		self.assertEqual([],self.verificationErrors)
		#driver.quit()

"""1.h5预约上门先付款下单原价5.01元，使用红包5元，实付0.01元 2.商铺后台验消费码并查看状态和金额 3.商铺后台发起补款 4.h5检查预约信息"""
class Subscribe_home_service(unittest.TestCase):
		order_number =''
		consumption_code = ''
		print("执行预约上门先付款测试")
		def setUp(self):
			self.verificationErrors = []
			self.accept_next_alert = True

		def test_subscribe_1(self):
			"""1.h5预约上门下单 ,并查看预约状态和金额显示"""
			h5_login()
			time.sleep(wait_time)
			driver.find_element_by_link_text("做美甲").click()
			time.sleep(wait_time)
			#查看店铺列表
			driver.find_element_by_xpath("//a[span='店铺']").click()
			time.sleep(wait_time)
			#搜索店铺
			search = driver.find_element_by_xpath("//input[@class='search-input']").send_keys(search_store_name)
			time.sleep(wait_time)
			driver.find_element_by_id("search-btn").click()
			time.sleep(wait_time)
			#打开店铺详情页
			driver.find_element_by_id("shop-list-key").click()
			time.sleep(wait_time)
			#领取5元店铺红包
			driver.find_element_by_id("redlist").find_element_by_xpath("//a[@data-id='15240']").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[@class='input-content']").find_element_by_link_text("确认").click()
			time.sleep(wait_time)
			#打开款式
			driver.find_element_by_id("wf-main-style").find_element_by_xpath("//p[span='￥5.01']").click()
			time.sleep(wait_time)
			#点击“立即预约”
			driver.find_element_by_xpath("//a[@class='buy-btn']").click()
			time.sleep(wait_time)
			#点击“预约上门”
			driver.find_element_by_xpath("//li[contains(.,'预约上门')]").click()
			time.sleep(wait_time)
			#填写预约信息并提交预约
			driver.find_element_by_id("txt-name").send_keys("罗勾勾")
			driver.find_element_by_id("txt-date").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[@role='dialog']").find_element_by_link_text("确定").click()
			driver.find_element_by_id("txt-address").send_keys("三里屯")
			time.sleep(wait_time)
			submit_order = driver.find_element_by_link_text("提交预约")
			driver.execute_script('$(arguments[0]).click()',submit_order)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//section[@class='red-info']/ul/li/span[contains(.,'未使用')]").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//li[@class='red-list']/ol/li[@data-val='5']").click()
			time.sleep(wait_time)

			real_total_price = ''
			expect_total_price = ''
			real_total_price = driver.find_element_by_xpath("//section[@class='red-info']").find_element_by_id("showprice").text
			expect_total_price = '5.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_paying_price = ''
			expect_paying_price = ''
			real_paying_price = driver.find_element_by_id("allprice").text
			expect_paying_price = '0.01'
			self.assertEqual(real_paying_price,expect_paying_price)
			#点击确认支付
			payment = driver.find_element_by_id("suborder")
			driver.execute_script('$(arguments[0]).click()',payment)
			time.sleep(20)
			driver.find_element_by_id("btn_submit").click()
			time.sleep(20)
			driver.find_element_by_id("logon_id").send_keys(account)
			driver.find_element_by_id("pwd_unencrypt").send_keys(accout_pay_password)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[button='登录']").click()

			# driver.find_element_by_id("account").send_keys(account)
			# driver.find_element_by_id("J-pwd").send_keys(accout_pay_password)
			# driver.find_element_by_xpath("//div[button='下一步']").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[button='确认付款']").click()
			time.sleep(wait_time)
			driver.find_element_by_link_text("返回商户").click()
			time.sleep(wait_time)
			#获取成功页面显示的订单号
			Subscribe_home_service.order_number = ''
			Subscribe_home_service.order_number = driver.find_element_by_xpath("//div[@class='main-content']/p[@class='memo']/strong").text
			driver.find_element_by_link_text("查看我的预约").click()
			time.sleep(wait_time)
			#验证我的预约列表中显示的订单信息正确
			real_order_price = ''
			expect_order_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][1]/span").text
			expect_order_price = '￥5.01'
			self.assertEqual(real_order_price,expect_order_price)

			real_off_price = ''
			expect_off_price = ''
			real_off_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscribe_home_service.order_number)]/p[@class='date'][2]/span").text
			expect_off_price = '￥5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			expect_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscribe_home_service.order_number)]/p[@class='date'][3]/span").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_subscribe_status = ''
			expect_subscribe_status = ''
			real_subscribe_status = driver.find_element_by_xpath("//div[contains(@onclick,Subscribe_home_service.order_number)]/p[@class='bottom']").text
			expect_subscribe_status = '等待美甲师上门'
			self.assertEqual(real_subscribe_status,expect_subscribe_status)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[contains(@onclick,Subscribe_home_service.order_number)]/p[@class='bottom']").click()
			time.sleep(wait_time)
			#检查订单详情页状态信息
			real_order_status = ''
			expect_order_status = ''
			real_order_status = driver.find_element_by_class_name("order-status").find_element_by_xpath("//span[@class='New_font']").text
			expect_order_status ='等待美甲师上门'
			self.assertEqual(real_order_status,expect_order_status)
			#获取预约消费码
			Subscribe_home_service.consumption_code = ''
			Subscribe_home_service.consumption_code = driver.find_element_by_id("detail_info").find_element_by_class_name("order-detail").find_element_by_class_name("item").find_element_by_class_name("right").text
			print("2.")
			print(Subscribe_home_service.consumption_code)

			real_total_price = ''
			expec_total_price = ''
			real_total_price = driver.find_element_by_xpath("//div[span='总金额']/span[2]").text
			expec_total_price = '￥5.01'
			self.assertEqual(real_total_price,expec_total_price)

			real_off_price = ''
			expect_off_price = ''
			real_off_price = driver.find_element_by_xpath("//div[span='优惠金额']/span[2]").text
			expect_off_price = '￥5'
			self.assertEqual(real_off_price,expect_off_price)
			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[span='付款金额']/span[2]").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)
			h5_logout()

		def test_subscribe_2(self):
			"""2.商铺后台验消费码，并查看状态和金额"""
			print("3.")
			print(Subscribe_home_service.consumption_code)
			web_login()
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='交易验证']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("advanceOrderCheckManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("shopRightInterface").find_element_by_id("shopOrderCodeCheckFuncVectorDiv").find_element_by_id("shopOrderCodeCheckInput").send_keys(Subscribe_home_service.consumption_code)
			driver.find_element_by_id("shopOrderCodeCheckBtn").click()
			time.sleep(wait_time)
			#验证预约信息
			real_code_status = ''
			expect_code_status = ''
			real_code_status = driver.find_element_by_id("singleShopOrderDetailTitleDiv").find_element_by_class_name("order-check-detail-title-status").text
			expect_code_status = '消费码未使用'
			self.assertEqual(real_code_status,expect_code_status)

			real_total_price = ''
			expect_total_price = ''
			real_total_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='总价：']/span[2]").text
			expect_total_price = '5.01元'
			self.assertEqual(real_total_price,expect_total_price)

			real_payed_price = ''
			expect_payed_price = ''
			real_payed_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='已付：']/span[2]").text
			expect_payed_price = '0.01元'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_paying_price = ''
			expect_paying_price = ''
			real_paying_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='待付：']/span[2]").text
			expect_paying_price = '0元'
			self.assertEqual(real_paying_price,expect_paying_price)
			driver.find_element_by_id("singleShopOrderDetailTitleDiv").find_element_by_xpath("//button[@class='order-check-detail-title-use-btn']").click()
			time.sleep(wait_time)

			real_code_status = ''
			real_code_status = driver.find_element_by_id("shopOrderCodeDetailVectorDiv").find_element_by_xpath("//div[@id='singleShopOrderDetailTitleDiv']/span[2]").text
			expect_code_status = '消费码已使用'
			self.assertEqual(real_code_status,expect_code_status)
			time.sleep(wait_time)
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='订单管理']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("homeFirstPayOrderTipsManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("homeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("homeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscribe_home_service.order_number)
			driver.find_element_by_id("homeFirstPayTipSearchBtn").click()
			time.sleep(wait_time)

			real_font_order_number = ''
			expect_font_order_number = '订单号：' + Subscribe_home_service.order_number
			real_font_order_number = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			self.assertEqual(real_font_order_number,expect_font_order_number)

			real_order_to_home = ''
			real_order_to_home = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			expect_order_to_home = '(预约上门先付款)'
			self.assertEqual(real_order_to_home,expect_order_to_home)

			real_order_status_word = ''
			real_order_status_word = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			expect_order_status_word = '进行中预约'
			self.assertEqual(real_order_status_word,expect_order_status_word)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			expect_total_price = '5.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			expect_off_price = '5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			expect_payed_price = '0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			expect_paying_price = '0'
			self.assertEqual(real_paying_price,expect_paying_price)
			web_logout()

		def test_subscribe_3(self):
			"""3.商铺后台追加补款并验证订单和预约状态"""
			web_login()
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='订单管理']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("homeFirstPayOrderTipsManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("homeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("homeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscribe_home_service.order_number)
			driver.find_element_by_id("homeFirstPayTipSearchBtn").click()
			time.sleep(wait_time)

			real_font_order_number = ''
			expect_font_order_number = '订单号：' + Subscribe_home_service.order_number
			real_font_order_number = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			self.assertEqual(real_font_order_number,expect_font_order_number)
			driver.find_element_by_link_text("追加补款").click()
			time.sleep(wait_time)
			driver.find_element_by_id("selfDefAlertWindowCnt").find_element_by_xpath("//span/span/input").send_keys('0.01')
			driver.find_element_by_xpath("//div/button").click()
			time.sleep(wait_time)
			#追加付款后的验证
			# driver.find_element_by_id("homeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("homeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").clear()
			# time.sleep(wait_time)
			# driver.find_element_by_id("homeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("homeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscribe_home_service.order_number)
			# driver.find_element_by_id("homeFirstPayTipSearchBtn").click()
			# time.sleep(wait_time)

			# real_font_order_number = '订单号：' + Subscribe_home_service.order_number
			# expect_font_order_number = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			# self.assertEqual(real_font_order_number,expect_font_order_number)

			# real_order_to_home = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			# expect_order_to_home = '(预约上门先付款)'
			# self.assertEqual(real_order_to_home,expect_order_to_home)

			# real_order_status_word = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			# expect_order_status_word = '已完成预约'
			# self.assertEqual(real_order_status_word,expect_order_status_word)

			# real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			# expect_total_price = '5.02'
			# self.assertEqual(real_total_price,expect_total_price)
			# real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			# expect_off_price = '5'
			# self.assertEqual(real_off_price,expect_off_price)
			# real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			# expect_payed_price = '0.01'
			# self.assertEqual(real_payed_price,expect_payed_price)
			# real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			# expect_paying_price = '0.01'
			# self.assertEqual(real_paying_price,expect_paying_price)

			web_logout()

		def test_subscribe_4(self):
			"""4.H5验证商家追加补款后的预约状态和金额显示，并完成补款"""
			h5_login()
			driver.find_element_by_link_text("个人中心").click()
			time.sleep(wait_time)
			driver.find_element_by_link_text("我的预约").click()
			time.sleep(wait_time)
			real_order_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscribe_home_service.order_number)]/p[@class='date'][1]/strong").text
			expect_order_price = '该订单需要在秀美甲APP中完成'
			self.assertEqual(real_order_price,expect_order_price)
			web_logout()

		def tearDown(self):
			self.assertEqual([],self.verificationErrors)
			#driver.quit()

"""1.h5预约到店先付款下单,价格5.01元，使用红包5元，实付0.01元 2.商铺后台验消费码并查看状态和金额 3.H5 在我的预约中查看订单金额和状态 4.商铺后台发起补款 5.h5检查预约信息"""
class Subscibe_store_pay_inadvance(unittest.TestCase):
		order_number =''
		consumption_code = ''
		print("执行了这里")
		def setUp(self):
			self.verificationErrors = []
			self.accept_next_alert = True

		def test_subscribe_1(self):
			"""h5预约到店先付款下单原价5.01元，使用红包5元，实付0.01元 """
			h5_login()
			time.sleep(wait_time)
			driver.find_element_by_link_text("做美甲").click()
			time.sleep(wait_time)
			#查看店铺列表
			driver.find_element_by_xpath("//a[span='店铺']").click()
			time.sleep(wait_time)
			#搜索店铺
			search = driver.find_element_by_xpath("//input[@class='search-input']").send_keys(search_store_name)
			driver.find_element_by_xpath("//a[@class='search-btn']").click()
			time.sleep(wait_time)
			#打开店铺详情页
			driver.find_element_by_id("shop-list-key").click()
			time.sleep(wait_time)
			#领取5元店铺红包
			driver.find_element_by_id("redlist").find_element_by_xpath("//a[@data-id='15240']").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[@class='input-content']").find_element_by_link_text("确认").click()
			time.sleep(wait_time)
			#打开款式
			driver.find_element_by_id("wf-main-style").find_element_by_xpath("//p[span='￥5.01']").click()
			time.sleep(wait_time)
			#点击“立即预约”
			driver.find_element_by_xpath("//a[@class='buy-btn']").click()
			time.sleep(wait_time)
			#点击“预约到店”
			driver.find_element_by_xpath("//li[contains(.,'预约到店')]").click()
			time.sleep(wait_time)
			#填写预约信息并提交预约
			driver.find_element_by_id("txt-name").send_keys("罗勾勾")
			driver.find_element_by_id("txt-date").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[@role='dialog']").find_element_by_link_text("确定").click()
			time.sleep(wait_time)
			submit_order = driver.find_element_by_link_text("提交预约")
			driver.execute_script('$(arguments[0]).click()',submit_order)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//section[@class='red-info']/ul/li/span[contains(.,'未使用')]").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//li[@class='red-list']/ol/li[@data-val='5']").click()
			time.sleep(wait_time)

			real_total_price  = ''
			real_total_price = driver.find_element_by_xpath("//section[@class='red-info']").find_element_by_id("showprice").text
			expect_total_price = '5.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_id("allprice").text
			expect_paying_price = '0.01'
			self.assertEqual(real_paying_price,expect_paying_price)
			#点击确认支付
			payment = driver.find_element_by_id("suborder")
			driver.execute_script('$(arguments[0]).click()',payment)
			time.sleep(wait_time)
			driver.find_element_by_id("btn_submit").click()
			time.sleep(wait_time)
			driver.find_element_by_id("logon_id").send_keys(account)
			driver.find_element_by_id("pwd_unencrypt").send_keys(accout_pay_password)
			driver.find_element_by_xpath("//div[button='登录']").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[button='确认付款']").click()
			time.sleep(wait_time)
			driver.find_element_by_link_text("返回商户").click()
			time.sleep(wait_time)
			#获取成功页面显示的订单号
			Subscibe_store_pay_inadvance.order_number = ''
			Subscibe_store_pay_inadvance.order_number = driver.find_element_by_xpath("//div[@class='main-content']/p[@class='memo']/strong").text
			driver.find_element_by_link_text("查看我的预约").click()
			time.sleep(wait_time)
			#验证我的预约列表中显示的订单信息正确
			real_order_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][1]/span").text
			expect_order_price = '￥5.01'
			self.assertEqual(real_order_price,expect_order_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][2]/span").text
			expect_off_price = '￥5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][3]/span").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_subscribe_status = ''
			real_subscribe_status = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='bottom']").text
			expect_subscribe_status = '等待到店'
			self.assertEqual(real_subscribe_status,expect_subscribe_status)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='bottom']").click()
			time.sleep(wait_time)
			#检查订单详情页状态信息
			real_order_status = ''
			real_order_status = driver.find_element_by_class_name("order-status").find_element_by_xpath("//span[@class='New_font']").text
			expect_order_status ='等待到店'
			self.assertEqual(real_order_status,expect_order_status)
			#获取预约消费码
			Subscibe_store_pay_inadvance.consumption_code = ''
			Subscibe_store_pay_inadvance.consumption_code = driver.find_element_by_id("detail_info").find_element_by_class_name("order-detail").find_element_by_class_name("item").find_element_by_class_name("right").text
			print("consumption code in 1 is :")
			print(Subscibe_store_pay_inadvance.consumption_code)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//div[span='总金额']/span[2]").text
			expec_total_price = '￥5.01'
			self.assertEqual(real_total_price,expec_total_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//div[span='优惠金额']/span[2]").text
			expect_off_price = '￥5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[span='付款金额']/span[2]").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)
			h5_logout()

		def test_subscribe_2(self):
			"""2.商铺后台验消费码，并查看状态和金额"""
			web_login()
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='交易验证']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("advanceOrderCheckManagement").click()
			time.sleep(wait_time)
			print("the consumption code in 2 is :")
			print(Subscibe_store_pay_inadvance.consumption_code)
			driver.find_element_by_id("shopRightInterface").find_element_by_id("shopOrderCodeCheckFuncVectorDiv").find_element_by_id("shopOrderCodeCheckInput").send_keys(Subscibe_store_pay_inadvance.consumption_code)
			driver.find_element_by_id("shopOrderCodeCheckBtn").click()
			time.sleep(wait_time)
			#验证预约信息
			real_code_status = ''
			real_code_status = driver.find_element_by_id("singleShopOrderDetailTitleDiv").find_element_by_class_name("order-check-detail-title-status").text
			expect_code_status = '消费码未使用'
			self.assertEqual(real_code_status,expect_code_status)

			real_total_price = ''
			real_total_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='总价：']/span[2]").text
			expect_total_price = '5.01元'
			self.assertEqual(real_total_price,expect_total_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='已付：']/span[2]").text
			expect_payed_price = '0.01元'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='待付：']/span[2]").text
			expect_paying_price = '0元'
			self.assertEqual(real_paying_price,expect_paying_price)
			driver.find_element_by_id("singleShopOrderDetailTitleDiv").find_element_by_xpath("//button[@class='order-check-detail-title-use-btn']").click()
			time.sleep(wait_time)

			real_code_status = ''
			real_code_status = driver.find_element_by_id("shopOrderCodeDetailVectorDiv").find_element_by_xpath("//div[@id='singleShopOrderDetailTitleDiv']/span[2]").text
			expect_code_status = '消费码已使用'
			self.assertEqual(real_code_status,expect_code_status)
			time.sleep(wait_time)
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='订单管理']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("homeFirstPayOrderTipsManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("homeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("homeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscibe_store_pay_inadvance.order_number)
			driver.find_element_by_id("homeFirstPayTipSearchBtn").click()
			time.sleep(wait_time)

			expect_font_order_number = '订单号：' + Subscibe_store_pay_inadvance.order_number
			real_font_order_number = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			self.assertEqual(real_font_order_number,expect_font_order_number)

			real_order_to_store = ''
			real_order_to_store = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			expect_order_to_store = '(预约到店先付款)'
			self.assertEqual(real_order_to_store,expect_order_to_store)

			real_order_status_word = ''
			real_order_status_word = driver.find_element_by_xpath("//div[@id='homeFirstPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			expect_order_status_word = '进行中预约'
			self.assertEqual(real_order_status_word,expect_order_status_word)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			expect_total_price = '5.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			expect_off_price = '5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			expect_payed_price = '0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			expect_paying_price = '0'
			self.assertEqual(real_paying_price,expect_paying_price)
			web_logout()

		def test_subscribe_3(self):
			""""3.消费码使用后，h5 验证预约状态和价格"""
			h5_login()
			time.sleep(wait_time)
			driver.find_element_by_link_text("个人中心").click()
			time.sleep(wait_time)
			driver.find_element_by_id("mycenter_html").find_element_by_link_text("我的预约").click()
			time.sleep(wait_time)

			real_paying_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][1]/span").text
			expect_order_price = '￥5.01'
			self.assertEqual(real_order_price,expect_order_price)
			real_paying_price = ''
			real_off_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][2]/span").text
			expect_off_price = '￥5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][3]/span").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_subscribe_status = ''
			real_subscribe_status = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='bottom']").text
			expect_subscribe_status = '已完成'
			self.assertEqual(real_subscribe_status,expect_subscribe_status)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='bottom']").click()
			time.sleep(wait_time)
			#检查订单详情页状态信息
			real_order_status = ''
			real_order_status = driver.find_element_by_class_name("order-status").find_element_by_xpath("//span[@class='New_font']").text
			expect_order_status ='已完成'
			self.assertEqual(real_order_status,expect_order_status)
			#获取预约消费码
			Subscibe_store_pay_inadvance.consumption_code = ''
			Subscibe_store_pay_inadvance.consumption_code = driver.find_element_by_id("detail_info").find_element_by_class_name("order-detail").find_element_by_class_name("item").find_element_by_class_name("right").text

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//div[span='总金额']/span[2]").text
			expec_total_price = '￥5.01'
			self.assertEqual(real_total_price,expec_total_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//div[span='优惠金额']/span[2]").text
			expect_off_price = '￥5'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[span='付款金额']/span[2]").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_payed_type = driver.find_element_by_xpath("//div[span='支付方式']/span[2]").text
			expect_payed_type = '支付宝网页支付'
			self.assertEqual(real_payed_type,expect_payed_type)
			h5_logout()

		def test_subscribe_4(self):
			"""4.商铺后台追加补款并验证订单和预约状态"""
			web_login()
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='订单管理']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeFirstPayOrderTipsManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("storeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscibe_store_pay_inadvance.order_number)
			driver.find_element_by_id("storeFirstPayTipSearchBtn").click()
			time.sleep(wait_time)

			real_font_order_number = ''
			expect_font_order_number = '订单号：' + Subscibe_store_pay_inadvance.order_number
			real_font_order_number = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			self.assertEqual(real_font_order_number,expect_font_order_number)
			driver.find_element_by_link_text("追加补款").click()
			time.sleep(wait_time)
			driver.find_element_by_id("selfDefAlertWindowCnt").find_element_by_xpath("//span/span/input").send_keys('0.01')
			driver.find_element_by_xpath("//div/button").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("storeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").clear()
			driver.find_element_by_id("storeFirstPayOrderTipsFuncVectorDiv").find_element_by_id("storeFirstPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscibe_store_pay_inadvance.order_number)
			time.sleep(wait_time)
			#点击搜索按钮
			driver.find_element_by_id("storeFirstPayTipSearchBtn").click()
			time.sleep(wait_time)
			# real_font_order_store = '订单号：' + Subscibe_store_pay_inadvance.order_number
			# expect_font_order_store = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			# self.assertEqual(real_font_order_number,expect_font_order_number)

			# real_order_to_store = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			# expect_order_to_store = '(预约到店先付款)'
			# self.assertEqual(real_order_to_store,expect_order_to_store)

			# real_order_status_word = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			# expect_order_status_word = '已完成预约'
			# self.assertEqual(real_order_status_word,expect_order_status_word)

			# real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			# expect_total_price = '5.02'
			# self.assertEqual(real_total_price,expect_total_price)
			# real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			# expect_off_price = '5'
			# self.assertEqual(real_off_price,expect_off_price)
			# real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			# expect_payed_price = '0.01'
			# self.assertEqual(real_payed_price,expect_payed_price)
			# real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			# expect_paying_price = '0.01'
			# self.assertEqual(real_paying_price,expect_paying_price)
			web_logout()

		def test_subscribe_5(self):
			"""5.H5验证商家追加补款后的预约状态和金额显示，并完成补款"""
			h5_login()
			driver.find_element_by_link_text("个人中心").click()
			time.sleep(wait_time)
			driver.find_element_by_link_text("我的预约").click()
			time.sleep(wait_time)
			real_order_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][1]/strong").text
			expect_order_price = '该订单需要在秀美甲APP中完成'
			self.assertEqual(real_order_price,expect_order_price)
			web_logout()

		def tearDown(self):
			self.assertEqual([],self.verificationErrors)
			#driver.quit()
"""1.h5预约到店后付款提交订单 2.商铺后台查看状态和金额，确认预约，查看状态 3.H5获取消费码，查看预约状态 4.商铺后台验证消费码，并检查预约信息 ,追加补款  5.H5验证商家追加补款后的预约状态和金额显示，并完成补款(补款功能H5暂未实现)"""
class Subscibe_store_pay_instore(unittest.TestCase):
		order_number =''
		consumption_code = ''
		def setUp(self):
			self.verificationErrors = []
			self.accept_next_alert = True

		def test_subscribe_1(self):
			"""1.h5预约到店后付款提交订单 """
			h5_login()
			time.sleep(wait_time)
			driver.find_element_by_link_text("做美甲").click()
			time.sleep(wait_time)
			#查看店铺列表
			driver.find_element_by_xpath("//a[span='店铺']").click()
			time.sleep(wait_time)
			#搜索店铺
			search = driver.find_element_by_xpath("//input[@class='search-input']").send_keys(search_store_name)
			driver.find_element_by_xpath("//a[@class='search-btn']").click()
			time.sleep(wait_time)
			#打开店铺详情页
			driver.find_element_by_id("shop-list-key").click()
			time.sleep(wait_time)
			#打开款式
			driver.find_element_by_id("wf-main-style").find_element_by_xpath("//p[span='￥0.01']").click()
			time.sleep(wait_time)
			#点击“立即预约”
			driver.find_element_by_xpath("//a[@class='buy-btn']").click()
			time.sleep(wait_time)
			#点击“预约到店”
			driver.find_element_by_xpath("//li[contains(.,'预约到店')]").click()
			time.sleep(wait_time)
			#填写预约信息并提交预约
			driver.find_element_by_id("txt-name").send_keys("罗勾勾")
			driver.find_element_by_id("txt-date").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[@role='dialog']").find_element_by_link_text("确定").click()
			time.sleep(wait_time)
			submit_order = driver.find_element_by_link_text("提交预约")
			driver.execute_script('$(arguments[0]).click()',submit_order)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//section[@class='pay-way']/ul/li[2]").click()
			time.sleep(wait_time)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//section[@class='red-info']").find_element_by_id("showprice").text
			expect_total_price = '0.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_id("allprice").text
			expect_paying_price = '0.01'
			self.assertEqual(real_paying_price,expect_paying_price)

			#点击确认支付
			driver.find_element_by_id("suborder").click()
			time.sleep(30)
			#获取成功页面显示的订单号
			Subscibe_store_pay_instore.order_number = driver.find_element_by_xpath("//div[@class='main-content']/p[@class='memo']/strong").text
			driver.find_element_by_link_text("查看我的预约").click()
			time.sleep(wait_time)
			#验证我的预约列表中显示的订单信息正确
			real_order_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='date'][1]/span").text
			expect_order_price = '￥0.01'
			self.assertEqual(real_order_price,expect_order_price)

			real_subscribe_status = ''
			real_subscribe_status = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='bottom']").text
			expect_subscribe_status = '等待店家确认\n取消订单'
			self.assertEqual(real_subscribe_status,expect_subscribe_status)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_inadvance.order_number)]/p[@class='bottom']").click()
			time.sleep(wait_time)
			#检查订单详情页状态信息
			real_order_status = ''
			real_order_status = driver.find_element_by_class_name("order-status").find_element_by_xpath("//span[@class='New_font']").text
			expect_order_status ='等待店家确认'
			self.assertEqual(real_order_status,expect_order_status)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//div[span='总金额']/span[2]").text
			expec_total_price = '￥0.01'
			self.assertEqual(real_total_price,expec_total_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[span='付款金额']/span[2]").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)
			h5_logout()

		def test_subscribe_2(self):
			"""2.商铺后台查看状态和金额，确认预约，查看状态"""
			web_login()
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='订单管理']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeSecondPayOrderTipsManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeSecondPayOrderTipsFuncVectorDiv").find_element_by_id("storeSecondPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscibe_store_pay_instore.order_number)
			driver.find_element_by_id("storeSecondPayTipSearchBtn").click()
			time.sleep(wait_time)

			real_font_order_number = ''
			expect_font_order_number = '订单号：' + Subscibe_store_pay_instore.order_number
			real_font_order_number = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			self.assertEqual(real_font_order_number,expect_font_order_number)

			real_order_to_store = ''
			real_order_to_store = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			expect_order_to_store = '(预约到店后付款)'
			self.assertEqual(real_order_to_store,expect_order_to_store)

			real_order_status_word = ''
			real_order_status_word = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			expect_order_status_word = '未确认预约'
			self.assertEqual(real_order_status_word,expect_order_status_word)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			expect_total_price = '0.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			expect_off_price = '0'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			expect_payed_price = '0'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			expect_paying_price = '0.01'
			self.assertEqual(real_paying_price,expect_paying_price)

			#确认预约
			driver.find_element_by_link_text("确认订单").click()
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[@class='self-ana-win-div']/div[@class='self-ana-win-bnt-vec-div']/button[1]").click()
			time.sleep(wait_time)

			real_order_status_word = ''
			real_order_status_word = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			expect_order_status_word = '已确认预约'
			self.assertEqual(real_order_status_word,expect_order_status_word)
			web_logout()

		def test_subscribe_3(self):
			""""3.H5获取消费码，查看预约状态"""
			h5_login()
			time.sleep(wait_time)
			driver.find_element_by_link_text("个人中心").click()
			time.sleep(wait_time)
			driver.find_element_by_id("mycenter_html").find_element_by_link_text("我的预约").click()
			time.sleep(wait_time)

			real_order_price = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_instore.order_number)]/p[@class='date'][1]/span").text
			expect_order_price = '￥0.01'
			self.assertEqual(real_order_price,expect_order_price)

			real_subscribe_status = ''
			real_subscribe_status = driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_instore.order_number)]/p[@class='bottom']").text
			expect_subscribe_status = '等待到店\n已取消'
			self.assertEqual(real_subscribe_status,expect_subscribe_status)
			time.sleep(wait_time)
			driver.find_element_by_xpath("//div[contains(@onclick,Subscibe_store_pay_instore.order_number)]/p[@class='bottom']").click()
			time.sleep(wait_time)
			#检查订单详情页状态信息
			real_order_status = ''
			real_order_status = driver.find_element_by_class_name("order-status").find_element_by_xpath("//span[@class='New_font']").text
			expect_order_status ='等待到店'
			self.assertEqual(real_order_status,expect_order_status)
			#获取预约消费码
			Subscibe_store_pay_instore.consumption_code = driver.find_element_by_id("detail_info").find_element_by_class_name("order-detail").find_element_by_class_name("item").find_element_by_class_name("right").text

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//div[span='总金额']/span[2]").text
			expec_total_price = '￥0.01'
			self.assertEqual(real_total_price,expec_total_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//div[span='付款金额']/span[2]").text
			expect_payed_price = '￥0.01'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_payed_type = ''
			real_payed_type = driver.find_element_by_xpath("//div[span='支付方式']/span[2]").text
			expect_payed_type = '到店付款'
			self.assertEqual(real_payed_type,expect_payed_type)
			h5_logout()

		def test_subscribe_4(self):
			"""4.商铺后台验证消费码，并检查预约信息 ,追加补款"""
			web_login()
			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='交易验证']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("advanceOrderCheckManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("shopRightInterface").find_element_by_id("shopOrderCodeCheckFuncVectorDiv").find_element_by_id("shopOrderCodeCheckInput").send_keys(Subscibe_store_pay_instore.consumption_code)
			driver.find_element_by_id("shopOrderCodeCheckBtn").click()
			time.sleep(wait_time)
			#验证预约信息
			real_code_status = ''
			real_code_status = driver.find_element_by_id("singleShopOrderDetailTitleDiv").find_element_by_class_name("order-check-detail-title-status").text
			expect_code_status = '消费码未使用'
			self.assertEqual(real_code_status,expect_code_status)

			real_total_price = ''
			real_total_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='总价：']/span[2]").text
			expect_total_price = '0.01元'
			self.assertEqual(real_total_price,expect_total_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='已付：']/span[2]").text
			expect_payed_price = '0元'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='红包：']/span[2]").text
			expect_off_price = '0元'
			self.assertEqual(real_off_price,expect_off_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_id("singleShopOrderDetailCntDiv").find_element_by_xpath("//span[span='待付：']/span[2]").text
			expect_paying_price = '0.01元'
			self.assertEqual(real_paying_price,expect_paying_price)

			driver.find_element_by_id("singleShopOrderDetailTitleDiv").find_element_by_xpath("//button[@class='order-check-detail-title-use-btn']").click()
			time.sleep(wait_time)

			real_code_status = ''
			real_code_status = driver.find_element_by_id("shopOrderCodeDetailVectorDiv").find_element_by_xpath("//div[@id='singleShopOrderDetailTitleDiv']/span[2]").text
			expect_code_status = '消费码已使用'
			self.assertEqual(real_code_status,expect_code_status)
			time.sleep(wait_time)

			driver.find_element_by_id("shopInterfaceLeftListVecDiv").find_element_by_xpath("//div[font='订单管理']").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeSecondPayOrderTipsManagement").click()
			time.sleep(wait_time)
			driver.find_element_by_id("storeSecondPayOrderTipsFuncVectorDiv").find_element_by_id("storeSecondPayOrderTipsFuncDiv").find_element_by_id("allTipsNumSearchInput").send_keys(Subscibe_store_pay_instore.order_number)
			driver.find_element_by_id("storeSecondPayTipSearchBtn").click()
			time.sleep(wait_time)

			real_font_order_number = ''
			expect_font_order_number = '订单号：' + Subscibe_store_pay_instore.order_number
			real_font_order_number = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			self.assertEqual(real_font_order_number,expect_font_order_number)

			real_order_to_store = ''
			real_order_to_store = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			expect_order_to_store = '(预约到店后付款)'
			self.assertEqual(real_order_to_store,expect_order_to_store)

			real_order_status_word = ''
			real_order_status_word = driver.find_element_by_xpath("//div[@id='storeSecondPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			expect_order_status_word = '进行中预约'
			self.assertEqual(real_order_status_word,expect_order_status_word)

			real_total_price = ''
			real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			expect_total_price = '0.01'
			self.assertEqual(real_total_price,expect_total_price)

			real_off_price = ''
			real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			expect_off_price = '0'
			self.assertEqual(real_off_price,expect_off_price)

			real_payed_price = ''
			real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			expect_payed_price = '0'
			self.assertEqual(real_payed_price,expect_payed_price)

			real_paying_price = ''
			real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			expect_paying_price = '0.01'
			self.assertEqual(real_paying_price,expect_paying_price)

			driver.find_element_by_link_text("追加补款").click()
			time.sleep(wait_time)
			driver.find_element_by_id("selfDefAlertWindowCnt").find_element_by_xpath("//span/span/input").send_keys('0.01')
			driver.find_element_by_xpath("//div/button").click()
			time.sleep(wait_time)
			web_logout()

			# real_font_order_store = '订单号：' + Subscibe_store_pay_inadvance.order_number
			# expect_font_order_store = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[2]").text
			# self.assertEqual(real_font_order_number,expect_font_order_number)

			# real_order_to_store = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span/font[3]").text
			# expect_order_to_store = '(预约到店先付款)'
			# self.assertEqual(real_order_to_store,expect_order_to_store)

			# real_order_status_word = driver.find_element_by_xpath("//div[@id='storeFirstPayOrderTipsCntVectorDiv']/div/div/span[2]").text
			# expect_order_status_word = '已完成预约'
			# self.assertEqual(real_order_status_word,expect_order_status_word)

			# real_total_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[1]/font").text
			# expect_total_price = '5.02'
			# self.assertEqual(real_total_price,expect_total_price)
			# real_off_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[2]/font").text
			# expect_off_price = '5'
			# self.assertEqual(real_off_price,expect_off_price)
			# real_payed_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[3]/font").text
			# expect_payed_price = '0.01'
			# self.assertEqual(real_payed_price,expect_payed_price)
			# real_paying_price = driver.find_element_by_xpath("//table/tbody/tr/td[2]/div/ul/li[4]/font").text
			# expect_paying_price = '0.01'
			# self.assertEqual(real_paying_price,expect_paying_price)

		def test_subscribe_5(self):
			"""5.H5验证商家追加补款后的预约状态和金额显示，并完成补款(补款功能H5暂未实现)"""
			h5_login()
			driver.find_element_by_link_text("个人中心").click()
			time.sleep(wait_time)
			driver.find_element_by_link_text("我的预约").click()
			time.sleep(wait_time)

			Subscibe_store_pay_instore.order_number = "MJ00000000000001680320"
			real_order_price = ''
			real_order_price = driver.find_element_by_xpath("//div[contains(p,Subscibe_store_pay_instore.order_number)]/div[2]/p[3]/strong").text

			expect_order_price = '该订单需要在秀美甲APP中完成'
			self.assertEqual(real_order_price,expect_order_price)
			web_logout()

		def tearDown(self):
			self.assertEqual([],self.verificationErrors)
			#driver.quit()


def web_login():
	driver.get(web_base_url)
	time.sleep(wait_time)
	driver.find_element_by_id("user").send_keys(user_name)
	driver.find_element_by_id("password").send_keys(user_pass)
	driver.find_element_by_id("loginBtn").click()
	time.sleep(wait_time)

def web_logout():
	driver.get(web_base_url)
	time.sleep(wait_time)
	driver.find_element_by_id("shopBanner").find_element_by_id("personalInfoDiv").find_element_by_link_text("注销").click()
	time.sleep(wait_time)

def h5_login():
	#登录
	driver.get(h5_base_url)
	time.sleep(wait_time)
	driver.find_element_by_link_text("个人中心").click()
	time.sleep(wait_time)
	#登录
	driver.find_element_by_id("txt-userName").send_keys(user_name)
	driver.find_element_by_id("txt-userPwd").send_keys(user_pass)
	driver.find_element_by_id("i-login").click()
	time.sleep(wait_time)

def h5_logout():
	#退出登录
	driver.get(h5_base_url)
	time.sleep(wait_time)
	driver.find_element_by_link_text("个人中心").click()
	time.sleep(wait_time)
	driver.find_element_by_id("mycenter_html").find_element_by_id("btn_logout").click()
	time.sleep(wait_time)





if __name__ == "__main__":

		#unittest.main()
		testsuite = unittest.TestSuite()
		#testsuite.addTest(Coupons("test_coupons_pay_order_1"))
		#testsuite.addTest(Coupons("test_coupons_pay_order_2"))
		#testsuite.addTest(Subscribe_home_service("test_subscribe_1"))
		#testsuite.addTest(Subscribe_home_service("test_subscribe_2"))
		#testsuite.addTest(Subscribe_home_service("test_subscribe_3"))
		testsuite.addTest(Subscribe_home_service("test_subscribe_4"))
		#testsuite.addTest(Subscibe_store_pay_inadvance("test_subscribe_1"))
		#testsuite.addTest(Subscibe_store_pay_inadvance("test_subscribe_2"))
		#testsuite.addTest(Subscibe_store_pay_inadvance("test_subscribe_3"))
		#testsuite.addTest(Subscibe_store_pay_inadvance("test_subscribe_4"))
		#testsuite.addTest(Subscibe_store_pay_inadvance("test_subscribe_5"))

		#testsuite.addTest(Subscibe_store_pay_instore("test_subscribe_1"))
		#testsuite.addTest(Subscibe_store_pay_instore("test_subscribe_2"))
		#testsuite.addTest(Subscibe_store_pay_instore("test_subscribe_3"))
		#testsuite.addTest(Subscibe_store_pay_instore("test_subscribe_4"))
		#testsuite.addTest(Subscibe_store_pay_instore("test_subscribe_5"))
		filename = 'C:\\result\\result_Subscribe_home_service4.html'
		fp = open(filename,'wb')

		runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp,
        title='Report_title',
        description='Report_description'
		)
		runner.run(testsuite)
