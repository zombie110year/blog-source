---
title:  PyPDF2
date:   2018-11-16 19:16:19
comments: true
mathjax:  false
tags:
    - Python
categories:
    - 日常
---

# 读写一个 PDF 文件

```python
import PyPDF2

book = PyPDF2.PdfFileReader("./test.pdf")
# 实例化一个 PdfFileReader 类, 将 PDF 文档转化为 Python 对象
editable_pdf = PyPDF2.PdfFileWriter()
# 但是只有 PdfFileWriter 类可以进行编辑修改.
editable_pdf.cloneDocumentFromReader(book)
# 可以使用 cloneDocumentFromReader 方法, 从 PdfFileReader 哪里复制内容

"""
之后对 editable_pdf 进行一系列操作
"""

with open("./test2.pdf", "wb") as foo:
    # 需要用二进制模式打开(新建) 一个文件, 才能把修改的文件写入.
    editable_pdf.write(foo)
```

# 使用 PyPDF2 添加书签

## `addBookmark` 函数

```python
addBookmark(title, pagenum, parent=None, color=None, bold=False, italic=False, fit='/Fit', *args)
```

- `title` 书签名
- `pagenum` 书签所在页码
- `parent` 该书签的父书签
- `color` 一个 RGB 元组, 取值范围为 0~1 的浮点数.
- `bold`, `italic` 是否适用粗体/斜体
- `fit` 跳转到页面后的缩放模式, 可以有以下选项:

|模式|需要额外参数|效果|
|:-:||:-|:-|
| `/Fit ` | No additional arguments |  |
| `/XYZ ` | [left] [top] [zoomFactor] |  |
| `/FitH ` | [top] |  |
| `/FitV ` | [left] |  |
| `/FitR ` | [left] [bottom] [right] [top] |  |
| `/FitB ` | No additional arguments |  |
| `/FitBH` | [top] |  |
| `/FitBV` | [left] |  |

该方法有一个返回值, 就是被添加的书签实例, 属于 `PyPDF2.generic.Destination` 类.

用这种方法得到它后, 可将其作为 `parent` 参数的值传入.

## 批量添加书签

在实际使用时, 还是先手打一个目录, 然后再对这个目录文件进行解析, 并调用 `addBookmark` 方法, 将书签批量添加到 PDF 文件中.

先编写一个解析器吧. 将手打的目录文件解析为 `addBookmark` 使用的参数字典.

已经做了一个 Python Package, 见 [GitHub](https://github.com/zombie110year/)
