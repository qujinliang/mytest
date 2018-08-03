"""
 Created by qujl on 2018-05-17
"""
__author__ = 'qujl'

'''
python 读取txt文档
'''
# 读取文档中的某一列，并且保存到新的文档
# 必须是gbk格式
ll = [l.split('\t')[0] for l in open("./data/test001.txt")]
with open('./data/test002.txt','wt') as f:
    for i in ll:
        f.write(i)
        f.write("\n")
print(ll)