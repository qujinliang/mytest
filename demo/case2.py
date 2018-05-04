"""
 Created by qujl on 2018-05-03
"""
__author__ = 'qujl'

"""语法和语句----语法和语句--------语法和语句--------语法和语句--------语法和语句--------语法和语句--------语法和语句--------语法和语句----"""

#- - 赋值语句的形式
    spam = 'spam'                                        # 基本形式
    spam, ham = 'spam', 'ham'                            # 元组赋值形式
    [spam,ham] = ['s','h']                               # 列表赋值形式
    a,b,c,d = 'abcd'                                     # 序列赋值形式
    a,*b,c = 'spam'                                      # 序列解包形式(Python3.x中才有)
    spam = ham = 'no'                                    # 多目标赋值运算，涉及到共享引用
    spam += 42                                           # 增强赋值，涉及到共享引用

#- - 序列赋值 序列解包
    [a,b,c] = (1,2,3)                                    # a = 1, b = 2, c = 3
    a,b,c,d = "spam"                                     # a = 's', b = 'p'
    a,b,c = range(3)                                     # a = 0, b = 1, c = 2
    a, *b = [1,2,3,4]                                    # a = 1, b = [2,3,5]
    *a, b = [1,2,3,4]                                    # a = [1,2,3], b = 4
    a, *b, c = [1,2,3,4]                                 # a = 1, b = [2,3], c = 4
    # 带有*时 会优先匹配*之外的变量 如
    a, *b, c  = [1,2]                                    # a = 1, c = 2, b = []

#- - print函数原型
    import sys
    print(value,..., sep=' ', end='\n', file=sys.stdout, flush=False)
    # 流的重定向
    print('hello world')                                 # 等于sys.stdout.wirte('hello world)
    temp = sys.stdout                                    # 原有流的保存
    sys.stdout = open('log.log', 'a')                    # 流的重定向
    print('hello world')                                 # 写入到文件log.log
    sys.stdout.close()                                   #
    sys.stdout = temp                                    # 原有流的复原

#- - Python中and或or总是返回对象（左边的对象或右边的对象）且具有短路求值的特性
    1 or 2 or  3                                         # 返回1
    1 and 2 and 3                                        # 返回3

#- - if/else三元表达符(if语句在行内)
    A = if X else 2
    A = 1 if X else (2 if Y else 3)
    # 也可以使用 and-or 语句(一条语句实现多个if-else)
    result = (a > 20 and "big than 20" or a > 10 and "big than 10 " or a > 5 and "big than 5")

#- - Python的while语句或者for语句可以带else语句 当夜也可以带continue/break/pass语句
    while a > 1:
        (......)
    else:
        (.....)
    # else语句会在循环结束后执行，除非在循环中执行了break,同样的还有for语句
    for i in range(5):
        (.....)
    else:
        (....)

#- - for循环的元组赋值
    for (a,b) in [(1,2),(3,4)]: pass                             # 最简单的赋值
    for ((a,b),c) in [((1,2),3), ((4,5),6)]:pass                 # 自动解包赋值
    for ((a,b),c) in [((1,2),3),("XY",6)]: pass                  # 自动解包 a = X, b = Y, c=6
    for (a,*b) in [(1,2,3),(4,5,6)]: pass                        # 自动解包赋值

#- - 列表解析语法
    M = [[1,2,3],[4,5,6],[7,8,9]]
    res = [sum(row) for row in M]                                # res = [6,15,24]一般的列表解析 生成一个列表
    res = [c * 2 for in 'spam']                                  # ['ss','pp','aa','mm']
    res = [a * b for a in [1,2] for b in [4,5]]                  # 多解析过程 返回[4,5,8,10]
    res = [a for a in [1,2,3] if a < 2]                          # 带判断条件的解析过程
    res = [a if a > 0 else 0 for a in [-1,0,1]]                  # 带判断条件的高级解析过程
    # 两个列表同时解析：使用zip函数
    for teama, teamb in zip (["Packers","49ers"],["Ravens","Patriots"]):
        print(teama + " vs." + teamb)
# 两个列表同时解析：使用zip函数
    for index,team in enumerate(["Packers","49ers","Ravens","Patriots"]):
        print(index,team)

#- - 生成器表示
    G = (sum(row) for row in M)                                   # 使用小括号可以创建所需接轨哦的生成器generator object
    next(G), next(G), next(G)                                     # 输出(6,15,24)
    G = {sum(row) for row in M}                                   # G = {6,15,24}解析语法还可以生成集合和字典


