---
comments: true
title: latex2png
tags: latex
date: 2019-11-10 18:28:40
---

# 配置 latex -> pdf -> png 工具链

在编辑一些文档时，可能有用 latex 编译公式，转化成位图，插入文档的需求。有这么一条工具链的话，可以将这一套流程自动化，有利于简化工作流程。

<!-- more -->

需要安装的程序有 texlive、imagemagick、ghostscript。

1. texlive 是一个流行的 latex 发行版，可以将 tex 源码编译为 pdf
2. imagemagick 是一个图形库，可以进行多种格式的图像转换与编辑。
3. ghostscript 是 PostScript（PDF） 的解析器，在将 pdf 转换为图片时，imagemagick 需要依赖此库。

对于 Windows 系统，可以使用 [scoop](https://scoop.sh) 安装除了 texlive 以外的软件，texlive 可以到 [清华大学镜像站](https://mirrors.tuna.tsinghua.edu.cn/) 下载安装包。

```powershell
# powershell
scoop install imagemagick ghostscript
```

## 配置 imagemagick 的 ghostscript 依赖

在 imagemagick 的 delegates.xml 配置文件中，配置了多种外部工具的使用规则，例如，在涉及到 PostScript 的场合，会调用 `&quot;@PSDelegate@&quot;` 工具，例如：

```xml
<delegate decode="pdf" encode="ps" mode="bi" command="&quot;@PSDelegate@&quot; -q -dQUIET -dSAFER -dBATCH -dNOPAUSE -dNOPROMPT -dMaxBitmap=500000000 -dAlignToPixels=0 -dGridFitTT=2 -sDEVICE=ps2write -sPDFPassword=&quot;%a&quot; &quot;-sOutputFile=%o&quot; -- &quot;%i&quot;"/>
```

但是根据 imagemagick 的内部规则，将 `"@PSDelegate@"` 转换成了 `gswin32c` 程序，而安装的 ghostscript 是 64 位的，提供的可执行文件是 `gswin64c`。不过 ghostscript 和 32 位版提供了相同的名为 `gs` 的程序，我们在配置文件中进行编辑，将 `"@PSDelegate@"` 替换成 `gs` 就好。

## 示例

示例 latex 文件为

```tex
% main.tex
\documentclass[preview]{standalone}
\usepackage{amsmath}
\begin{document}
$$ E = mc^2 $$
\end{document}
```

经过以下流程将其编译

```powershell
xelatex main.tex
magick -density 300 main.pdf -quality 100 -trim main.png
```

imagemagick 的这几个参数分别表示

- `-density 300` density 表示密度，这里指像素线密度，每英寸 300 像素
- `-quality 100` 质量，从 0~100，100 表示无损
- `-trim` 表示裁剪，只留下存在文字的矩形区域

imagemagick 的参数会分成 input 和 output 两个组，这点需要注意。
