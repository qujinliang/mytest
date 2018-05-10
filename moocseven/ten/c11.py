# re.sub正则替换
import re
lanuage = 'PythonC#JavaPHPC#C#'
def convert(value):
    print(value)
    matched = value.group()
    return '!!' + matched + '!!'
r = re.sub('C#', convert, lanuage)
print(r)
