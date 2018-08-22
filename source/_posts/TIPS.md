---
title: 'Tips'
date: 2018-08-22 18:48:02
categories: Tips
---

# 更换Hexo主题的背景图


将喜欢的背景图放到 `project-->themes-->next-->source-->images` 目录下。
打开 `project-->themes-->next-->source-->css-->_custom-->custom.styl` 文件，加入代码

```
body { background:url(/images/imagename.jpg);}
```

重新编译项目就OK了。

[参考](http://www.lieeber.com/2016/05/15/Hexo%E4%BD%BF%E7%94%A8%E4%B8%8A%E7%9A%84%E4%B8%80%E4%BA%9B%E5%B0%8Ftips/#%E6%9B%B4%E6%8D%A2next%E4%B8%BB%E9%A2%98%E7%9A%84%E8%83%8C%E6%99%AF)

> date:2018-08-22 18:48:02

<!--more-->

# PowerShell 中的转义字符

PowerShell 使用反引号作为转义字符;

```
所以如果要在终端中使用反引号, 就打两个反引号就好了
```

> date:2018-08-22 18:07:10

# 在ConEmu中启动 PowerShell 执行启动动作

我安装了 `oh-my-posh` 后, 想要在启动 PowerShell 时自动生效, 但是因为一些问题, VsCode 上的终端会出现光标错位的现象.

我希望在 ConEmu 启动时执行自定义的 `Start-ConEmu` 函数, 而在 VsCode 下就使用原生 PowerShell.

task 设置中, 如果直接设置

```
powershell Start-ConEmu
```

会导致执行完命令就退出. 需要加上参数 `-NoExit`

```
powershell -NoExit Start-ConEmu
```

这样, 执行完我自定义的函数后, PowerShell 就不会退出了.

> date:2018-08-22 17:31:53

# ~/.ssh/config 配置

```
Host <hostname>
        HostName <domain or IP adress>
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa # 使用的私钥
        User <登陆的用户名>
```

之后就可以直接使用 `ssh <hostname>` 登陆了.

> date:2018-08-22 13:13:42

# Linux BBR

内核版本必须大于 4.9.

检查是否已开启:

```sh
uname -r # 查看内核版本
sysctl net.ipv4.tcp_avaliable_congestion_control # 查看内核是否启用 BBR 算法
lsmod | grep bbr    # 如果有 tcp_bbr 说明启动成功
```

通过写入配置文件开启 BBR

```sh
echo net.core.default_qdisc=fq >> /etc/sysctl.conf
echo net.ipv4.tcp_congestion_control=bbr >> /etc/sysctl.conf
```

> date:2018-08-21 22:11:40

# Keepass 自动输入, 终端登陆ssh格式:

```
ssh {USERNAME}@{URL}{ENTER}{PASSWORD}{ENTER}
```

> date:2018-08-21 21:56:46

# Android 刷机包结构?

> date:2018-08-21 10:01:46

# TODO: Vim 内置命令

- 打开模式
- 分栏操作
- 打开, 切换编辑文件

> date:2018-08-21 01:28:04

# 今晚研究变量的作用域

> date:2018-08-20 18:10:22

# Python @ Windows 如何处理字符编码

读到内存中的字符串都是Unicode编码吗?

只有在IO时才会编码解码?

> date:2018-08-20 18:08:19

