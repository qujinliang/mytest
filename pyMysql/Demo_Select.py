"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'
'''
    fetchone():该方法获取一下个查询结果集，结果集是一个对象
    fetchall():接受全部的返回结果
    rowcount():这是一个只读属性，并返回执行execute()方法最后影像的行数。
'''

# 实例：查询 EMPLOYEE表中的salary(工资) 字段大于1000的所有数据：
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %d" %(1000)

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s, lname=%s,age=%s,sex=%s,income=%d" %(fname,lname,age,sex,income))
except:
    print("Error: unable to fetch data")
# 关闭数据连接
db.close()