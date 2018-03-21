# 组

import re
a = 'PythonPythonPythonPythonPythonPython'

r = re.findall('(Python){2}', a)
print(r)