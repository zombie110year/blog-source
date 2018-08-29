---
title:  PyLib-getopt
data:   2018-8-26 2:39:13
mathjax:  false
tags:
    - PythonLibrary
categories:
    - Python
---

> [OriginFile](/assert/resources/python/lib.getopt.help.txt.html)

# 函数

## getopt()

```py
getopt(args, shortopts, longopts=[])
    getopt(args, options[, long_options]) -> opts, args
```
解析命令行选项与参数列表. 参数列表将被分析, 而不带前导地引用到正在运行的程序. 通常, 参数列表意味着 `sys.argv[1:]`.

### 必选参数: `args`, `options`(短选项).

`shortopts` 是脚本将要识别的选项字母字符串, 前导字符 `-` 不应包含在此字符串中, 需求参数的选项后应跟着冒号 `:`(即与 Unix `getopt()` 使用的格式相同).

### 可选参数: `long_options`(长选项).

`longopts` 是一个字符串列表, 其中带有要提供的长选项名称. 前导字符 `--` 不应包含在选项名称中. 需要参数的选项后跟等号 `=`.

### 返回值: 元组 (opts, args)

- opts 为一个列表, 其中元素为 `(选项, 参数)` 形式的元组.
- args 为一个列表, 其中元素为输入的原始命令行参数经 `shortopt` 或 `longopts` 解析之后的剩余部分.

返回值由两个元素组成: 第一个为 `(选项, 值)` 对(类型为元组) 组成的列表; 第二个是由解析之后剩下的参数(第一个参数的尾随切片)组成的列表.
返回的每个 `选项-值` 对都有一个选项作为它的第一个元素, 以连字符作为前缀 (如 `-x`), 选项参数作为第二个元素, 或者如果该选项没有参数, 则为空字符串.
这些选项在列表中以找到它们的顺序出现, 从而允许多个实现发生.
长选项和短选项可能会混合.


## gun_getopt()

```py
gnu_getopt(args, shortopts, longopts=[])
    getopt(args, options[, long_options]) -> opts, args
```

此函数工作方式类似于 `getopt()`, 除了默认以 GNU 风格扫描. 这意味着选项与 non-option 参数可能互相混合.
`getopt()` 函数在遭遇到 non-option 参数时将立刻停止处理选项.

如果选项字符串的第一个字符为 `+`, 或者环境变量 `POSIXLY_CORRECT` 被设置, 遭遇到 non-option 参数时也将停止处理.