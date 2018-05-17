import json

response= [{'a':1,'b':2,'c':None}]
res = json.dumps(response,separators=[',',':'],sort_keys=True)
print(res)
ress = json.loads(res)
print(ress)


# dump 文件
with open('demo.json','wt') as f:
    json.dump(res,f)

with open('demo.json','rt') as f:
    result = f.read()
print(result)