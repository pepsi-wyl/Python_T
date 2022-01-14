# -*- coding: utf-8 -*-
# @Time: 2022/1/9 9:58
# @Author: pepsi-wyl
# @File: xlwt_T.py
# @Software: PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")     # 创建workbook对象
worksheet = workbook.add_sheet("sheet1")       # 创建工作表
for i in range(1, 10, 1):
    for j in range(1, i + 1, 1):
        worksheet.write(i, j, "%d * %d = %d" %(i, j, i*j))     # 写入数据
workbook.save("student.xls")                   # 保存数据表



