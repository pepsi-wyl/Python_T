# -*- coding: utf-8 -*-
# @Time: 2022/1/6 20:29
# @Author: pepsi-wyl
# @File: test4.py
# @Software: PyCharm


# 元组 Tuple 列表可以修改 元组不可以修改
tup1 = ()     # 定义空元组
tup2 = (50,)  # 定义有数据的元组

tup = (1, "pepsi-wyl", 2, "zhazha", 3, "wyl")

# for 循环遍历    不能引用下标
for t in tup:
    print(type(t))
    print(t)

for i in range(len(tup)):
    print(type(tup[i]))
    print(tup[i])

# while 循环遍历  可以引用下标
i = 0
while i < len(tup):
    print(type(tup[i]))  # 下标访问列表元素
    print(tup[i])
    i = i + 1

# 增 (连接)
# tupTemp = tup + tup
# print(tupTemp)

# 删 删除元组变量
# del tup
# print(tup)

# 改  不能修改
# tup[0] = 4

# 查
# 切片
# print(tup[2: 4])

