# -*- coding: utf-8 -*-
# @Time: 2022/1/6 21:11
# @Author: pepsi-wyl
# @File: test5.py
# @Software: PyCharm

# dict 字典 key-value

dictInfo = {"name": "pepsi-wyl",  "age": "18"}  # 定义一个字典

# 增
# dictInfo["sex"] = "男"
# print(dictInfo)

# 删

# del    删除
# del dictInfo["name"]
# print(dictInfo)

# clear  清空
# dictInfo.clear()
# print(dictInfo)

# 改
# dictInfo["name"] = "wyl"
# print(dictInfo["name"])
# print(dictInfo.get("name"))

# 查

# # 直接访问
# print(dictInfo["name"])
# print(dictInfo["age"])
# print(dictInfo["sex"])   # 不存在则抛异常
#
# # get访问
# print(dictInfo.get("name"))
# print(dictInfo.get("age"))
# print(dictInfo.get("sex"))        # 不存在则默认为None
# print(dictInfo.get("sex", "男"))   # 不存在则为男
#
# print(dictInfo.keys())   # keys
# print(dictInfo.values()) # values
# print(dictInfo.items())  # items

# 遍历所有的key
for key in dictInfo.keys():
    print(key)
# 遍历所有的value
for value in dictInfo.values():
    print(value)

# 遍历所有的 key- value
for key in dictInfo.keys():
    print(key, end="---")
    print(dictInfo.get(key))

for key, value in dictInfo.items():
    print(key, "---", value)


# 集合  set  一组key的集合(key不重复)


# 列表[]  有序  可变类型
# 元组()  有序  不可变类型
# 字典{}  无序  key不可变 value可变
# 集合{}  无序  可变类型(不重复)


