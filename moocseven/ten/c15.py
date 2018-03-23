# re.sub把函数作为参数传递

import re
s = 'ABC3721D86'
 
def convert(value):
    matched = value.group()
    nine = 9
    zero = 0
    if int(matched) >= 6:
        return '9'
    else:
        return '0'
r = re.sub('\d', convert, s)
print(r)

