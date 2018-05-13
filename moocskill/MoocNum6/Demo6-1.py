'''
读写csv数据
'''
# coding:utf-8

# 1.使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写。

from urllib.request import urlretrieve
import csv
from itertools import islice
# url = 'http://quotes.money.163.com/service/chddata.html?code=1000002'
# urlretrieve(url,'pingan.csv')

# 读CSV文件，编码格式需要用gbk,默认utf8会报错

with open('pingan.csv','rt',encoding='gbk') as csvfile:
    readCSV = csv.reader(csvfile)
    # 截取前30行
    # result = islice(readCSV,30)

    # 写CSV文件

    with open('pingan2.csv', 'wt', encoding='gbk') as csvfile2:
        writeCSV = csv.writer(csvfile2)
        headers = readCSV.__next__()     # python3 next 是内置方法
        writeCSV.writerow(headers)       # 先把头部信息写进去，然后再迭代

        for row in readCSV:
            if row[0] < '2018-01-01':
                break
            if float(row[12]) >= 50000000:
                print(row)
                writeCSV.writerow(row)

print('end')