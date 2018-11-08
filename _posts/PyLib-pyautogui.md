---
comments: true
title:  使用 PyAutoGUI 操纵键鼠
data:   2018-10-06 20:33:01
mathjax:  false
tags:
    - Python
categories:
    - 日常
---

[PyAutoGUI 文档](https://pyautogui.readthedocs.io/en/latest/)

下载 [PyAutoGUI](https://pypi.org/project/PyAutoGUI/):

```sh
pip install pyautogui
```

`PyAutoGUI` 中提供 操作光标, 键盘的函数, 除此之外, 还提供简单的图形界面工具, 以及截屏功能.

<!--more-->

# 移动光标

在操作光标之前, 应当先获取当前屏幕的尺寸, `PyAutoGUI` 使用的单位都是像素, 屏幕尺寸其实就是当前分辨率.

使用 `size()` 函数获取屏幕分辨率, 返回值为元组.

```python
pyautogui.size() -> (X, Y)
```

如果要获取当前光标的位置, 使用 `position` 函数, 这个函数会返回当前光标的坐标.

```python
pyautogui.position() -> (x, y)
```

---

移动到屏幕的绝对位置. 单位为像素 (px), 屏幕的尺寸为分辨率.

```python
# 移动到绝对位置
moveTo(x=None, y=None, duration=0.0, tween=<function linear at 0x000002341DF5EE18>, pause=None, _pause=True)
# 移动到相对位置
moveRel(xOffset=None, yOffset=None, duration=0.0, tween=<function linear at 0x000002341DF5EE18>, pause=None, _pause=True)
```

- 参数 `x`, `y` 就是坐标, 这个坐标系是从屏幕左上角开始的, 原点处于左上角, 向右为 X 轴, 向左为 Y 轴.
- `duration` 意为持续时间, 其实是指从原位置移动到新位置这个过程所花费的时间, 在两次移动中, 光标是有轨迹的.

要设置的参数只有以上三项, `tween` 参数指向一个控制移动效果的函数, 定义在包的 `tweens.py` 模块中. 至于 `pause`, `_pause`, 文档中没有说明, 就不要动了.

`moveRel` 函数是根据当前光标所处的位置移动一个相对的坐标, 除了坐标设置之外的参数与 `moveTo` 相同.

需要注意: 如果将光标移动至原点, 也就是 `(0,0)` 坐标处, `PyAutoGUI` 会抛出错误:

```
FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to upper-left corner. To disable this fail-safe, set pyautogui.FAILSAFE to False.
```

如果要禁止这项检查, 需要将变量 `pyautogui.FAILSAFE` 赋值为 `False`.

# 鼠标点击

点击, 有 `click` 函数.

```python
click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=<function linear at 0x000002341DF5EE18>, pause=None, _pause=True)
```

- `x`, `y` 绝对坐标, 尽管有移动光标的函数, 但是点击事件依然需要传入绝对坐标, 点击之前会将光标移动到该坐标.
- `clicks` 点击次数.
- `interval` 点击间隔, 就是每两次点击之间等待的时间.
- `botton` 点击的按键, 可以用字符串的形式设置, 或者传入整数:(中键是指按下滚轮, 不是滑动滚轮)
    - `'left' : 1`
    - `'middle' : 2`
    - `'right' : 3`

---

`mouseDown` 是按住, 不松开, `mouseUp` 则是松开, 至于 `dragTo` 以及 `dragRel`, 分别是拖曳(按住左键)至绝对位置和相对位置.

其参数和 `click` 基本相同, 不再赘述.

```python
mouseUp(x=None, y=None, button='left', duration=0.0, tween=<function linear at 0x000001B615244E18>, pause=None, _pause=True)
mouseDown(x=None, y=None, button='left', duration=0.0, tween=<function linear at 0x000001B615244E18>, pause=None, _pause=True)
dragTo(x=None, y=None, duration=0.0, tween=<function linear at 0x000001B615244E18>, button='left', pause=None, _pause=True, mouseDownUp=True)
dragRel(xOffset=0, yOffset=0, duration=0.0, tween=<function linear at 0x000001B615244E18>, button='left', pause=None, _pause=True, mouseDownUp=True)
```

# 滑动滚轮

```python
scroll(clicks, x=None, y=None, pause=None, _pause=True)
```

- `clicks` 滚动的像素数目, 正值向上, 负值向下. 像素级的控制!
- `x`, `y` 滑动滚轮时光标所在位置

# 按下键盘

```python
press(keys, presses=1, interval=0.0, pause=None, _pause=True)
```

- `keys` 参数可以是字符串或者列表(元组), 字符串应为键名, 所有可用的键名储存在 `pyautogui.KEYBOARD_KEYS` 中; 也可为列表, 其中的键将依次按下.
- `presses` 按键重复次数
- `interval` 按键间隔

---

按键也有 `Down` 与 `Up` 两个过程, 也提供了对应的函数.

```python
keyDown(key, pause=None, _pause=True)
keyUp(key, pause=None, _pause=True)
```

不过在 `keyDown` 与 `KeyUp` 中的 `key` 参数只能是一个键(字符串).

---

```python
typewrite(message, interval=0.0, pause=None, _pause=True)
```

- `message` 可以是长字符串或列表, 对于长字符串中的每一个字符, `typewrite` 会依次按下对应的字母(符号)键位, 不过在这种时候, 不能输入特殊键, 例如 `left`(代表左方向键) 不能用, 要键入特殊按键, 就得使用列表了, 在使用列表的情况下, 每一项都得是 `pyautogui.KEYBOARD_KEYS` 中的元素.
- `interval` 控制每一次按键的间隔.

```python
hotkey(*args)
```

`hotkey` 函数提供热键功能, 向 `*args` 传入要按下的键(列表), 就会依次按下对应键位, 只要所有键位被按下才会松开.

例如

```python
pyautogui.hotkey('ctrl', 'c')
```

就会按下 <kbd>Ctrl</kbd> + <kbd>C</kbd> 键.

# 简单的图形界面

```python
alert(text='', title='', button='OK', root=None, timeout=None)
# 显示一个简单的弹窗, 含有一个按钮(显示内容由 `button` 设置), 按下按钮返回
# button 参数设置的值.

confirm(text='', title='', buttons=['OK', 'Cancel'], root=None, timeout=None)
# 类似于 alert, 不过拥有多个按钮, 按下返回对应值

prompt(text='', title='', default='', root=None, timeout=None)
# 弹出输入框, 并有两个按钮 'OK' 和 'Cancel', 按下 'OK' 返回输入内容, 按下
# 'Cancel' 返回 None

password(text='', title='', default='', mask='*', root=None, timeout=None)
# 类似 prompt, 不过输入框的字符会被 `mask` 覆盖
```
