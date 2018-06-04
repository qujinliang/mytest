from pymongo import MongoClient
import re
import xlwt

# client = MongoClient('', 27017)  # 演示环境
# client = MongoClient('', 27017)  # 测试环境
client = MongoClient('###', 27017)  # 小当家线上数据库
db = client.user
db.authenticate("###", '###')
db = client.user
collection_company = db.fc_company_info
collection_invoce = db.fc_invoice_info


# 查询发票结合中所有发票
# for i in collection.find():
# 	print(i)

# 查询指定fphm的发票
# for i in collection.find({"fplx":"10"}):
# print(i)
# zggj_list = collection.find({'gfmc':'中钢新元矿业发展有限公司','owner':'诸葛亮911'})
# for i in zggj_list:
# 	if 'fphm' in i:
# 		collection.remove(i)

class Check:
	__list_1 = []
	"""
	userid:传入账号的userid 查询该账号下的所有抬头
	返回List列表
	调用check_company 得到抬头信息的迭迭代器
	然后遍历nssbh，循环调用check_invoice方法得到gfsh等信息
	"""

	# 查询用户方法，传一个参数 Userid,返回用户列表迭代器
	# pymongo.find返回的是游标，转成list就好判断了
	def check_company(self, userid):
		__list_1 = list(collection_company.find({'user_id': int(userid)}))
		if __list_1:
			return __list_1
		else:
			print('不存在的userid %s' % userid)
			return __list_1

	# 查询发票库，传一个参数 购方识别号，返回迭一个发票的列表
	def check_invoce(self, gfsbh):
		lt = collection_invoce.find({'gfsbh': gfsbh})
		if type(lt) != type('a'):
			return lt
		else:
			lt = ' '
			print(lt)

	# 传3个参数，userid必传,name 和 nssbh可以不传，默认None
	# 如果不传name和nssbh会打印抬头信息而不是返回结果
	def company_data(self, userid, name=None, nssbh=None):
		__name_list = []
		__nssbh_list = []
		__data_list = []
		data = Check.check_company(self, userid)
		for i in data:
			if name == 'name':
				company_name = i.get('name')
				__name_list.append(company_name)
			if nssbh == 'nssbh':
				company_nssbh = i.get('nssbh')
				__nssbh_list.append(company_nssbh)
			if name == None and nssbh == None:
				zip_list = [i.get('name'),i.get('nssbh'),i.get('addr'),i.get('bank'),i.get('bank_No'),i.get('create_time')]
				__data_list.append(zip_list)
		if __data_list:
			return __data_list
		if __name_list:
			return __name_list
		if __nssbh_list:
			return __nssbh_list

	# 传入纳税人识别号，打印出发票中的信息
	def company_invoice(self,nssbh):
		__fp_list = []
		for i in nssbh:
			gfsh = Check.check_invoce(self,i)
			for j in gfsh:
				if j.get('gfdzdh'):
					dzdh = j.get('gfdzdh')
					gfyhzh = j.get('gfyhzh')
					gfmc = j.get('gfmc')
					gfsbh = j.get('gfsh')
			if i != gfsbh:
				pass
			else:
				# print(i,gfsbh,gfmc,dzdh,gfyhzh)
				zip_list = [i,gfsbh,gfmc,dzdh,gfyhzh]
				__fp_list.append(zip_list)
		if __fp_list:
			print(__fp_list)
			return __fp_list


if __name__ == '__main__':

	ck = Check()
	nssbh = ck.company_data(1106,nssbh='nssbh')
	print(nssbh)
	fp_list = ck.company_invoice(nssbh)
	wbook = xlwt.Workbook()
	wsheet = wbook.add_sheet('sheet1')
	data1 = fp_list[0]
	nc = len(data1)
	title = ['抬头', '纳税人识别号', '地址', '开户行', '银行账号', '开通时间']

	for t in range(len(title)):
		wsheet.write(0, t, title[t])

	for r in range(1, len(fp_list)):
		for c in range(nc):
			wsheet.write(r, c, fp_list[r][c])

	wbook.save('./data/output2.xlsx')
	client.close()



#     # 循环调用check_invoce方法,循环传入nssbh
#     gfsh = ck.check_invoce(nssbh)
#     for j in gfsh:
#
#         # 判断只有 gfdzdh不为None的发票才留存
#         if j.get('gfdzdh'):
#             dzdh = j.get('gfdzdh')
#             gfyhzh = j.get('gfyhzh')
#             gfmc = j.get('gfmc')
#             gfsh = j.get('gfsbh')
#
#     # 如果MongoDB是空的话会返回一个class:pymong.cousor的类型
#     # 所以这里做一个判断，要求必须nssbh和gfsh相等才打印
#     if nssbh != gfsh:
#         pass
#     else:
#         # print(nssbh,gfsh,gfmc,dzdh,gfyhzh)
#         with open('huilianyi.txt', 'at') as huilianyi:
#             huilianyi.writelines("%s %s \n" % nssbh % gfsh)

# for i in fp_list3:
# 	if i.get('fplx') == '10':
# 		fplx = i.get('fplx')
# 		fpdm = i.get('fpdm')
# 		fphm = i.get('fphm')
# 		fpje = i.get('je')
# 		jym = i.get('jym')
# 		kprq = i.get('kprq')
# 		l = [fplx, fpdm, fphm, fpje, jym, kprq]
# 		print(l)
# return list
#
# 		print('fpdm %s,fphm %s ' %(fpdm,fphm))
