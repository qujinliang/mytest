'''
创建大量实例节省内存

'''
# 有__dict__ 动态绑定
class Player(object):
    def __init__(self, uid, name, status=0, level=0):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

# 节省内存，关闭动态字典绑定
class Player2(object):
    __slots__ = ['uid','name', 'status', 'level']
    def __init__(self,uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

p1 = Player('0001','Jim')
p2 = Player2('0001','Jim')

print(dir(p1))
print(dir(p2))
print(set(dir(p1)) - set(dir(p2)))

import sys
print(sys.getsizeof(p1))
print(sys.getsizeof(p2))


