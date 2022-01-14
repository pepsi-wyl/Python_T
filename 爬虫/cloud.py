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
