---
comments: true
title: Windows安装Jupyter
tags:
  - python
  - anaconda
  - jupyter
categories: 日常
date: 2018-08-23 16:12:38
---


安装 Anaconda
=============

不要从官方下载, 去清华大学镜像站, 否则你就会知道什么叫 “毛细作用”

`清华大学镜像站 <https://mirrors.tuna.tsinghua.edu.cn>`__

在右侧导航栏有一个 获取下载链接, 在里面 “获取安装镜像”–> “应用软件”
–>“Conda” 中下载对应版本.

下载完成后使用 ``.exe`` 安装.

配置软件源
==========

`清华大学官方帮助 <https://mirrors.tuna.tsinghua.edu.cn/help/anaconda>`__

配置环境变量
============

设 ``$INSTALL`` 为安装 ``Anaconda`` 的目录, 需要将以下三个路径添加到
``Path`` 环境变量.

::

   $INSTALL/
   $INSTALL/Scripts
   $INSTALL/Library/bin

配置 Jupyter Notebook
=====================

首先创建一个目录 ``~/.jupyter``, 随后使用
``jupyter notebook --generate-config`` 生成默认配置文件.

配置文件为 ``~/.jupyter/jupyter_notebook_config.py``

比较在意的配置项有:

::

   工作目录            c.NotebookApp.notebook_dir 项
   监听的IP地址        c.NotebookApp.ip 项, 默认为 localhost, 无法在非本机访问.
   使用的端口          c.NotebookApp.port 项
   使用的密码          c.NotebookApp.password 项, 应使用由密码生成的 sha1 散列值.
                       也就是 jupyter_notebook_config.json 中的 password 的值. 如果在 .py 中配置, .json 就不需要了.
   是否自动打开浏览器  c.NotebookApp.open_browser 项

需要生成一个密码用于登陆, 使用 ``jupyter notebook password`` 命令行,
或者在 Python 环境中使用内部函数生成密码.

.. code:: py

   import notebook.auth
   notebook.auth.passwd()

随后会要求在终端输入密码. 输入密码并确认一次之后, 在配置文件目录中生成
``jupyter_notebook_config.json`` 文件, 其中存储了密码的 ``sha1`` 散列值.

使用 ``jupyter notebook`` 运行服务, 随后可在浏览器中访问
``localhost:8888`` (或自定义 IP:端口) 使用 ``Jupyter NoteBook``.
进去之后会要求输入密码, 只需要输入设置的密码就好(别输散列值).

Enjoy! 🙂

修改 Jupyter Notebook 主题
==========================

`Jupyter-Themes <https://github.com/dunovank/jupyter-themes>`__

使用 ``pip`` 安装之后, 对于浏览器界面, 需要在命令行中执行命名更改主题,
所有代码参考
`这里 <https://github.com/dunovank/jupyter-themes#command-line-usage>`__.

比如我使用了

::

   jt -t oceans16 -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T
   #设置 oceans16 主题, 设置 fira 字体, 设置代码字体大小 13px, 设置 Cell 宽度 90% 屏幕, 设置输出块字体大小 11px, 设置工具栏可见.

而对于作图(ploting) 的主题, 需要在 Notebook 代码中使用

.. code:: py

   from jupyterthemes import jtplot
   jtplot.style(<args>)

Enjoy!😄

在远程服务器上部署 Jupyter NoteBook
===================================

TODO: 应使用 JupyterHub, 此版本才有多用户控制. 其安装配置与本地的
Jupyter Notebook 基本相同.

虽然如此, 但是最基本的 Jupyter Notebook 也可以开放到网络中,
只不过只能使用同一个用户而已:

修改配置文件 ``jupyter_notebook_config.py`` 中的 ``c.NotebookApp.ip``
项. 其默认值为 ``localhost``, 也就是 ``127.0.0.1`` 之类的本机 IP,
是无法通过其他机器访问的, 将其修改为开放的 IP 地址,
就能在局域网进行访问.

如果要在公网访问, 除了需要公网 IP 之外, 还需要有认证的 SSL 证书并且使用
https. 否则浏览器会因为安全问题将它拦下来…
