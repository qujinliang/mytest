import requests
import hashlib
from exa_100.py_mongo import Check
import re
import time
import os
import json

'''
1. 调用py_mongo读取数据函数
2. 对读取的数据数据进行格式化处理
3. 使用格式化后的数据调用查验接口进行批量查验
4. 如果查验成功只打印返回结果，否则打印请求发票数据并写入rizhi文件
'''
url = "http://check.fapiaoxx.com/invoice/check/"
url2 = "http://localhost:8000/invoice/check/"

def md5(md5_str):
    m2 = hashlib.md5()
    m2.update(md5_str)
    return m2.hexdigest()

# 调用Check()类的check_xjdmongo函数获得要查询的发票数据集合
# 返回字典的列表
# 顺便进行了参数sordkey排序并且Md5加密sign
def data1():
    check = Check().check_xdjmongo('04', '20171015','20171030')
    list_data = []
    for i in check:
        if i.get('fplx')=='04':
            fpdm = int((i.get('fpdm')))
            fphm = int((i.get('fphm')))
            fplx = int((i.get('fplx')))
            jym = int((i.get('jym')[-6:]))  #截取校验码的后6位
            kprq = int((i.get("kprq")))
            # 校验码有时会以0开头，整型的话会被省略，所以需要使用zfill方法补0
            # 如果是Int型，就使用格式化 '%06d' %jym 格式
            sign = ("fpdm=%d&fphm=%08d&fplx=%d&jym=%06d&kprq=%d&uniqueId=1000001&16fc375eabe411e686cdb0c090607876".encode("utf-8") % (fpdm, fphm, fplx, jym, kprq))
            fp_data = {"fpdm":str(fpdm), "fphm":'%08d' %(fphm), "fplx":str(fplx), "jym":'%06d' %(jym), "kprq":str(kprq),
                     "uniqueId":"1000001", "sign": md5(sign)}
            list_data.append(fp_data)

        elif i.get('fplx')=='01':
            pass
    # 要把返回结果放在循环平级，也就是循环结束后返回，
    # 这样才会返回完整的列表
    return list_data

# 实例化data1方法
# 循环读取data1列表中的字典格式发票数据
# requests.post请求查验接口
data1 = data1()
with open('rizhi.txt', 'a') as f:
    for j in data1:
        r = requests.post(url, json=j)
        r = r.json()
        if r['code'] == 0:
            print(r)
            #time.sleep()
        else:
            print(r, j)
            f.write(str(j))

