import requests
import hashlib
import json

url = "http://company.fapiaoxx.com/companys/invoice/check"
url2 = "http://check.fapiaoxx.com/invoice/check/"

def md5(md5_str):
    m2 = hashlib.md5()
    m2.update(md5_str)
    return m2.hexdigest()

data1 = {
            "fpdm": "3100162130","fphm": "44564484","fplx": "01","fpje": "1198.11","kprq": "20170406","uniqueId": "1000004",
            "sign": md5("fpdm=3100162130&fphm=44564484&fpje=1198.11&fplx=01&kprq=20170406""&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
data2 ={
            "fpdm": "3100162130","fphm": "44564484","fplx": "01","fpje": "1198.11","kprq": "20170406","uniqueId": "1000004",
            "sign": md5("fpdm=3100162130&fphm=44564484&fpje=1198.11&fplx=01&kprq=20170406""&uniqueId=1000004&de92dbf0b12d11e6aa28b0c090607876".encode("utf-8"))
        }
r = requests.post(url, json = data1)
r2 = requests.post(url2,json = data2)
r = r.json()
r2 = r2.json()
print(r)
print(r2)
for i,j in r2['data'].items():
    if i in r['data'].keys() and j in r['data'].values():
        pass
    else:
        print(i, j)

a=1


