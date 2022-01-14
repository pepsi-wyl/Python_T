# -*- coding: utf-8 -*-
# @Time: 2022/1/7 10:21
# @Author: pepsi-wyl
# @File: test7.py
# @Software: PyCharm

# 文件操作
# r w rb wb
# file = open("test.txt", "w")  # 打开文件  w写模式     文件不存在则创建
# file = open("test.txt")       # 打开文件  默认为r模式  文件不存在则抛出异常
# file.close()                  # 关闭文件

# 写入  write
# file = open("test.txt", "w")
# file.write("Hello Python!")
# file.close()

# 读出  read
# file = open("test.txt", "r")
#
# # 读取指定个数的字符
# content = file.read(5)
# print(content)
# content = file.read(5)     # 往后移动5个字符
# print(content)
#
# # 读取一行
# content = file.readline()
# print(content)
#
# # 读取多行
# content = file.readlines()
# for i in range(len(content)):
#     print(i+1, " ", content[i])


# file.close()


import os
# os.rename("test.txt", "test.txt")   # 修改文件名称
# os.remove("test.txt")               # 删除文件


