---
title:  PyLib-asciimatics
data:   2018-10-15 18:31:20
mathjax:  false
tags:
    - null
categories:
    - null
---

- [asciimatics](https://github.com/peterbrittain/asciimatics)
- [asciimatic-doc](https://asciimatics.readthedocs.io/en/stable/)

## 常量-颜色与格式

```python
# 颜色
COLOUR_BLACK = 0
COLOUR_RED = 1
COLOUR_GREEN = 2
COLOUR_YELLOW = 3
COLOUR_BLUE = 4
COLOUR_MAGENTA = 5
COLOUR_CYAN = 6
COLOUR_WHITE = 7

# 文本格式
A_BOLD = 1
A_NORMAL = 2
A_REVERSE = 3
A_UNDERLINE = 4
```

## 创建一个 Screen

asciimatics 里的 `Screen` 不是一个图形窗口, 而是基于当前终端大小(以字符为单位) 的一片显示区域. 任何使用 asciimatics 的程序都必须由 `Screen` 开始.

一个 `Screen` 类有以下方法:

```python
class asciimatics.screen.Screen(height, width, buffer_height, unicode_aware):
    """用于跟踪屏幕基本状态的类. 这构造了必要的资源以允许我们执行 ASCII 动画.

    这是一个抽象类, 当您调用 wrapper() 时, 它将为您构建正确的具体类. 如果需要, 您可以使用 open() 和 close() 方法对结构进行更精细的控制并整理.
    
    注意, 你需要为你的屏幕缓冲区定义需求的高度, 如果你计划使用任何将会垂直滚动的效果, 这非常重要. 它必须足够大才能处理所选效果的完整滚动
    
    不要直接调用此构造函数."""

    def centre(text, y, colour=7, attr=0, colour_map=None):
    """适用可选的颜色和属性使指定行 `y` 上的文本居中

参数:

    - `text`    将打印的单行文本
    - `y`       文本开头的行数 (y 坐标)
    - `color`   要显示的文本的颜色 (支持的颜色见 TODO:
    - `attr`    要显示的文本的单元格属性
    - `colour_map` 多色文本的颜色/属性列表"""

```

```python
from asciimatics.screen import Screen
```

# 参考

- [Create TUI on Python](medium.com/@bad_day/create-tui-on-python-71377849879d)
- [Good Python library for a text-based interface - Raddit](www.reddit.com/r/Python/comments/5gd3jd/good_python_library_for_a_text_based_interface/)
- [asciimatic-doc](https://asciimatics.readthedocs.io/en/stable/)
