---
title:  Pandoc使用
data:   2018-9-6 11:51:41
mathjax:  false
tags:
    - Pandoc
categories:
    - Context
---

# pandoc 转换 Markdown 到其他格式

通过 Pandoc 可以将 Markdown 转换为许多格式, 例如 PDF, Docx, 或者 html 与 tex.

一般来说, 可以使用命令行参数

```sh	
pandoc --from=markdown --to=docx --output=/path/to/output.docx input.md
```

这是一个完整的命令行参数表达, 但实际上, 只需要输入 `input.md -o /path/to/output.docx`, pandoc 也能从文件后缀名自动识别文件格式, 并将输出文件放在指定路径.

转换 `docx` 非常简单, 基本上不需要什么设置.

如果转换 `html`, 要知道, 如果没有 `--standalone` 参数 (或其短形式 `-s`) 生成的 `html` 文档是没有 `<html>` 和 `<head>` 这些标签内容的. 在浏览器中会以乱码的形式呈现, 并且毫无样式. (因为没有设定 `charset` 与引用 CSS). 加上了 `--standalone` 参数, 就会生成较完整的 `html` 文档. 如果需要引入自定义的样式, 使用 `--css=URL` 指定 CSS 文件的链接.

## HTML

## PDF

## TeX

# pandoc 行内公式

参考: [Issue #2976](https://github.com/jgm/pandoc/issues/2976)

pandoc 在转换行内公式的时候, 不能在公式的 `$` 符号内测紧贴空格. 否则 `$ ... $` 将不会被识别为数学环境. 例如:

```
$ E = m c^2 $    # 这个不会被识别为公式
$E = m c^2 $     # 这个也不会
$ E = m c^2$     # 同上
$E = m c^2$      # 只有公式紧贴$, 才会被识别为公式
```

据 issue 讲, 这是为了不将诸如 `This one costs $5, and that one costs $6` 这样的句子误识别为公式环境.

# pandoc 指定资源路径

参考: [Issue #3342](https://github.com/jgm/pandoc/issues/3342)

使用 `pandoc` 转换 Markdown 文档时, 会自动导入嵌入的图片, 如果是在线图片或者以绝对路径引用的图片不会有问题. 但是如果是以相对路径引用的图片, 则会无法找到.

原因是 Pandoc 以运行时所处的目录为相对路径的起始, 要指定资源路径, 使用 `--resource-path=DIR` 选项.

如果使用相对路径, 路径的输入格式应为 `first/second/last/example.jpg`, 而不能在路径的开始输入 `/`. 否则会被识别为绝对路径.

`/first/second/last/example.jpg` 会寻找 `/first/second/last/example.jpg`; `first/second/last/example.jpg` 则会寻找 `sourcedir/first/second/last/example.jpg`, `sourcedir` 是通过 `--resource-path=` 指定的.

这个功能是在较新的版本中出现的. 如果使用的 pandoc 是 Anaconda 提供的, 需要手动升级( Anaconda 的 pandoc 才 v1.19). 如果环境变量中 `Anaconda/Script` 在自己安装的 pandoc 的目录之前, 就会使用其提供的 pandoc ...
