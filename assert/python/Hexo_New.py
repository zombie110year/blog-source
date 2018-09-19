#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from time import localtime
from sys import argv
from getopt import getopt
import re

__doc__ = """用于生成博文模板
Usage:  python Hexo_New.py -t 标题 -m 模式
"""

BLOG_PATH = r"D:/Blog/source"

class _PrintableTime(str):
    "可打印格式的时间(string)"
    def __init__(self):
        _crt_time = _PrintableTime.get_time()
        self.date = _crt_time[0]
        self.time = _crt_time[1]
    @staticmethod
    def get_time():
        CRT_TIME = localtime()
        date = "{year:0>4d}-{mon:0>2d}-{mday:0>2d}".format(year=CRT_TIME.tm_year, mon=CRT_TIME.tm_mon, mday=CRT_TIME.tm_mday)
        time = "{hour:0>2d}:{min:0>2d}:{sec:0>2d}".format(hour=CRT_TIME.tm_hour, min=CRT_TIME.tm_min, sec=CRT_TIME.tm_sec)
        return date, time

def frontmatter_writer(title):
    "返回格式化后的 Markdown 头信息"
    TEMP = """\
---
title:  {title}
data:   {date} {time}
mathjax:  false
tags:
    - null
categories:
    - null
---

"""
    t = _PrintableTime()
    _prt_temp = TEMP.format(title=title, date=t.date, time=t.time)
    return _prt_temp

def check_opts():
    "返回整理好的参数"
    OPT = "t:m:"
    options, args = getopt(argv[1:], OPT)
    opt_dict = dict(options)
    if not re.match("^_\S+$", opt_dict['-m']):
        opt_dict['-m'] = '_' + opt_dict['-m']
    return opt_dict

def main():
    opt = check_opts()
    file_path = r"{source}\{folder}\{file}.md".format(source=BLOG_PATH, folder=opt['-m'], file=opt['-t'])
    front_matter = frontmatter_writer(opt['-t']).encode("utf-8")
    with open(file_path, "wb") as f:
        f.write(front_matter)
    print(front_matter.decode("utf-8"))


if __name__ == "__main__":
    main()
