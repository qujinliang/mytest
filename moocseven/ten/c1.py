# 正则表达式
import re

a = 'C|C++|Java|C#|Python|JavaScript'

r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')