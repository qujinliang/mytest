'''
读写文件
'''

# 1.
f = open('py3.txt','w',encoding='utf8')
f.write('hello world!')
f.close()

f = open('py3.txt','r',encoding='utf8')
res = f.read()
print(res)
f.close()