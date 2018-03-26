# filter
import re
list_y = ['a','B','c','E']
list_x = '2sfdsDJFDljsdf'

# st = re.findall('[a-z]',list_y[1])
# print(st)
def saml():
    for x in list_y:
        if re.findall('[a-z]',x):
            print(x)

r = filter(lambda x: True if re.findall('[a-z]', x) else False, list_y)
print(list(r))