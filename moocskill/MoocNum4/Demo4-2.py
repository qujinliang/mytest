'''
判断字符串a是否以字符串b开头或结尾
'''
# 使用 os.listdir(), str.endswith()

import os
file = os.listdir('../../.')
print(file)
res = [x for x in file if x.endswith('.py')]
print(res)