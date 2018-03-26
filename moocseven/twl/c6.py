# 装饰器
import time
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper
@decorator
def f1(func_name, **kw):
    print('This is a function ' + func_name)
    print(kw)
f1('test func', a=1, b=2,c='sb')

@decorator
def f2(func_name1, **kw):
    print('This is a function2 ' +func_name1)
    print(kw)
f2('test func2', a=1,b=2)

