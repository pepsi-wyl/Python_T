# -*- coding: utf-8 -*-
# @Time: 2022/1/6 21:47
# @Author: pepsi-wyl
# @File: test6.py
# @Software: PyCharm

# 函数

# 函数的定义
def printInfo():
    print("________________________")
    print("---服务器永不宕机 @zhazha--")
    print("________________________")
# 函数的调用
printInfo()


# 带参数的函数
def addNum(num1, num2):
    print(num1+num2)
addNum(1, 2)

# 带返回值的函数
# 一个返回值
def addNum(num1, num2):
    return num1+num2
print(addNum(1, 2))
# 多个返回值
def divNum(num1, num2):
    return num1 // num2, num1 % num2
n1, n2 = divNum(5, 2)
print("商", n1, "余数", n2)

# 函数之间的调用
def divNum(num1, num2):
    printInfo()
    return num1 // num2, num1 % num2
n1, n2 = divNum(5, 2)
print("商", n1, "余数", n2)

# 例题

# def printOneLine():
#     print("-" * 30)
# printOneLine()
# def printNumLine(number):
#     i = 0
#     while i < number:
#         printOneLine()
#         i = i + 1
# printNumLine(3)
#
# # 求3个数字的和
# def sumNumber(a, b, c):
#     return a+b+c
# print(sumNumber(1, 2, 3))
#
# # 求3个数字的平均值
# def avgNumber(a, b, c):
#     return sumNumber(a, b, c) / 3.0
# print(avgNumber(1, 2, 3))
#
# # 函数中修改局部变量
# number = 100
# def changeNumber():
#     global number  # 表示使用的是全局变量
#     number = 200
# def printNUmber():
#     print(number)
# changeNumber()
# printNUmber()

def main():
    print("Hello")

# 主函数
if __name__ == "__main__":    # 当程序执行时候
    main()  # 调用函数