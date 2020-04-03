---
title: ANSI 转义序列
date: 2019-07-07 10:37:13
tags:
  - 控制台
categories: 笔记
---

ANSI 转义序列(ANSI Escape Sequence)
===================================

ANSI
转义序列是一种用于控制终端输出的色彩、样式、光标位置以及控制终端行为的特殊字节.
它的使用方式就是通过 stdout
在字符串、字节中向外输出**Control当终端支持此转义序列的功能时,
就会呈现出相应的效果. 此功能常常用于终端的彩色输出、构建 Text User
Interface 应用等.

ANSI 转义序列在 Linux、 MacOS 的各终端下得到了广泛运用, 但是在 Windows
系统上支持不佳. 不过 Microsoft 新出的
`microsoft/terminal <https://github.com/microsoft/terminal>`__
很好地支持了 ANSI 转义序列, 现在就有了足够的动力去学习它了.

ANSI 转义序列使用 ASCII 码为 ``0x1b`` 的字节作为转义字符,
而不是通常使用的反斜杠转义符 ``\``\ (``0x5c``), 这个字符是非打印字符,
被称为 ``ESC``. 它在大多数编程语言中可以使用 ``\x1b`` 或 ``\e`` 来输入.

转义序列采用了 ``\x1b[<code><tail>`` 这样的格式.

其中 ``\x1b[`` 被称作 **Control Sequence Introducer** , 简称 CSI,
它是大多数 ANSI 转义序列的开头. 而字符 ``<tail>``
则用于标志一个转义序列的结尾, 不同的 tail 对应不同功能.
在这两个组件之间的部分 ``<code>``, 则是转义序列的具体内容.


字符渲染序列(SGR)
-----------------

字符渲染序列用来描述此序列之后的字符在终端中的呈现格式. 它采用字母 ``m``
作为结尾. 在中间的 code 部分, 可以使用 ``;`` 分号来分隔不同的样式码.

它的形式类似于 ``\x1b[31;43m``, 这样的 CSI 也被称为 **Select Graphic
Rendition** (SGR) 序列.

大多数终端支持 4 bit 色彩与 8 种样式:

::

       # 前景色代码
       F_BLACK = 30
       F_RED = 31
       F_GREEN = 32
       F_YELLOW = 33
       F_BLUE = 34
       F_PURPLE = 35
       F_LIGHTBLUE = 36
       F_WHITE = 37

       # 背景色代码
       B_BLACK = 40
       B_RED = 41
       B_GREEN = 42
       B_YELLOW = 43
       B_BLUE = 44
       B_PURPLE = 45
       B_LIGHTBLUE = 46
       B_WHITE = 47

       # 效果代码
       X_NULL = 0                  # 清空
       X_BOLD = 1                  # 加粗
       X_LIGHT = 2                 # 浅色
       X_ITALIC = 3                # 斜体
       X_UNDERLINE = 4             # 下划线
       X_BLINK = 5                 # 闪烁
       X_NEGA = 7                  # 负片
       X_TRANSPARENT = 8           # 透明

例如, ``\x1b[31;43m Hello World \x1b[0m`` 将会呈现为黄底红字的
``Hello World``. 在 CSI 与 其他组件之间并不需要空格,
这里的空格仅仅是为了方便阅读.

在末尾的 ``\x1b[0m`` 将会清空样式, 由于 CSI 将会影响之后的所有输出,
如果不清空的话, 会导致之后的所有输出都具有此样式.

有些终端可接受 8 bit 256 色, 这被称作 “True Color”,
现代终端模拟器甚至可以支持 24bit 颜色, 已经是标准的图像颜色支持了.

要使用 256 色, 以这样的形式输出

::

       \x1b[38:5:<code>m       前景色
       \x1b[48:5:<code>m       背景色

其码表可以参考 https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit

24bit 色彩使用 RGB 序列, 以这样的形式输出:

::

       \x1b[38;2;<r>;<g>;<b>m      前景色
       \x1b[48;2;<r>;<g>;<b>m      背景色

光标移动序列
------------

=============== ==========================
转义序列        作用
=============== ==========================
``CSI<n>A``     光标向上移动 n 行
``CSI<n>B``     光标向下移动 n 行
``CSI<n>C``     光标向前移动 n 列
``CSI<n>D``     光标向后移动 n 列
``CSI<n>;<m>H`` 光标移动到第 n 行, 第 m 列
=============== ==========================

清屏指令
--------

``CSI<code>J`` 清空屏幕, 当 ``code`` 为:

-  ``0``: 清空光标以下区域
-  ``1``: 清空光标以上区域
-  ``2``: 清空全部

``CSI<code>K`` 清空行, 当 ``code`` 为:

-  ``0``: 清空光标之后区域
-  ``1``: 清空光标之前区域
-  ``2``: 清空整行

参考阅读
--------

   -  https://zhuanlan.zhihu.com/p/69885819
   -  https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
   -  https://en.wikipedia.org/wiki/ANSI_escape_code
