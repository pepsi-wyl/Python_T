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
    initDatabase(dbPath="doubanMovie.db")






