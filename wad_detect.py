#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :wad_detect.py
@说明        :
@时间        :2020/09/07 23:45:21
@作者        :ppka0606
@版本        :1.0
'''

import wad.detection
det = wad.detection.Detector()
url = 'http://www.12306.cn/'
print(det.detect(url))

'''
@提交说明    :wad内部没有处理编码异常，因此该程序暂时无法使用，会报DecodeError
@提交时间    :2020/09/07 23:54:46
@提交作者    :ppka0606
'''

