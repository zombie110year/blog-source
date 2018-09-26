---
title: Android使用Termux
tags:
  - Linux
  - Termux
categories:
  - 日常
date: 2018-08-22 23:22:44
---

Termux 是运行在安卓手机上的一个终端模拟器, 不需要 root 权限.

其文件系统相对于安卓根目录的路径如下:

- 根目录为 `/data/data/com.termux/files/`
- 其用户家目录在 `/data/data/com.termux/files/home/`
- 而传统 Linux 的 `/bin` ,`/etc` 等等目录都被塞进 `/data/data/com.termux/files/usr/*` 中了.

# Termux 配置

<!--more-->

```
vim
openssh
zsh
git
oh-my-zsh
```

## 基本配置

安装 Termux 后运行以下指令(可以复制粘贴):

```sh
echo "deb [arch=all,aarch64] http://mirrors.tuna.tsinghua.edu.cn/termux stable main" > /etc/apt/sources.list
apt update && apt upgrade
```

将 Termux 的软件源由 termux 官网切换到清华大学镜像.

之后下载几个必要软件:

```sh
apt install vim
apt install openssh
```

> 注: 安装完 vim 之后, 立刻在家目录下创建 `.vimrc`, 至少先设置 `set background=dark` 否则配色瞎眼.

## 配置 SSH

手机上的键盘输入极其不爽, 因为是需要找个 Linux 环境, 所以就通过在 PC 上用 SSH 远程登陆的方式进入 Termux.

安装了 `openssh` 之后就使用 `sshd` 指令开启 SSH 服务.

之后需要确认 3 条信息:

0. Termux 用户名:
  - Android 系统对每个应用都创建了一个用户便于控制权限, 这些用户名大多是 `u0_a123` 之类的格式.
  - 使用 `whoami` 指令, 这是最简单的方法. 此指令用于查询当前登陆的用户名.
  - 使用 `ps` 指令查看 termux 运行的进程, 其中就有用户名信息. 在我得知 `whoami` 之前, 我都是用这个的...
  - 使用 `id` 指令.
  - 参考链接告知的其他命令在 Termux 上不受支持.
0. SSH 服务使用的端口.
  - 一般的 Linux 使用 `:22` 作为 SSH Server 的端口, 但是 Termux 默认 SSH 端口为 `8022`.
  - 如果手机有防火墙把此端口封锁了(表现就是 Connection Refuse), 而又没有权限设置. 在 `/usr/etc/ssh/sshd_config` 文件中配置 `Port 65500` 换一个不常用的端口号.
  - 如果想知道查看 Linux 系统占用端口的命令, 它就是 `netstat -ntlp`.
0. 手机的 IP 地址.
  - `ifconfig`.

Termux 不允许使用密码登陆, 因为用户是安卓系统自动创建的, 鬼知道密码是什么. 要登陆必须配置 `authorized_keys`.

在 PC 上使用 `ssh-keygen` 生成一个新密钥, 或者用以前使用的老密钥. 将 `id_rsa.pub` 公钥内容添加到 Termux 的 `~/.ssh/authorized_keys` 中.

之后就可以使用 `ssh u0_a123 -p 8022` 登陆了. `-p` 参数指定连接端口.

# 安装 zsh 与 oh-my-zsh

`apt install zsh` 之后, 使用 `chsh -s zsh` 将登陆 Shell 切换为 zsh.

安装 [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) 之前需要安装 git 和 curl, `apt install git curl`.

之后下载并运行作者提供的安装脚本.

```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

之后使用 `ls ~/.oh-my-zsh/themes` 查看有哪些支持的主题, 编辑 `~/.zshrc` 中的 `ZSH_THEME=""` 项目, 选择喜欢的主题.

# apt 源中 `termux-*` 软件包的作用

[Termux Wiki](https://wiki.termux.com/wiki) .

```
======================= ========================================================
Package Name            Function
----------------------- --------------------------------------------------------
termux-am               Android 活动管理.
termux-api              提供操作手机硬件的一些指令.
termux-apt-repo         用于创建 Termux 包的脚本.
termux-create-package   用于在 Termux 环境下创建 .deb 软件包. 默认为 Termux 环境创建.
termux-elf-cleaner      用于清理编译程序时连接器未使用的 ELF 文件.
termux-exec             提供识别 shebang 的功能. (shebang, 脚本的特殊注释, 如: #! /bin/bash)
termux-tools            Termux 非官方工具库.
```

## termux-api

官方 Wiki 只解释了 `termux-notification` 的用法:


```
Usage:  termux-notification <options>
Options:
 --action action          action to execute when pressing the notification
 --button1 text           text to show on the first notification button
 --button1-action action  action to execute on the first notification button
 --button2 text           text to show on the second notification button
 --button2-action action  action to execute on the second notification button
 --button3 text           text to show on the third notification button
 --button3-action action  action to execute on the third notification button
 --content content        contnet to show in the notification. Read from stdin not specified here.
 --id id                  notification id (will overwrite any previous notification with the same id)
 --led-color rrggbb       color of the blinking led as RRGGBB (default: none)
 --led-on milliseconds    number of milliseconds for the LED to be on while it's flashing (default: 800)
 --led-off milliseconds   number of milliseconds for the LED to be off while it's flashing (default: 800)
 --on-delete action       action to execute when the the notification is cleared
 --priority prio          notification priority (high/low/max/min/default)
 --sound                  play a sound with the notification
 --title title            notification title to show
 --vibrate pattern        vibrate pattern, comma separated as in 500,1000,200
```

---

# 参考链接

- [Linux查询用户](https://blog.csdn.net/newdriver2783/article/details/8059368)
- [TermuxWiki](https://wiki.termux.com/wiki/Main_Page)
- [Android + Termux + SSH + Django + Ngrok 个人博客搭建过程](https://blog.csdn.net/MemoryD/article/details/81664494)
- [关于安卓手机的牛逼软件termux使用](https://www.cnblogs.com/BlogOfMr-Leo/p/7788103.html)
- [Termux中安装gcc-7/gfortran-7实操过程，安装成功可以编译Fortran,c/c++](http://www.cnblogs.com/BlogOfMr-Leo/p/8660920.html)
- [神器Termux的使用日常](https://www.jianshu.com/p/5c8678cef499)
- [在安卓上部署服务器--解决内网穿透](http://zkeeer.space/?p=96)
