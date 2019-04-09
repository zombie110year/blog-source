---
title:  使用 Sphinx 制作文档与电子书
date:   2018-11-28 11:36:55
comments: true
mathjax:  false
tags:
    - Python
    - Ebook
categories:
    - 日常
---

Sphinx 是一个用于生成 Python 文档的工具, 但是也可以用来制作电子书. 本文记录使用该工具的一些经验.

# 首先使用 Sphinx 的自动配置工具

在准备好的工作目录下, 使用 `sphinx-quickstart` 将会弹出一堆文本, 并让你在其中选择要使用的配置, 一般情况下, 只需要手动修改两项, 其他保持默认即可. 让我们来看看 Sphinx 询问了我们哪些问题吧.

```
Welcome to the Sphinx 1.8.1 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .           # 选择当前工作目录为项目根目录

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y
# 是否将源文件(使用 .rst 或 .md 标记语言写的文档)和生成文件(html 或 epub, pdf 等)
# 分开放置在不同的目录

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:
# 对于模板或静态目录(文件不被解析渲染), 设它们的前缀为 `_`

The project name will occur in several places in the built documentation.
> Project name: Learn-Sphinx
> Author name(s): Zombie110year
> Project release []:
# 分别是 项目名, 作者名, Project release 是指项目发布版本, 根据实际项目来填.


If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: zh_CN
# 选择项目语言, 默认是英语, 用 zh_CN 表示简体中文, 可以在上面那个链接看支持的语言以及其表示代码

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:
# 文档文件后缀, 只有拥有这些后缀的文件才会被解析, 在当前使用的版本(v1.8.1)中只能
# 接受 .rst 与 .txt 后缀. 要解析 Markdown, 需要安装额外的插件 recommonmark, 这个稍后再讲.

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:
# 这个是主文件, 对于 html, 就是指 index.html 能够被浏览器直接默认显示的. 建议保持默认.

Indicate which of the following Sphinx extensions should be enabled:
# 接下来就是插件配置

> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: n
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: y
> Create Windows command file? (y/n) [y]: y

Finished: An initial directory structure has been created.

You should now populate your master file .\source\index.md and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

就算在 quickstart 中有选项不满意, 也可以在接下来的 `conf.py` 中修改.

# 如何规划目录结构

在运行了如上的 `sphinx-quickstart` 程序后, 目录下出现了以下文件/目录:

```
├─build
└─source
    ├─_static
    ├─_templates
    |  conf.py
    |  index.rst
  Makefile
```

在根目录下设置了 `Makefile` 便于使用 make 工具自动构建, 而配置文件和索引则放在了 source 目录下.

# 插件介绍

# toctree

在 source 目录下添加 .rst 文件, 但是如果要在编译项目后从首页 (index.html) 进行访问, 还需要在 index.rst 中将这个文件添加到 `toctree` 中. 在原始的 index.rst 中, 应当有如下 toctree.

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:
```

要在 toctree 中添加一个文件, 应当在上面那个 toctree 结构下空一行, 添加文件名(不需要扩展)

例如, 有一个 `example.rst` 就将 toctree 编辑为

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   example
```

如果, 在 `source` 目录中, 添加了子目录, 将文档放在子目录里了, 那么, 只需要在原来 `example` 里面按相对于 `index.rst` 的路径填就可以了, 例如 `/source/text/example.rst` 就填:

```
.. toctree::
   :maxdepth: 2

   text/example
```

## toctree 参数

toctree 下的 `:maxdepth: 2`, `:caption: Contents:` 等就是它的参数, 可以选用的参数有:

- `:maxdepth: n` 将目录的标题深度设为 n. 意思是 example 文件为目录的根标题, 在这个标题下, 会建立文件中的 1, 2, ..., n 级标题的索引.
- `:numbered:` 给标题自动编号.
- `:caption: xxx`

# 更改 html 页面主题

默认的 html 页面看起来并不是很好看, 可以使用 pip 安装 `sphinx_*_theme` 等包, 然后在 `conf.py` 中引用, 就可以使用更多的主题.

例如 [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/latest/) 这个受很多人欢迎的主题.

```python
# 下载
pip install sphinx_rtd_theme

