#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from re import findall, match   # 从 re 模块中导入 findall, match 函数
TEST_STRING = ""                # 设置待测文本
REGEX = r""                     # 设置正则表达式, r 表示 raw 字符串, 引号内即使有转义字符也不转义.

def main(regex=REGEX, test_str=TEST_STRING, mode=0):
    if mode == 0:
        out_put = findall(regex, test_str)      # findall 按 regex 在 test_str 里搜索所有匹配的字符串, 返回一个列表
    elif mode == 1:
        out_put = match(regex, test_str)        # match 检查 regex 是否匹配 test_str
    print(out_put)

# 可以编辑此文件中的 TEST_STRING 和 REGEX 变量之后直接运行脚本.
# 也可以在交互式 Python 控制台中 import 这个文件在自己选择调用主函数时传递的参数.
# 以下是一些预定义的字符串

URL_TEST = """
这个字符串中放着两个使用 http(s)协议的网址:
http://zombie110year.github.io/assert/python/regex_test.py
用一个 regex 正则表达式匹配它,
注意不要和其他类型的网页弄错了: git@github.com:zombie110year/zombie110year.github.io/assert/python/regex_test.py
你得想办法弄一个能匹配所有 URL 类型的字符串的正则表达式, 而且不会与其他的弄混.
我的博文:
https://zombie110year.github.io/2018/08/regex-正则表达式.html嘿!
"""

URL_REGEX = r"https?://[\S]+[\.a-zA-Z]+"
# https?:// 匹配 http:// 或 https://
# [\S]+ 匹配 URL 路径
# [\.a-zA-Z]+ 匹配最后的文件后缀名(后缀名不应该有中文吧...)


if __name__ == "__main__":
    main(URL_REGEX, URL_TEST)

