'''
根据字典中值的大小，对字典中的项进行排序
'''

from random import randint

data = {x : randint(60,100) for x in 'axcfdwe'}
print(data)

# 使用sorted函数，data.items()得到字典，然后设置key关键字，需要传入一个函数，
# 这里使用的是lambda匿名函数，传入参数i 返回i[1]的值，这样就按value大小排序了
sor = sorted(data.items(),key= lambda i:i[1], reverse=True)[:3]
print(sor)