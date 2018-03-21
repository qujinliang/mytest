from random import randint
import moocskill

a = [x for x in range(0,10)]

b = a[0:len(a):3]
print(b)
for i in range(0,len(a),2):
    print (i, end='|')

print('name:' + __name__)
print('file:'+ __file__)
print('package:'+ (__package__ or '当前模块不属任何包'))
