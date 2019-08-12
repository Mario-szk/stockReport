#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2019/7/4 15:32
# @Author : lixufeng
# @File   : chech_today.py.py

import pymysql

connection = pymysql.connect(host='cdb-rcpqxkrm.bj.tencentcdb.com',
                             user='root',
                             password='xxx123455',
                             db='Trade_Detail',
                             port=10158)

cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("select * from Detail_1907 where date='2019-07-04'")

data = cursor.fetchall()

# 统计上证的交易量、交易金额
sh_price = 0
sh_many = 0
sz_many = 0
sz_price = 0
for i,d in enumerate(data):
    if d['stock_exchange'] == 'sh':
        sh_price += d['price']*d['stock_num']
        sh_many += d['stock_num']/100
    if d['stock_exchange'] == 'sz':
        sz_price += d['price']*d['stock_num']
        sz_many += d['stock_num']/100
    if i%10000==0:
        print(i)
