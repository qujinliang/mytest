from pymongo import MongoClient
import re

# client = MongoClient('',27017)  #演示环境
#client = MongoClient('', 27017)  # 测试环境
client = MongoClient('', 27017)  # 小当家线上数据库
db = client.user
db.authenticate("user", 'ysyc-mongo-user')
db = client.user
collection = db.fc_invoice_info

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

class Check():
	list = []
	# 该方法是链接Mongodb数据库并读取发票数据
	# 需要传三个参数，第一个参数是发票类型，第二个参数是查询日期范围的开始时间
	# 第三个参数是查询日期范围的结束时间
	def check_xdjmongo(self,fplx, startime, endtime):
		list = collection.find({'fplx':re.compile(fplx),'kprq':{"$gt":startime,"$lt":endtime}})
		return list




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

