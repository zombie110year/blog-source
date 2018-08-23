---
title: '[PyNote]-Python模块'
tags:
    - Python
    - Note
categories:
    - Python
---

# Python 模块的目录结构

```
Module_root/            # 模块的根目录
├── __init__.py         # 每一个模块中必须要有 __init__.py 文件
├── childdir/           # 模块的一个子目录, 被称为包
│   ├── __init__.py     # 一个有效的包里必须含有 __init__.py 文件
│   ├── script1.py
│   └── scriptn.py
├── childdirn/
│   ├── __init__.py
│   ├── childdir/       # 这个目录里没有 __init__.py 文件, 不能作为包引用.
|   |   └──script.py
│   ├── script1.py
│   └── scriptn.py
├── script1.py
├── script2.py
└── scriptn.py
```

- 每一个模块中可以含有无数个 `.py` 文件, 也可以含有无数个子目录, 模块中的子目录被称为 包(`package`).
- 模块, 包, `.py` 文件都是 `模块-子模块` 的关系, 本质上都是模块, 可以引用其中任意一级.
- 一个有效的模块或者包中必须含有 `__init__.py` 文件. 
- `__init__.py` 文件中可以有代码, 也可以是一个空文件. 因为 `__init__.py` 在模块中代表该目录自身.


# 在 Python 中引用模块或包

```py
import Module_root                      # 引用整个模块
import Module_root.childdirn            # 引用模块中的一个包
import Module_root.childdir.script1     # 引用模块中的一个包的文件
from . import *                         # 引用当前目录中所有模块
```

## 引用模块时, Python 解释器做了什么

以以下目录结构为例:

具体文件已打包 [module.example.zip](/assert/repos/python/module.example.zip)

```
main/
    - subdir/
        - __init__.py
        - test.py
    - invalidir/
        - test.py
    - __init__.py
    - echo.py
    - echo_imported.py
```

其中,

- `/main/echo_imported.py` 在 `/main/__init__.py` 中引用, 而 `echo.py` 没有.
- `/main/subdir/__init__.py` 是个空文件

0. 首先, 运行模块下的 `__init__.py` 文件.
    - 同目录下的其他文件不会被执行.
    - 
0. 创建一个和模块名一致的变量, 将模块对象赋值给此变量.
    - 模块对象是模块类的一个实例.

注意:

- 当 Python 解释器直接解释执行 `.py` 文件时, 会将一个特殊变量 `__name__` 赋值为 `"__main__"`, 因此, 许多模块中都会有判断结构 `if __name__ == "__main__": test()` 方便测试.

# 编写自己的 Python 模块

TODO:

# 常用系统模块(标准库)

所有系统模块都在 [Python安装目录/Lib/](file:///C:/Python37/Lib/) 中.

- `platform`    获取操作系统平台信息.
- `sys`         操作 Python 解释器.
- `os`          操作系统接口.
- `subprocess`  子进程.
- `getopt`      解析命令行参数.
- `re`          正则表达式.
- `urllib`      网络爬虫.
- `glob`        模块提供了一个 `glob()` 函数用于用通配符搜索当前目录, 生成文件列表.
- `random`      生成随机数.