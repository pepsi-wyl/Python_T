# -*- coding: utf-8 -*-
# @Time: 2022/1/8 10:14
# @Author: pepsi-wyl
# @File: bs4_T.py
# @Software: PyCharm

import urllib.request
try:
        url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?city=%E6%B2%B3%E5%8D%97-%E6%B2%B3%E5%8D%97"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "Referer": url,
            "Connection": "keep-alive",
            "Cookie": 'bid=RYyYJTz3evg; dbcl2="252561375:aDsS5a8NfUY"; ck=QD23; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1641609628%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.992860265.1641532328.1641561033.1641609628.3; __utmc=30149280; __utmz=30149280.1641609628.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.752140223.1641532328.1641561033.1641609628.3; __utmc=223695111; __utmz=223695111.1641609628.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25256; __utmt_douban=1; __utmb=30149280.10.10.1641609628; __utmt=1; __utmb=223695111.8.10.1641609628; _pk_id.100001.4cf6=482e19d060ed6011.1641532327.3.1641611594.1641561052.'
        }
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req, timeout=30)
        print("爬取的url为", url, "爬取状态码为:", response.status)
        html = response.read().decode('utf8')
        file = open("test.html", "w", encoding="utf-8")
        file.write(html)
        file.close()
except Exception as result:
    print("异常为:", result.reason)


import re
import bs4

html = open("test.html", "rb").read().decode('utf8')

bs = bs4.BeautifulSoup(html, "html.parser")

# print(bs)
# print(type(bs))        # <class 'bs4.BeautifulSoup'>
# print(bs.name)         # [document]

# print(bs.head)
# print(type(bs.head))    # <class 'bs4.element.Tag'>
# print(bs.title)
# print(type(bs.title))   # <class 'bs4.element.Tag'>

# print(bs.title.string)
# print(bs.a.string)
# print(type(bs.a.string)) # <class 'bs4.element.NavigableString'>
# print(bs.a.attrs)

# ----------------------------
# 文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])

# 文档的搜索

# 1)查找所有  find_all
# 字符串过滤      完全符合
# list_T = bs.find_all("a")
# 正则表达式搜索   包含即可    (常用)
# list_T = bs.find_all(re.compile("a"))
# 方法:传入一个函数，根据函数的要求去搜索
# def nameIsExists(tag):
#     return tag.has_attr("name")
# list_T = bs.find_all(nameIsExists)


# 2)kwargs  参数
# list_T = bs.find_all(id="top-nav-notimenu")
# list_T = bs.find_all(herf="https://img3.doubanio.com/favicon.ico")
# list_T = bs.find_all(class_="more-items")

# 3)text 参数
# list_T = bs.find_all(text="个人主页")
# list_T = bs.find_all(text=re.compile("\d"))

# 4)limit 参数
# list_T = bs.find_all("a", limit=3)

# 5)css选择器
# list_T = bs.select("title")               # 标签
# list_T = bs.select(".more-items")         # class
# list_T = bs.select("#top-nav-notimenu")   # id

# for item in list_T:
#     print(item)
