---
title: "Python 小程序: SimpleTTYNote"
date:   2018-10-15 16:09:36
mathjax:  false
tags:
    - Python
    - TUI
categories:
    - Python
---

TUI ( Text-based User's Interface) 文本用户界面是使用文本, 字符来实现的一种用户界面.
和 GUI (Graphic User's Interface) 图形用户界面相比, 文本用户界面可以在终端中运行, 并且不需要图形窗口, 拥有更少的依赖和更低的性能需求等等.

(而且, 在终端里面感觉很酷)

本次开发主要是想要实现一个简单的笔记记录器:

```
+-----------Tip-----------+                            Simple Note
|                         | Title       功能: 以 Markdown 的格式存储简单的笔记, 
+-------------------------+                   保存在指定目录中, config.py 中指定
|                         | Note              ----------------------------------
|                         |                   # Title
|                         |
|                         |                    Note
|                         |
|                         |                   > date: YYYY-MM-DD hh:mm:ss
|                         |                   ----------------------------------
|                         |                   Tab 切换               Enter 结束
+-------------------------+                             Ctrl+C 放弃
```

要求:

0. 显示如上 TUI 于终端中.
0. 解析命令行参数, `-h` 时显示右侧帮助文本, 直接运行时则只显示左侧界面.
0. 允许在 `title` 与 `note` 中输入纯文本(并实时显示)
0. 使用 `Tab` 让光标在 `title` 与 `note` 间切换
0. 按下 `Enter` 键完成输入.
0. 将写入的文本存入文件中(此功能和 [此 Python 脚本](/assert/python/tipadd.py) 一样)

准备编写为以下模块:

```
main.py         # 主模块
config.py       # 配置文件 (就定义一个 FILE_PATH 变量)
    utils/
        __init__.py
        display.py      # 编写界面
        interactive.py  # 交互规则
        save.py         # 保存文件
```

# 界面显示
