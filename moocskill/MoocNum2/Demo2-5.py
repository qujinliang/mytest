'''
快速找到多个字典中的公共键
字典对比，找出多个字典中相同或不同的键值
'''

from random import randint,sample
from functools import reduce   # python3需要导入

# sample：更具传入的参数，从参数中随机抽取给定范围的值
qy = 'abcdefsdqwerty'
s1 = {x:randint(1,10) for x in sample(qy, randint(3,10))}
s2 = {x:randint(1,10) for x in sample(qy, randint(3,10))}
s3 = {x:randint(1,10) for x in sample(qy, randint(3,10))}

# 使用map方法 映射dict.keys和[s1,s2,s3] 对字典列表进行循环读取key 并生成一个map迭代器
s_set = map(dict.keys,[s1,s2,s3])
# 与上面基本相同，多了一步将value 字典列表转 set集合
v_set = map(dict.values,[s1,s2,s3])
v_set = map(lambda a:set(a),v_set)

# 使用reduce方法 通过lambda表达式，分别对s_set 和 v_set进行运算
result = reduce(lambda a,b:a&b,s_set)

# difference取差集
result1 = reduce(lambda a,b:a.difference(b),v_set)
print(result,result1)