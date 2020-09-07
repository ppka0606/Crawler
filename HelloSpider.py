#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :HelloSpider.py
@说明        :
@时间        :2020/09/07 18:34:59
@作者        :ppka0606
@版本        :1.0
'''

import lxml.html
import requests

url = 'https://www.python.org/dev/peps/pep-0020/'
# 原本书上的url已经更新为这个
xpath = '//*[@id="the-zen-of-python"]/pre/text()'
res = requests.get(url)
ht = lxml.html.fromstring(res.text)
text = ht.xpath(xpath)

print("Hello,\n"+"".join(text))
