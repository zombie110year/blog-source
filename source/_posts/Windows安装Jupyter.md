---
title: Windows安装Jupyter
tags:
  - Python
  - Anaconda
  - Jupyter
categories:
  - 日常
date:
---

# 安装 Anaconda

不要从官方下载, 去清华大学镜像站, 否则你就会知道什么叫 "毛细作用"

[清华大学镜像站](https://mirrors.tuna.tsinghua.edu.cn)

在右侧导航栏有一个 获取下载链接, 在里面 "获取安装镜像"--> "应用软件" -->"Conda" 中下载对应版本.

下载完成后使用 `.exe` 安装.

# 配置软件源

[清华大学官方帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda)

# 配置环境变量

设 `$INSTALL` 为安装 `Anaconda` 的目录, 需要将以下三个路径添加到 `Path` 环境变量.

```
$INSTALL/
$INSTALL/Scripts
$INSTALL/Library/bin
```

# 配置 Jupyter Notebook

首先创建一个目录 `~/.jupyter`, 随后使用 `jupyter notebook --generate-config` 生成默认配置文件.

配置文件为 `~/.jupyter/jupyter_notebook_config.py`

在默认配置文件中, 修改默认工作目录. 配置项处于第 214 行.

随后需要生成一个密码用于登陆, 使用 `jupyter notebook password`

随后会要求在终端输入密码. 输入密码并确认一次之后, 在配置文件目录中生成 `jupyter_notebook_config.json` 文件, 其中存储了密码的 `sha1` 散列值.

使用 `jupyter notebook` 运行服务, 随后可在 `localhost:8888` 使用 `Jupyter NoteBook`. 进去之后会要求输入密码, 只需要输入设置的密码就好(别输散列值).

Enjoy! 🙂

# 修改 Jupyter Notebook 主题

[Jupyter-Themes](https://github.com/dunovank/jupyter-themes)

使用 `pip` 安装之后, 对于浏览器界面, 需要在命令行中执行命名更改主题, 所有代码参考 [这里](https://github.com/dunovank/jupyter-themes#command-line-usage).

比如我使用了

```
jt -t oceans16 -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T
#设置 oceans16 主题, 设置 fira 字体, 设置代码字体大小 13px, 设置 Cell 宽度 90% 屏幕, 设置输出块字体大小 11px, 设置工具栏可见.
```

而对于作图(ploting) 的主题, 需要在 Notebook 代码中使用

```py
from jupyterthemes import jtplot
jtplot.style(<args>)
```

Enjoy!😄

# 在远程服务器上部署 Jupyter NoteBook

就像在本地上安装并运行 Jupyter NoteBook 一样.

除此之外, 需要讲以下 Jupyter NoteBook 的用户和权限控制.