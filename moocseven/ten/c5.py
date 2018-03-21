# 数量词
# *匹配0次或者无限多次
# +匹配1次或者无限多次
# ?匹配0次或者1次
import re

a = 'pytho11python2342pythonn'

r = re.findall('python?', a)
print(r)
