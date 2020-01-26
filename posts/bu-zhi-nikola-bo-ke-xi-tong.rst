.. title: 布置 Nikola 博客系统
.. slug: bu-zhi-nikola-bo-ke-xi-tong
.. date: 2020-01-10 15:57:39 UTC+08:00
.. tags: nikola
.. category: 日常
.. link:
.. description: 初次使用 Nikola 博客系统的体验
.. type: text
.. has_math: true

.. include:: refs/aliases.ref
.. include:: refs/links.ref

.. role:: file
    :class: literal

.. sidebar:: 本文目录

    .. contents::


Nikola 博客系统的特点
#####################

之所以换用了 Nikola 博客系统，是因为它的这些特点吸引了我：

多格式解析
    除了 Markdown 以外，还支持 |a_rst| 和 |a_ipynb| 等多种格式的解析。
    这些格式相比 Markdown，有更强的表达能力和扩展功能。
    例如，|a_rst| 的域、|a_ipynb| 的代码单元胞等等。
Python 应用程序
    这个纯粹属于个人原因，因为相比 Node.js，个人对 Python 这边的工具链更熟悉，
    有能力对 Nikola 的扩展进行开发。

Nikola 的安装问题
#################

推荐使用 pipx 来安装 Nikola，这样 Python 环境比较干净。
关于一些配置，主要参考了 |l_macplay|_ 上的博文。

推荐这些文章：

*   `30 分钟搭建一个 Nikola 博客 <https://macplay.github.io/posts/30-fen-zhong-jian-li-yi-ge-nikola-bo-ke/>`_
*   `静态博客 Nikola 之写作实践 <https://macplay.github.io/posts/jing-tai-bo-ke-nikola-zhi-xie-zuo-shi-jian/>`_

简单来说，在安装好 Nikola 之后，先通过

.. code:: sh

    nikola init

来初始化项目，然后用

.. code:: sh

    nikola new_post

来新建文件进行编辑，博客系统需要的文档元数据都会预先设置好。
其中比较重要的是 :code:`.. slug` 设置，这条数据设置了输出的文章 url，
最好保持稳定，在发布后就不要修改。

数学支持
########

可以通过 |a_katex| 来实现数学支持，默认使用 MathJax，但由于太慢了，
本人不太喜欢。

在博客根目录的 :code:`conf.py` 文件中编辑:

.. code:: python

    USE_KATEX = True
    KATEX_AUTO_RENDER = r"""
    delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "\\[", right: "\\]", display: true},
        {left: "\\begin{equation*}", right: "\\end{equation*}", display: true},
        {left: "$", right: "$", display: false},
        {left: "\\(", right: "\\)", display: false}
    ]
    """

再在需要启用 |a_katex| 的文章中配置 :code:`.. has_math: true`
就可以启用 |a_katex|，不需要其他配置，可以使用 |a_rst| 的 math role 或 directive::

    .. math:: e^{i\pi} + 1 = 0

.. math:: e^{i\pi} + 1 = 0

不过由于 |a_katex| 相比 MathJax 缺少一些特性，例如 :code:`align` 环境，
而在 :code:`.. math` 域中使用的默认多行公式正是 :code:`align*` 环境，
因此在默认情况下，直接编辑的多行公式是渲染不了的，如果有使用多行公式的需求，
需要手动使用 :code:`aligned` |a_latex| 环境:

.. code:: rst

    .. math::

        \begin{aligned}
        x = \cos{t} \\
        y = \sin{t} \\
        t \in [0, 2 \pi]
        \end{aligned}

.. math::

    \begin{aligned}
    x &= \cos{t} \\
    y &= \sin{t} \\
    t &\in [0, 2 \pi]
    \end{aligned}

像 :code:`equation`, :code:`cases` 等环境也是支持的，具体的列表可以参考 |a_katex| 的 `文档 <https://katex.org/docs/supported.html>`_ 。

打造 Nikola 的新主题
####################

在 |a_rst| 中，可以使用 :code:`container` 和 :code:`class` 来快速地创建 html :code:`div` 元素，并且用相比 Markdown 直接嵌入 HTML 更好的表达能力。

为了方便地制作各种样式的 class，可以自己制作一个新的主题，在 CSS 中编写相关类的样式。
例如

.. code:: css

    .zom-banner {
        display: flex;
        justify-content: center;
        text-align: justify;
        font-size: xx-large;
    }

.. code:: rst

    .. class:: zom-banner

        Hello, Zombie110year!

.. class:: zom-banner

    Hello, Zombie110year!

如果不出意外的话，上面将是一个超大的，横穿屏幕的欢迎词。

要管理样式，可以使用 nikola 命令行：

.. code:: sh

    nikola theme -n zombie110year
    # 创建一个新的命名为 zombie110year 的主题

nikola 将会在 :code:`themes/zombie110year` 目录中创建主题所需的一切资源。

主题管理系统
------------

在 :code:`themes/zombie110year` 中，会有一个 :code:`zombie110year.theme` 文件，这是
一个 ini 格式的配置文件。需要配置以下键值对：

.. code:: ini

    [Theme]
    # 模板引擎
    engine = jinja
    # 继承关系，缺失的资源将会从父主题获取
    parent = bootstrap4-jinja
    author = Zombie110year
    author_url = https://zombie110year.top/
    license = MIT
    based_on = Bootstrap 4 <http://getbootstrap.com/>, Bootstrap 4 blog example <http://getbootstrap.com/docs/4.0/examples/blog/>
    tags = bootstrap

为了支持 jinja2 模板引擎，需要在 nikola 所在的 Python 环境中安装 Jinja2。
bootstrap 是一个流行的前端框架。在构建后，所有的 CSS 都会打包到 :file:`all-nocdn.css` 文件中去。

暂时，先从 bootblog-jinja 复制文件过来，然后在 :file:`bootblog.css` 中 :code:`@import ("custom.css")` 来引入自定的样式文件。

bootblog 是基于 bootstrap 的一个主题，可以使用 bootstrap 预先提供的样式。例如

.. container:: row

    .. class:: col-md-6

        .. code:: rst

            .. container:: row

                .. class:: col-md-6

                    左边

                .. class:: col-md-6

                    右边（col-md 将屏幕分成 12 份）

    .. class:: col-md-6

        .. container:: row

            .. class:: col-md-6

                左边

            .. class:: col-md-6

                右边（col-md 将屏幕分成 12 份）

为 Nikola 编写扩展
##################

先🕊️了。

使用 :code:`nikola --version` 确认版本，目前的最新版应当是 :code:`8.0.3`。

参考文献
########

想要在写博客时能用 bibtex 格式化参考文件。
例如

.. code:: rst

    此处参考了 :cite:`nikola-documentation`。

    .. bibgraphy::

        @misc{nikola-documentation,
            note={https://getnikola.com/theming.html},
        }

似乎没有实现此功能的库，先😴️。

Travic CI 与 GitHubPages 部署
#############################

nikola 是基于 Python 开发的应用，这个博客也可以采用 Python 的 CI 文件来自动化构建：

Travis CI 集成 Python 工程的文档为 https://docs.travis-ci.com/user/languages/python/，
参考之，编写 :code:`.travis.yml` 为

.. include:: .travis.yml
    :encoding: utf-8
    :code: yml
    :literal:
