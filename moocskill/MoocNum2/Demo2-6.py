'''
  使字典有序
'''

from collections import OrderedDict

d = OrderedDict()

d['Jim'] = (1,30)

d['Bob'] = (2,34)

d['Leo'] = (3,40)

for k in d:print(k)