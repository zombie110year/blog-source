#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from time import localtime
from getopt import getopt
from re import sub

FILE_PATH = "./source/Tips/index.md"

MD_TEMPLATE = \
"""\
{front_matter}

{the_new}

<!--more-->

{the_old}"""

FRONT_MATTER = \
"""---
title: Tips
type: "tips"
---"""

CONTEXT = \
"""# {title}
{content}
> date: {date}"""

def get_date():
    _ = localtime()
    date = "{year:0>4d}-{mon:0>2d}-{day:0>2d} {hour:0>2d}:{min:0>2d}:{sec:0>2d}".format(
        year    =   _.tm_year    ,
        mon     =   _.tm_mon     ,
        day     =   _.tm_mday    ,
        hour    =   _.tm_hour    ,
        min     =   _.tm_min     ,
        sec     =   _.tm_sec
    )
    return date

def get_context():
    options, args = getopt(argv[1:], shortopts="t:c:")
    opt = dict(options)
    if '-c' in opt:
        context = CONTEXT.format(title=opt['-t']+'\n', content=opt['-c']+'\n', date=get_date())
    else:
        context = CONTEXT.format(title=opt['-t'], content='', date=get_date())
    return context

def get_old():
    with open(FILE_PATH, "rt", encoding="utf-8") as f:
        the_old = f.read()
    return sub(pattern="<!--more-->\n\n", repl="", string=the_old[34:]) # Front Matter 部分正好 34 个字符.

def write_file(context):
    with open(FILE_PATH, "wt", encoding="utf-8") as f:
        f.write(context)

def main():
    the_new = get_context()
    the_old = get_old()
    to_write = MD_TEMPLATE.format(
        front_matter=FRONT_MATTER,
        the_new=the_new,
        the_old=the_old
        )
    write_file(to_write)
    print(the_new)

if __name__ == "__main__":
    main()
