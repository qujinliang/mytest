'''
去掉字符串中不需要的字符
'''

# 1.去掉字符串前后两端的方法
s = '   abc    123    '
s = s.strip()
print(s)

# 2.删除固定位置字符 切片
ss = 'abc:123'
ss = ss[:3]+ss[4:]
print(ss)

# 3.replace 或 正则表达式
s = '\tabc\t123\txyz'
s = s.replace('\t','')
print(s)

import re
s = '\tabc\t123\txyz\ropg'
res = re.sub('[\t\r]','',s)
print(res)

# 4.