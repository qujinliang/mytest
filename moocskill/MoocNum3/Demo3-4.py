'''
对迭代器做且切片操作
比如：读一个大的log日志，只截取100：300行
'''

from itertools import islice

f = open('../tree')
result = islice(f,5,10)             # 第5行到第10行
f = open('../tree')                 # 重新生成迭代器
result5 = islice(f,5)               # 前5行
result6 = islice(f,6,None)          # 从6行以后到结尾
for i in result:print(i)

for i in result5:print(i)
