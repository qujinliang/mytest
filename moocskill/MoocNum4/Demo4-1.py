'''
拆分含有多种分隔符的字符串
'''

# 1.单个使用str.spilt()一个一个拆
s = 'sdljd,sdfj,sdjfl'
res = s.split(',')
print(res)




# 2. 混合使用re.split()方法
import re
s = 'sdf,jkj|jkjs\tjskf'
res = re.split('[,|\t]+',s)
print(res)