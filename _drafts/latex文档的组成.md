---
title:  LaTeX文档的组成
data:   2018-9-5 9:33:9
mathjax:  false
tags:
    - LaTeX
categories:
    - LaTeX
---

# TeX 简介

TeX 既是一个排版引擎家族的统称, 又是对应的标记语言的名字.

TeX 家族包含 TeX, LaTeX, pdfTeX, luaTeX, XeLaTeX , ... 等等成员. 它们的功能就是将 tex 标记语言写成的源文件编译为可视可打印的文档.

TeX 是最原始的 TeX, 其作者 Donald E. Knuth (《The Art of Programming》 的作者) 使用 Plain TeX 对其元指令进行了封装， Plain TeX 是后来开发其他 TeX 引擎的基础, 但实际上, Plain TeX 是以 TeX 为内核的.

目前对中文支持最好的 TeX 引擎是 XeLaTeX.

>  XeLaTeX 工作时有两个步骤, 第一步输出中间文件, Extented DVI (.xdv), 第二步用驱动把 .xdv 转为 PDF. 缺省方式是两步一起执行, 直接输出 PDF, xdv 只在内存中露过一小脸儿. 用户也可以要求只执行第一步, 保存 xdv.
> 
>       --《雷太赫排版系统简介》 包太雷

TeX 语言和 HTML 标记语言类似:

- 都是以源文件(`.tex`:`.html`) 经过渲染引擎(`*TeX`:`浏览器`) 处理后, 生成可视文档.
- 都可以使内容与样式分离, `.html`+`.css`:`.tex`+`.cls`

## 小结

> 包老师语重心长地总结道, 数字排版有四个重要环节: 标记语言,页面描述语言,光栅图像处理器,输出设备. TeX 是最精确,最高级的面向专业排版的标记语言. TeX 家族可以划分为四个层次: 引擎,格式,宏包,驱动. 包老师通常选择 XeTeX 引擎和 LaTeX 格式.

# TeX 工程

一个 "工程", 指的是一种目录组织, 其中包含了 TeX 的源文件, 与各种资源文件. 在编译 TeX 源代码时, 引擎会以运行路径为相对根路径, 在此目录下的其他资源文件可在源码中通过 `\include{}` 语句嵌入.

例如, 一个典型的 TeX 工程有以下结构:

```
src/
        main.tex
        img/
                image1.jpg
                image2.jpg
                ...
```

在 `main.tex` 中, 可以使用 `\include{/img/image1.jpg}` 来嵌入一个图片.

# tex 文件结构

# TeX 语法结构

# 数学环境


