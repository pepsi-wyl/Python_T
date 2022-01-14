# -*- coding: utf-8 -*-
# @Time: 2022/1/7 21:01
# @Author: pepsi-wyl
# @File: urllib_T.py
# @Software: PyCharm

# 导入模块
import urllib.request




# get请求
# try:
#     # 封装req
#     url = "http://httpbin.org/get"
#     headers = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
#          "Referer": url,
#          "Connection": "keep-alive"
#     }
#     req = urllib.request.Request(url, headers=headers)
#
#     # 获取获取响应
#     response = urllib.request.urlopen(req, timeout=3)
#
#     # 得到网页信息
#     html = response.read().decode('utf8')
#     print(html)
#
# except Exception as result:
#     print("爬取时间超时!!!异常为:", result)




# post请求
# try:
#
#     # 封装req
#     url = "http://httpbin.org/post"
#     headers = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
#          "Referer": url,
#          "Connection": "keep-alive"
#     }
#     data = bytes(urllib.parse.urlencode({"name": "pepsi-wyl"}), encoding="utf-8")
#     req = urllib.request.Request(url, headers=headers, data=data, method="POST")
#
#     # 获取响应
#     response = urllib.request.urlopen(req, timeout=3)
#
#     # 得到网页信息
#     html = response.read().decode('utf8')
#     print(html)
#
# except Exception as result:
#     print("爬取时间超时!!!异常为:", result)



# 实例
try:
    url = "https://eyesight.news.qq.com/sars/riskarea"
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



