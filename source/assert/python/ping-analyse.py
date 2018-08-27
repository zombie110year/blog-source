#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import json

FILE_PATH = "C:/Users/zombi/Desktop/ping.vultr"

#*=============================>>>>>RE ANALYSE<<<<<=============================
RAW_REGEX_LOCATION = r"""={24}
正在 ping 位于 "([ \w]+?)" 的机房"""
RAW_REGEX_STATUS = r"""(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) 的 Ping 统计信息:
    数据包: 已发送 = (\d+)，已接收 = (\d+)，丢失 = (\d+) \((\d+%) 丢失\)，
往返行程的估计时间\(以毫秒为单位\):
    最短 = (\d+)ms，最长 = (\d+)ms，平均 = (\d+)ms
"""

REGEX_LOCATION = re.compile(RAW_REGEX_LOCATION, flags=re.UNICODE)
REGEX_STATUS   = re.compile(RAW_REGEX_STATUS, flags=re.UNICODE)

with open(FILE_PATH, "rt", encoding="utf-8") as f:
    context = f.read()

location_list   = list()
status_list     = list()

for item in re.findall(REGEX_LOCATION, context):
    location_list.append(item)
for item in re.findall(REGEX_STATUS, context):
    _ = ( item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
    status_list.append(_)

# 元组各元素含义:
# item[0]       IP 地址
# item[1]       发包数
# item[2]       接包数
# item[3]       丢包数
# item[4]       丢包率
# item[5]       最短延迟
# item[6]       最长延迟
# item[7]       平均延迟

loc_status_dict = {}

for i in range(0, len(location_list)):
    tmp = {location_list[i]:status_list[i]}
    loc_status_dict = {**loc_status_dict, **tmp}
#*=============================<<<<<RE ANALYSE>>>>>=============================
#*================================>>>>>JSON<<<<<================================

import json