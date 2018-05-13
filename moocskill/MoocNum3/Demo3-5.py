'''
在一个for语句中迭代多个可迭代对象
'''
from random import randint

# 1.并行，用zip
chines = [randint(60,100) for i in range(40)]
math = [randint(60,100) for i in range(40)]
english = [randint(60,100) for i in range(40)]

total = []
l = zip(chines,math,english)
l = list(l)
print(l)
for c,m,e in zip(chines,math,english):
    total.append(c + m + e)

print(total)

# 2.串行，用itertools.chain方法
from itertools import chain

e1 = [randint(60,100) for i in range(40)]
e2 = [randint(60,100) for i in range(42)]
e3 = [randint(60,100) for i in range(45)]
e4 = [randint(60,100) for i in range(41)]

count = 0
for x in chain(e1,e2,e3,e4):
    if x >= 90:
        count += 1
print(count)

