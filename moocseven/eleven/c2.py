# 进阶  闭包 = 函数 + 环境变量

def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve
f = curve_pre()
# 打印f.__closure__闭包 内置变量
print(f.__closure__)
# 获取闭包中内置变量的值
print(f.__closure__[0].cell_contents)
print(f(5))



