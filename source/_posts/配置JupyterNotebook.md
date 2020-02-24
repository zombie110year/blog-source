---
comments: true
title:  配置 Jupyter Notebook
date:   2018-09-15 22:39:08
mathjax:  false
tags:
    - python
    - anaconda
    - jupyter
categories: 记录
---

# 概览

在 [安装了 Jupyter Notebook](/2018/08/Windows安装Jupyter/) 之后, 使用了大约一周的时间(从安装到现在, 中间有很长一段时间是闲置的), 越发感觉到 Jupyter Notebook 的强大之处了:

## 用Cell区分代码块与文本

在 Jupyter Notebook 中, 是用 Cell 来作为文件的基本单位, 对于每一个 Cell, 可以设定独立的属性, 比如设定为

- Code          代码块
- Markdown
- Raw NBConvert 纯文本, 在 Jupyter 中不会对此 Cell 的内容进行计算处理, 但是把 notebook 转换为其他格式, 比如 html 或 pdf 时, 会将此 Cell 按照对应规定转换.
- Heading       标题, 但是根据官方的建议, 应当在 Markdown 中使用对应语法创建标题, 此选项为历史遗留.

因为 Jupyter NoteBook 将代码与说明文本区分得明明白白, 并且其 Markdown Cell 支持所有 Markdown 特性, 甚至可以使用 MathJax 渲染数学环境! 这就是任何其他形式的 Python 编辑器无法做到的了. 一边在 Code 中编写代码, 一边还能在 Markdown 中进行说明, 插入表格,图片,链接,数学公式等等一系列注释无法做到的表达方式.

## 实时输出

在 Jupyter Notebook 中, 其代码的运行结果可以紧跟在代码块后输出. 在每一个代码块前, 都有一个 `In [xxx]` 标识符, 如果有输出, 则输出块前也会有一个 `Out[xxx]` 并且, 如果使用 matplotlib 等画图工具, 还能直接在网页上显示图像!

如果在进行一系列处理后, 代码产生的返回值没有赋值给一个变量, 那么此值就会直接输出. 也可以使用 `print` 等方法将值输出, 但是不会有 `Out[xxx]` 标记. 作图也是如此.

## 多种格式导出

原生的 Jupyter Notebook 就可以将 `.ipynb` 文件导出为 `markdown`, `html`, `pdf`, `tex` 等多种格式的文档, 并且同样区分不同的 Cell.

如果文档中有图, 那么在导出为 `markdown`, `tex` 时, 会导出一个压缩包, 图片在文本中以相对路径的方式引用.

如果导出 `pdf`, 需要调用系统上安装的 LaTeX 引擎, 如果要成功渲染中文还需要一番折腾.

也可以导出为 `.py` 脚本, 这会去除非 Code 的 Cell.

<!--more-->

# JupyterNotebook配置

对于 [上篇文章](2018/08/Windows%E5%AE%89%E8%A3%85Jupyter/#%E9%85%8D%E7%BD%AE-Jupyter-Notebook) 提到的美化, 需要注意的是最好不要把整个界面的颜色都换掉, 这样的话在作图或者进行其他操作时会很丑...

使用原本的界面风格即可, 最多改改字体就好了.

再总结一下上篇文章的配置项:

> 在使用 `jupyter notebook --generate-config` 生成模板之后, 在文件最后添加配置项即可. 修改模板中的项会导致配置项混乱, 难以找到, 是真的傻呼呼的...

|配置项|作用|备注|
|:----:|----|----|
|`c.NotebookApp.notebook_dir='D:/jupyter'`|配置工作目录|默认为启动jupyter的 cwd 路径|
|`c.NotebookApp.ip='0.0.0.0'`|使用IP|默认为本机 hosts 文件设置的 localhost, 一般为 127.0.0.1, 是其他机器无法访问的. 如果要在网络中开放, 设置为 `0.0.0.0` 或 `*` 可以通过任何该机器连接的 IP 地址访问|
|`c.NotebookApp.port=18888`|使用端口|浏览器访问 ip:port 来使用 jupyter notebook|
|`c.NotebookApp.open_browser=False`|是否自动打开浏览器|在启动 jupyter notebook 时是否自动打开浏览器|
|`c.NotebookApp.password='sha1:kf454f641sd31df1a2f...'`|登陆密码, 用于单用户|其实最好将生成的密码存放在同目录的 jupyter_notebook_config.json 中|

注意, 由于配置文件就是一个 `.py` 文件, 所以可以在里面进行 Python 运算, 可以动态地设置可变配置, 比如经常变动的公网 IP 等等... 还可以设置动态密码...

## 安装插件

使用以下代码安装并启用插件管理器:

```sh
pip install jupyter_contrib_nbextensions
pip install jupyter_nbextensions_configurator
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user
```

重启 Jupyter Notebook 后, 就可以在主页面看到额外的标签了.

推荐启用的插件:

- Nbextensions dashboard tab 插件管理标签页, 如果禁用了, 就只能丢掉鼠标, 去找配置文件了...
- AutoSaveTime  看名字就是必需品~
- Code prettify 在工具栏中会出现一个锤子图标, 点击会格式化代码.
- Collapsible Headings  折叠 Cell (以 Markdown title 分级)
- Codefolding in Editor 折叠代码块
- Table of Contents     目录
- Variable Inspector    变量监视器

不推荐启用的插件:

- LaTeX environments for Jupyter        如果启用它, 会导致 MathJax 反复渲染公式, 根本停不下来, 导致页面胡乱跳动...
- Live Markdown Preview         实时预览会导致 Markdown Cell 在编辑时占用双倍空间, 如果文档写长了, 就会很难受...

其他插件没怎么使用, 所以不评价.

# JupyterNotebook版本控制

由于 `.ipynb` 是一个二进制文件, 所以版本控制相对困难, 不过可以用一定的方法规避:

1. 为一个 `.ipynb` 创建一个目录
2. 在目录下创建许多 `.py` 文件或其他资源
3. 在 `.ipynb` 中使用 magic 指令 `%load ...` 来导入 `.py` 文件的内容.

这样, 就可以控制外面的 `.py` 文件的版本, 而 `.ipynb` 文件基本上不会有太多的更改...

# 使用在线Jupyter服务

[微软 Azure Jupyter](https://notebooks.azure.com/)

# 参考

- [把Jupyter Notebook配置成Coding神器](http://resuly.me/2017/11/03/jupyter-config-for-windows/)
- [如何优雅地使用jupyter？ - 陈乐群的回答 - 知乎](https://www.zhihu.com/question/59392251/answer/403124614): 渲染矢量图
- [如何优雅地使用jupyter？ - 品颜完月的回答 - 知乎](https://www.zhihu.com/question/59392251/answer/272305529): 快捷键与 `%matplotlib inline`
- [如何优雅地使用jupyter？ - SHAN的回答 - 知乎](https://www.zhihu.com/question/59392251/answer/177708041): 去除 Code Cell
