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

Tmux 的划分涉及到四个层次: Server, Session, Window, Pane.

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
set -g mode-keys vi
```

> `<prefix>` 是 tmux 的快捷键前缀, 大多数功能键都是以它开始, 默认为 Ctrl+b, 在上面的配置文件中被修改为 Ctrl+x (用过 Emacs 的都懂)
> `C-` 表示 Ctrl 键, `M-` 表示 Alt 键.

# pane 相关的操作

| 操作                                 | 指令                                       | 记忆方法 |
| ------------------------------------ | ------------------------------------------ | -------- |
| 水平分割，创建新 pane                | `<prefix> %`                               |          |
| 竖直分割，创建新 pane                | `<prefix> "`                               |          |
| 在 pane 间切换                       | `<prefix> o，或` `<prefix> 方向键`         |          |
| 删除 pane                            | `<prefix> x` 或者在 shell 里执行 exit 命令 | exit     |
| 切换 pane 的全屏/非全屏              | `<prefix> z`                               | zoom     |
| 调整 pane 的大小                     | `<prefix> C-方向键`                        |          |
| 调整 pane 的大小(一次 5 个单位)      | `<prefix> M-方向键`                        |          |
| 显示 pane 编号, 并在之后输入编号跳转 | `<prefix> q <num>`                         |          |
| 交换 pane 的位置                     | `<prefix> {` 或者 `<prefix> }`             |          |

# Window

Window 是 session 之下的一个层级. 一个屏幕一次只能显示一个 Window, 在 Window 中又可以划分多个 pane.
有点类似 "标签页" 的概念.

| 操作              | 指令                         | 记忆方法       |
| ----------------- | ---------------------------- | -------------- |
| 创建新的 Window   | `<prefix> c`                 | create         |
| 列出所有 Window   | `<prefix> w`                 | window         |
| 切换 Window       | `<prefix> n` 或 `<prefix> p` | next, previous |
| 重命名当前 Window | `<prefix> ,`                 |                |
| 删除当前 Window   | `<prefix> &`                 |                |

# Session

| 操作                          | 指令         | 记忆方法 |
| ----------------------------- | ------------ | -------- |
| 将当前 session 转移到后台运行 | `<prefix> d` | daemon   |
| 列出所有 session              | `<prefix> s` | session  |
| 重命名当前 session            | `<prefix> $` |          |

由于 session 是连接 tmux 与普通 shell 的第一层概念, 因此, 也有许多操作可以通过命令行参数来进行.

重新进入后台 session:

```sh
    tmux a  # 进入上一个 session
    tmux attach-session -t <session-id> # 进入指定的 session
    tmux at -t <session-id> # at 是 attach-session 的简写
```

给 session 重命名

```sh
    tmux rename-session -t <session-di> new-id
```

列出已有 session

```sh
    tmux list-sessions
```

# tmux 子命令

tmux 子命令可以在 Shell 中使用:

```sh
    tmux <subcmd> <args> ...
```

也可以在 tmux session 中, 通过内置命令行使用:

```sh
# 按下 <prefix> : 进入内置命令行, 就像 Vim 一样
<subcmd> <args> ...
```

可用的子命令可参考文档 (`man tmux`) . 快捷键都是对这些命令的封装.
这些功能不一定会用, 因此用到了再查.

Tmux 中有一系列 `new-` `kill-` `list-` 开头的命令, 用于操作 Session, Window, pane.

# tmux 256 色

- 首先, 需要设置环境变量 `export TERM=screen-256color`
- 然后, 启动 tmux 时附加 `-2` 参数: `tmux -2 new ...`, 可以将此设为一个别名: `alias tmux='tmux -2'`.

# 查看历史输出

在 Tmux 中, 无法使用鼠标滚轮等操作滚动当前窗口以查看历史输出的信息.
但是可以在 **Copy Mode** 中查看历史输出, 并且可选择并复制其中的内容:

|     操作     | 行为                                                   |
| :----------: | ------------------------------------------------------ |
| `<prefix> [` | 进入 copy 模式                                         |
|     `q`      | 在 copy 模式中按下此键以退出                           |
|  `<space>`   | 进入选择模式                                           |
|  `<enter>`   | 复制并退出选择模式, 同时会将复制内容存储在剪贴板历史中 |
| `<prefix> ]` | 粘贴复制的内容                                         |
| `<prefix> =` | 在剪贴板历史中选择内容进行粘贴                         |

如果想要删除剪贴板历史中的某条记录, 可以选中目标记录并使用命令 `delete-buffer` 将其删除;
如果要修改目标记录, 则使用命令 `set-buffer` 将当前记录重写为输入的参数:

```
    : set-buffer "新的内容"
```

> 参考:
> - https://gist.github.com/MohamedAlaa/2961058
> - http://mingxinglai.com/cn/2012/09/tmux/
> - https://suixinblog.cn/2018/12/tmux.html
> - http://louiszhai.github.io/2017/09/30/tmux/
> - http://www.wutianqi.com/blog/3681.html

# 速查表

<script src="https://gist.github.com/zombie110year/1f02c500eae2006f2d0fd958a242aece.js"></script>
