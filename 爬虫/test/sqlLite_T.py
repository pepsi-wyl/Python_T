# -*- coding: utf-8 -*-
# @Time: 2022/1/9 11:00
# @Author: pepsi-wyl
# @File: sqlLite_T.py
# @Software: PyCharm

import sqlite3

# 创建表
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
sql = """
     create table user
     (
     id int primary key,
     name char(50) not null,
     age int not null,
     address char (50),
     salary real
     )
"""
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接

# 插入
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
sql = """
     insert into user(id, name, age, address, salary)
     values (1,'pepsi-wyl', 20,'安阳市', 8000),
     (2,'wyl', 20,'安阳市', 8000)
"""
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接

# 删除
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
sql = """
     delete from user where id=1
"""
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接

# 查询
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
sql = """
     select * from user
"""
result = conn.cursor().execute(sql)             # 获取游标  执行sql语句
for row in result:
    for i in range(len(row)):
        print(row[i], end="\t")
    print()
conn.close()                           # 关闭数据库连接

# 修改
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
sql = """
     update user set name='pepsi-wyl' where id=2
"""
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接



