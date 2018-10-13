---
title:  PyQt5 安装与 HelloWorld
data:   2018-10-12 09:16:15
mathjax:  false
tags:
    - Python
    - Qt
categories:
    - Python
---

# PyQt5 与 sip 版本对应

使用 Anaconda3 安装包, 安装的一大堆 Python 模块中就有 PyQt5 和对应的 sip.

我安装的版本为:

```
PyQt5                              5.11.3
PyQt5-sip                          4.19.13
```

在 Windows 上使用命令 ` pip list | findstr PyQt5` 查看, 如果在 Linux 上, 那么就用 `grep` 替换命令中的 `findstr`.

# import 注意事项

如果你直接 `import PyQt5`, 会发现根本无法使用,

```
AttributeError: module 'PyQt5' has no attribute 'QtWidgets'
```

如果用 `dir(PyQt5)`, 会得到这样的结果:

```python
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_os', '_path']
```

因此, 要显性地引用相关模块:

```python
>>> import PyQt5.QtWidgets
>>> dir(PyQt5)
['QtCore', 'QtGui', 'QtWidgets', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_os', '_path', 'sip']
```

另外, 如果是使用 `from PyQt5.QtWidgets import QApplication`, pylint 会报错:

```
[pylint] E0611:No name 'QApplication' in module 'PyQt5.QtWidgets'
```

但是对程序的运行没有影响, 虽然 pylint 报错, 但是程序运行是正常的.

如果对代码检测有洁癖的话, 可以使用这种方式:

```python
import PyQt5.QtWidgets
QApplication = PyQt5.QtWidgets.QApplication
```

# 使用 pyuic5 转换 .ui 文件

`pyuic5` 和 `QtDesigner` 一样, 是 `PyQt5_tools` 的一部分, 使用 `pip` 安装, `QtDesigner` 将会被安装于 `Anaconda3/Lib/site-packages/pyqt5_tools/` 目录下, `pyuic5` 可以通过 `python.exe -m PyQt5.uic.pyuic ...` 的方式来调用, 在 `Anaconda3/Script/` 目录下也有编译的 `pyuic5.exe` 文件存在.

使用 QtDesigner 设计出的窗体布局将会以 `.ui` 格式的文件保存, 其实际上是 `.xml` 文件, 需要使用 `pyuic5` 将其编译为 `.py` 文件才能在 Python 中调用.

```sh
pyuic5 example.ui -o example.py
```

如果不指定 `-o` 参数, 输出会打印到 stdout 中, 不会存入文件.

# 一个简单的 GUI 窗口

```python
import sys
import PyQt5.QtWidgets
# from PyQt5.QtWidgets import QApplication, QWidget
QApplication = PyQt5.QtWidgets.QApplication
QWidget = PyQt5.QtWidgets.QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(1000,60)
w.move(300,300)
w.setWindowTitle('Hello World')
w.show()

sys.exit(app.exec_())
```
