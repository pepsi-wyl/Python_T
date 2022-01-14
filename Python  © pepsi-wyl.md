
<br />Python 官网  [https://docs.python.org/zh-cn/3/tutorial/index.html](https://docs.python.org/zh-cn/3/tutorial/index.html)
<a name="588fe6e4"></a>
# Python基础


<a name="x2EDM"></a>
## 认识Python


<a name="INMgz"></a>
### 简介


- Python是一门解释性，面向对象的高级编程语言
- Python是开源免费的、支持交互式、可跨平台移植的脚本语言
- Python具有广泛的标准库，功能强大
- Python3.0不兼容Python2.0没有向后兼容
- Python运行速度慢，代码不能加密



<a name="HD1S4"></a>
### 应用方向


- 人工智能
- 网络爬虫
- WEB开发
- 数据分析
- 科学计算
- 常规软件开发



<a name="DhzeS"></a>
### 环境安装

<br />Python官网 [https://www.python.org](https://www.python.org/)<br />pycharm官网 [https://www.jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)<br />

<a name="TitkD"></a>
## 基础语法


<a name="VrG6p"></a>
### 第一个Python程序


```python
# 第一个Python程序
print("hello world")
```


<a name="I6gdh"></a>
### 标识符与保留字


<a name="Q7eUL"></a>
#### 标识符


- 第一个字符必须是字母表中字母或下划线 **_** 。
- 标识符的其他的部分由字母、数字和下划线组成。
- 标识符对大小写敏感。



<a name="LvRca"></a>
#### 保留字

<br />保留字即关键字，我们不能把它们用作任何标识符名称<br />

```python
>>>import keyword
>>>keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
 'raise', 'return', 'try', 'while', 'with', 'yield']
```


<a name="RB5y9"></a>
### 注释

<br />单行注释以 **#** 开头<br />多行注释可以用多个 **#** 号，还有 **'''** 和 **"""**<br />

<a name="MsxCf"></a>
### 语句的特殊情况


<a name="PbmPh"></a>
#### 多行语句

<br />Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句<br />

```python
item_one = 1
item_two = 1
item_two = 1
total = item_one + \
        item_two + \
        item_two
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
total = ['item_one', 'item_two', 'item_two',
         'item_four', 'item_five', 'item_six']
```


<a name="zqGpU"></a>
#### 同一行显示多条语句


```python
import sys; x = 'pepsi-wyl'; sys.stdout.write(x + '\n')
```


<a name="Hwezg"></a>
### 空行

<br />空行与代码缩进不同，空行并不是 Python 语法的一部分。书写时不插入空行，Python 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构<br />空行也是程序代码的一部分<br />

<a name="lALkZ"></a>
### 行与缩进

<br />python最具特色的就是使用缩进来表示代码块，不需要使用大括号 **{}** 。<br />缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数<br />

```python
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")    # 缩进不一致，会导致运行错误
```


<a name="fWq44"></a>
## 随机数库
<a name="avAVa"></a>
### 实例


```python
import random  # 引入随机数库
number = random.randint(0, 2)   # 0 - 2 的整数
print(number)
```


<a name="NyeJH"></a>
## 变量赋值


<a name="W3WCV"></a>
### 多个变量赋值


```python
a = b = c = 1
a, b, c = 1, 2, "pepsi-wyl"
```


<a name="OPckO"></a>
## 输入输出


<a name="LAAsc"></a>
### 输入


```python
# 等待用户输入
input("\n\n按下 enter 键后退出")

password = input("请输入密码:")
print("刚刚输入的密码为:", password)

# input输入类型为str   强制类型转化 number = int(str)
number = int(input("请输入数字:"))
print("刚刚输入的数字为:", number, type(number))
```


<a name="Ex1HN"></a>
### 输出


```python
age = 20
print("我的年龄为:%d岁" % age)
print("我的名字为%s,我的国籍为%s" % ("pepsi-wyl", "中国"))

print("www", "baidu", "com", sep=".")

print("不换行", end="")
print("tab键", end="\t")
print("换行", end="\n")
```


<a name="oi9Kz"></a>
## 条件判断


<a name="mPWJ3"></a>
### 基础语法


```python
if True:
    print("True")
else:
    print("False")
    
if 1:   # 非0为True
    print("True")
else:
    print("False")
    
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")  # 缩进不一致，会导致运行错误
```


<a name="MLYke"></a>
### 实例1


```python
score = int(input("请输入成绩h:"))
if score > 100 or score < 0:
    print("输入有误!!!")
else:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")
```


<a name="E54un"></a>
### 实例2


```python
性别 = 1  # 1为男生
单身 = 1  # 1为单身
if 性别 == 1:
    print("男生")
    if 单身 == 1:
        print("男单身")
    else:
        print("非男单身")
else:
    print("女生")
    if 单身 == 1:
        print("女单身")
    else:
        print("非女单身")
```


<a name="Zuu8f"></a>
## 循环


<a name="c2iql"></a>
### while循环


<a name="FwJa5"></a>
#### 基本使用


```python
i = 0
while i < 5:
    print(i)
    i += 1
```


<a name="hiakM"></a>
#### 与else连用


```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print(i, "已经循环完毕!")
```


<a name="u8APe"></a>
#### 例子

<br />while 1~100 求和<br />

```python
i = 1; sum = 0
while i <= 100:
    sum += i
    i += 1
else:
    print("循环完毕")
print(sum)
```


<a name="UTVKr"></a>
### for循环


<a name="jdcvQ"></a>
#### 数字


```python
for i in range(5):  # 0-5
    print(i)
for i in range(0, 10, 3):  # 0 10 step为3
    print(i)
for i in range(-10, -100, -30):  # -10--100 step为-30
    print(i)
```


<a name="BNb2o"></a>
#### 字符串


```python
name = 'pepsi-wyl'
for i in name:
    print(i)
```


<a name="K9dJk"></a>
#### 列表


```python
languages = ["C", "C++", "Perl", "Python"]
for i in languages:
    print(i)
```


<a name="IzyQo"></a>
#### range()和len()


```python
languages = ["C", "C++", "Perl", "Python"]
for i in range(len(languages)):
    print(i, languages[i])
```


<a name="WrMwP"></a>
#### enumerate


```python
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499]]
for i, product in enumerate(products):
    print(i+1, product)
```


<a name="yIx8v"></a>
### break continue  pass


<a name="HfZxG"></a>
#### break


```python
# break
i = 0
while i < 10:
    i += 1
    print("-" * 30)
    if i == 5:
        break           # 结束整个循环
    print(i)
print("循环结束")
```


<a name="AA7ue"></a>
#### continue


```python
# continue
i = 0
while i < 10:
    i += 1
    print("-" * 30)
    if i == 5:
        continue
    print(i)
print("循环结束")         # 结束本次循环
```


<a name="WYqBg"></a>
#### pass


```python
# pass  无任何作用 防止代码块报错(起到代码块的作用)
i = 0
while i < 10:
    i += 1
    print("-" * 30)
    if i == 5:
        pass
        print('执行 pass 块')
    print(i)
print("循环结束")           # 结束本次循环
```


<a name="qlZhu"></a>
## 字符串


<a name="Nhihc"></a>
### 基本使用


```python
word = '字符串'
sentence = "这是一个句子"
paragraph = """
  这是一个段落
"""
print(word); print(sentence); print(paragraph)
```


<a name="YKmAy"></a>
### 转义字符


```python
# 转义字符
myStr1 = "I'm a student!"
myStr2 = 'I\'m a student!'   # '需要转义字符
print(myStr1); print(myStr2)

myStr3 = 'Jason said "I like you"'
myStr4 = "Jason said \"I like you\""
print(myStr3); print(myStr4)

print('hello\npepsi-wyl')   # 使用反斜杠(\)+n转义特殊字符
print(r'hello\npepsi-wyl')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
```


<a name="gYTcp"></a>
### 字符串的截取


```python
# 字符串的截取
# [起始位置:结束位置:步长值]  遵循左闭右开原则
str = "pepsi-wyl"
str = "1234567"
print(str)             # 输出字符串
print(str[:])          # 输出字符串     [:] 默认取全部字符
print(str[0])          # 输出字符串第一个字符
print(str[0:6])        # 输出从第一个开始到第五个的字符
print(str[2:5])        # 输出从第三个开始到第五个的字符
print(str[0:-1])       # 输出第一个到倒数第二个的所有字符
print(str[1:5:2])      # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str[2:])         # 输出从第三个开始后的所有字符
print(str[:2])         # 输出从开始到第三个结束的所有字符
print(str*2)           # 输出字符串两次
print(str+'你好')       # 连接字符串
```


<a name="kelPC"></a>
### 常见操作


```python
# 字符串的常见操作

# 将字符串的第一个字符转换为大写
print(str.capitalize())

# 编码 解码
str.encode(encoding='UTF-8', errors='strict').decode(encoding='UTF-8', errors='strict')

# 检测 str 是否包含在字符串中
print(str.find("wyl"))
print(str.index("wyl"))

# 返回字符串长度
print(len(str))

# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False
print(str.isalnum())

# 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
print(str.isalpha())

# 如果字符串只包含数字则返回 True 否则返回 False..
print(str.isdigit())

# 如果字符串中只包含数字字符，则返回 True，否则返回 False
print(str.isnumeric())

# 删除字符串左边的空格或指定字符
print(str.lstrip())

# 删除字符串末尾的空格或指定字符
print(str.rstrip())
```
<a name="zUHzH"></a>
## 容器


<a name="bIvgk"></a>
### 列表 List


<a name="Nfhhd"></a>
#### 列表定义


```python
nameList = []  # 定义空列表
nameList = [1, "pepsi-wyl", 2, "zhazha", 3, "wyl"]  # 定义一个列表
```


<a name="hyZlX"></a>
#### 遍历列表


```python
# for 循环遍历    不能引用下标
for name in nameList:
    print(type(name))
    print(name)

# for 循环遍历    可以引用下标
for i in range(len(nameList)):
    print(type(nameList[i]))
    print(nameList[i])

# while 循环遍历  可以引用下标
i = 0
while i < len(nameList):
    print(type(nameList[i]))  # 下标访问列表元素
    print(nameList[i])
    i = i + 1
```


<a name="u2dlX"></a>
#### 增


```python
# append 末尾添加
nameList.append(4)
nameList.append("bsy")
print(nameList)

# append 与 extend
a = [1, 2]
b = [3, 4]
a.append(b)  # 列表当成一个元素
print(a)
a.extend(b)  # 列表拆分成多个元素
print(a)

# 插  insert
nameList.insert(2, 4)
nameList.insert(3, "bsy")
print(nameList)
```


<a name="QcaW2"></a>
#### 删


```python
# del
del nameList[4]
del nameList[4]
print(nameList)

# pop
nameList.pop(4)
nameList.pop(4)
print(nameList)

# remove   只移除第一个匹配元素
nameList.remove(3)
nameList.remove("wyl")
print(nameList)
```


<a name="MXhRv"></a>
#### 查


```python
# in
if "wyl" in nameList:
    print(True)
else:
    print(False)

# not in
if "wyl" not in nameList:
    print(True)
else:
    print(False)

# index 返回找到首元素的下标  ("findContent", beginIndex, endIndex)  [左闭右开]
print(nameList.index("wyl", 0, len(nameList)))
print(nameList.index("wyl", 0, 5))  # 左闭右开 找不抛出异常

# count 统计该元素有几个
print(nameList.count("wyl"))

# 切片
print(nameList[2: 4])
```


<a name="CdjOY"></a>
#### 改


```python
nameList[4] = 4
nameList[5] = "bys"
print(nameList)
```


<a name="RPMWS"></a>
#### 排序和反转


```python
numbers = [1, 4, 2, 3]
# 排序 sort 默认升序 降序((reverse=True)
numbers.sort(reverse=True)
print(numbers)

# 反转 reverse
numbers.reverse()
print(numbers)
```


<a name="l1La2"></a>
#### 列表嵌套


```python
# 列表嵌套
schoolList = [["南阳理工学院", "南阳师范学院"], ["安阳师范学院", "安阳工学院", "安阳学院"], ["信阳学院"]]

# 直接访问
print(schoolList[0])
print(schoolList[0][0])

# 二维遍历
for schools in schoolList:
    for school in schools:
        print(school)
```


<a name="CVSVQ"></a>
#### 例子


```python
# 帮老师随机分配办公室
import random
offices = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
for i in range(len(offices)):
    print("办公室", i + 1, ": 为", len(offices[i]), "人 为", end=" ")
    for name in offices[i]:
        print(name, end=" ")
    print(end="\n")
```


```python
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499]]
for i in range(len(products)):
    print(i+1, end="\t")
    for j in range(len(products[i])):
        print(products[i][j], end="\t")
    print(end="\n")

    
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499]]
for i, product in enumerate(products):
    print(i+1, product)
```


<a name="jqfkN"></a>
### 元组 Tuple

<br />列表可以修改 元组不可以修改<br />

<a name="EZJ26"></a>
#### 元组定义


```python
tup1 = ()     # 定义空元组
tup2 = (50,)  # 定义有数据的元组

tup = (1, "pepsi-wyl", 2, "zhazha", 3, "wyl")
```


<a name="QK0gn"></a>
#### 遍历元组


```python
# for 循环遍历    不能引用下标
for t in tup:
    print(type(t))
    print(t)

# for  循环遍历   可以引用下标
for i in range(len(tup)):
    print(type(tup[i]))
    print(tup[i])

# while 循环遍历  可以引用下标
i = 0
while i < len(tup):
    print(type(tup[i]))  # 下标访问列表元素
    print(tup[i])
    i = i + 1
```


<a name="oiY1q"></a>
#### 增


```python
tupTemp = tup + tup
print(tupTemp)
```


<a name="EBUca"></a>
#### 删


```python
del tup
print(tup)
```


<a name="WEPZE"></a>
#### 查


```python
# 切片
# print(tup[2: 4])
```


<a name="DXXiL"></a>
#### 改 不能修改


```python
# 改  不能修改
tup[0] = 4
```


<a name="fTTYU"></a>
### 字典Dict


<a name="qIf7P"></a>
#### 字典定义


```python
dictInfo = {"name": "pepsi-wyl",  "age": "18"}  # 定义一个字典
```


<a name="mJuCd"></a>
#### 增


```python
dictInfo["sex"] = "男"
print(dictInfo)
```


<a name="RgqXa"></a>
#### 删


```python
# del    删除
del dictInfo["name"]
print(dictInfo)

# clear  清空
dictInfo.clear()
print(dictInfo)
```


<a name="t4qhz"></a>
#### 查


```python
# 直接访问
print(dictInfo["name"])
print(dictInfo["age"])
print(dictInfo["sex"])   # 不存在则抛异常

# get访问
print(dictInfo.get("name"))
print(dictInfo.get("age"))
print(dictInfo.get("sex"))        # 不存在则默认为None
print(dictInfo.get("sex", "男"))   # 不存在则为男

print(dictInfo.keys())   # keys
print(dictInfo.values()) # values
print(dictInfo.items())  # items# 切片
# print(tup[2: 4])
```


<a name="Pe6J2"></a>
#### 改


```python
dictInfo["name"] = "wyl"
print(dictInfo["name"])
print(dictInfo.get("name"))
```


<a name="SsxuU"></a>
#### 遍历字典


```python
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
```


<a name="wuaAO"></a>
### 集合 Set
<a name="jI4eh"></a>
#### 集合定义
一组key的集合(key不重复)
<a name="XNFLr"></a>
### 小结
```python
# 列表[]  有序  可变类型
# 元组()  有序  不可变类型
# 字典{}  无序  key不可变 value可变
# 集合{}  无序  可变类型(不重复)
```


<a name="Q11Bi"></a>
## 函数


<a name="WJWdd"></a>
### 定义函数及其调用


```python
# 函数的定义
def printInfo():
    print("________________________")
    print("---服务器永不宕机 @zhazha--")
    print("________________________")
# 函数的调用
printInfo()
```


<a name="aqagk"></a>
### 带参数的函数


```python
# 带参数的函数
def addNum(num1, num2):
    print(num1+num2)
addNum(1, 2)
```


<a name="BNIqK"></a>
### 带返回值的函数


```python
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
```


<a name="dz9S3"></a>
### 函数之间的调用


```python
# 函数之间的调用
def divNum(num1, num2):
    printInfo()
    return num1 // num2, num1 % num2
n1, n2 = divNum(5, 2)
print("商", n1, "余数", n2)
```


<a name="rmB0y"></a>
### 主函数


```python
def main():
    print("main")

# 主函数
if __name__ == "__main__":    # 当程序执行时候
    main()  # 调用函数
```


<a name="NXfvD"></a>
### 例子


```python
def printOneLine():
    print("-" * 30)
printOneLine()
def printNumLine(number):
    i = 0
    while i < number:
        printOneLine()
        i = i + 1
printNumLine(3)

# 求3个数字的和
def sumNumber(a, b, c):
    return a+b+c
print(sumNumber(1, 2, 3))

# 求3个数字的平均值
def avgNumber(a, b, c):
    return sumNumber(a, b, c) / 3.0
print(avgNumber(1, 2, 3))

# 函数中修改局部变量
number = 100
def changeNumber():
    global number  # 表示使用的是全局变量
    number = 200
def printNUmber():
    print(number)
changeNumber()
printNUmber()
```


<a name="eXbWK"></a>
## 文件


<a name="jnzAr"></a>
### 基本操作


```python
# 文件操作
# r w rb wb
file = open("test.txt", "w")  # 打开文件  w写模式     文件不存在则创建
file = open("test.txt")       # 打开文件  默认为r模式  文件不存在则抛出异常
file.close()                  # 关闭文件
```


<a name="aKe19"></a>
### 写入 write


```python
file = open("test.txt", "w")
file.write("Hello Python!")
file.close()
```


<a name="kh4uA"></a>
### 读出 read


```python
# 读出  read
file = open("test.txt", "r")

# 读取指定个数的字符
content = file.read(5)
print(content)
content = file.read(5)     # 往后移动5个字符
print(content)

# 读取一行
content = file.readline()
print(content)

# 读取多行
content = file.readlines()
for i in range(len(content)):
    print(i+1, " ", content[i])
```


<a name="zv3pc"></a>
### os库


```python
os.rename("test.txt", "test.txt")   # 修改文件名称
os.remove("test.txt")               # 删除文件
```


<a name="AF1qj"></a>
## 异常


<a name="ClnFl"></a>
### 简单使用


```python
# 简单使用
try:
    print("------1------")
    fopen = open("test_T.txt", "r")  # FileNotFoundError
    print("------2------")
except IOError:         # FileNotFoundError 属于 IO 异常(输入输出异常)
    pass                # 捕获异常后，执行的代码
```


<a name="KL3eS"></a>
### 捕获类型要一致


```python
# 捕获类型需要一致
try:
    print(number)                    # NameError
except NameError:        # 异常类型需要匹配
    print("NameError")   # 捕获异常后，执行的代码
```


<a name="Oz7Jy"></a>
### 多个异常类型处理及其展示


```python
# 多个异常类型处理以及展示
try:
    print("------1------")
    fopen = open("test_T.txt", "r")    # FileNotFoundError
    print("------2------")
    print(number)  # NameError: name 'number' is not defined
except (NameError, IOError) as result:  # 把出错信息写入result
    print(result)   # 捕获异常后，执行的代码
```


<a name="VxsXz"></a>
### 多个异常类型统一处理


```python
# 多个异常类型统一处理
try:
    print("------1------")
    fopen = open("test_T.txt", "r")    # FileNotFoundError
    print("------2------")
    print(number)   # NameError: name 'number' is not defined
except Exception as result:             # Exception 表示所有异常信息
    print(result)   # 捕获异常后，执行的代码
```


<a name="MMzKH"></a>
### finally块


```python
# try------finally  (可以不用加 except块)
import time
try:
    fopen = open("test.txt", "r")  # FileNotFoundError
    try:
        while True:
            content = fopen.readline()
            if len(content) == 0:
                break
            print(content)
            time.sleep(2)
    except Exception as result:
        print(result)
    finally:
        fopen.close()
        print("文件关闭")
except Exception as result:
    print(result)   # 捕获异常后，执行的代码
```


<a name="o0hgq"></a>
# Python爬虫


<a name="8453e91e"></a>
## 基础知识


<a name="87611fc3"></a>
### 爬取网页
<a name="QScAM"></a>
#### get
```python
# get请求
try:
    # 封装req
    url = "http://httpbin.org/get"
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
         "Referer": url,
         "Connection": "keep-alive"
    }
    req = urllib.request.Request(url, headers=headers)

    # 获取获取响应
    response = urllib.request.urlopen(req, timeout=3)

    # 得到网页信息
    html = response.read().decode('utf8')
    print(html)

except Exception as result:
    print("爬取时间超时!!!异常为:", result) 
```
<a name="nEIRB"></a>
#### post
```python
# post请求
try:

    # 封装req
    url = "http://httpbin.org/post"
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
         "Referer": url,
         "Connection": "keep-alive"
    }
    data = bytes(urllib.parse.urlencode({"name": "pepsi-wyl"}), encoding="utf-8")
    req = urllib.request.Request(url, headers=headers, data=data, method="POST")

    # 获取响应
    response = urllib.request.urlopen(req, timeout=3)

    # 得到网页信息
    html = response.read().decode('utf8')
    print(html)

except Exception as result:
    print("爬取时间超时!!!异常为:", result)
```
<a name="Uo0r4"></a>
#### 补充
```python
import requests

# 模拟浏览器去访问指定URL
def askUrl(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "Referer": url,
            "Connection": "keep-alive"
        }
        return requests.get(url=url, headers=headers, timeout=3)
    except Exception as result:
        print("异常为:", result)
```
<a name="xzKPf"></a>
#### 实例
```python
# 实例
try:
    url = "https://movie.douban.com/top250?start="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Referer": url,
        "Connection": "keep-alive",
        "Cookie": 'bid=RYyYJTz3evg; dbcl2="252561375:aDsS5a8NfUY"; ck=QD23; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1641609628%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.992860265.1641532328.1641561033.1641609628.3; __utmc=30149280; __utmz=30149280.1641609628.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.752140223.1641532328.1641561033.1641609628.3; __utmc=223695111; __utmz=223695111.1641609628.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25256; __utmt_douban=1; __utmb=30149280.10.10.1641609628; __utmt=1; __utmb=223695111.8.10.1641609628; _pk_id.100001.4cf6=482e19d060ed6011.1641532327.3.1641611594.1641561052.'
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req, timeout=1)
    print("爬取的url为", url, "爬取状态码为:", response.status)
    print(response.read().decode('utf8'))
except Exception as result:
    print("异常为:", result.reason)
```

<br />注意 ： 网站有反爬机制 需要伪装浏览器 需要User-Agent参数 有时候需要用cookie去伪装用户登陆<br />

<a name="BeautifulSoup"></a>
### BeautifulSoup


<a name="d19f2c10-2"></a>
#### 基本使用


```python
import re
import bs4

html = open("test.html", "rb").read().decode('utf8')

bs = bs4.BeautifulSoup(html, "html.parser")
```


<a name="b7b05952-1"></a>
#### 基本操作


```python
print(bs)
print(type(bs))        # <class 'bs4.BeautifulSoup'>
print(bs.name)         # [document]

print(bs.head)
print(type(bs.head))    # <class 'bs4.element.Tag'>
print(bs.title)
print(type(bs.title))   # <class 'bs4.element.Tag'>

print(bs.title.string)
print(bs.a.string)
print(type(bs.a.string)) # <class 'bs4.element.NavigableString'>
print(bs.a.attrs)
```


<a name="f869a244"></a>
#### 文档的遍历


```python
print(bs.head.contents)
print(bs.head.contents[1])
```


<a name="8d63d43a"></a>
#### 文档的搜索


```python
# 1)查找所有  find_all
# 字符串过滤      完全符合
list_T = bs.find_all("a")
# 正则表达式搜索   包含即可    (常用)
list_T = bs.find_all(re.compile("a"))
# 方法:传入一个函数，根据函数的要求去搜索
def nameIsExists(tag):
    return tag.has_attr("name")
list_T = bs.find_all(nameIsExists)

# 2)kwargs  参数
list_T = bs.find_all(id="top-nav-notimenu")
list_T = bs.find_all(herf="https://img3.doubanio.com/favicon.ico")
list_T = bs.find_all(class_="more-items")

# 3)text 参数
list_T = bs.find_all(text="个人主页")
list_T = bs.find_all(text=re.compile("\d"))

# 4)limit 参数
list_T = bs.find_all("a", limit=3)

# 5)css选择器
list_T = bs.select("title")               # 标签
list_T = bs.select(".more-items")         # class
list_T = bs.select("#top-nav-notimenu")   # id
```


<a name="2e576047"></a>
### 正则表达式

<br />正则表达式(字符串模式) 判断字符串是否符合一定的标准<br />

<a name="b59c9e0f"></a>
#### 概念


```python
.     表示任何单个字符
[  ]  字符集，对单个字符给出取值范围    [a,b,c] 表示a、b、c  [a-z] 表示a到z单个字符
[^ ]  非字符集，对单个字符给出排除范围   [^abc]  表示非a或b或c的单个字符
*     前一个字符0次或无限次扩展         abc*  表示 ab、abc、abcc、abccc等
+     前一个字符1次或无限次扩展         abc+  表示 abc、abcc、abccc等
？    前一个字符0次或一次扩展           abc?  表示 ab、abc
|     左右表达式任意一个                abc|def 表示abc、def
{m}   扩展前一个字符m次                 ab{2}c    表示abbc
{m,n} 扩展前一个字符m至n次(含n次)       ab{1，2}  表示abc、abbc
^     匹配字符串开头                    ^abc 表示abc且在一个字符串的开头
$     匹配字符串结尾                    abc$ 表示abc且在一个字符串的结尾
()    分组标记,内部只能使用 | 操作符     (abc)表示abc (abc|cef)表示abc、cef
\d    数字,等价于[0-9]
\w    单词字符,等价于[a-z A-Z 0-9 _]

re.search()
re.match()
re.findall()
re.split()
re.finditer()
re.sub()

re.l   对大小写不敏感
re.L   做本地化识别(locale-aware)
re.M   多行匹配,影响^和&
re.s   使.匹配包括换行在内的所有字符
re.U   根据Unicode字符集解析字符。这个标志影响 \w,\W,\b\B
re.X   该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解
```


<a name="ecff77a8"></a>
#### 使用


```python
import re

# search
pat = re.compile("AA")               # 创建模式对象
result = pat.search("CBAAAAAA")      # search字符串被校验的内容
print(result)

result = re.search("AA", "CBAAAAAA")  # 规则(模板) 校验的字符串
print(result)

# findall
result = re.findall("a", "ASDaDFGAa")
print(result)

result = re.findall("[A-Z]", "ASDaDFGAa")
print(result)

result = re.findall("[A-Z]+", "ASDaDFGAa")
print(result)

# sub
result = re.sub("a", "A", "abcdcasd")  # 找到a用A替换，在第三个字符串中查找
print(result)
```


<a name="xlwt"></a>
### xlwt
<a name="Bs2Kp"></a>
#### 使用


```python
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")     # 创建workbook对象
worksheet = workbook.add_sheet("sheet1")       # 创建工作表
for i in range(1, 10, 1):
    for j in range(1, i + 1, 1):
        worksheet.write(i, j, "%d * %d = %d" %(i, j, i*j))     # 写入数据
workbook.save("student.xls")                   # 保存数据表
```


<a name="sqlite"></a>
### sqlite


<a name="157d5306"></a>
#### 创建数据库


```python
import sqlite3

conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
conn.close()                           # 关闭数据库连接
```


<a name="b9cdb1ae"></a>
#### 创建表


```python
import sqlite3

# 创建表
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
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接
```


<a name="9bdb07e7"></a>
#### 插入


```python
# 插入

sql = """
     insert into user(id, name, age, address, salary)
     values (1,'pepsi-wyl', 20,'安阳市', 8000),
     (2,'wyl', 20,'安阳市', 8000)
"""
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接
```


<a name="2f4aaddd"></a>
#### 删除


```python
# 删除

sql = """
     delete from user where id=1
"""
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接
```


<a name="bee912d7"></a>
#### 查询


```python
# 查询

sql = """
     select * from user
"""
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
result = conn.cursor().execute(sql)             # 获取游标  执行sql语句
for row in result:
    for i in range(len(row)):
        print(row[i], end="\t")
    print()
conn.close()                           # 关闭数据库连接
```


<a name="8347a927"></a>
#### 修改


```python
# 修改

sql = """
     update user set name='pepsi-wyl' where id=2
"""
conn = sqlite3.connect("test.db")      # 打开或者创建数据库文件
conn.cursor().execute(sql)             # 获取游标  执行sql语句
conn.commit()                          # 提交数据库操作
conn.close()                           # 关闭数据库连接
```


<a name="31ecc0e6"></a>
## 爬取豆瓣TOP250


<a name="5afc4ad1"></a>
### 源码  spider.py


```python
# -*- coding: utf-8 -*-
# @Time: 2022/1/7 13:12
# @Author: pepsi-wyl
# @File: spider.py
# @Software: PyCharm

"""
#  爬取豆瓣网 https://movie.douban.com/top250
#  名称 豆瓣评分 评价数 电影概况 电影链接
"""

# 引入模块(库)
from bs4 import BeautifulSoup         # 网页解析,获取数据
import re                             # 正则表达式，文字匹配
import urllib.request                 # 制定URL，获取网页数据
import xlwt                           # Excel操作
import sqlite3                        # SQLLite数据库操作

# 主函数
def main():

    url = "https://movie.douban.com/top250?start="
    savePath = "doubanTop250.xls"
    dbPath="doubanMovie.db"

    dataList = getDate(url)
    saveDateToFile(dataList, savePath)
    saveDataToDatabase(dataList, dbPath)

# 爬取网页 和 数据解析
def getDate(url):
    dataList = []
    for i in range(0, 10):
        # 循环爬取数据   0-10
        html = askUrl(url + str(i*25))
        # 数据解析 HTML
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.find_all("div", class_="item"):  # 获取class为item的div
            data = []  # 存储一部电影的信息
            # 电影名称
            title = re.findall(
                re.compile(r'<span class="title">(.*)</span>'),
                str(item)
            )
            otherTitle = re.findall(
                re.compile(r'<span class="other">(.*)</span>'),
                str(item)
            )
            data.append(title[0])
            if len(title) == 2:
                data.append(title[1].replace("/", " ").replace("\xa0", ""))
            else:
                data.append(' ')
            data.append(otherTitle[0].replace("/", " ").replace("\xa0", ""))
            # 照片链接
            img = re.findall(
                re.compile(re.compile(r'<img.*src="(.*?)"', re.S)),  # re.s 让换行符号包含在字符串中
                str(item)
            )[0]
            data.append(img)
            # 电影详情链接
            link = re.findall(
                re.compile(r'<a href="(.*?)">'),
                str(item)
            )[0]
            data.append(link)
            # 评价分数
            ratingNumber = re.findall(
                re.compile(r'<span class="rating_num" property="v:average">(.*)</span>'),
                str(item)
            )[0]
            data.append(ratingNumber)
            # 评价人数
            JudgeNumber = re.findall(
                re.compile(r'<span>(\d*)人评价</span>'),
                str(item)
            )[0]
            data.append(JudgeNumber)
            # 电影评价
            inq = re.findall(
                re.compile(r'<span class="inq">(.*)</span>'),
                str(item)
            )
            if len(inq) != 0:
                data.append(inq[0].replace("。", ""))
            else:
                data.append(' ')
            # 相关内容
            related = re.findall(
                re.compile(r'<p class="">(.*?)</p>', re.S),
                str(item)
            )
            data.append(related[0].replace("<br/>", "    ").replace("/", " ").replace("\xa0", " ").
                        replace("\n                            ", "").replace("\n                        ", "")
                        )
            dataList.append(data)    # 数据集合
    return dataList

# 模拟浏览器去访问指定URL 返回HTML值
def askUrl(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "Referer": url,
            "Connection": "keep-alive",
            "Cookie": 'bid=RYyYJTz3evg; dbcl2="252561375:aDsS5a8NfUY"; ck=QD23; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1641609628%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.992860265.1641532328.1641561033.1641609628.3; __utmc=30149280; __utmz=30149280.1641609628.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.752140223.1641532328.1641561033.1641609628.3; __utmc=223695111; __utmz=223695111.1641609628.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25256; __utmt_douban=1; __utmb=30149280.10.10.1641609628; __utmt=1; __utmb=223695111.8.10.1641609628; _pk_id.100001.4cf6=482e19d060ed6011.1641532327.3.1641611594.1641561052.'
        }
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request, timeout=2)
        print("爬取的url为", url, "爬取状态码为:", response.status, "......")
        return response.read().decode('utf8')
    except Exception as result:
        print("异常为:", result.reason)

# 保存数据
def saveDateToFile(dataList, savePath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)          # 创建workbook对象
    worksheet = workbook.add_sheet("doubanTop250", cell_overwrite_ok=True)   # 创建工作表
    column= ['影片中文名', '影片外文名', '影片别名', '图片链接', '电影详情链接', '评分', '评价数', '概况', '相关信息']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    for i in range(len(dataList)):
        data = dataList[i]
        for j in range(len(data)):
            worksheet.write(i+1, j, data[j])
    workbook.save(savePath)  # 保存数据表

# 保存数据到数据库
def saveDataToDatabase(dataList, dbPath):
    initDatabase(dbPath)
    for data in dataList:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
        sql="insert into movieTop250 (title1,title2,otherTitle,imgLink,infoLink,score,rated,instroduction,info)values (%s)" % ",".join(data)
        dbUtil(sql, dbPath)

# 创建数据库和数据表
def initDatabase(dbPath):
    sql = """
    create table movieTop250
    (
    id integer primary key autoincrement,
    title1 varchar ,
    title2 varchar ,
    otherTitle varchar ,
    imgLink text,
    infoLink text,
    score numeric ,
    rated numeric ,
    instroduction text,
    info text
    )
    """
    dbUtil(sql, dbPath)

def dbUtil(sql, dbPath):
    conn = sqlite3.connect(dbPath)       # 打开或者创建数据库文件
    conn.cursor().execute(sql)           # 获取游标  执行sql语句
    conn.commit()                        # 提交数据库操作
    conn.close()                         # 关闭数据库连接

# 调用主函数
if __name__ == "__main__":
    main()
    # initDatabase(dbPath="doubanMovie.db")
    
```


<a name="7b34382d"></a>
### 运行截图


<a name="yvc4u"></a>
#### 项目结构<br />![1641722336(1).png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1641722368160-1a27eddf-3ba9-40c5-946c-28a08b2e3111.png#clientId=u8500ef8c-802b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=68&id=u421c021c&margin=%5Bobject%20Object%5D&name=1641722336%281%29.png&originHeight=68&originWidth=185&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12651&status=done&style=none&taskId=u395ed187-ee2c-472c-8ea6-adc36d13d33&title=&width=185#crop=0&crop=0&crop=1&crop=1&id=DxA7g&originHeight=68&originWidth=185&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)<br /><br />
<a name="druJA"></a>
#### 控制台<br />![cf9482cd8e5c3b24e9cc581d34cebb7.png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1641722183672-20f9f5a3-9043-4b36-b564-ecf09ce98134.png#clientId=u8500ef8c-802b-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u1d0fd226&margin=%5Bobject%20Object%5D&name=cf9482cd8e5c3b24e9cc581d34cebb7.png&originHeight=342&originWidth=807&originalType=binary&ratio=1&rotation=0&showTitle=false&size=370084&status=done&style=none&taskId=uc61eb02d-ae69-4c93-8caf-1c3d174e7d3&title=#crop=0&crop=0&crop=1&crop=1&id=DRzgH&originHeight=342&originWidth=807&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
<a name="IOCSc"></a>
#### <br />doubanTop250.xls<br />![595a49983669d21873038dcd56a08ac.png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1641722243592-9a27896f-cb58-43d9-9e04-cfed3d4ad180.png#clientId=u8500ef8c-802b-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=ub978a186&margin=%5Bobject%20Object%5D&name=595a49983669d21873038dcd56a08ac.png&originHeight=670&originWidth=1580&originalType=binary&ratio=1&rotation=0&showTitle=false&size=182930&status=done&style=none&taskId=u89236f55-d766-4c35-80d4-d93d8f2ffc8&title=#crop=0&crop=0&crop=1&crop=1&id=exlU3&originHeight=670&originWidth=1580&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
<a name="UUdYe"></a>
#### <br />sqlLite数据库<br />![1641722349(1).png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1641722365029-91bda3c0-9f28-4aab-aad7-cfcc8728cd96.png#clientId=u8500ef8c-802b-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=143&id=jbXID&margin=%5Bobject%20Object%5D&name=1641722349%281%29.png&originHeight=143&originWidth=297&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39621&status=done&style=none&taskId=uc4d39346-d71d-4ac8-885e-78ce09f5e1a&title=&width=297#crop=0&crop=0&crop=1&crop=1&id=hvBst&originHeight=143&originWidth=297&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)<br />![e0bff89c6536e7dd61afa92c88e628e.png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1641722320833-59cf0851-ff13-468c-b87e-68f8b6ef6bb5.png#clientId=u8500ef8c-802b-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u05c1fff8&margin=%5Bobject%20Object%5D&name=e0bff89c6536e7dd61afa92c88e628e.png&originHeight=725&originWidth=2187&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1867753&status=done&style=none&taskId=u3fd68c9d-ed86-49fe-a8ce-e54dadd68f4&title=#crop=0&crop=0&crop=1&crop=1&id=tXtMm&originHeight=725&originWidth=2187&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)


<a name="zksm9"></a>
## 爬取疫情数据和豆瓣TOP250 (多线程)


<a name="jolwK"></a>
### 源码 spider.py
```python
# -*- coding: utf-8 -*-
# @Time: 2022/1/12 14:26
# @Author: pepsi-wyl
# @File: spider.py
# @Software: PyCharm

# 爬取疫情数据
import re
import sqlite3
import threading
import requests
import xlwt as xlwt
from bs4 import BeautifulSoup  # 网页解析,获取数据

# 初始化数据库
def initDatabase(dbPathYingQing, dbPathDouBan):
    sql = "drop table province"
    dbUtil(sql, dbPathYingQing)
    sql = "create table province(id integer primary key autoincrement, year numeric,date varchar,country varchar,province varchar, confirm numeric,dead numeric,heal numeric,newConfirm numeric,newHeal numeric,newDead numeric)"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table provinceNow"
    dbUtil(sql, dbPathYingQing)
    sql = "create table provinceNow(id integer primary key autoincrement, year numeric,date varchar,country varchar,province varchar, confirm numeric,dead numeric,heal numeric,newConfirm numeric,newHeal numeric,newDead numeric)"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table address"
    dbUtil(sql, dbPathYingQing)
    sql = "create table address(id integer primary key autoincrement, area varchar ,type numeric )"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table province31"
    dbUtil(sql, dbPathYingQing)
    sql = "create table province31(id integer primary key autoincrement, province varchar ,city varchar ,syear numeric ,date varchar ,confirm numeric ,nowConfirm numeric ,confirmAdd numeric ,dead numeric ,grade varchar )"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table movieTop250"
    dbUtil(sql, dbPathDouBan)
    sql = "create table movieTop250(id integer primary key autoincrement, title1 varchar , title2 varchar , otherTitle varchar , imgLink text, infoLink text, score numeric , rated numeric , instroduction text, info text )"
    dbUtil(sql, dbPathDouBan)

# 模拟浏览器去访问指定URL
def askUrl(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "Referer": url,
            "Connection": "keep-alive"
        }
        return requests.get(url=url, headers=headers, timeout=3)
    except Exception as result:
        print("异常为:", result)


#  处理数据得到dataListProvince
def getDataProvince(urlProvince, province, savePath, dbPath):
    print("......正在爬取全国各个省份疫情的历史数据......")
    dataList = []
    for item in province:
        item = (str(item.encode('utf-8')).lstrip("b'").rstrip("'").replace(r'\x', '%').upper())
        data = askUrl(urlProvince + item).json()['data']
        dataList.extend(data)
    t1 = threading.Thread(target=saveDateToFileProvince, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabaseProvince, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件Province
def saveDateToFileProvince(dataList, savePath):
    print("......正在保存全国各个省份疫情的历史数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['年', '日期', '国家', '省份', '累计确诊', ' 累计死亡', '累计治愈', '新确诊', '新确诊', '新死亡']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    i = 1
    for item in dataList:
        param = [item['year'], item['date'], item['country'], item['province'], item['confirm'], item['dead'],
                 item['heal'], item['newConfirm'], item['newHeal'], item['newDead']]
        for j in range(len(param)):
            worksheet.write(i, j, param[j])
        i = i + 1
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库Province
def saveDateToDatabaseProvince(dataList, dbPath):
    print("......正在保存全国各个省份疫情的历史数据到数据库......")
    for item in dataList:
        #             年            日期            国家              省份             累计确诊         累计死亡      累计治愈          新确诊             新确诊            新死亡
        param = [item['year'], item['date'], item['country'], item['province'], item['confirm'], item['dead'],
                 item['heal'], item['newConfirm'], item['newHeal'], item['newDead']]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into province(year,date,country,province,confirm,dead,heal,newConfirm,newHeal,newDead) values (%s)" % ",".join(
            param)
        print(sql)
        dbUtil(sql, dbPath)


#  处理数据得到dataListProvinceNow
def getDataProvinceNow(province, savePath, dbPath):
    print("......正在查询全国各个省份疫情的最新数据......")
    dataList = []
    # 解决省份更新时间不同问题
    for item in province:
        item = '"' + item + '"'
        sql = "select * from province where province like %s order by year DESC ,date DESC ,province limit 1" % item
        print(sql)
        conn = sqlite3.connect(dbPath)
        result = conn.cursor().execute(sql)
        for data in result:
            dataList.append(data)
        conn.close()
    t1 = threading.Thread(target=saveDateToFileProvinceNow, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabaseProvinceNow, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件ProvinceNow
def saveDateToFileProvinceNow(dataList, savePath):
    print("......正在保存全国各个省份疫情的历史数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['年', '日期', '国家', '省份', '累计确诊', ' 累计死亡', '累计治愈', '新确诊', '新确诊', '新死亡']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    for i in range(len(dataList)):
        data = dataList[i]
        for j in range(len(data) - 1):
            worksheet.write(i + 1, j, data[j + 1])
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库ProvinceNow
def saveDateToDatabaseProvinceNow(dataList, dbPath):
    print("......正在保存全国各个省份疫情的历史数据到数据库......")
    for item in dataList:
        param = [item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10]]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into provinceNow(year,date,country,province,confirm,dead,heal,newConfirm,newHeal,newDead) values(%s)" % ",".join(
            param)
        print(sql)
        dbUtil(sql, dbPath)


# 处理数据得到dataListAddress
def getDataAddress(urlAddress, savePath, dbPath):
    print("......正在爬取全国各个省份的风险地区数据......")
    dataList = askUrl(urlAddress).json()['data']
    t1 = threading.Thread(target=saveDateToFileAddress, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabaseAddress, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件Address
def saveDateToFileAddress(dataList, savePath):
    print("......正在保存全国各个省份的风险地区数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['地区', '风险类型']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    i = 1
    for item in dataList:
        param = [item['area'], "中风险地区" if ['type'] == '1' else "高风险地区"]
        for j in range(len(param)):
            worksheet.write(i, j, param[j])
        i = i + 1
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库Address
def saveDateToDatabaseAddress(dataList, dbPath):
    print("......正在保存全国各个省份的风险地区数据到数据库......")
    for item in dataList:
        param = [item['area'], "中风险地区" if item['type'] == '1' else "高风险地区"]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into address (area,type) values(%s)" % ",".join(param)
        print(sql)
        dbUtil(sql, dbPath)


# 处理数据得到dataList31Province
def getData31Province(url31Province, savePath, dbPath):
    print("......正在爬取近期31省区市本土病例数据......")
    dataList = askUrl(url31Province).json()['data']['statisGradeCityDetail']
    t1 = threading.Thread(target=saveDateToFile31Province, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabase31Province, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件31Province
def saveDateToFile31Province(dataList, savePath):
    print("......正在保存近期31省区市本土病例数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['省份', '城市', '年', '日期', '累计确诊', ' 现确诊', '确诊增加', '死亡', '风险等级']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    i = 1
    for item in dataList:
        param = [item['province'], item['city'], item['syear'], item['date'], item['confirm'], item['nowConfirm'],
                 item['confirmAdd'], item['dead'], item['grade']]
        for j in range(len(param)):
            worksheet.write(i, j, param[j])
        i = i + 1
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库31Province
def saveDateToDatabase31Province(dataList, dbPath):
    print("......正在保存近期31省区市本土病例数据到数据库......")
    for item in dataList:
        #               省份              城市            年           日期           累计确诊           现确诊               确诊增加           死亡        风险等级
        param = [item['province'], item['city'], item['syear'], item['date'], item['confirm'], item['nowConfirm'],
                 item['confirmAdd'], item['dead'], item['grade']]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into province31 (province,city,syear,date,confirm,nowConfirm,confirmAdd,dead,grade) values ( %s )" % ",".join(param)
        print(sql)
        dbUtil(sql, dbPath)


# 爬取网页和数据解析DouBanTop
def getDateDouBanTop(url, savePath, dbPath):
    dataList = []
    for i in range(0, 10):
        # 循环爬取数据   0-10
        print("正在爬取豆瓣电影Top250的数据......")
        html = askUrl(url + str(i * 25)).text
        # 数据解析 HTML
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.find_all("div", class_="item"):  # 获取class为item的div
            data = []  # 存储一部电影的信息
            # 电影名称
            title = re.findall(
                re.compile(r'<span class="title">(.*)</span>'),
                str(item)
            )
            otherTitle = re.findall(
                re.compile(r'<span class="other">(.*)</span>'),
                str(item)
            )
            data.append(title[0])
            if len(title) == 2:
                data.append(title[1].replace("/", " ").replace("\xa0", ""))
            else:
                data.append(' ')
            data.append(otherTitle[0].replace("/", " ").replace("\xa0", ""))
            # 照片链接
            img = re.findall(
                re.compile(re.compile(r'<img.*src="(.*?)"', re.S)),  # re.s 让换行符号包含在字符串中
                str(item)
            )[0]
            data.append(img)
            # 电影详情链接
            link = re.findall(
                re.compile(r'<a href="(.*?)">'),
                str(item)
            )[0]
            data.append(link)
            # 评价分数
            ratingNumber = re.findall(
                re.compile(r'<span class="rating_num" property="v:average">(.*)</span>'),
                str(item)
            )[0]
            data.append(ratingNumber)
            # 评价人数
            JudgeNumber = re.findall(
                re.compile(r'<span>(\d*)人评价</span>'),
                str(item)
            )[0]
            data.append(JudgeNumber)
            # 电影评价
            inq = re.findall(
                re.compile(r'<span class="inq">(.*)</span>'),
                str(item)
            )
            if len(inq) != 0:
                data.append(inq[0].replace("。", ""))
            else:
                data.append(' ')
            # 相关内容
            related = re.findall(
                re.compile(r'<p class="">(.*?)</p>', re.S),
                str(item)
            )
            data.append(related[0].replace("<br/>", "    ").replace("/", " ").replace("\xa0", " ").
                        replace("\n                            ", "").replace("\n                        ", "")
                        )
            dataList.append(data)  # 数据集合
    t1 = threading.Thread(target=saveDateToFileDouBanTop, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDataToDatabaseDouBanTop, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件
def saveDateToFileDouBanTop(dataList, savePath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet("doubanTop250", cell_overwrite_ok=True)  # 创建工作表
    column = ['影片中文名', '影片外文名', '影片别名', '图片链接', '电影详情链接', '评分', '评价数', '概况', '相关信息']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    for i in range(len(dataList)):
        data = dataList[i]
        for j in range(len(data)):
            worksheet.write(i + 1, j, data[j])
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库
def saveDataToDatabaseDouBanTop(dataList, dbPath):
    for data in dataList:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = "insert into movieTop250 (title1,title2,otherTitle,imgLink,infoLink,score,rated,instroduction,info)values (%s)" % ",".join(
            data)
        dbUtil(sql, dbPath)


def dbUtil(sql, dbPath):
    conn = sqlite3.connect(dbPath)  # 打开或者创建数据库文件
    conn.cursor().execute(sql)  # 获取游标  执行sql语句
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接


# 主函数
def main():
    dbPathYiQing = "chinaYiQing.db"
    dbPathDouBan = "doubanMovie.db"
    savePathDouBan = "doubanTop250.xls"
    savaPathProvince = "province.xls"
    savaPathAddress = "address.xls"
    savaPath31Province = "province31.xls"
    savaPathProvinceNow = "provinceNow.xls"
    province = ['河南', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏',
                '浙江', '安徽', '福建', '江西', '山东', '湖北', '湖南',
                '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃',
                '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆',
                '北京', '天津', '上海', '重庆', '香港', '澳门']
    urlDouBan = "https://movie.douban.com/top250?start="
    urlProvince = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province="
    urlAddress = "https://eyesight.news.qq.com/sars/riskarea"
    url31Province = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail"

    threading.Thread(target=initDatabase, args=(dbPathYiQing, dbPathDouBan)).start()  # 初始化数据库
    thread1 = threading.Thread(target=getDataProvince, args=(urlProvince, province, savaPathProvince, dbPathYiQing))
    thread2 = threading.Thread(target=getData31Province, args=(url31Province, savaPath31Province, dbPathYiQing))
    thread3 = threading.Thread(target=getDataAddress, args=(urlAddress, savaPathAddress, dbPathYiQing))
    thread4 = threading.Thread(target=getDateDouBanTop, args=(urlDouBan, savePathDouBan, dbPathDouBan))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5 = threading.Thread(target=getDataProvinceNow, args=(province, savaPathProvinceNow, dbPathYiQing))
    thread5.start()
    thread5.join()

# 调用主函数
if __name__ == "__main__":
    main()

```
<a name="sHNXa"></a>
### 截图
![1642043896(1).png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1642043906681-a39045c8-8a92-4ada-8803-34fea49d86d8.png#clientId=u13afb36a-07d8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=183&id=u93d7f441&margin=%5Bobject%20Object%5D&name=1642043896%281%29.png&originHeight=183&originWidth=197&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37878&status=done&style=none&taskId=u0c51bffd-e578-4e7f-9d72-120b773c2a9&title=&width=197)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1642043942892-f341d981-3948-4fa7-a982-15a715dddba6.png#clientId=u13afb36a-07d8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=357&id=u4aa85f5f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=357&originWidth=320&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102698&status=done&style=none&taskId=u9b5c16d8-85b6-4aac-9c50-f82b974fac2&title=&width=320)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/23219042/1642043976921-aaf889b2-70c6-4af4-8d6d-7c39232e0dbb.png#clientId=u13afb36a-07d8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=342&id=u25898ec7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=342&originWidth=1255&originalType=binary&ratio=1&rotation=0&showTitle=false&size=541786&status=done&style=none&taskId=ue9a4bad8-7742-4d51-992b-a8e00ea5091&title=&width=1255)<br />
<br />​<br />
<a name="KSXJm"></a>
# Python词云
<a name="ssHtv"></a>
## 导入库
```python
# 引入库
import jieba  # 分词
import matplotlib.pyplot as plt
from matplotlib import pyplot  # 绘图
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy      # 矩阵运算
import sqlite3    # sqlite数据库
```
<a name="KZNI8"></a>
## 从数据库查取数据切割成词
```python
# 获取字符串切割形成词
def getWords():
    str = ""
    conn = sqlite3.connect("doubanMovie.db")
    sql = "select instroduction from movieTop250"
    result = conn.cursor().execute(sql)
    for item in result:
        str = str + item[0]
    conn.close()
    cut = jieba.cut(str)
    str = ' '.join(cut)
    print(len(str))
    return str
```
<a name="oWXXB"></a>
## 绘制词云图片
```python
# 绘制词云图片
def getImg(str):
    wc = WordCloud(
        background_color='white',
        mask=numpy.array(Image.open("tree.jpg")),
        font_path="msyh.ttc"
    ).generate_from_text(str)
    pyplot.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig("treeWord.jpg")

```
tree.jpg<br />![tree.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/23219042/1642042028893-a2deedbd-14e3-4971-a0ff-2413d0ca451c.jpeg#clientId=u13afb36a-07d8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=562&id=u82aedb54&margin=%5Bobject%20Object%5D&name=tree.jpg&originHeight=438&originWidth=500&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42976&status=done&style=none&taskId=u6375ea25-c6f2-4755-b7c0-8fef099063d&title=&width=641)<br />treeWord.jpg<br />![treeWord.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/23219042/1642042033858-d5fc127f-e71f-4827-b7ce-9b398981183a.jpeg#clientId=u13afb36a-07d8-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=480&id=ubc476763&margin=%5Bobject%20Object%5D&name=treeWord.jpg&originHeight=480&originWidth=640&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26005&status=done&style=none&taskId=ub691725e-7917-48c6-8a03-2acf0e9b09e&title=&width=640)
<a name="pIccz"></a>
## 项目代码
```python
# -*- coding: utf-8 -*-
# @Time: 2022/1/10 19:42
# @Author: pepsi-wyl
# @File: cloud.py
# @Software: PyCharm


# 引入库
import jieba  # 分词
import matplotlib.pyplot as plt
from matplotlib import pyplot  # 绘图
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy      # 矩阵运算
import sqlite3    # sqlite数据库

# 主函数
def main():
    getImg(getWords())

# 获取字符串切割形成词
def getWords():
    str = ""
    conn = sqlite3.connect("doubanMovie.db")
    sql = "select instroduction from movieTop250"
    result = conn.cursor().execute(sql)
    for item in result:
        str = str + item[0]
    conn.close()
    cut = jieba.cut(str)
    str = ' '.join(cut)
    print(len(str))
    return str

# 绘制词云图片
def getImg(str):
    wc = WordCloud(
        background_color='white',
        mask=numpy.array(Image.open("tree.jpg")),
        font_path="msyh.ttc"
    ).generate_from_text(str)
    pyplot.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig("treeWord.jpg")

# 调用主函数
if __name__ == "__main__":
    getImg(getWords())
```
<a name="gWii7"></a>
# Python数据可视化
<a name="JFkgJ"></a>
## flask
<a name="tyJjP"></a>
### Test
```python
# app.py
from flask import Flask
app = Flask(__name__)

# 接口 http://127.0.0.1:5000/test
@app.route('/test')
def test():
    return 'test success!'

if __name__ == '__main__':
    app.run()
```
<a name="mKcAH"></a>
### HTML渲染模板
```python
# app.py
from flask import Flask, render_template
app = Flask(__name__)
import datetime

# 通过访问路径，返回渲染模板
@app.route('/index1')
def index1():
    return render_template("XXXXXX.html")

if __name__ == '__main__':
    app.run()
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
hello world
</body>
</html>
```
<a name="vq7Oh"></a>
### 前端携带参数返回后端
```python
# app.py
from flask import Flask
app = Flask(__name__)

# 通过访问路径，获取用户的字符串参数
@app.route('/user/<name>')
def getName(name):
    return '%s' % name

# 通过访问路径，获取用户的整形参数    
@app.route('/user/<int:pwd>')
def getPassword(pwd):
    return '%d' % pwd

# 此外还有float类型

if __name__ == '__main__':
    app.run()
```
<a name="CX9Tk"></a>
### 后台解析数据返回前端
```python
# app.py
from flask import Flask, render_template, request
app = Flask(__name__)

# 后台数据解析
@app.route('/index2')
def index2():
    time = datetime.date.today()
    nameList = ["wyl", "pepsi-wyl", "bsy"]
    userDict = {"name": "wyl", "password": "123456789"}
    return render_template("XXXXXX.html",
                           time=time,
                           nameList=nameList,
                           userDict=userDict
                           )
     
if __name__ == '__main__':
    app.run()
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
        {#字符串#}
        {{ time }}
        <br/>
        {#列表#}
        {% for name in nameList %}
        {{ name }}
        {% endfor %}
        <br/>
        {#字典#}
        <table border="1">
            {% for name, password in userDict.items() %}
             <tr>
                <td>
                    {{ name }}
                </td>
                 <td>
                     {{ password }}
                 </td>
             </tr>
            {% endfor %}
        </table>
</body>
</html>
```
<a name="TRNEk"></a>
### 表单提交
```python
# app.py
from flask import Flask, render_template, request
app = Flask(__name__)

# 表单提交
@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/toRegister', methods=['POST', 'GET'])
def toRegister():
    result = request.form
    print(result)
    return render_template("XXXXXX.html", userDict=result)
    
if __name__ == '__main__':
    app.run()
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>register</title>
</head>
<body>

<form action="{{ url_for('toRegister') }}" method="post">
    <p>username：<input type="text" name="username"></p>
    <p>password：<input type="text" name="password"></p>
    <p><input type="submit"></p>
</form>

</body>
</html>
```
<a name="hjJyZ"></a>
## Echarts
<a name="gvFcU"></a>
### 获取Echarts
从CDN获取
```
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
```
<a name="aInVX"></a>
### 引入Echatrs
```python
<div id="container" style="height: 500px"></div>
            <script type="text/javascript">
                var dom = document.getElementById("container");
                var myChart = echarts.init(dom);
                var app = {};
                var option;
                option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    legend: {},
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            data: {{ cityList|tojson }}
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '累计确诊',
                            type: 'bar',
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ conformList }}
                        },
                        {
                            name: '现确诊',
                            type: 'bar',
                            stack: 'Ad',
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ nowConfirmList }}
                        },
                        {
                            name: '新增确诊',
                            type: 'bar',
                            stack: 'Ad',
                            emphasis: {
                                focus: 'series'
                            },
                            data:  {{ confirmAddList }}
                        },
                        {
                            name: '死亡',
                            type: 'bar',
                            stack: 'Ad',
                            emphasis: {
                                focus: 'series'
                            },
                            data:  {{ deadList }}
                        }
                    ]
                };
                if (option && typeof option === 'object') {
                    myChart.setOption(option);
                }
            </script>
```
<a name="nvqc3"></a>
# Python爬虫+词云+数据可视化+flask
<a name="gEyob"></a>
## spider.py
```python
# -*- coding: utf-8 -*-
# @Time: 2022/1/12 14:26
# @Author: pepsi-wyl
# @File: spider.py
# @Software: PyCharm

# 爬取疫情数据
import re
import sqlite3
import threading
import requests
import xlwt as xlwt
from bs4 import BeautifulSoup  # 网页解析,获取数据

# 初始化数据库
def initDatabase(dbPathYingQing, dbPathDouBan):
    sql = "drop table if exists province"
    dbUtil(sql, dbPathYingQing)
    sql = "create table province(id integer primary key autoincrement, year numeric,date varchar,country varchar,province varchar, confirm numeric,dead numeric,heal numeric,newConfirm numeric,newHeal numeric,newDead numeric)"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table if exists provinceNow"
    dbUtil(sql, dbPathYingQing)
    sql = "create table provinceNow(id integer primary key autoincrement, year numeric,date varchar,country varchar,province varchar, confirm numeric,dead numeric,heal numeric,newConfirm numeric,newHeal numeric,newDead numeric)"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table if exists address"
    dbUtil(sql, dbPathYingQing)
    sql = "create table address(id integer primary key autoincrement, area varchar ,type numeric )"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table if exists province31"
    dbUtil(sql, dbPathYingQing)
    sql = "create table province31(id integer primary key autoincrement, province varchar ,city varchar ,syear numeric ,date varchar ,confirm numeric ,nowConfirm numeric ,confirmAdd numeric ,dead numeric ,grade varchar )"
    dbUtil(sql, dbPathYingQing)
    sql = "drop table if exists movieTop250"
    dbUtil(sql, dbPathDouBan)
    sql = "create table movieTop250(id integer primary key autoincrement, title1 varchar , title2 varchar , otherTitle varchar , imgLink text, infoLink text, score numeric , rated numeric , instroduction text, info text )"
    dbUtil(sql, dbPathDouBan)

# 模拟浏览器去访问指定URL
def askUrl(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "Referer": url,
            "Connection": "keep-alive"
        }
        return requests.get(url=url, headers=headers, timeout=3)
    except Exception as result:
        print("异常为:", result)

#  处理数据得到dataListProvince
def getDataProvince(urlProvince, province, savePath, dbPath):
    print("......正在爬取全国各个省份疫情的历史数据......")
    dataList = []
    for item in province:
        item = (str(item.encode('utf-8')).lstrip("b'").rstrip("'").replace(r'\x', '%').upper())
        data = askUrl(urlProvince + item).json()['data']
        dataList.extend(data)
    t1 = threading.Thread(target=saveDateToFileProvince, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabaseProvince, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件Province
def saveDateToFileProvince(dataList, savePath):
    print("......正在保存全国各个省份疫情的历史数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['年', '日期', '国家', '省份', '累计确诊', ' 累计死亡', '累计治愈', '新确诊', '新确诊', '新死亡']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    i = 1
    for item in dataList:
        param = [item['year'], item['date'], item['country'], item['province'], item['confirm'], item['dead'],
                 item['heal'], item['newConfirm'], item['newHeal'], item['newDead']]
        for j in range(len(param)):
            worksheet.write(i, j, param[j])
        i = i + 1
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库Province
def saveDateToDatabaseProvince(dataList, dbPath):
    print("......正在保存全国各个省份疫情的历史数据到数据库......")
    for item in dataList:
        #             年            日期            国家              省份             累计确诊         累计死亡      累计治愈          新确诊             新确诊            新死亡
        param = [item['year'], item['date'], item['country'], item['province'], item['confirm'], item['dead'],
                 item['heal'], item['newConfirm'], item['newHeal'], item['newDead']]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into province(year,date,country,province,confirm,dead,heal,newConfirm,newHeal,newDead) values (%s)" % ",".join(
            param)
        print(sql)
        dbUtil(sql, dbPath)


#  处理数据得到dataListProvinceNow
def getDataProvinceNow(province, savePath, dbPath):
    print("......正在查询全国各个省份疫情的最新数据......")
    dataList = []
    # 解决省份更新时间不同问题
    for item in province:
        item = '"' + item + '"'
        sql = "select * from province where province like %s order by year DESC ,date DESC ,province limit 1" % item
        print(sql)
        conn = sqlite3.connect(dbPath)
        result = conn.cursor().execute(sql)
        for data in result:
            dataList.append(data)
        conn.close()
    t1 = threading.Thread(target=saveDateToFileProvinceNow, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabaseProvinceNow, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件ProvinceNow
def saveDateToFileProvinceNow(dataList, savePath):
    print("......正在保存全国各个省份疫情的历史数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['年', '日期', '国家', '省份', '累计确诊', ' 累计死亡', '累计治愈', '新确诊', '新确诊', '新死亡']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    for i in range(len(dataList)):
        data = dataList[i]
        for j in range(len(data) - 1):
            worksheet.write(i + 1, j, data[j + 1])
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库ProvinceNow
def saveDateToDatabaseProvinceNow(dataList, dbPath):
    print("......正在保存全国各个省份疫情的历史数据到数据库......")
    for item in dataList:
        param = [item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10]]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into provinceNow(year,date,country,province,confirm,dead,heal,newConfirm,newHeal,newDead) values(%s)" % ",".join(
            param)
        print(sql)
        dbUtil(sql, dbPath)


# 处理数据得到dataListAddress
def getDataAddress(urlAddress, savePath, dbPath):
    print("......正在爬取全国各个省份的风险地区数据......")
    dataList = askUrl(urlAddress).json()['data']
    t1 = threading.Thread(target=saveDateToFileAddress, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabaseAddress, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件Address
def saveDateToFileAddress(dataList, savePath):
    print("......正在保存全国各个省份的风险地区数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['地区', '风险类型']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    i = 1
    for item in dataList:
        param = [item['area'], "中风险地区" if ['type'] == '1' else "高风险地区"]
        for j in range(len(param)):
            worksheet.write(i, j, param[j])
        i = i + 1
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库Address
def saveDateToDatabaseAddress(dataList, dbPath):
    print("......正在保存全国各个省份的风险地区数据到数据库......")
    for item in dataList:
        param = [item['area'], "中风险地区" if item['type'] == '1' else "高风险地区"]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into address (area,type) values(%s)" % ",".join(param)
        print(sql)
        dbUtil(sql, dbPath)


# 处理数据得到dataList31Province
def getData31Province(url31Province, savePath, dbPath):
    print("......正在爬取近期31省区市本土病例数据......")
    dataList = askUrl(url31Province).json()['data']['statisGradeCityDetail']
    t1 = threading.Thread(target=saveDateToFile31Province, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDateToDatabase31Province, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件31Province
def saveDateToFile31Province(dataList, savePath):
    print("......正在保存近期31省区市本土病例数据到文件......")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet(savePath, cell_overwrite_ok=True)
    column = ['省份', '城市', '年', '日期', '累计确诊', ' 现确诊', '确诊增加', '死亡', '风险等级']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    i = 1
    for item in dataList:
        param = [item['province'], item['city'], item['syear'], item['date'], item['confirm'], item['nowConfirm'],
                 item['confirmAdd'], item['dead'], item['grade']]
        for j in range(len(param)):
            worksheet.write(i, j, param[j])
        i = i + 1
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库31Province
def saveDateToDatabase31Province(dataList, dbPath):
    print("......正在保存近期31省区市本土病例数据到数据库......")
    for item in dataList:
        #               省份              城市            年           日期           累计确诊           现确诊               确诊增加           死亡        风险等级
        param = [item['province'], item['city'], item['syear'], item['date'], item['confirm'], item['nowConfirm'],
                 item['confirmAdd'], item['dead'], item['grade']]
        for index in range(len(param)):
            param[index] = '"' + str(param[index]) + '"'
        sql = "insert into province31 (province,city,syear,date,confirm,nowConfirm,confirmAdd,dead,grade) values ( %s )" % ",".join(param)
        print(sql)
        dbUtil(sql, dbPath)


# 爬取网页和数据解析DouBanTop
def getDateDouBanTop(url, savePath, dbPath):
    dataList = []
    for i in range(0, 10):
        # 循环爬取数据   0-10
        print("正在爬取豆瓣电影Top250的数据......")
        html = askUrl(url + str(i * 25)).text
        # 数据解析 HTML
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.find_all("div", class_="item"):  # 获取class为item的div
            data = []  # 存储一部电影的信息
            # 电影名称
            title = re.findall(
                re.compile(r'<span class="title">(.*)</span>'),
                str(item)
            )
            otherTitle = re.findall(
                re.compile(r'<span class="other">(.*)</span>'),
                str(item)
            )
            data.append(title[0])
            if len(title) == 2:
                data.append(title[1].replace("/", " ").replace("\xa0", ""))
            else:
                data.append(' ')
            data.append(otherTitle[0].replace("/", " ").replace("\xa0", ""))
            # 照片链接
            img = re.findall(
                re.compile(re.compile(r'<img.*src="(.*?)"', re.S)),  # re.s 让换行符号包含在字符串中
                str(item)
            )[0]
            data.append(img)
            # 电影详情链接
            link = re.findall(
                re.compile(r'<a href="(.*?)">'),
                str(item)
            )[0]
            data.append(link)
            # 评价分数
            ratingNumber = re.findall(
                re.compile(r'<span class="rating_num" property="v:average">(.*)</span>'),
                str(item)
            )[0]
            data.append(ratingNumber)
            # 评价人数
            JudgeNumber = re.findall(
                re.compile(r'<span>(\d*)人评价</span>'),
                str(item)
            )[0]
            data.append(JudgeNumber)
            # 电影评价
            inq = re.findall(
                re.compile(r'<span class="inq">(.*)</span>'),
                str(item)
            )
            if len(inq) != 0:
                data.append(inq[0].replace("。", ""))
            else:
                data.append(' ')
            # 相关内容
            related = re.findall(
                re.compile(r'<p class="">(.*?)</p>', re.S),
                str(item)
            )
            data.append(related[0].replace("<br/>", "    ").replace("/", " ").replace("\xa0", " ").
                        replace("\n                            ", "").replace("\n                        ", "")
                        )
            dataList.append(data)  # 数据集合
    t1 = threading.Thread(target=saveDateToFileDouBanTop, args=(dataList, savePath))
    t2 = threading.Thread(target=saveDataToDatabaseDouBanTop, args=(dataList, dbPath))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# 保存数据到文件
def saveDateToFileDouBanTop(dataList, savePath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet("doubanTop250", cell_overwrite_ok=True)  # 创建工作表
    column = ['影片中文名', '影片外文名', '影片别名', '图片链接', '电影详情链接', '评分', '评价数', '概况', '相关信息']
    for i in range(len(column)):
        worksheet.write(0, i, column[i])
    for i in range(len(dataList)):
        data = dataList[i]
        for j in range(len(data)):
            worksheet.write(i + 1, j, data[j])
    workbook.save(savePath)  # 保存数据表


# 保存数据到数据库
def saveDataToDatabaseDouBanTop(dataList, dbPath):
    for data in dataList:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = "insert into movieTop250 (title1,title2,otherTitle,imgLink,infoLink,score,rated,instroduction,info)values (%s)" % ",".join(
            data)
        dbUtil(sql, dbPath)


def dbUtil(sql, dbPath):
    conn = sqlite3.connect(dbPath)  # 打开或者创建数据库文件
    conn.cursor().execute(sql)  # 获取游标  执行sql语句
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接


# 主函数
def main():
    dbPathYiQing = "chinaYiQing.db"
    dbPathDouBan = "doubanMovie.db"
    savePathDouBan = "doubanTop250.xls"
    savaPathProvince = "province.xls"
    savaPathAddress = "address.xls"
    savaPath31Province = "province31.xls"
    savaPathProvinceNow = "provinceNow.xls"
    province = ['河南', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏',
                '浙江', '安徽', '福建', '江西', '山东', '湖北', '湖南',
                '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃',
                '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆',
                '北京', '天津', '上海', '重庆', '香港', '澳门']
    urlDouBan = "https://movie.douban.com/top250?start="
    urlProvince = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province="
    urlAddress = "https://eyesight.news.qq.com/sars/riskarea"
    url31Province = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail"

    threading.Thread(target=initDatabase, args=(dbPathYiQing, dbPathDouBan)).start()  # 初始化数据库
    thread1 = threading.Thread(target=getDataProvince, args=(urlProvince, province, savaPathProvince, dbPathYiQing))
    thread2 = threading.Thread(target=getData31Province, args=(url31Province, savaPath31Province, dbPathYiQing))
    thread3 = threading.Thread(target=getDataAddress, args=(urlAddress, savaPathAddress, dbPathYiQing))
    thread4 = threading.Thread(target=getDateDouBanTop, args=(urlDouBan, savePathDouBan, dbPathDouBan))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5 = threading.Thread(target=getDataProvinceNow, args=(province, savaPathProvinceNow, dbPathYiQing))
    thread5.start()
    thread5.join()

# 调用主函数
if __name__ == "__main__":
    main()

```
<a name="cvLBx"></a>
## app.py
```python

from flask import Flask, render_template, redirect, request
import jieba  # 分词
import matplotlib.pyplot as plt
from matplotlib import pyplot  # 绘图
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy    # 矩阵运算
import sqlite3  # sqlite数据库
import spider

app = Flask(__name__)

# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# 电影
@app.route('/movie')
def movie():
    dataList = []
    conn = sqlite3.connect("doubanMovie.db")
    result = conn.cursor().execute("select * from movieTop250")
    for item in result:
        dataList.append(item)
    conn.close()
    return render_template("movie.html", dataList=dataList)

# 评分
@app.route('/score')
def score():
    date = []; dataName = []; dataValue= []
    conn = sqlite3.connect("doubanMovie.db")
    result = conn.cursor().execute("select score,count(score) from movieTop250 group by score")
    for name, value in result:
        dataDict = {'name': name, 'value': value}
        dataName.append(name); dataValue.append(value); date.append(dataDict)
    conn.close()
    return render_template("score.html",
                           date=date,
                           dataName=dataName,
                           dataValue=dataValue
                           )

# 词云
@app.route('/word')
def word():
    str = ""
    conn = sqlite3.connect("doubanMovie.db")
    sql = "select instroduction from movieTop250"
    result = conn.cursor().execute(sql)
    for item in result:
        str = str + item[0]
    conn.close()
    cut = jieba.cut(str)
    str = ' '.join(cut)
    print(len(str))
    wc = WordCloud(
        background_color='white',
        mask=numpy.array(Image.open("static/assets/img/tree.jpg")),
        font_path="msyh.ttc"
    ).generate_from_text(str)
    pyplot.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig("static/assets/img/treeWord.jpg")
    return render_template("word.html")

# province31
@app.route('/province31')
def province31():
    cityList=[]; conformList=[]; nowConfirmList=[]; confirmAddList=[]; deadList=[]
    conn = sqlite3.connect("chinaYiQing.db")
    result = conn.cursor().execute("select * from province31 order by confirmAdd DESC limit 19")
    for item in result:
        cityList.append(item[2])
        conformList.append(item[5])
        nowConfirmList.append(item[6])
        confirmAddList.append(item[7])
        deadList.append(item[8])
    conn.close()
    return render_template("province31.html",
                           cityList=cityList,
                           conformList=conformList,
                           nowConfirmList=nowConfirmList,
                           confirmAddList=confirmAddList,
                           deadList=deadList
                           )

# address
@app.route('/address')
def address():
    areaListMiddle = []; areaListHigh = []
    conn = sqlite3.connect("chinaYiQing.db")
    resultMiddle = conn.cursor().execute("select * from address where type like '中风险地区' order by area ")
    resultHigh = conn.cursor().execute("select * from address where type like '高风险地区' order by area ")
    for item in resultMiddle:
        areaListMiddle.append(item[1])
    for item in resultHigh:
        areaListHigh.append(item[1])
    conn.close()
    return render_template("address.html",
                           areaListMiddle=areaListMiddle,
                           areaListHigh=areaListHigh
                           )

# provinceNow
@app.route('/provinceNow')
def provinceNow():
    cityList = []; confirmList = []; deadList = []; healList = []; newConfirmList = []; newDeadList = []; newHealList = []; dataList=[]
    conn = sqlite3.connect("chinaYiQing.db")
    result = conn.cursor().execute("select * from provinceNow  order by confirm")
    for item in result:
        cityList.append(item[4])
        confirmList.append(item[5])
        deadList.append(item[6])
        healList.append(item[7])
        newConfirmList.append(-item[8])
        newDeadList.append(-item[10])
        newHealList.append(-item[9])
        data = {"name": item[4], "value": item[5]}
        dataList.append(data)
    conn.close()
    return render_template("provinceNow.html",
                           cityList=cityList,
                           confirmList=confirmList,
                           deadList=deadList,
                           healList=healList,
                           newConfirmList=newConfirmList,
                           newDeadList=newDeadList,
                           newHealList=newHealList,
                           dataList=dataList
                           )

# provinceHistory
@app.route('/provinceHistory')
def provinceHistory():
    conn = sqlite3.connect("chinaYiQing.db")
    timeList = []; confirmList = []; deadList = []; healList = []; newConfirmList = []; newDeadList = []; newHealList = []
    result = conn.cursor().execute("select * from province  where province like '河南' order by year ,date")
    for item in result:
        timeList.append(str(item[1]) + "-" + item[2])
        confirmList.append(item[5])
        deadList.append(item[6])
        healList.append(item[7])
        newConfirmList.append(item[8])
        newDeadList.append(item[10])
        newHealList.append(item[9])
    conn.close()
    dataList = []
    conn = sqlite3.connect("chinaYiQing.db")
    provinces = ['河南', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏',
                 '浙江', '安徽', '福建', '江西', '山东', '湖北', '湖南',
                 '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃',
                 '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆',
                 '北京', '天津', '上海', '重庆', '香港', '澳门']
    for province in provinces:
        result = conn.cursor().execute(
            "select * from province  where province like %s order by year ,date " % ("'" + province + "'"))
        oneProvinceData = []
        for item in result:
            oneProvinceData.append(item[8])
        dataList.append(oneProvinceData)
    conn.close()
    return render_template('provinceHistory.html',
                           timeList=timeList,
                           confirmList=confirmList,
                           deadList=deadList,
                           healList=healList,
                           newConfirmList=newConfirmList,
                           newDeadList=newDeadList,
                           newHealList=newHealList,
                           henan=dataList[0],
                           hebie=dataList[1],
                           shanxi=dataList[2],
                           liaoning=dataList[3],
                           jilin=dataList[4],
                           helongjiang=dataList[5],
                           jiangsu=dataList[6],
                           zhejiang=dataList[7],
                           anhui=dataList[8],
                           fujian=dataList[9],
                           jiangxi=dataList[10],
                           shandong=dataList[11],
                           hubei=dataList[12],
                           hunan=dataList[13],
                           guandong=dataList[14],
                           hainan=dataList[15],
                           sichuan=dataList[16],
                           guizhou=dataList[17],
                           yunnan=dataList[18],
                           shaixi=dataList[19],
                           gansu=dataList[20],
                           qinghai=dataList[21],
                           taiwan=dataList[22],
                           neinonggu=dataList[23],
                           guangxi=dataList[24],
                           xizhang=dataList[25],
                           ningxia=dataList[26],
                           xinjiang=dataList[27],
                           biejing=dataList[28],
                           tianjing=dataList[29],
                           shanghai=dataList[30],
                           chongqing=dataList[31],
                           xianggang=dataList[32],
                           aomen=dataList[33]
                           )

@app.route('/admin')
def admin():
    return render_template('login.html')

@app.route('/toLogin', methods=['POST', 'GET'])
def toLogin():
    result = request.form
    if result['username']=='pepsi-wyl' and result['password']=='888888':
        spider.main()
    return redirect('/index', code=302, Response=None)

if __name__ == '__main__':
    app.run()

```
<a name="XKZzr"></a>
## templates
<a name="Dv3og"></a>
### index.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>数据分析首页</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">
</head>

<body>

<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li class="active"><a href="/index">首页<i class="la la-angle-down"></i></a></li>
                <li><a href="/movie">电影</a></li>
                <li><a href="/score">评分</a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>

                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <div class="section-title">
            <h2>豆瓣电影Top250数据分析</h2>
            <p>技术支持: Python爬虫、Flask框架、Echarts、WordCloud等</p>
        </div>
        <section class="counts section-bg">
            <div class="container">

                <div class="row">
                    <div class="col-lg-4 col-md-8 text-center" data-aos="fade-up">
                        <a href="/movie">
                            <div class="count-box">
                                <i class="icofont-movie" style="color: #20b38e;"></i>
                                <span data-toggle="counter-up">250</span>
                                <p>经典电影</p>
                            </div>
                        </a>
                    </div>
                    <div class="col-lg-4 col-md-8 text-center" data-aos="fade-up" data-aos-delay="200">
                        <a href="/score">
                            <div class="count-box">
                                <i class="icofont-score-board" style="color: #c042ff;"></i>
                                <span data-toggle="counter-up">9.9</span>
                                <p>评分统计</p>
                            </div>
                        </a>
                    </div>
                    <div class="col-lg-4 col-md-8 text-center" data-aos="fade-up" data-aos-delay="400">
                        <a href="/word">
                            <div class="count-box">
                                <i class="icofont-contacts" style="color: #46d1ff;"></i>
                                <span data-toggle="counter-up">5462</span>
                                <p>词汇统计</p>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </div>
</section>


<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer>


<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="r6qae"></a>
### movie.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta name="referrer" content="no-referrer"/>
    <title>豆瓣电影Top250榜单</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">

</head>

<body>


<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li class="active"><a href="/movie">电影<i class="la la-angle-down"></i></a></li>
                <li><a href="/score">评分</a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>
                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <div class="section-title">
            <h2>豆瓣电影Top250榜单</h2>
        </div>
        <section class="counts section-bg">
            <div class="container">
                <table class="table table-striped">
                    <tr>
                        <td>排名</td>
                        <td>图片</td>
                        <td>电影中文名称</td>
                        <td>电影外国名称</td>
                        <td>电影其他名称</td>
                        <td>评分</td>
                        <td>评价人数</td>
                        <td>一句话概述</td>
                        <td>其他信息</td>
                    </tr>
                    {% for movie in dataList %}
                        <tr>
                            <td>{{ movie[0] }}</td>
                            <td>
                                <a href="{{ movie[4] }}">
                                    <img width="50" alt="{{ movie[1] }}" src="{{ movie[4] }}" class="">
                                </a>
                            </td>
                            <td><a href="{{ movie[5] }}" class="">{{ movie[1] }}</a></td>
                            <td>{{ movie[2] }}</td>
                            <td>{{ movie[3] }}</td>
                            <td>{{ movie[6] }}</td>
                            <td>{{ movie[7] }}</td>
                            <td>{{ movie[8] }}</td>
                            <td>{{ movie[9] }}</td>
                        </tr>
                    {% endfor %}
                </table>
            </div>
        </section>
    </div>
</section>

<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer>

<!-- ======= 返回顶部 ======= -->
<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="SEJs7"></a>
### score.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>豆瓣Top250评分分布图</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">
    <!-- Echarts 文件 -->
    <script src="static/assets/js/echarts.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5.2.2/dist/echarts.min.js"></script>

</head>

<body>

<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li><a href="/movie">电影</a></li>
                <li class="active"><a href="/score">评分<i class="la la-angle-down"></i></a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>
                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <div class="section-title">
            <h2>豆瓣Top250评分分布图</h2>
        </div>
        <section class="counts section-bg">
            <div class="container">


                <HR align=center width=100% color=#987cb9 SIZE=1>
                <br/>
                <div id="main1" style="width: 100%;height:400px;"></div>
                <script type="text/javascript">
                    let dom = document.getElementById("main1");
                    let myChart = echarts.init(dom);
                    let app = {};
                    let option;
                    option = {
                        title: {
                            text: '豆瓣Top250评分分布图',
                            subtext: '饼状图',
                            left: 'right'
                        },
                        tooltip: {
                            trigger: 'item', formatter: '{a} <br/>{b} : {c} ({d}%)'
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left'
                        },
                        series: [
                            {
                                name: 'Access From',
                                type: 'pie',
                                radius: '50%',
                                data:{{ date|tojson }},
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                    };
                    if (option && typeof option === 'object') {
                        myChart.setOption(option);
                    }
                </script>

                <HR align=center width=100% color=#987cb9 SIZE=1>
                <br/>
                <div id="main3" style="width: 100%;height:400px;"></div>
                <script type="text/javascript">
                    var dom2 = document.getElementById("main3");
                    var myChart2 = echarts.init(dom2);
                    var app2 = {};
                    var option2;
                    option2 = {
                        tooltip: {
                            trigger: 'item'
                        },
                        xAxis: {
                            type: 'category',
                            data: {{ dataName }}
                        },
                        yAxis: {
                            type: 'value'
                        },
                        series: [
                            {
                                data: {{ dataValue }},
                                type: 'line',
                                smooth: true
                            }
                        ]
                    };
                    if (option2 && typeof option2 === 'object') {
                        myChart2.setOption(option2);
                    }
                </script>

                <HR align=center width=100% color=#987cb9 SIZE=1>
                <br/>
                <div id="main2" style="width: 100%;height:400px;"></div>
                <script type="text/javascript">
                    var dom1 = document.getElementById("main2");
                    var myChart1 = echarts.init(dom1);
                    var app1 = {};
                    var option1;
                    option1 = {
                        tooltip: {
                            trigger: 'item'
                        },
                        legend: {
                            top: '5%',
                            left: 'center'
                        },
                        series: [
                            {
                                name: 'Access From',
                                type: 'pie',
                                radius: ['40%', '70%'],
                                avoidLabelOverlap: false,
                                itemStyle: {
                                    borderRadius: 10,
                                    borderColor: '#fff',
                                    borderWidth: 2
                                },
                                label: {
                                    show: false,
                                    position: 'center'
                                },
                                emphasis: {
                                    label: {
                                        show: true,
                                        fontSize: '40',
                                        fontWeight: 'bold'
                                    }
                                },
                                labelLine: {
                                    show: false
                                },
                                data: {{ date|tojson }},
                            }
                        ]
                    };
                    if (option1 && typeof option1 === 'object') {
                        myChart1.setOption(option1);
                    }
                </script>



            </div>
        </section>
    </div>
</section>

<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer><!-- End Footer -->

<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="vulgH"></a>
### word.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>豆瓣Top250数据分析</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">

</head>

<body>

<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li><a href="/movie">电影</a></li>
                <li><a href="/score">评分</a></li>
                <li class="active"><a href="/word">词云<i class="la la-angle-down"></i></a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>
                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->


<section id="about" class="about">
    <div class="container">
        <div class="row no-gutters">
            <div class="col-lg-6 video-box">
                <img src="static/assets/img/treeWord.jpg" class="img-fluid" alt="">
            </div>
            <div class="col-lg-6 d-flex flex-column justify-content-center about-content">
                <div class="section-title">
                    <h2>词频统计</h2>
                    <p>根据250部电影的一句话描述，提炼出词云树，可以让我们更加清晰的了解人们对经典电影的理解</p>
                </div>
                <div class="icon-box" data-aos="fade-up" data-aos-delay="100">
                    <div class="icon"><i class="bx bx-fingerprint"></i></div>
                    <h4 class="title"><a href="/movie">关于电影</a></h4>
                    <p class="description">不知道你从中悟道了什么</p>
                </div>
            </div>
        </div>

    </div>
</section>


<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer><!-- End Footer -->

<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="pLa1y"></a>
### login.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>adminLogin</title>
    <link href='/static/assets/css/bootstrop.css' rel="stylesheet">
    <script type="text/javascript" src="/static/assets/js/jquery.js"></script>
    <style type="text/css">
        /* Override some defaults */
        html, body {
            background-color: #eee;
        }

        body {
            padding-top: 40px;
        }

        .container {
            width: 300px;
        }

        /* The white background content wrapper */
        .container > .content {
            background-color: #fff;
            padding: 20px;
            margin: 0 -20px;
            -webkit-border-radius: 10px 10px 10px 10px;
            -moz-border-radius: 10px 10px 10px 10px;
            border-radius: 10px 10px 10px 10px;
            -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .15);
            -moz-box-shadow: 0 1px 2px rgba(0, 0, 0, .15);
            box-shadow: 0 1px 2px rgba(0, 0, 0, .15);
        }

        .login-form {
            margin-left: 65px;
        }

        legend {
            margin-right: -50px;
            font-weight: bold;
            color: #404040;
        }

    </style>

</head>
<body>
<div class="container">
    <div class="content">
        <div class="row">
            <div class="login-form">
                <h2>重新爬取数据</h2>
                <p>爬取数据耗时较长</p>
                <form action="{{ url_for('toLogin') }}" method="post">
                    <div class="clearfix">
                        <input type="text" placeholder="用户名" name="username" autofocus="autofocus">
                    </div>
                    <div class="clearfix">
                        <input type="password" placeholder="密码" name="password">
                    </div>
                    <p><input type="submit" style="width: 224px"></p>
                </form>
            </div>
        </div>
    </div>
</div> <!-- /container -->
</body>
</html>
```
<a name="yEfu4"></a>
### province31.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>中国近期31省区市病例</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">

    <!-- Echarts -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
</head>

<body>

<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li><a href="/movie">电影</a></li>
                <li><a href="/score">评分</a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop active"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>

                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <section class="counts section-bg">
            <div id="container" style="height: 500px"></div>
            <script type="text/javascript">
                var dom = document.getElementById("container");
                var myChart = echarts.init(dom);
                var app = {};
                var option;
                option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    legend: {},
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            data: {{ cityList|tojson }}
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '累计确诊',
                            type: 'bar',
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ conformList }}
                        },
                        {
                            name: '现确诊',
                            type: 'bar',
                            stack: 'Ad',
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ nowConfirmList }}
                        },
                        {
                            name: '新增确诊',
                            type: 'bar',
                            stack: 'Ad',
                            emphasis: {
                                focus: 'series'
                            },
                            data:  {{ confirmAddList }}
                        },
                        {
                            name: '死亡',
                            type: 'bar',
                            stack: 'Ad',
                            emphasis: {
                                focus: 'series'
                            },
                            data:  {{ deadList }}
                        }
                    ]
                };
                if (option && typeof option === 'object') {
                    myChart.setOption(option);
                }
            </script>
        </section><!-- End Counts Section -->
    </div>
</section><!-- End Our Team Section -->

<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">

        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>

    </div>
</footer><!-- End Footer -->

<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="CDfQi"></a>
### address.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>中国各省疫情风险地区</title>
    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">
    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">
    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">
</head>
<body>
<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">
        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>
        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li><a href="/movie">电影</a></li>
                <li><a href="/score">评分</a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop active"><a href="/address">中国各省疫情风险地区<i class="la la-angle-down"></i></a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>

                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <div class="section-title">
          <h2>疫情风险地区一览表</h2>
        </div>
        <section class="counts section-bg">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-md-8 text-center" data-aos="fade-up">
                        <div class="section-title">
                            <h2>中风险地区</h2>
                        </div>
                        <table class="table table-striped">
                            {% for area in areaListMiddle %}
                                <tr>
                                    <td>{{ area }}</td>
                                </tr>
                            {% endfor %}
                        </table>
                    </div>
                    <div class="col-lg-6 col-md-8 text-center" data-aos="fade-up" data-aos-delay="200">
                        <div class="section-title">
                            <h2>高风险地区</h2>
                        </div>
                         <table class="table table-striped">
                            {% for area in areaListHigh %}
                                <tr>
                                    <td>{{ area }}</td>
                                </tr>
                            {% endfor %}
                        </table>
                    </div>
                </div>
            </div>
        </section>
    </div>
</section>


<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer><!-- End Footer -->

<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="Gw6dX"></a>
### provinceNow.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>中国各省疫情实时情况</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
    <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
    <script type="text/javascript" src="https://assets.pyecharts.org/assets/maps/china.js"></script>

</head>

<body>

<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li><a href="/movie">电影</a></li>
                <li><a href="/score">评分</a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop active"><a href="/provinceNow">中国各省疫情实时情况<i class="la la-angle-down"></i></a></li>
                        <li class="drop"><a href="/provinceHistory">中国各省疫情历史数据分析</a></li>
                    </ul>
                </li>

                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <section class="counts section-bg">

            <div id="1ba033cb2ae24d458d8c6079805cbe0f" class="chart-container"
                 style="width:1000px; height:880px;"></div>
            <script type="text/javascript">
                var chart_1ba033cb2ae24d458d8c6079805cbe0f = echarts.init(
                    document.getElementById('1ba033cb2ae24d458d8c6079805cbe0f'), 'white', {renderer: 'canvas'});
                var option_1ba033cb2ae24d458d8c6079805cbe0f = {
                    "animation": true,
                    "animationThreshold": 2000,
                    "animationDuration": 1000,
                    "animationEasing": "cubicOut",
                    "animationDelay": 0,
                    "animationDurationUpdate": 300,
                    "animationEasingUpdate": "cubicOut",
                    "animationDelayUpdate": 0,
                    "color": [
                        "#c23531",
                        "#2f4554",
                        "#61a0a8",
                        "#d48265",
                        "#749f83",
                        "#ca8622",
                        "#bda29a",
                        "#6e7074",
                        "#546570",
                        "#c4ccd3",
                        "#f05b72",
                        "#ef5b9c",
                        "#f47920",
                        "#905a3d",
                        "#fab27b",
                        "#2a5caa",
                        "#444693",
                        "#726930",
                        "#b2d235",
                        "#6d8346",
                        "#ac6767",
                        "#1d953f",
                        "#6950a1",
                        "#918597"
                    ],
                    "series": [
                        {
                            "type": "map",
                            "name": "\u7d2f\u8ba1\u786e\u8bca\u4eba\u6570",
                            "label": {
                                "show": true,
                                "position": "top",
                                "margin": 8
                            },
                            "mapType": "china",
                            "data": {{ dataList|tojson }},
                            {#"data": [{'name': '湖北', 'value': 68320}, {'name': '台湾', 'value': 17624}, {'name': '香港', 'value': 12821}, {'name': '广东', 'value': 3602}, {'name': '上海', 'value': 3403}, {'name': '陕西', 'value': 2804}, {'name': '河南', 'value': 2234}, {'name': '浙江', 'value': 2090}, {'name': '黑龙江', 'value': 2035}, {'name': '云南', 'value': 1838}, {'name': '江苏', 'value': 1629}, {'name': '河北', 'value': 1458}, {'name': '福建', 'value': 1434}, {'name': '四川', 'value': 1345}, {'name': '湖南', 'value': 1229}, {'name': '北京', 'value': 1222}, {'name': '内蒙古', 'value': 1191}, {'name': '山东', 'value': 1050}, {'name': '安徽', 'value': 1009}, {'name': '新疆', 'value': 981}, {'name': '江西', 'value': 959}, {'name': '辽宁', 'value': 802}, {'name': '天津', 'value': 752}, {'name': '广西', 'value': 677}, {'name': '重庆', 'value': 611}, {'name': '吉林', 'value': 590}, {'name': '甘肃', 'value': 356}, {'name': '山西', 'value': 266}, {'name': '海南', 'value': 190}, {'name': '贵州', 'value': 160}, {'name': '宁夏', 'value': 122}, {'name': '澳门', 'value': 79}, {'name': '青海', 'value': 30}, {'name': '西藏', 'value': 1}],#}
                            "roam": true,
                            "zoom": 1,
                            "showLegendSymbol": false,
                            "emphasis": {}
                        }
                    ],
                    "legend": [
                        {
                            "data": [
                                "\u7d2f\u8ba1\u786e\u8bca\u4eba\u6570"
                            ],
                            "selected": {
                                "\u7d2f\u8ba1\u786e\u8bca\u4eba\u6570": true
                            },
                            "show": false,
                            "padding": 5,
                            "itemGap": 10,
                            "itemWidth": 25,
                            "itemHeight": 14
                        }
                    ],
                    "tooltip": {
                        "show": true,
                        "trigger": "item",
                        "triggerOn": "mousemove|click",
                        "axisPointer": {
                            "type": "line"
                        },
                        "showContent": true,
                        "alwaysShowContent": false,
                        "showDelay": 0,
                        "hideDelay": 100,
                        "textStyle": {
                            "fontSize": 14
                        },
                        "borderWidth": 0,
                        "padding": 5
                    },
                    "title": [
                        {
                            "text": "\u4e2d\u56fd\u75ab\u60c5\u5730\u56fe\u5206\u5e03",
                            "left": "center",
                            "top": "10px",
                            "padding": 5,
                            "itemGap": 10
                        }
                    ],
                    "visualMap": {
                        "show": true,
                        "type": "piecewise",
                        "min": 0,
                        "max": 200,
                        "inRange": {
                            "color": [
                                "#50a3ba",
                                "#eac763",
                                "#d94e5d"
                            ]
                        },
                        "calculable": true,
                        "inverse": false,
                        "splitNumber": 5,
                        "orient": "vertical",
                        "showLabel": true,
                        "itemWidth": 20,
                        "itemHeight": 14,
                        "borderWidth": 0,
                        "pieces": [
                            {
                                "max": 999999,
                                "min": 1001,
                                "label": ">10000",
                                "color": "#8A0808"
                            },
                            {
                                "max": 9999,
                                "min": 1000,
                                "label": "1000-9999",
                                "color": "#B40404"
                            },
                            {
                                "max": 999,
                                "min": 100,
                                "label": "100-999",
                                "color": "#DF0101"
                            },
                            {
                                "max": 99,
                                "min": 10,
                                "label": "10-99",
                                "color": "#F78181"
                            },
                            {
                                "max": 9,
                                "min": 1,
                                "label": "1-9",
                                "color": "#F5A9A9"
                            },
                            {
                                "max": 0,
                                "min": 0,
                                "label": "0",
                                "color": "#FFFFFF"
                            }
                        ]
                    }
                };
                chart_1ba033cb2ae24d458d8c6079805cbe0f.setOption(option_1ba033cb2ae24d458d8c6079805cbe0f);
            </script>

            <div id="container" style="height: 1000px"></div>
            <script type="text/javascript">
                var dom = document.getElementById("container");
                var myChart = echarts.init(dom);
                var app = {};
                var option;
                option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    legend: {
                        data: ['累计确诊', '累计治愈', '累计死亡', '新增确诊', '新增治愈', '新增死亡']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    yAxis: [
                        {
                            type: 'category',
                            axisTick: {
                                show: false
                            },
                            data: {{ cityList|tojson }}
                        }
                    ],
                    series: [
                        {
                            name: '累计确诊',
                            type: 'bar',
                            label: {
                                show: true,
                                position: 'right'
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ confirmList }}
                        },
                        {
                            name: '累计治愈',
                            type: 'bar',
                            stack: 'Total',
                            label: {
                                show: true,
                                position: 'inside'
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ healList }}
                        },
                        {
                            name: '累计死亡',
                            type: 'bar',
                            label: {
                                show: true,
                                position: 'inside'
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ deadList }}
                        },
                        {
                            name: '新增确诊',
                            type: 'bar',
                            stack: 'Total',
                            label: {
                                show: true,
                                position: 'left'
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ newConfirmList }}
                        },
                        {
                            name: '新增治愈',
                            type: 'bar',
                            stack: 'Total',
                            label: {
                                show: true,
                                position: 'left'
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ newHealList }}
                        },
                        {
                            name: '新增死亡',
                            type: 'bar',
                            stack: 'Total',
                            label: {
                                show: true,
                                position: 'left'
                            },
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ newDeadList }}
                        }

                    ]
                };
                if (option && typeof option === 'object') {
                    myChart.setOption(option);
                }
            </script>

        </section>
    </div>
</section>


<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer>


<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="dwr1y"></a>
### provinceHistory.html
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>中国各省疫情历史数据分析</title>

    <!-- Favicons -->
    <link href="static/assets/img/favicon.ico" rel="icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,600,600i,700,700i,900"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="static/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="static/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="static/assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="static/assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="static/assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="static/assets/css/style.css" rel="stylesheet">

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5.2.2/dist/echarts.min.js"></script>
</head>

<body>

<!-- ======= 头部 ======= -->
<header id="header">
    <div class="container">

        <div class="logo float-left">
            <img src="static/assets/img/favicon.ico" alt="" class="img-fluid">
        </div>

        <nav class="nav-menu float-right d-none d-lg-block">
            <ul>
                <li><a href="/index">首页</a></li>
                <li><a href="/movie">电影</a></li>
                <li><a href="/score">评分</a></li>
                <li><a href="/word">词云</a></li>

                <!-- ======= 疫情 ======= -->
                <li class="drop-down"><a href="">疫情</a>
                    <ul>
                        <li class="drop"><a href="/province31">中国近期31省区市病例</a></li>
                        <li class="drop"><a href="/address">中国各省疫情风险地区</a></li>
                        <li class="drop"><a href="/provinceNow">中国各省疫情实时情况</a></li>
                        <li class="drop active"><a href="/provinceHistory">中国各省疫情历史数据分析<i class="la la-angle-down"></i></a>
                        </li>
                    </ul>
                </li>

                <!-- ======= 关于 ======= -->
                <li class="drop-down"><a href="">关于</a>
                    <ul>

                        <li class="drop-down"><a href="#">pepsi-wyl</a>
                            <ul>
                                <a href="#" class="phone">
                                    <i class="icofont-phone"> 136 7333 0837 </i>
                                </a>
                                <a href="/static/assets/img/qq.png" class="qq" target="_blank">
                                    <i class="icofont-qq"> 2322535585 </i>
                                </a>
                                <a href="/static/assets/img/wechat.jpg" class="wechat" target="_blank">
                                    <i class="icofont-wechat"> wyl15236596738 </i>
                                </a>
                                <a href="https://mail.qq.com/" target="_blank">
                                    <i class="icofont-email"> 2322535585@qq.com </i>
                                </a>
                                <a href="https://github.com/pepsi-wyl" class="github" target="_blank">
                                    <i class="icofont-github">GitHub | pepsi-wyl</i>
                                </a>
                            </ul>
                        </li>

                        <li class="drop-down"><a href="#">锋芒工作室</a>
                            <ul>
                                <li><a href="#">关于工作室</a></li>
                            </ul>
                        </li>

                    </ul>
                </li>

            </ul>
        </nav><!-- .nav-menu -->

    </div>
</header><!-- End Header -->

<!-- ======= 内容 ======= -->
<section id="team" class="team">
    <div class="container">
        <section class="counts section-bg">

            <HR align=center width=100% color=#987cb9 SIZE=1>
            <br/>
            <div id="container" style="height: 700px"></div>
            <script type="text/javascript">
                var dom = document.getElementById("container");
                var myChart = echarts.init(dom);
                var app = {};
                var option;
                option = {
                    title: {
                        text: '河南省疫情历史数据'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985'
                            }
                        }
                    },
                    legend: {
                        data: ['累计确诊', '新增确诊', '累计死亡', '新增死亡', '累计治愈', '新增治愈']
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            {#日期#}
                            data:{{ timeList|tojson }}
                            {#data: ['2020-01.21', '2020-01.22', '2020-01.23', '2020-01.24', '2020-01.25', '2020-01.26', '2020-01.27', '2020-01.28', '2020-01.29', '2020-01.30', '2020-01.31', '2020-02.01', '2020-02.02', '2020-02.03', '2020-02.04', '2020-02.05', '2020-02.06', '2020-02.07', '2020-02.08', '2020-02.09', '2020-02.10', '2020-02.11', '2020-02.12', '2020-02.13', '2020-02.14', '2020-02.15', '2020-02.16', '2020-02.17', '2020-02.18', '2020-02.19', '2020-02.20', '2020-02.21', '2020-02.22', '2020-02.23', '2020-02.24', '2020-02.25', '2020-02.26', '2020-02.27', '2020-02.28', '2020-02.29', '2020-03.01', '2020-03.02', '2020-03.03', '2020-03.04', '2020-03.05', '2020-03.06', '2020-03.07', '2020-03.08', '2020-03.09', '2020-03.10', '2020-03.11', '2020-03.12', '2020-03.13', '2020-03.14', '2020-03.15', '2020-03.16', '2020-03.17', '2020-03.18', '2020-03.19', '2020-03.20', '2020-03.21', '2020-03.22', '2020-03.23', '2020-03.24', '2020-03.25', '2020-03.26', '2020-03.27', '2020-03.28', '2020-03.29', '2020-03.30', '2020-03.31', '2020-04.01', '2020-04.02', '2020-04.03', '2020-04.04', '2020-04.05', '2020-04.06', '2020-04.07', '2020-04.08', '2020-04.09', '2020-04.10', '2020-04.11', '2020-04.12', '2020-04.13', '2020-04.14', '2020-04.15', '2020-04.16', '2020-04.17', '2020-04.18', '2020-04.19', '2020-04.20', '2020-04.21', '2020-04.22', '2020-04.23', '2020-04.24', '2020-04.25', '2020-04.26', '2020-04.27', '2020-04.28', '2020-04.29', '2020-04.30', '2020-05.01', '2020-05.02', '2020-05.03', '2020-05.04', '2020-05.05', '2020-05.06', '2020-05.07', '2020-05.08', '2020-05.09', '2020-05.10', '2020-05.11', '2020-05.12', '2020-05.13', '2020-05.14', '2020-05.15', '2020-05.16', '2020-05.17', '2020-05.18', '2020-05.19', '2020-05.20', '2020-05.21', '2020-05.22', '2020-05.23', '2020-05.24', '2020-05.25', '2020-05.26', '2020-05.27', '2020-05.28', '2020-05.29', '2020-05.30', '2020-05.31', '2020-06.01', '2020-06.02', '2020-06.03', '2020-06.04', '2020-06.05', '2020-06.06', '2020-06.07', '2020-06.08', '2020-06.09', '2020-06.10', '2020-06.11', '2020-06.12', '2020-06.13', '2020-06.14', '2020-06.15', '2020-06.16', '2020-06.17', '2020-06.18', '2020-06.19', '2020-06.21', '2020-06.22', '2020-06.23', '2020-06.24', '2020-06.25', '2020-06.26', '2020-06.27', '2020-06.28', '2020-06.29', '2020-06.30', '2020-07.01', '2020-07.02', '2020-07.03', '2020-07.04', '2020-07.05', '2020-07.06', '2020-07.07', '2020-07.08', '2020-07.09', '2020-07.10', '2020-07.11', '2020-07.12', '2020-07.13', '2020-07.14', '2020-07.15', '2020-07.16', '2020-07.17', '2020-07.18', '2020-07.19', '2020-07.20', '2020-07.21', '2020-07.22', '2020-07.23', '2020-07.24', '2020-07.25', '2020-07.26', '2020-07.27', '2020-07.28', '2020-07.29', '2020-07.30', '2020-07.31', '2020-08.01', '2020-08.02', '2020-08.03', '2020-08.04', '2020-08.05', '2020-08.06', '2020-08.07', '2020-08.08', '2020-08.09', '2020-08.10', '2020-08.11', '2020-08.12', '2020-08.13', '2020-08.14', '2020-08.15', '2020-08.16', '2020-08.17', '2020-08.18', '2020-08.19', '2020-08.20', '2020-08.21', '2020-08.22', '2020-08.23', '2020-08.24', '2020-08.25', '2020-08.26', '2020-08.27', '2020-08.28', '2020-08.29', '2020-08.30', '2020-08.31', '2020-09.01', '2020-09.02', '2020-09.03', '2020-09.04', '2020-09.05', '2020-09.06', '2020-09.07', '2020-09.08', '2020-09.09', '2020-09.10', '2020-09.11', '2020-09.12', '2020-09.13', '2020-09.14', '2020-09.15', '2020-09.16', '2020-09.17', '2020-09.18', '2020-09.19', '2020-09.20', '2020-09.21', '2020-09.22', '2020-09.23', '2020-09.24', '2020-09.25', '2020-09.26', '2020-09.27', '2020-09.28', '2020-09.29', '2020-09.30', '2020-10.01', '2020-10.02', '2020-10.03', '2020-10.04', '2020-10.05', '2020-10.06', '2020-10.07', '2020-10.08', '2020-10.09', '2020-10.10', '2020-10.11', '2020-10.12', '2020-10.13', '2020-10.14', '2020-10.15', '2020-10.16', '2020-10.17', '2020-10.18', '2020-10.19', '2020-10.20', '2020-10.21', '2020-10.22', '2020-10.23', '2020-10.24', '2020-10.25', '2020-10.26', '2020-10.27', '2020-10.28', '2020-10.29', '2020-10.30', '2020-10.31', '2020-11.01', '2020-11.02', '2020-11.03', '2020-11.04', '2020-11.05', '2020-11.06', '2020-11.07', '2020-11.08', '2020-11.09', '2020-11.10', '2020-11.11', '2020-11.12', '2020-11.13', '2020-11.14', '2020-11.15', '2020-11.16', '2020-11.17', '2020-11.18', '2020-11.19', '2020-11.20', '2020-11.21', '2020-11.22', '2020-11.23', '2020-11.24', '2020-11.25', '2020-11.26', '2020-11.27', '2020-11.28', '2020-11.29', '2020-11.30', '2020-12.01', '2020-12.02', '2020-12.03', '2020-12.04', '2020-12.05', '2020-12.06', '2020-12.07', '2020-12.08', '2020-12.09', '2020-12.10', '2020-12.11', '2020-12.12', '2020-12.13', '2020-12.14', '2020-12.15', '2020-12.16', '2020-12.17', '2020-12.18', '2020-12.19', '2020-12.20', '2020-12.21', '2020-12.22', '2020-12.23', '2020-12.24', '2020-12.25', '2020-12.26', '2020-12.27', '2020-12.28', '2020-12.29', '2020-12.30', '2020-12.31', '2021-01.01', '2021-01.02', '2021-01.03', '2021-01.04', '2021-01.05', '2021-01.06', '2021-01.07', '2021-01.08', '2021-01.09', '2021-01.10', '2021-01.11', '2021-01.12', '2021-01.13', '2021-01.14', '2021-01.15', '2021-01.16', '2021-01.17', '2021-01.18', '2021-01.19', '2021-01.20', '2021-01.21', '2021-01.22', '2021-01.23', '2021-01.24', '2021-01.25', '2021-01.26', '2021-01.27', '2021-01.28', '2021-01.29', '2021-01.30', '2021-01.31', '2021-02.01', '2021-02.02', '2021-02.03', '2021-02.04', '2021-02.05', '2021-02.06', '2021-02.07', '2021-02.08', '2021-02.09', '2021-02.10', '2021-02.11', '2021-02.12', '2021-02.13', '2021-02.14', '2021-02.15', '2021-02.16', '2021-02.17', '2021-02.18', '2021-02.19', '2021-02.20', '2021-02.21', '2021-02.22', '2021-02.23', '2021-02.24', '2021-02.25', '2021-02.26', '2021-02.27', '2021-02.28', '2021-03.01', '2021-03.02', '2021-03.03', '2021-03.04', '2021-03.05', '2021-03.06', '2021-03.07', '2021-03.08', '2021-03.09', '2021-03.10', '2021-03.11', '2021-03.12', '2021-03.13', '2021-03.14', '2021-03.15', '2021-03.16', '2021-03.17', '2021-03.18', '2021-03.19', '2021-03.20', '2021-03.21', '2021-03.22', '2021-03.23', '2021-03.24', '2021-03.25', '2021-03.26', '2021-03.27', '2021-03.28', '2021-03.29', '2021-03.30', '2021-03.31', '2021-04.01', '2021-04.02', '2021-04.03', '2021-04.04', '2021-04.05', '2021-04.06', '2021-04.07', '2021-04.08', '2021-04.09', '2021-04.10', '2021-04.11', '2021-04.12', '2021-04.13', '2021-04.14', '2021-04.15', '2021-04.16', '2021-04.17', '2021-04.18', '2021-04.19', '2021-04.20', '2021-04.21', '2021-04.22', '2021-04.23', '2021-04.24', '2021-04.25', '2021-04.26', '2021-04.27', '2021-04.28', '2021-04.29', '2021-04.30', '2021-05.01', '2021-05.02', '2021-05.03', '2021-05.04', '2021-05.05', '2021-05.06', '2021-05.07', '2021-05.08', '2021-05.09', '2021-05.10', '2021-05.11', '2021-05.12', '2021-05.13', '2021-05.14', '2021-05.15', '2021-05.16', '2021-05.17', '2021-05.18', '2021-05.19', '2021-05.20', '2021-05.21', '2021-05.22', '2021-05.23', '2021-05.24', '2021-05.25', '2021-05.26', '2021-05.27', '2021-05.28', '2021-05.29', '2021-05.30', '2021-05.31', '2021-06.01', '2021-06.02', '2021-06.03', '2021-06.04', '2021-06.05', '2021-06.06', '2021-06.07', '2021-06.08', '2021-06.09', '2021-06.10', '2021-06.11', '2021-06.12', '2021-06.13', '2021-06.14', '2021-06.15', '2021-06.16', '2021-06.17', '2021-06.18', '2021-06.19', '2021-06.20', '2021-06.21', '2021-06.22', '2021-06.23', '2021-06.24', '2021-06.25', '2021-06.26', '2021-06.27', '2021-06.28', '2021-06.29', '2021-06.30', '2021-07.01', '2021-07.02', '2021-07.03', '2021-07.04', '2021-07.05', '2021-07.06', '2021-07.07', '2021-07.08', '2021-07.09', '2021-07.10', '2021-07.11', '2021-07.12', '2021-07.13', '2021-07.14', '2021-07.15', '2021-07.16', '2021-07.17', '2021-07.18', '2021-07.19', '2021-07.20', '2021-07.21', '2021-07.22', '2021-07.23', '2021-07.24', '2021-07.25', '2021-07.26', '2021-07.27', '2021-07.28', '2021-07.29', '2021-07.30', '2021-07.31', '2021-08.01', '2021-08.02', '2021-08.03', '2021-08.04', '2021-08.05', '2021-08.06', '2021-08.07', '2021-08.08', '2021-08.09', '2021-08.10', '2021-08.11', '2021-08.12', '2021-08.13', '2021-08.14', '2021-08.15', '2021-08.16', '2021-08.17', '2021-08.18', '2021-08.19', '2021-08.20', '2021-08.21', '2021-08.22', '2021-08.23', '2021-08.24', '2021-08.25', '2021-08.26', '2021-08.27', '2021-08.28', '2021-08.29', '2021-08.30', '2021-08.31', '2021-09.01', '2021-09.02', '2021-09.03', '2021-09.04', '2021-09.05', '2021-09.06', '2021-09.07', '2021-09.08', '2021-09.09', '2021-09.10', '2021-09.11', '2021-09.12', '2021-09.13', '2021-09.14', '2021-09.15', '2021-09.16', '2021-09.17', '2021-09.18', '2021-09.19', '2021-09.20', '2021-09.21', '2021-09.22', '2021-09.23', '2021-09.24', '2021-09.25', '2021-09.26', '2021-09.27', '2021-09.28', '2021-09.29', '2021-09.30', '2021-10.01', '2021-10.02', '2021-10.03', '2021-10.04', '2021-10.05', '2021-10.06', '2021-10.07', '2021-10.08', '2021-10.09', '2021-10.10', '2021-10.11', '2021-10.12', '2021-10.13', '2021-10.14', '2021-10.15', '2021-10.16', '2021-10.17', '2021-10.18', '2021-10.19', '2021-10.20', '2021-10.21', '2021-10.22', '2021-10.23', '2021-10.24', '2021-10.25', '2021-10.26', '2021-10.27', '2021-10.28', '2021-10.29', '2021-10.30', '2021-10.31', '2021-11.01', '2021-11.02', '2021-11.03', '2021-11.04', '2021-11.05', '2021-11.06', '2021-11.07', '2021-11.08', '2021-11.09', '2021-11.10', '2021-11.11', '2021-11.12', '2021-11.13', '2021-11.14', '2021-11.15', '2021-11.16', '2021-11.17', '2021-11.18', '2021-11.19', '2021-11.20', '2021-11.21', '2021-11.22', '2021-11.23', '2021-11.24', '2021-11.25', '2021-11.26', '2021-11.27', '2021-11.28', '2021-11.29', '2021-11.30', '2021-12.01', '2021-12.02', '2021-12.03', '2021-12.04', '2021-12.05', '2021-12.06', '2021-12.07', '2021-12.08', '2021-12.09', '2021-12.10', '2021-12.11', '2021-12.12', '2021-12.13', '2021-12.14', '2021-12.15', '2021-12.16', '2021-12.17', '2021-12.18', '2021-12.19', '2021-12.20', '2021-12.21', '2021-12.22', '2021-12.23', '2021-12.24', '2021-12.25', '2021-12.26', '2021-12.27', '2021-12.28', '2021-12.29', '2021-12.30', '2021-12.31', '2022-01.01', '2022-01.02', '2022-01.03', '2022-01.04', '2022-01.05', '2022-01.06', '2022-01.07', '2022-01.08', '2022-01.09', '2022-01.10', '2022-01.11', '2022-01.12', '2022-01.13']#}
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '累计确诊',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ confirmList|tojson }}
                            {#data: [1, 5, 9, 32, 83, 128, 168, 206, 278, 352, 422, 493, 566, 675, 764, 851, 914, 981, 1033, 1073, 1105, 1135, 1169, 1184, 1184, 1231, 1246, 1257, 1262, 1265, 1267, 1270, 1271, 1271, 1271, 1271, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1272, 1273, 1273, 1273, 1273, 1273, 1273, 1273, 1273, 1273, 1273, 1273, 1274, 1274, 1274, 1275, 1275, 1275, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1276, 1277, 1277, 1277, 1277, 1278, 1278, 1278, 1279, 1279, 1279, 1280, 1280, 1280, 1280, 1280, 1280, 1280, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1281, 1283, 1283, 1283, 1283, 1283, 1283, 1283, 1284, 1284, 1284, 1284, 1284, 1284, 1284, 1284, 1286, 1286, 1286, 1286, 1286, 1286, 1286, 1286, 1287, 1287, 1288, 1288, 1288, 1288, 1288, 1288, 1288, 1288, 1288, 1289, 1289, 1289, 1289, 1289, 1289, 1289, 1289, 1290, 1290, 1292, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1296, 1296, 1297, 1297, 1297, 1297, 1298, 1298, 1298, 1298, 1298, 1299, 1299, 1299, 1299, 1299, 1299, 1299, 1300, 1300, 1300, 1301, 1301, 1301, 1301, 1302, 1302, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1303, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1304, 1305, 1305, 1305, 1305, 1305, 1305, 1307, 1307, 1308, 1308, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1309, 1310, 1310, 1310, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1311, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1312, 1313, 1313, 1313, 1313, 1313, 1314, 1314, 1314, 1314, 1314, 1314, 1314, 1314, 1314, 1314, 1315, 1315, 1315, 1315, 1315, 1315, 1315, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1316, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1317, 1318, 1320, 1320, 1320, 1320, 1321, 1324, 1324, 1324, 1325, 1325, 1325, 1325, 1326, 1326, 1326, 1326, 1327, 1328, 1330, 1330, 1330, 1331, 1331, 1331, 1344, 1347, 1349, 1352, 1355, 1356, 1360, 1384, 1425, 1462, 1469, 1472, 1503, 1507, 1512, 1518, 1518, 1518, 1519, 1521, 1521, 1522, 1523, 1524, 1525, 1525, 1527, 1528, 1528, 1528, 1528, 1528, 1528, 1530, 1531, 1531, 1532, 1532, 1532, 1532, 1532, 1535, 1536, 1536, 1536, 1537, 1537, 1539, 1539, 1539, 1539, 1539, 1539, 1539, 1539, 1539, 1540, 1540, 1540, 1540, 1540, 1540, 1542, 1542, 1542, 1542, 1542, 1542, 1543, 1543, 1544, 1544, 1544, 1544, 1545, 1547, 1550, 1550, 1550, 1550, 1551, 1552, 1553, 1553, 1553, 1553, 1555, 1555, 1558, 1558, 1558, 1559, 1559, 1559, 1559, 1562, 1567, 1570, 1574, 1592, 1594, 1603, 1616, 1628, 1629, 1629, 1632, 1632, 1632, 1633, 1634, 1634, 1634, 1636, 1636, 1636, 1636, 1636, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1637, 1638, 1638, 1638, 1638, 1638, 1638, 1638, 1638, 1638, 1640, 1640, 1640, 1640, 1640, 1641, 1641, 1641, 1641, 1641, 1642, 1644, 1650, 1654, 1719, 1777, 1821, 1880, 1941, 2029, 2147, 2223, 2234]#}
                        },
                        {
                            name: '新增确诊',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ newConfirmList|tojson }}
                        },
                        {
                            name: '累计死亡',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ deadList|tojson }}
                        },
                        {
                            name: '新增死亡',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ newDeadList|tojson }}
                        },
                        {
                            name: '累计治愈',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ healList|tojson }}
                        },
                        {
                            name: '新增治愈',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ newHealList|tojson }}
                        },
                    ]
                };
                if (option && typeof option === 'object') {
                    myChart.setOption(option);
                }
            </script>

            <HR align=center width=100% color=#987cb9 SIZE=1>
            <br/>

            <div id="container1" style="height: 700px; width: 100%;"></div>
            <script type="text/javascript">
                var dom1 = document.getElementById("container1");
                var myChart1 = echarts.init(dom1);
                var app1 = {};
                var option1;
                option1 = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985'
                            }
                        }
                    },
                    legend: {
                        data: ['河南', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏',
                            '浙江', '安徽', '福建', '江西', '山东', '湖北', '湖南',
                            '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃',
                            '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆',
                            '北京', '天津', '上海', '重庆', '香港', '澳门']
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data:{{ timeList|tojson }}
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '河南',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ henan|tojson }}
                        },
                        {
                            name: '河北',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ hebie|tojson }}
                        },
                        {
                            name: '山西',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ shanxi|tojson }}
                        },
                        {
                            name: '辽宁',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ liaoning|tojson }}
                        },
                        {
                            name: '吉林',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ jilin|tojson }}
                        },
                        {
                            name: '黑龙江',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ helongjiang|tojson }}
                        },
                        {
                            name: '江苏',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ jiangsu|tojson }}
                        },
                        {
                            name: '浙江',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ zhejiang|tojson }}
                        },
                        {
                            name: '安徽',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ anhui|tojson }}
                        },
                        {
                            name: '福建',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ fujian|tojson }}
                        },
                        {
                            name: '江西',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ jiangxi|tojson }}
                        },
                        {
                            name: '山东',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ shandong|tojson }}
                        },
                        {
                            name: '湖北',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ hubei|tojson }}
                        },
                        {
                            name: '湖南',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ hunan|tojson }}
                        },
                        {
                            name: '广东',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ guandong|tojson }}
                        },
                        {
                            name: '海南',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ hainan|tojson }}
                        },
                        {
                            name: '四川',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ sichuan|tojson }}
                        },
                        {
                            name: '贵州',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ guizhou|tojson }}
                        },
                        {
                            name: '云南',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ yunnan|tojson }}
                        },
                        {
                            name: '陕西',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ shaixi|tojson }}
                        },
                        {
                            name: '甘肃',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ gansu|tojson }}
                        },
                        {
                            name: '青海',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ qinghai|tojson }}
                        },
                        {
                            name: '台湾',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ taiwan|tojson }}
                        },
                        {
                            name: '内蒙古',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ neinonggu|tojson }}
                        },
                        {
                            name: '广西',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ guangxi|tojson }}
                        },
                        {
                            name: '西藏',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ xizhang|tojson }}
                        },
                        {
                            name: '宁夏',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ ningxia|tojson }}
                        },
                        {
                            name: '新疆',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ xinjiang|tojson }}
                        },
                        {
                            name: '北京',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ biejing|tojson }}
                        },
                        {
                            name: '天津',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ tianjing|tojson }}
                        },
                        {
                            name: '上海',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ shanghai|tojson }}
                        },
                        {
                            name: '重庆',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ chongqing|tojson }}
                        },
                        {
                            name: '香港',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ xianggang|tojson }}
                        },
                        {
                            name: '澳门',
                            type: 'line',
                            smooth: true,
                            areaStyle: {},
                            emphasis: {
                                focus: 'series'
                            },
                            data: {{ aomen|tojson }}
                        }
                    ]
                };
                if (option1 && typeof option1 === 'object') {
                    myChart1.setOption(option1);
                }
            </script>
        </section>
    </div>
</section>

<!-- ======= 页脚 ======= -->
<footer id="footer">
    <div class="container">
        <div class="copyright">
            Designed by pepsi-wyl.
        </div>
        <div class="copyright">
            &copy; 2022 <strong><span> 锋芒工作室 </span></strong>. All Rights Reserved.
        </div>
    </div>
</footer>

<a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

<!-- Vendor JS Files -->
<script src="static/assets/vendor/jquery/jquery.min.js"></script>
<script src="static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="static/assets/vendor/jquery.easing/jquery.easing.min.js"></script>
<script src="static/assets/vendor/php-email-form/validate.js"></script>
<script src="static/assets/vendor/jquery-sticky/jquery.sticky.js"></script>
<script src="static/assets/vendor/venobox/venobox.min.js"></script>
<script src="static/assets/vendor/waypoints/jquery.waypoints.min.js"></script>
<script src="static/assets/vendor/counterup/counterup.min.js"></script>
<script src="static/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="static/assets/vendor/aos/aos.js"></script>

<!-- Template Main JS File -->
<script src="static/assets/js/main.js"></script>

</body>

</html>
```
<a name="hUIHS"></a>
## static/accsts
css js 文件 和 img图片
