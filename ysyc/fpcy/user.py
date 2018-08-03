"""
 Created by qujl on 2018-06-20
"""
__author__ = 'qujl'


import requests
import hashlib
from urllib import parse


def md5(md5_str):
    m2 = hashlib.md5()
    m2.update(md5_str)
    return m2.hexdigest()

# 用户信息更改
url = "http://dev.fapiaoxx.com/imanager/manager/userSynchronizationMerchantInfo.ysy"
str = ("address=苏州街16号神州数码大厦5层checker=zhangyudongcity_id=0000001county_id=00000101create_time=2018-06-16 22:41:40"
        "max_invoice_amount=100000max_invoice_amount_common=100000name=神州数码payee=范范province_id=00000seller_bank_account=123456789987654321"
        "seller_bank_name=12345678987654321seller_phone=15010347893taxpaper_num=1234567890c111"
        "taxpayer_key=cbzlm7R89aehDabPT02Fuser_id=21")

# JS encodeURIComponent 对应 python urllib.parse.quote
data = parse.quote(str)
print(data)
sign = md5(data.encode("utf-8"))
print(sign)

payload =  {
    "merchant_id" :"17654321",
    "user_id" : "21",
    "taxpaper_num" :"1234567890c111",
    "name":"神州数码",
    "type":"2",
    "payee":"范范",
    "checker": "zhangyudong",
    "max_invoice_amount":"100000",
    "max_invoice_amount_common":"100000",
    "province_id":"00000",
    "city_id":"0000001",
    "county_id":"00000101",
    "address":"苏州街16号神州数码大厦5层",
    "seller_phone":"15010347893",
    "seller_bank_name":"12345678987654321",
    "seller_bank_account":"123456789987654321",
    "taxpayer_key":"cbzlm7R89aehDabPT02F",
    "sign":sign,
    "tax_disk_type":"0",
    "create_time":"2018-06-16 22:41:40"
}
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)