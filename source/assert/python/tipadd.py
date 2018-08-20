#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from time import localtime
import codecs
from getopt import getopt

MD_TEMPLATE = [
    "---\n",                    #  4
    "title: 'Tips'\n",          # 14
    "date: %s\n",               # 26
    "categories: Tips\n",       # 17
    "---\n",                    #  4
    "\n",                       #  1
    "",
    "\n",
    "",
    ]

def main():
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
    with open("./source/_posts/_TIPS.md", "rt", encoding="utf-8") as f:
        full_text = f.read()
        MD_TEMPLATE[2] = "date: %s\n"%date
        MD_TEMPLATE[8] = full_text[66:]
        MD_TEMPLATE[6] = context
    with open("./source/_posts/_TIPS.md", "wb") as f:
        out_text = ""
        for lines in MD_TEMPLATE:
            out_text += lines
        # print(out_text, file=f, end='')
        f.write(out_text.encode("utf-8"))
    print(context)

if __name__ == "__main__":
    main()