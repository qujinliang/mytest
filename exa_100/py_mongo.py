from pymongo import MongoClient
import re

# client = MongoClient('139.219.109.239',27017)  #演示环境
client = MongoClient('40.125.209.24', 27017)  # 测试环境
#client = MongoClient('42.159.115.213', 27017)  # 小当家线上数据库
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

fp_list3 = collection.find({'fplx':re.compile('10'),'kprq':{"$gt":"20180101"}})
#
for i in fp_list3:
	if i.get('fplx') == '10':
		fplx = i.get('fplx')
		fpdm = i.get('fpdm')
		fphm = i.get('fphm')
		fpje = i.get('je')
		jym = i.get('jym')
		kprq = i.get('kprq')
		gfmc = i.get('gfmc')
		gfsbh = i.get('gfsbh')
		xfmc = i.get('xfmc')
#
		print(fplx,fpdm,fphm,fpje,jym,kprq)
#
# 		print('fpdm %s,fphm %s ' %(fpdm,fphm))
