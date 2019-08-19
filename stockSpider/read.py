#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2019/8/14 21:21
# @Author : lixufeng
# @File   : read.py
import os

query = open("allquery.txt")
outquery = open("outquery.txt", "w")
for line in query:
    words = line.split(",")
    for word in words:
        # out = os.system("sh /opt/workspace/esclient/zzesclient/search.sh %s 1"%(word))
        if word.replace(' ','') != '':
            outquery.write(word + "\n")
query.close()
outquery.close()
