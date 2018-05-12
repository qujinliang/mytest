
'''
统计序列中元素出现的频度
'''

from collections import Counter
from random import randint



data = [randint(0,20) for i in range(30)]


# 方法一 data做为键 0为值生成字典
keys = data
c = dict.fromkeys(keys,0)
# 遍历键，并给每一个存在的键+1
for x in keys:
    c[x] +=1
sor = sorted(c.items(),key=lambda i:i[1],reverse=True)
print(sor)


# 方法二 直接用Counter方法
# most_common 方法统计出现最多的前3个
d2 = Counter(data).most_common(3)
print(d2)