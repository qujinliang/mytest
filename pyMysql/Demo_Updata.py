"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'

import pymysql

db = pymysql.connect("localhost","testuser","test123","TESTDB")
cursor = db.cursor()
# SQL更新语句
sql = "UPDATA EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" %('M')

try:
    cursor.execute(sql)
    # 提交到数据库
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()