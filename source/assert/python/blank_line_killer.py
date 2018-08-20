#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import getopt
import os
import platform
import re
import sys

# * getopt 获取 target_dir, file_mode
# * 获取目标目录文件列表
# * 对其中一个文件:
## * 调用外部程序格式化             # 下载代码格式化工具: jdf
## * 读取文本内容
## * 删除空行
## * 覆盖写入源文件

__doc__ = """\
功能:
    删除文本文件中的空行. 使文件更紧凑.
================================================================================
Usage:  %s -d target -m file_ext
Note:   target 不以路径分隔符结尾, 可以为目录, 也可以为文件
>>>     file_ext 会特异性检测文件扩展名, 只有规定的文件后缀会被处理(暂无此功能). 默认
>>>     处理html文件. 需要带 "." 号, 如 ".html"
"""%__file__

#! =================================重要变量 开始=================================
REPLACE_TARGET = re.compile(r"^[ \t]*\n{1}$")          # 设置替换目标 == 换行符 \n 前仅有空白字符或什么也没有的一行
sysinfo = platform.platform()
SEPERATOR = "/"          # * 根据系统类型设置路径分隔符
if "Windows" in sysinfo:
    SEPERATOR = "\\"
elif "Linux" in sysinfo:
    SEPERATOR = "/"
target_dir = ""
file_mode = ".html"
root_dir = ""
file_list = []
#* =================================重要变量 结束=================================

#! ================================声明函数部分 开始================================
def get_file_name(file_path):                                # TODO: 检测其他文件
    file_type = re.findall(r'\.[^.\/:*?"<>|\r\n]+$', file_path)[0]
    return file_type
def walk_path(father_dir):
    """递归读取目标目录下目标文件的绝对路径, 储存在全局变量 file_list[] 中"""
    global file_list
    for child_item in os.listdir(father_dir):
        item_full_path = "%s%s%s"%(father_dir, SEPERATOR, child_item)
        if os.path.isfile(item_full_path):
            if get_file_name(item_full_path) == file_mode:
                file_list.append(item_full_path)
        elif os.path.isdir(item_full_path) or os.path.islink(item_full_path):
            walk_path(item_full_path)
    return True

def write_file(file_path):
    """一行一行地读取文本, 去除其中只有换行符的一行, 添加至out_string变量, 然后一股脑地覆盖写入原文件"""
    file_path = file_path
    out_string = ""
    with open(file_path, "r", encoding="utf-8") as file_in:
        for lines in file_in.readlines():
            out_string += REPLACE_TARGET.sub("", lines)
    with open(file_path, "wb") as file_out:
        file_out.write(out_string.encode("utf-8"))
    return True

def cover_file(file_path):                      # TODO: 另一种删除空行的方法.
    """\
读取文本文件, 按字符递进;
遇到连续的 \\n\\n\\n... 将其替换为一个 \\n;
遇到连续的 \\t\\t<space>...\\n 将其删除.
    """
    pass

def my_format():
    walk_path(root_dir)
    for item in file_list:
        write_file(item)

def test_walk_path(mode="print"):
    """测试 walk_path 函数, mode 参数 print 将结果显示在 stdout 上, write 将结果写进文件"""
    walk_path(root_dir)
    if mode == "write":
        with open(target_dir+r"\tmp.txt", "wb") as f:
            for item in file_list:
                f.write((item+"\n").encode("utf-8"))
    elif mode == "print":
        i = 1
        for item in file_list:
            print("%d:\t|%s"%(i, item))
            i += 1

def blank_line_killer():
    """ main 函数"""
    global target_dir
    global file_mode
    global root_dir
    args = sys.argv[1:]
    options, arguments = getopt.getopt(args, "d:m:h")
    for key, value in options:
        if key == "-d":
            target_dir = value
        elif key == "-m":
            file_mode = value
        elif key == "-h":
            print(__doc__)
            return 0
    if os.path.isfile(target_dir):
        write_file(target_dir)
        return 0
    else:
        os.chdir(target_dir)
        root_dir = os.getcwd()
    my_format()

#* ================================声明函数部分 结束================================

if __name__ == "__main__":
    blank_line_killer()
