'''
字符串拼接
'''

# 1.使用+号拼接
pl = ["<0112","<32>","<1024x768>","<60>","<1>","<100.0>","<500.0>"]
s = ''
for p in pl:
    s += p
print(s)


# 2. 使用str.join()方法

st = ''
print(st.join(pl))

# 3. 混合类型字符串拼接
l = ['abc','342',35,'sdf']
print(st.join(str(x) for x in l))