# conf.py 中配置
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
```

# reStructureText 标记语言

Sphinx 默认使用 rst 标记语言, 要能够处理 Markdown 还需要额外的渲染器, 而且在了解一番过后, 发现 rst 支持的内容比 Markdown 更丰富, 于是决定学习一下.

## 标题

x 级标题分别对应 `<hx>...</hx>`.

rst 中各级标题使用符号衬在文字下一行, 并且, 符号的数目应不少于文字数目. 对于中文等宽字符, 一个字符对应两个普通符号.

注意, rst 并不在意使用的符号类型, 只需要是 "相同符号衬托文字" 就会被解析为标题, 并根据符号的出现顺序与嵌套结构划分标题层级.

一般来讲, 会用以下符号来标注标题层级.

```
一级标题
########

二级标题
********

三级标题
========

四级标题
--------

五级标题
^^^^^^^^

六级标题
""""""""
```

以上是章节标题, 还有一种标题是 "文档标题", 对应 html 标签 `<title>` 或 `<subtitle>`. 和章节标题类似, 文档标题只是用两行相同符号包裹文字. 这个貌似和主题有关, `sphinx_rst_theme` 把多余的标题解析成 `<h7>` `<h8>` 了.

```
======
主标题
======

------
副标题
------
```

## 段落

这一点 rst 几乎和 md 一样, 都是由空行划分的段落. 只不过, rst 中, 缩进也是控制段落的一个因素, 相同层级的段落, 缩进应当是一样的. 段落的缩进, 会影响渲染后文字的缩进.

```
这是一个 reStructureText 段落.

这是第二个 reStructureText 段落.

    这个段落被缩进了一下.
```

## 列表

和 Markdown 的列表标记差不多

```
* 无序列表第一位
* 无序列表第二位
  也可以换行写, 只需要保持相同的缩进

  * 也可以嵌套, 但是需要空一行, 并且增加一级缩进.

0. 有序列表
1. 有序列表第二项
2. 编号乱跳是不行的, 只能按顺序来. (如果把前面的序号从 2 变成 3 或其他任何不是 2 的数字, 就会报错, 并且不会被解析为列表的下一项, 而是直接解在上一项的后面.)


#. 自动编号会接在同一缩进的有序列表下, 除非有其他段落隔断.

比如我这里就随便输了一个段落进行隔断.

#. 自动编号
```

## 代码块

这下面是一个 C 语言的代码块. 只需要一个 `::` 符号, 在之后空一行, 并缩进一级后编辑代码.

可以指定代码高亮模式, 默认是 Python 代码的高亮模式.

```
::

    #include <stdio.h>
    int main()
    {
        printf("Hello\n");
        return 0;
    }
```

要指定高亮模式, 应使用 `codeblock` 指令.

```
.. codeblock:: c
   :linenos:

    #include <stdio.h>
    int main()
    {
        printf("Hello\n");
        return 0;
    }
```

## 引用图片

使用 `image` 指令. 开头两个点, 空一格, 输入 `image`, 然后连用两个冒号 `::` 再空一格, 输入到图片的路径, 可以使用相对路径或绝对路径, 相对路径是相对于文档文件的. 可以在下面添加属性, 所有属性和 HTML 中的图片属性是一样的.

```
.. image:: path/to/picture
   :alt: 示例图片
```

## 其他元素

### 内联样式

```
*斜体*

**粗体**

``代码``
```

### 水平线

```
至少四个 ``-`` 将会被解析为水平线. (``<hr />`` 标签)

----
```

# 参考

[Docutils 中文文档](https://docutils-zh-cn.readthedocs.io/zh_CN/latest/)
