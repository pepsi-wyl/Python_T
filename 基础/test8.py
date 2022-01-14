# -*- coding: utf-8 -*-
# @Time: 2022/1/7 10:50
# @Author: pepsi-wyl
# @File: test8.py
# @Software: PyCharm

# 异常

# 异常捕获

# 简单使用
# try:
#     print("------1------")
#     fopen = open("test_T.txt", "r")  # FileNotFoundError
#     print("------2------")
# except IOError:         # FileNotFoundError 属于 IO 异常(输入输出异常)
#     pass                # 捕获异常后，执行的代码

# 捕获类型需要一致
# try:
#     print(number)                    # NameError
# except NameError:        # 异常类型需要匹配
#     print("NameError")   # 捕获异常后，执行的代码

# 多个异常类型处理以及展示
# try:
#     print("------1------")
#     fopen = open("test_T.txt", "r")    # FileNotFoundError
#     print("------2------")
#     print(number)  # NameError: name 'number' is not defined
# except (NameError, IOError) as result:  # 把出错信息写入result
#     print(result)   # 捕获异常后，执行的代码

# 多个异常类型统一处理
# try:
#     print("------1------")
#     fopen = open("test_T.txt", "r")    # FileNotFoundError
#     print("------2------")
#     print(number)   # NameError: name 'number' is not defined
# except Exception as result:             # Exception 表示所有异常信息
#     print(result)   # 捕获异常后，执行的代码

# try------finally  (可以不用加 except块)
# import time
# try:
#     fopen = open("test.txt", "r")  # FileNotFoundError
#     try:
#         while True:
#             content = fopen.readline()
#             if len(content) == 0:
#                 break
#             print(content)
#             time.sleep(2)
#     except Exception as result:
#         print(result)
#     finally:
#         fopen.close()
#         print("文件关闭")
# except Exception as result:
#     print(result)   # 捕获异常后，执行的代码





