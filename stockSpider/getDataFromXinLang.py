#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2019/8/1 13:52
# @Author : lixufeng
# @File   : getDataFromXinLang.py

import requests
from lxml import etree

data = requests.get(url="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradedetail.php?symbol=sz002405&date=2019-07-31&page=60").content.decode("gbk")
data0 = etree.HTML(data)
result = data0.xpath('//*[@id="datatbl"]/tbody//*')  # //后面跟所有的子元素
print(len(result))
for r in result:
    print(r.tag, r.text)

data = '%'.join([res.tag + '=' + res.text for res in result])
splitData = data.split("tr=None")
for sd in splitData:
    print(sd.split('%'))
