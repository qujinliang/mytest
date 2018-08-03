"""
 Created by qujl on 2018-06-28
"""
__author__ = 'qujl'
# -*- coding:UTF-8 -*-
import redis
import re
import csv

pool = redis.ConnectionPool(host='139.219.227.123', port=12210, password='ysyc-redis-test',decode_responses=True,db=0)
r = redis.Redis(connection_pool=pool)
# l = []
# for i in range(71000,71500):
#     i = '0' + str(i)
#     l.append(i)
#
# data = []
# for dat in l:
#     name = "invoice:1000009:%s" %dat
#     # print(r.hgetall(name)['response'])
#     if r.hgetall(name):
#         data.append(r.hgetall(name))
#
# # 逐行写入列表中的每一个元素到txt
# with open('redisdata.txt','wt') as f:
#     for i in data:
#         f.write(str(i))
#         f.write("\n")


# 读取txt所有行 并且为列表
with open('redisdata.txt','rt') as f:
    data = f.readlines()
ll = []
for i in  data:
    if '2018-02-' in i:
        ll.append(i)
print(len(ll))

# data = list(data)
# print(data)
# for dd in data:
#     if dd['response'] == '106':
#         pass
#     elif dd['msg']['cysj'] >= '2018-02-01' and dd['msg']['cysj'] <= '2018-02-28':
#         print(dd)
#         print(data.count())

