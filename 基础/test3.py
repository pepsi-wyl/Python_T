# -*- coding: utf-8 -*-
# @Time: 2022/1/5 15:41
# @Author: pepsi-wyl
# @File: test3.py
# @Software: PyCharm


# 列表 List
# 定义列表

nameList = []  # 定义空列表
nameList = [1, "pepsi-wyl", 2, "zhazha", 3, "wyl"]  # 定义一个列表

# for 循环遍历    不能引用下标
# for name in nameList:
#     print(type(name))
#     print(name)
#
# for i in range(len(nameList)):
#     print(type(nameList[i]))
#     print(nameList[i])

# while 循环遍历  可以引用下标
# i = 0
# while i < len(nameList):
#     print(type(nameList[i]))  # 下标访问列表元素
#     print(nameList[i])
#     i = i + 1


# 增

# # append 末尾添加
# nameList.append(4)
# nameList.append("bsy")
# print(nameList)
#
# # append 与 extend
a = [1, 2]
b = [3, 4]
# a.append(b)  # 列表当成一个元素
# print(a)
a.extend(b)  # 列表拆分成多个元素
print(a)
#
# # 插  insert
# nameList.insert(2, 4)
# nameList.insert(3, "bsy")
# print(nameList)


# 删

# # del
# del nameList[4]
# del nameList[4]
# print(nameList)
#
# # pop
# nameList.pop(4)
# nameList.pop(4)
# print(nameList)
#
# # remove   只移除第一个匹配元素
# nameList.remove(3)
# nameList.remove("wyl")
# print(nameList)

# 改
# nameList[4] = 4
# nameList[5] = "bys"
# print(nameList)

# 查

# # in
# if "wyl" in nameList:
#     print(True)
# else:
#     print(False)
#
# # not in
# if "wyl" not in nameList:
#     print(True)
# else:
#     print(False)
#
# # index 返回找到首元素的下标  ("findContent", beginIndex, endIndex)  [左闭右开]
# print(nameList.index("wyl", 0, len(nameList)))
# print(nameList.index("wyl", 0, 5))  # 左闭右开 找不抛出异常
#
# # count 统计该元素有几个
# print(nameList.count("wyl"))
#
# # 切片
# print(nameList[2: 4])

# numbers = [1, 4, 2, 3]
# # 排序 sort 默认升序 降序((reverse=True)
# numbers.sort(reverse=True)
# print(numbers)
#
# # 反转 reverse
# numbers.reverse()
# print(numbers)

# # 列表嵌套
# schoolList = [["南阳理工学院", "南阳师范学院"], ["安阳师范学院", "安阳工学院", "安阳学院"], ["信阳学院"]]
#
# # 直接访问
# print(schoolList[0])
# print(schoolList[0][0])
#
# # 二维遍历
# for schools in schoolList:
#     for school in schools:
#         print(school)

# 例子
# 帮老师随机分配办公室
# import random
# offices = [[], [], []]
# names = ["A", "B", "C", "D", "E", "F", "G", "H"]
# for name in names:
#     index = random.randint(0, 2)
#     offices[index].append(name)
# for i in range(len(offices)):
#     print("办公室", i + 1, ": 为", len(offices[i]), "人 为", end=" ")
#     for name in offices[i]:
#         print(name, end=" ")
#     print(end="\n")

# 展示商品
# products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499]]
# for i in range(len(products)):
#     print(i+1, end="\t")
#     for j in range(len(products[i])):
#         print(products[i][j], end="\t")
#     print(end="\n")
#
# products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499]]
# for i, product in enumerate(products):
#     print(i+1, product)


