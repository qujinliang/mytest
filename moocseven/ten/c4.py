# 概括字符集

import re
# \d 匹配所有数字  \D 匹配非数字

a = 'python1111java67 8ph p2#@#@@$@$'

r = re.findall('[\D]', a)
print(str(r))


