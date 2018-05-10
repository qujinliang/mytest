"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB")

cursor = db.cursor()
# 使用 execute() 方法执行 SQL， 如果表存在就删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1)
        INCOME FLOAT)"""
cursor.execute(sql)
# 关闭数据库连接
db.close()