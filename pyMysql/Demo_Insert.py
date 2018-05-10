"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'

import pymysql

# 打开数据连接
db = pymysql.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
        LAST_NAME, AGE, SEX, INCOME)
        VALUES('Mac','Mohan',20,'M',2000)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生异常错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()