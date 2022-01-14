# -*- coding: utf-8 -*-
# @Time: 2022/1/3 21:22
# @Author: pepsi-wyl
# @File: test2.py
# @Software: PyCharm

# 多个变量赋值
# a = b = c = 1
# a, b, c = 1, 2, "pepsi-wyl"


# print 格式话输出
age = 20
# print("我的年龄为:%d岁" % age)
print("我的名字为%s,我的国籍为%s" % ("pepsi-wyl", "中国"))

# print("www", "baidu", "com", sep=".")

# print("不换行", end="")
# print("tab键", end="\t")
# print("换行", end="\n")


# 等待用户输入
# input("\n\n按下 enter 键后退出")

# password = input("请输入密码:")
# print("刚刚输入的密码为:", password)

# # input输入类型为str   强制类型转化 number = int(str)
# number = int(input("请输入数字:"))
# print("刚刚输入的数字为:", number, type(number))


# 条件判断
# 行与缩进 最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
# if True:
#     print("True")
# else:
#     print("False")
# if 1:   # 非0为True
#     print("True")
# else:
#     print("False")
# if True:
#     print("Answer")
#     print("True")
# else:
#     print("Answer")
#     print("False")  # 缩进不一致，会导致运行错误

# if elif else 实例
# score = int(input("请输入成绩h:"))
# if score > 100 or score < 0:
#     print("输入有误!!!")
# else:
#     if score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >= 70:
#         print("C")
#     elif score >= 60:
#         print("D")
#     else:
#         print("E")

# 性别 = 1  # 1为男生
# 单身 = 1  # 1为单身
# if 性别 == 1:
#     print("男生")
#     if 单身 == 1:
#         print("男单身")
#     else:
#         print("非男单身")
# else:
#     print("女生")
#     if 单身 == 1:
#         print("女单身")
#     else:
#         print("非女单身")

# 随机数库
# import random  # 引入随机数库
# number = random.randint(0, 2)
# print(number)

# while循环

# 基本使用
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# while 使用 else语句
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print(i, "已经循环完毕!")

# while 1~100 求和
# i = 1; sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# else:
#     print("循环完毕")
# print(sum)


# for循环  可以遍历任何可迭代对象

# 遍历数字序列，range()函数
# for i in range(5):  # 0-5
#     print(i)
# for i in range(0, 10, 3):  # 0 10 step为3
#     print(i)
# for i in range(-10, -100, -30):  # -10--100 step为-30
#     print(i)

# 字符串
# name = 'pepsi-wyl'
# for i in name:
#     print(i)

# 列表
# languages = ["C", "C++", "Perl", "Python"]
# for i in languages:
#     print(i)

# range()和len()
# languages = ["C", "C++", "Perl", "Python"]
# for i in range(len(languages)):
#     print(i, languages[i])

# break
# i = 0
# while i < 10:
#     i += 1
#     print("-" * 30)
#     if i == 5:
#         break           # 结束整个循环
#     print(i)
# print("循环结束")

# continue
# i = 0
# while i < 10:
#     i += 1
#     print("-" * 30)
#     if i == 5:
#         continue
#     print(i)
# print("循环结束")         # 结束本次循环

# pass
# i = 0
# while i < 10:
#     i += 1
#     print("-" * 30)
#     if i == 5:
#         pass
#         print('执行 pass 块')
#     print(i)
# print("循环结束")           # 结束本次循环

# 例子  乘法表
# for i in range(1, 10, 1):
#     for j in range(1, i + 1, 1):
#         print(i, "*", j, "=", i*j, end="\t")
#     print("\n")

# 字符串

# word = '字符串'
# sentence = "这是一个句子"
# paragraph = """
#   这是一个段落
# """
# print(word); print(sentence); print(paragraph)

# 转义字符
# myStr1 = "I'm a student!"
# myStr2 = 'I\'m a student!'   # '需要转义字符
# print(myStr1); print(myStr2)
# myStr3 = 'Jason said "I like you"'
# myStr4 = "Jason said \"I like you\""
# print(myStr3); print(myStr4)
# print('hello\npepsi-wyl')   # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\npepsi-wyl')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 字符串的截取
# [起始位置:结束位置:步长值]  遵循左闭右开原则
# str = "pepsi-wyl"
# str = "1234567"
# print(str)             # 输出字符串
# print(str[:])          # 输出字符串     [:] 默认取全部字符
# print(str[0])          # 输出字符串第一个字符
# print(str[0:6])        # 输出从第一个开始到第五个的字符
# print(str[2:5])        # 输出从第三个开始到第五个的字符
# print(str[0:-1])       # 输出第一个到倒数第二个的所有字符
# print(str[1:5:2])      # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str[2:])         # 输出从第三个开始后的所有字符
# print(str[:2])         # 输出从开始到第三个结束的所有字符
# print(str*2)           # 输出字符串两次
# print(str+'你好')       # 连接字符串

# 字符串的常见操作

# # 将字符串的第一个字符转换为大写
# print(str.capitalize())
#
# # 编码 解码
# str.encode(encoding='UTF-8', errors='strict').decode(encoding='UTF-8', errors='strict')
#
# # 检测 str 是否包含在字符串中
# print(str.find("wyl"))
# print(str.index("wyl"))
#
# # 返回字符串长度
# print(len(str))
#
# # 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False
# print(str.isalnum())
#
# # 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
# print(str.isalpha())
#
# # 如果字符串只包含数字则返回 True 否则返回 False..
# print(str.isdigit())
#
# # 如果字符串中只包含数字字符，则返回 True，否则返回 False
# print(str.isnumeric())
#
# # 删除字符串左边的空格或指定字符
# print(str.lstrip())
#
# # 删除字符串末尾的空格或指定字符
# print(str.rstrip())
