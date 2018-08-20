---
title: '[PyNote]-读写文件'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-08-16 00:38:16
---

# `open()` 打开文件

Python 内置函数 `open()` 可以完成对文件的打开.

## `open()`

```py
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

`open()` 函数是 Python 内建函数, 以 `mode` 指定模式打开 `file` 指定文件, 返回一个文件对象. 例如

```py
f = open("./test.txt", "r")
# 以 只读(r) 模式打开工作目录下的 test.txt 文件. 返回一个 file 类型的对象, 赋值给变量 f
# file 参数同时接受 DOS 路径分隔符 \ 和 Unix 路径分隔符 /
```

[open() 的文档](/assert/resources/buildin.open.__doc__.html)

### 参数 `file`

**参数** `file` 是字符串类型数据, 可以是普通文本, 也可以是二进制编码的字符串. 给出需要打开的文件名 (如果文件不在当前目录, 需要给出文件的路径, 绝对路径或相对路径.) 或者要 wrap 的文件的整数文件描述符. (如果给出了文件描述符, 则在关闭 I/O 对象时关闭它, 除非设置 `closefd=False`).

TODO:

- 什么是文件描述符?
- wrap 文件描述符是什么意思?

### 参数 `mode`

`mode` 是一个字符串类型的数据, 用于指定文件的打开方式. 默认为 "r", 意味着 文本只读(text readonly) 模式打开.

所有接受的模式:

```
========= ================== ===================================================
字符      读/写指针初始位置  Meaning
--------- ----------------------- ----------------------------------------------
'r'       头部               文本 只读. (默认模式)
'w'       头部               文本 只写, 如果文本已存在则截断文件.
'x'       头部               创建新文件, 并以写模式打开它. 如果文件已存在则抛出 
                             FileExistsError
'a'       尾部               以写模式打开, 如果文件存在则在末尾添加.
'b'                          二进制模式.
't'                          文本模式.
'+'                          打开文件以更新. (读写)
========= ================== ===================================================
```

打开模式与对象类型的关系:

```
rt  <class '_io.TextIOWrapper'>
wt  <class '_io.TextIOWrapper'>
xt  <class '_io.TextIOWrapper'>
r+t <class '_io.TextIOWrapper'>
w+t <class '_io.TextIOWrapper'>
x+t <class '_io.TextIOWrapper'>
rb  <class '_io.BufferedReader'>
wb  <class '_io.BufferedWriter'>
xb  <class '_io.BufferedWriter'>
r+b <class '_io.BufferedRandom'>
w+b <class '_io.BufferedRandom'>
x+b <class '_io.BufferedRandom'>
```

### 其他参数

```
=============== =============== ================================================
Args            ValueType       Meaning
--------------- --------------- ------------------------------------------------
buffering       int             设置缓冲区大小
encoding        str             设置字符编码
errors          str             设置错误处理策略
newline         str             设置对换行的处理方式
closefd         bool            设置对文件描述符的处理方式
opener          Unknown         Unknown
=============== =============== ================================================
```

### 挖坑代填

<div id="todo">TODO:</div>

```
open() 的参数:
closefd         什么是文件描述符?
opener          这是什么鬼东西?

?Python 内置 class :
rt  <class '_io.TextIOWrapper'>
wt  <class '_io.TextIOWrapper'>
rb  <class '_io.BufferedReader'>
wb  <class '_io.BufferedWriter'>
r+t <class '_io.TextIOWrapper'>
w+t <class '_io.TextIOWrapper'>
r+b <class '_io.BufferedRandom'>
w+b <class '_io.BufferedRandom'>
```

> 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
> 
> ---[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000)

# `file` 类可用的方法

```
=============== =============== ================================================
Method          Args (self,...) Meaning
--------------- --------------- ------------------------------------------------
close()                         关闭文件.
flush()                         刷新文件内部缓冲, 将缓冲区数据立即写入.
? fileno()                      返回一个整型的文件描述符.
isatty()                        判断文件是否是终端 (例如 Linux 下的 /dev/ttyX)
read()          [int size]      读取文件, 得到文件所有内容, 返回一个字符串. 可选
                                参数 size, 指定读取字节数, 如果未指定或为负数, 
                                则读取至 EOF.
readline()      [int size]      读取一行, 以换行符结尾. 可选参数 四则, 读取指定
                                字节数, 如果未指定或为负数或超过本行字符数, 则读
                                取至本行换行符.
                                返回值带有换行符, 读到文件末尾会返回空字符串.
readlines()                     读取文件, 获取所有行的内容, 返回一个列表, 其中一
                                行一项. 读取到 EOF 时返回空字符串.
write()         str             向文件中写入字符串.
seek()          int, 
=============== =============== ================================================
```

# 