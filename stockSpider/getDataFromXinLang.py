#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2019/8/1 13:52
# @Author : lixufeng
# @File   : getDataFromXinLang.py

import requests
from lxml import etree

data = requests.get(url="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradedetail.php?symbol=sz002405&date=2019-07-31&page=60").content.decode("gbk")
data0 = etree.HTML(data)
result = data0.xpath('//*[@id="datatbl"]/tbody/tr[1]/*')
print(len(result))
for r in result:
    print(r.tag, r.text)

