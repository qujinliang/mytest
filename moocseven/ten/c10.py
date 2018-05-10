# 组
# 并配连续出现这组字符的次数

import re
a = 'PythonPythonPythonPythonPythonPython'

r = re.findall('(Python){1}', a)
print(r)