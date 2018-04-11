import requests
import hashlib
import json

url = "http://check1.fapiaoxx.com/invoice/check/"
url2 = "http://localhost:8000/invoice/check/"

def md5(md5_str):
    m2 = hashlib.md5()
    m2.update(md5_str)
    return m2.hexdigest()

data1 = {
            "fpdm": "1100173320","fphm": "59993614","fplx": "04","jym":"743598","fpje": "","kprq": "20171227","uniqueId": "1000004",
            "sign": md5("fpdm=1100173320&fphm=59993614&fpje=&fplx=04&jym=743598&kprq=20171227""&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
data2 ={
            "fpdm": "1100173320","fphm": "59993614","fplx": "04","jym":"743598","fpje": "","kprq": "20171227","uniqueId": "1000004",
            "sign": md5("fpdm=1100173320&fphm=59993614&fpje=&fplx=04&jym=743598&kprq=20171227""&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
r = requests.post(url, json = data1)
r2 = requests.post(url2,json = data2)
r = r.json()
r2 = r2.json()
print(r)
print(r2)


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]

for i,j in r2['data'].items():
        if i not in r['data'].keys() or j not in r['data'].values():
            val = r['data'].get(i,'null')
            print(i,j,':',get_keys(r['data'],val),val)













a=1


