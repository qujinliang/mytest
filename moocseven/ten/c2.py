import re

a = 'C0C++23Java6C#78Python5JavaScript'

r = re.findall('\D', a)
print(r)