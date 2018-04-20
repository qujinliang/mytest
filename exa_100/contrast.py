import requests
import hashlib
import os
import json

url = "http://check1.fapiaoxx.com/invoice/check/"
url2 = "http://localhost:8000/invoice/check/"

def md5(md5_str):
    m2 = hashlib.md5()
    m2.update(md5_str)
    return m2.hexdigest()

data1 = {"fpdm": "3100173320","fphm": "15422724","fplx": "04","jym":"650946","fpje": "","kprq": "20171230","uniqueId": "1000001",
            "sign": md5("fpdm=3100173320&fphm=15422724&fpje=&fplx=04&jym=650946&kprq=20171230""&uniqueId=1000001&16fc375eabe411e686cdb0c090607876".encode("utf-8"))}

data2 ={"fpdm": "3100173320","fphm": "15422724","fplx": "04","jym":"650946","fpje": "","kprq": "20171230","uniqueId": "1000001",
        "sign": md5("fpdm=3100173320&fphm=15422724&fpje=&fplx=04&jym=650946&kprq=20171230""&uniqueId=1000001&16fc375eabe411e686cdb0c090607876".encode("utf-8"))}

r = requests.post(url, json = data1)
r = r.json()
print(r)
r2 = requests.post(url2,json = data2)
r2 = r2.json()
print(r2)


# 字典key , value倒转方法
# 可以通过value找到Key
def get_keys(d, value):
    return [k for k, v in d.items() if v == value]

for i,j in r2['data'].items():
        if i not in r['data'].keys() or j not in r['data'].values():
            val = r['data'].get(i,'null')
            print(i,j,':',get_keys(r['data'],val),val)













a=1


