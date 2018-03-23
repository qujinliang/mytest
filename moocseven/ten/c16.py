# group分组

import re

s = 'life is short,i use python, i love python'

r = re.search('(life)(.*)python(.*)python', s)
print(r.groups())

r = re.findall('life(.*)python(.*)python', s)
print(r)
strr = r[0][0]
print(strr)