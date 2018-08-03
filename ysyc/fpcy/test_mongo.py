"""
 Created by qujl on 2018-06-22
"""
__author__ = 'qujl'

from pymongo import MongoClient

client = MongoClient('', )  #
db = client.user
db.authenticate("", '')
db = client.user
collection_invoce = db.fc_invoice_info


for i in collection_invoce.find({"fplx":"01"}):
    hjje = i.get('je')
    if float(hjje) > 500000:
        print(i)
# zggj_list = collection_invoce.find({'gfmc':'中钢新元矿业发展有限公司','owner':'诸葛亮911'})


