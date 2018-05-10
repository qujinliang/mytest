"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB")

# 使用curosr() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL查询
cursor = cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据，
data = cursor.fetchone()

print("Database version: %s" % data)

# 关闭数据库连接
db.close()


