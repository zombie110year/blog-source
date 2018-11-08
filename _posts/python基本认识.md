---
comments: true
title: '[PyNote]-0-Python基础认识'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-07-26 15:29:44
---

<!--more-->

# Python 基础认识

## 配置 Python 开发环境

先来了解一下怎么安装 Python 吧.

对于 Windows 系统, 安装 Python 可以去 [Python 官网](http://www.python.org/) 下载官方提供的 `Windows x86-64 executable installer` 安装包. Python2 还是 Python3 随便选择, 不过 Python2 是历史遗留, 未来大部分 Python 语言肯定都会用 Python3 的. 我准备学习 Python3 .

下载完成之后, 直接运行该 .exe 文件, 安装路径最好就选在 `C:\Python` . 如果按照默认设置 安装在 APPDATA 里的话, 可能在执行一些脚本时由于路径过长导致一些问题...

安装时选择 "add Python to PATH" 可以自动将 Python 添加进系统的环境变量里. 如果忘了的话, 也可以自行在系统设置里添加环境变量. `C:\Python` 和 `C:\Python\Scripts` 都需要添加到环境变量 `PATH` 里, 前者是 Python 解释器的路径, 后者是通过 Python-pip 下载的第三方模块或脚本的路径.

安装之后, 可以使用

```powershell
python -V # 或 python --version
pip -v
```

来确认一下 `C:\Python` 和 `C:\Python\Scripts` 是否已经配置好了.

之后最好配置一下 pip 的软件源. 否则按国内的网络环境, 经常会下载失败或者只有毛细作用般的下载速度...

依照着 [清华大学镜像的帮助文档](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/) 将 pip 的软件源更换为清华镜像. 

> **设为默认**
> 修改 %APPDATA%\\pip\\pip.ini (Windows 10) (没有就创建一个)， 修改 index-url至tuna，例如

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

> pip 和 pip3 并存时，只需修改 ~/.pip/pip.conf。

虽然在用户的家目录下就有一个 `APPDATA` 的隐藏文件夹, 但是实际上这个文件的路径应该是 `C:\Users\userhome\AppData\Roaming\pip\pip.ini`, `%APPDATA%` 变量也是指向 `C:\Users\userhome\AppData\Roaming\` 这个路径的.

配置好之后, 先通过 pip 下载 Python 的 lint 程序和代码格式化程序.

- 下载 [pylint](https://www.pylint.org/#install)
- 下载 [autopep8](https://github.com/hhatto/autopep8) , 该程序会按照 [pep8](https://lizhe2004.gitbooks.io/code-style-guideline-cn/content/python/python-pep8.html) 代码规范格式化文档.
  - 另一种代码格式化程序的选择是 [yapf](https://github.com/google/yapf) , 按 [Google 的标准](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/) .

```powershell
python -m pip install pylint
python -m pip install autopep8
```

搞完这些步骤, 就可以用任意喜欢的文本编辑器(最好是支持代码高亮的, 默认的 Notepad 就算了吧) 进行 Python 编程了.

## Python 的脚本模式和交互式模式

Python 安装好了之后, 可以用两种方式使用 Python

0. 交互式
  要进入这种模式, 只需要在终端中输入 `Python` 就可以进入 Python 的交互式环境. 在里面可以一句一句地执行代码. 如果输入的是一个表达式, 在计算之后, Python 会自动地把结果 print 出来, 不需要使用 `print()` 函数. 要退出此环境, 需要执行 `exit()` 函数.
0. 脚本模式
  这个模式就是编写一个 Python 脚本, 文件需要以 `.py` 结尾. 然后以参数的形式传递给 Python 解释器. 在这个模式下, 文件中写了什么, Python 就做什么, 没写的就不会做. 所以, 要在终端中显示内容, 必须使用 `print()` 函数了. 当执行到文件末尾的时候, 程序会自动退出, 不需要 `exit()` 函数. 不过如果需要向系统传递特定的退出参数, 也可以使用 `exit(xxx)` 函数.

Python 更受欢迎的交互式 Shell 是 `IPython`, 可通过 `pip install ipython` 下载.

## Python 脚本的源代码是怎样的

编写一个 Python 程序并没有多苛刻的要求, 只需要一行一行地把功能给实现了就好.
下面以一个 "Hello World" 程序介绍一下 Python 的源代码一般长什么样吧.

```py
#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
这是一条文档字符串
可以换行, 写很多行
一般会用于写文档, 
比如在一个自定义函数下面说明函数的功能和参数的含义
"""
import os
for i in range(1,10):
    print("Hello World") # 使用 Python 内建函数 print()
os.system("echo Hello World") # 使用 os 模块的 system() 函数调用外部命令 echo Hello World.
```
- Python 程序可以有两条特殊注释, 这两条注释必须写在源代码前两行, 在其他地方不会起作用:
  - 第一行: `#! /usr/bin/python3` 用来向系统声明 Python 解释器的路径. 不过这个功能只有 Linux 等类 Unix 的系统才有用, 如果看过 Linux 的 bash 脚本, 会发现其第一行也有类似的特殊注释 `#! /bin/bash`. 有了这条注释, 在终端中运行该脚本的时候, 只需要输入 `./filename` 就可以调用声明的解释器来执行了, 连文件扩展名都不需要的. 但是 Windows 系统基于 NT 内核. 这条特殊注释没有作用. 无论怎样, 都需要 `python .\filename.py`.
  - 第二行: `# -*- coding: utf-8 -*-` 向 Python 解释器声明该文件使用的字符编码. 如果不写该注释的话, Python 默认以 utf-8 作为编码格式. 一般情况下都用 utf-8. 这个注释估计是一个历史遗留功能了吧...
- Python 用 `""" 文档字符串 """` 和 `# 单行注释` 注释.
- Python 可以用 import 语句导入一个模块, 比如这里导入的 `os` 模块. 导入之后, 使用 `.` 对象运算符从模块中使用该模块定义的 `system()` 函数.
- Python 的控制结构后面会用 `:` 冒号.
- Python 以相同的 **缩进** 标识一个语句块.

## 小结

安装 Python:

- 下载安装包并安装  ->
- 配置环境变量      ->
- 配置 pip 软件源   ->
- 通过 pip 安装 pylint 和 代码格式化程序

Python 代码的基本结构:

- (可选) 特殊注释, 前两行
- 语句

了解了 Python 的基本概念之后, 就先学习一下 Python 的 [运算符](/2018/07/python运算符/) 和 [控制结构](/2018/07/python控制结构) 吧. 先把 Python 用起来.

- 数据结构
  - 数字
    - 整数
    - 浮点数
    - 复数
  - 字符串
  - 集合
    - 列表
    - 元组
    - 字典
- 运算符
  - 算术运算符
  - 关系运算符
  - 赋值运算符
  - 逻辑运算符
  - 位运算符
  - 成员运算符
  - 身份运算符
- 控制结构
  - 分支
  - 循环
