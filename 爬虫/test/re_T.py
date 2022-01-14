# -*- coding: utf-8 -*-
# @Time: 2022/1/8 15:27
# @Author: pepsi-wyl
# @File: re_T.py
# @Software: PyCharm

# 正则表达式(字符串模式) 判断字符串是否符合一定的标准

"""

.     表示任何单个字符
[  ]  字符集，对单个字符给出取值范围    [a,b,c] 表示a、b、c  [a-z] 表示a到z单个字符
[^ ]  非字符集，对单个字符给出排除范围   [^abc]  表示非a或b或c的单个字符
*     前一个字符0次或无限次扩展        abc*  表示 ab、abc、abcc、abccc等
+     前一个字符1次或无限次扩展        abc+  表示 abc、abcc、abccc等
？    前一个字符0次或一次扩展          abc?  表示 ab、abc
|     左右表达式任意一个              abc|def 表示abc、def
{m}   扩展前一个字符m次               ab{2}c    表示abbc
{m,n} 扩展前一个字符m至n次(含n次)      ab{1，2}  表示abc、abbc
^     匹配字符串开头                  ^abc 表示abc且在一个字符串的开头
$     匹配字符串结尾                  abc$ 表示abc且在一个字符串的结尾
()    分组标记,内部只能使用 | 操作符    (abc)表示abc (abc|cef)表示abc、cef
\d    数字,等价于[0-9]
\w    单词字符,等价于[a-z A-Z 0-9 _]

"""

"""
                            re 库
re.search()
re.match()
re.findall()
re.split()
re.finditer()
re.sub()
"""

"""
re.l   对大小写不敏感
re.L   做本地化识别(locale-aware)
re.M   多行匹配,影响^和&
re.s   使.匹配包括换行在内的所有字符
re.U   根据Unicode字符集解析字符。这个标志影响 \w,\W,\b\B
re.X   该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解
"""

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

