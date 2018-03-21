# 数量词

import re

a = 'python1111java67 8ph p2#@#@@$@$'

r = re.findall('[a-z]{3,8}?', a)
print(r)
