#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2019/8/1 13:52
# @Author : lixufeng
# @File   : getDataFromXinLang.py

import requests
from lxml import etree
import pandas as pd
import numpy as np
"""
数据处理部分
"""
# 获取基础数据
data = requests.get(url="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradedetail.php?symbol=sz002405&date=2019-08-14&page=11").content.decode("gbk")
data0 = etree.HTML(data)
result = data0.xpath('//*[@id="datatbl"]/tbody//*')  # //后面跟所有的子元素
print(len(result))
for r in result:
    print(r.tag, r.text)

# 数据整理
data = '%'.join([str(res.tag) + '=' + str(res.text) for res in result])
splitData = data.split("tr=None")

splitData = [a.split('%') for a in splitData]
# 数据转至dataframe

dataPd = pd.DataFrame(splitData,columns=[1,2,3,4,5,6,7,8,9,10,11])
print(dataPd)
