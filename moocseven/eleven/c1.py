# 枚举
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
lst = [0,1,2,3,4,5,6]
# 通过值 获取枚举名称
a = 1
print(VIP(a))

print(lst[VIP.YELLOW.value])
# 遍历枚举类里面的所有名称、别名、和值
for v in VIP.__members__.items():
    print(v)

