---
title:  Python setuptools
date:   2018-11-17 23:34:54
comments: true
mathjax:  false
tags:
    - Python
categories:
    - 软件
---

# 在什么情况下使用 setuptools

对一个 Python 模块/包 使用 setuptools 进行设置, 可以很方便地将其编译为命令行工具.

当然, 也方便构建,分发等步骤, 不过这些在这里暂且不谈.

要让一个 Python 功能的调用, 从 `python -m package args ...` 变成一个 `command args...`, 需要使用到 setuptools 中设置入口点 (`entry_points`) 的功能.

# 如何规划目录结构

```
/
    source_code/
        __init__.py
        __main__.py
        utiles.py
        others.py
    alone_module.py
    setup.py
    LICENSE
    README.md
    others...
```

这个目录被分为 两个 层级. 分别是 `Root package`, `source_code`

其中, 像 `setup.py`, `LICENSE` 等等文件都放在 `Root package` 中, 而 Python 的源代码, 则放在 `source_code` 目录下--注意, 这个目录里面有一个 `__init__.py`, 说明这是一个 包(`package`)

`Root package` 是 Python setuptools 使用的概念, 对于其他 Python 程序来说, 这根本不是一个包, 因为它没有 `__init__.py` 文件. 在使用 `setuptools` 的时候, 工具会从这一层目录开始, 寻找编写的 Python 包/模块.

`alone_module.py` 也在 `Root package` 这一级.

# setup 函数

## 必填参数

没有这些参数, setup 函数有可能成功运行, 但是不会达成效果.

### `packages` 

这是一个列表, 用从 `Root package` 开始的相对路径, 用和 `import` 时一样的语法填写在这个项目中的 包/模块.

比如上面的示例项目中, 分别有 `source_code`, `alone_module` 分别一个包和一个模块, 那么 `packages` 就应该是这样的内容.

```python
setup(
    ...
    packages=["source_code", "alone_module"],
    ...
)
```
