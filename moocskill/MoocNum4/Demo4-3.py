'''
调整字符串中文本的格式
'''

# 只替换字符，不变格式
data = '2018-05-13'
data = data.replace('-','\\')
print(data)


# 替换字符，并且改变格式
import re
date = '2018-05-13 匹配日期，替换字符，并且改变格式'
res = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',date)
print(res)