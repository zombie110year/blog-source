#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from time import localtime
from sys import argv
#from hashlib import md5

__doc__ = """用于生成博文模板, 放置于草稿文件夹中
Usage:  python Hexo_New.py 标题
"""

BLOG_PATH = r"D:/Blog/source"

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

class _PrintableTime(str):
    "可打印格式的时间(string)"
    def __init__(self):
        _crt_time = _PrintableTime.getTime()
        self.date = _crt_time[0]
        self.time = _crt_time[1]
    @staticmethod
    def getTime():
        "返回 (日期, 时间) 元组"
        CRT_TIME = localtime()
        date = "{year:0>4d}-{mon:0>2d}-{mday:0>2d}".format(year=CRT_TIME.tm_year, mon=CRT_TIME.tm_mon, mday=CRT_TIME.tm_mday)
        time = "{hour:0>2d}:{min:0>2d}:{sec:0>2d}".format(hour=CRT_TIME.tm_hour, min=CRT_TIME.tm_min, sec=CRT_TIME.tm_sec)
        return date, time

def writeFrontMatter(title):
    "返回格式化后的 Markdown 头信息"
    t = _PrintableTime()
    _prt_temp = TEMP.format(title=title, date=t.date, time=t.time)
    return _prt_temp

def getTitle():
    "检查参数"
    title = argv[1]
    return title

def main():
    title = getTitle()
    #md5_title = md5(title.encode('utf-8')).hexdigest()
    file_path = r"{source}\{folder}\{file}.md".format(
        source=BLOG_PATH,
        folder="_drafts",
        file=title.lower().replace(' ', '-')
        )

    front_matter = writeFrontMatter(title).encode("utf-8")

    with open(file_path, "wb") as f:
        f.write(front_matter)
    print(front_matter.decode("utf-8"))

if __name__ == "__main__":
    main()
