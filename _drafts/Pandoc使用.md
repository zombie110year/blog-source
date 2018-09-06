---
title:  Pandoc使用
data:   2018-9-6 11:51:41
mathjax:  false
tags:
    - Pandoc
categories:
    - Context
---

# 帮助文件

<iframe src="/assert/resources/pandoc/pandoc.help.txt.html" style="width=800px; height=500px"></iframe>

# pandoc 指定资源路径

参考: [Issue #3342](https://github.com/jgm/pandoc/issues/3342)

使用 `pandoc` 转换 Markdown 文档时, 会自动导入嵌入的图片, 如果是在线图片或者以绝对路径引用的图片不会有问题. 但是如果是以相对路径引用的图片, 则会无法找到.

原因是 Pandoc 以运行时所处的目录为相对路径的起始, 要指定资源路径, 使用 `--resource-path=DIR` 选项.

如果使用相对路径, 路径的输入格式应为 `first/second/last/example.jpg`, 而不能在路径的开始输入 `/`. 否则会被识别为绝对路径.

`/first/second/last/example.jpg` 会寻找 `/first/second/last/example.jpg`; `first/second/last/example.jpg` 则会寻找 `sourcedir/first/second/last/example.jpg`, `sourcedir` 是通过 `--resource-path=` 指定的.
