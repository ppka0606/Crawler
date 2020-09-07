#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :robotparser.py
@说明        :尝试使用robotparser解析robots.txt文件指导爬虫的编写
@时间        :2020/09/07 22:48:09
@作者        :ppka0606
@版本        :1.0
'''
import urllib.robotparser as urobot
import requests

url = 'https://www.taobao.com/'
rp = urobot.RobotFileParser()
rp.set_url(url + "/robots.txt")
rp.read()

useragent = 'Baiduspider'
if rp.can_fetch(useragent, 'https://www.taobao.com/product/'):
    site = requests.get(url)
    print('succeed!')
else:
    print("failed! can't fetch.")

# 实例分析：淘宝网的 Robots.txt文件
# User-agent: Baiduspider
# Disallow: /
# User-agent: baiduspider
# Disallow: /
# 很显然淘宝不允许百度的机器人访问其网站下其所有的目录。
