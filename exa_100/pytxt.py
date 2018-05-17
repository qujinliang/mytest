"""
 Created by qujl on 2018-05-17
"""
__author__ = 'qujl'

'''
python 读取txt文档
'''
# 读取文档中的某一列，并且保存到新的文档
ll = [l.split(',')[3] for l in open("./data/客户信息(百旺) (1).txt")]
with open('./data/客户信息(百旺) (3).txt','wt') as f:
    for i in ll:
        f.write(i)
        f.write("\n")
print(ll)