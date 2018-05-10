"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'

import pymysql

db = pymysql.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" %(20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    db.rollback()

db.close()