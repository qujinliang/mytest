
'''
1.列表推导式
2.set filter
3.set 可以被推导
4.dict 也可以被推导
'''

# 列表推导式
num = [1, 1, 3, 4, 5, 6, 7, 8]
result = {i**2 for i in num if i <= 5}
print(result)

print('----------------------- 分割线 -------------------------')
# 字典推导式
studens = {
    '喜小乐':18,
    '屎大颗':20,
    '冯小刚':50
}
b = {key:values for key,values in studens.items()}
# key value 反转
d = {values: key for key,values in studens.items()}

print(b)
print('----------------------- 分割线 -------------------------')
print(d)
