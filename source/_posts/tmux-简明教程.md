---
title: tmux 简明教程
date: 2019-04-09 21:54:47
tags:
    - Tmux
categories:
    - Linux
---

# Tmux 介绍

Tmux 是一个可在 Linux, MacOS 中运行的终端复用工具. 最直观的效果就是将终端一个屏幕划分成多个屏幕使用.

Tmux 的划分涉及到四个层次:

1. Server
2. Session
3. Window
4. Pane

其中, 一个 Linux 主机只能运行一个 Server, 其他的则是按照层次有着 一对多 的关系:

1. 一个 Server 上可运行多个 Session
2. 一个 Session 可包含多个 Window
3. 一个 Window 可被划分为多个 Pane

看看下面这个示意图:

![Tmux Intro](/assert/img/tmux-intro.webp)

<!--more-->

tmux 的配置文件为 `~/.tmux.conf`

# tmux 一般配置

```conf
# 重设 prefix 键
set -g prefix C-x
unbind C-b

# 模仿 Vim 键位
bind-key k select-pane -U
bind-key j select-pane -D
bind-key h select-pane -L
bind-key l select-pane -R
```

> `<prefix>` 是 tmux 的快捷键前缀, 大多数功能键都是以它开始, 默认为 Ctrl+b, 在上面的配置文件中被修改为 Ctrl+x (用过 Emacs 的都懂)
> `C-` 表示 Ctrl 键, `M-` 表示 Alt 键.

# pane 相关的操作

操作 | 指令
-|-
水平分割，创建新 pane | prefix + %
竖直分割，创建新 pane | prefix + "
在 pane 间切换 | prefix + o，或 prefix + 方向键
删除 pane | 在 panel 中的 shell 里输入 exit 即可
切换 pane 的全屏/非全屏 | prefix + z
调整 pane 的大小 | prefix + C-方向键
调整 pane 的大小(一次 5 个单位) | prefix + M-方向键
显示 pane 编号 | prefix p
按号码跳转至 pane | prefix 号码

<!-- # Window(TODO) -->

# Session

将当前 session 转移到后台运行: `<prefix> d`

重新进入后台 session:

```sh
    tmux a  # 进入上一个 session
    tmux attach-session -t <session-id> # 进入指定的 session
```

给 session 重命名

```sh
    tmux rename-session -t <session-di> new-id
```

例如已有 session

```sh
    tmux list-session
```

> 参考:
> - https://gist.github.com/MohamedAlaa/2961058
> - http://mingxinglai.com/cn/2012/09/tmux/
