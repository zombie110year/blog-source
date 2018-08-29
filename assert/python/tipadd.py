#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from time import localtime
import codecs
from getopt import getopt

FILE_PATH = "./source/_posts/TIPS.md"

MD_TEMPLATE = [
    "---\n",                    #  4
    "title: 'Tips'\n",          # 14
    "date: %s\n",               # 26
    "categories: Tips\n",       # 17
    "---\n",                    #  4
    "\n",                       #  1
    "",                         # 新条目插入位置
    "\n",
    "<!--more-->\n\n",              # More 分隔符
    "",                         # 旧内容插入位置
    ]

def main(file_path=FILE_PATH):
    options, args = getopt(argv[1:], "m:o:")
    options = dict(options)
    #print(options)
    main_str = options['-m']
    other_str = options['-o']
    global MD_TEMPLATE
    t = localtime()
    date = "%4d-%02d-%02d %02d:%02d:%02d"%(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    context = """\
# %s

%s

> date:%s
"""%(main_str, other_str, date)
    with open(file_path, "rt", encoding="utf-8") as f:
        full_text = f.read()
        MD_TEMPLATE[2] = MD_TEMPLATE[2]%date
        MD_TEMPLATE[9] = del_more(full_text[66:])         # yaml 配置的字符数为 66
        MD_TEMPLATE[6] = context
    with open(file_path, "wb") as f:
        out_text = ""
        for lines in MD_TEMPLATE:
            out_text += lines
        # print(out_text, file=f, end='')
        f.write(out_text.encode("utf-8"))
    print(context)

def del_more(context):
    return context.replace("<!--more-->\n\n", "")


if __name__ == "__main__":
    main()
