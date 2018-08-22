---
title: 'Tips'
date: 2018-08-22 17:31:53
categories: Tips
---

# 在ConEmu中启动PowerShell执行特定命令

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

<!--more-->

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

