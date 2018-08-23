---
title: 'Tips'
date: 2018-08-23 22:14:26
categories: Tips
---

# 映射自定义域名到 GitHub Page

0. 首先, 需要自己拥有一个域名, 在域名服务商处购买 (买国内的需要实名认证, 但是不推荐买国外的, 因为.)
0. 其次, 需要在 DNS 解析服务商处建立域名映射
0. 最后, 需要在 GitHub 仓库中添加 CNAME 文件, 使其接受映射. 

如果映射域名为 `blog.example.com`, 则 CNAME 文件内容为

```
blog.example.com
```

注意, CNAME 文件中只能有一个域名.

## 添加 HTTPS

添加 HTTPS 协议需要拥有 SSL 证书.

> date:2018-08-23 22:14:26

<!--more-->

# 检查翻墙VPS是否被封的办法

## 首先, `ping` 测试.

- 检查能否 `ping` 通.

## 其次, 端口测试

国内端口测试:

[站长工具/port](http://tool.chinaz.com/port)

国外端口测试:

[Open Port Finder](https://www.yougetsignal.com/tools/open-ports/)

> date:2018-08-23 03:39:16

# 更换Hexo主题的背景图


将喜欢的背景图放到 `project-->themes-->next-->source-->images` 目录下。
打开 `project-->themes-->next-->source-->css-->_custom-->custom.styl` 文件，加入代码

```
body { background:url(/images/imagename.jpg);}
```

重新编译项目就OK了。

[参考](http://www.lieeber.com/2016/05/15/Hexo%E4%BD%BF%E7%94%A8%E4%B8%8A%E7%9A%84%E4%B8%80%E4%BA%9B%E5%B0%8Ftips/#%E6%9B%B4%E6%8D%A2next%E4%B8%BB%E9%A2%98%E7%9A%84%E8%83%8C%E6%99%AF)

> date:2018-08-22 18:48:02

# PowerShell 中的转义字符

PowerShell 使用反引号作为转义字符;

```
所以如果要在终端中使用反引号, 就打两个反引号就好了
```

> date:2018-08-22 18:07:10

# ~/.ssh/config 配置

```
Host <hostname>
        HostName <domain or IP adress>
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa # 使用的私钥
        Port 22         # 如果使用其他端口, 自行设置
        User <登陆的用户名>
```

之后就可以直接使用 `ssh <hostname>` 登陆了.

> date:2018-08-22 13:13:42

# Linux BBR

内核版本必须大于 4.9.

[升级内核](https://www.google.com/search?q=Linux+升级内核)

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

> date:2018-08-21 21:56:46

# Android 刷机包结构?

> date:2018-08-21 10:01:46

# TODO: Vim 内置命令

- 打开模式
- 分栏操作
- 打开, 切换编辑文件

> date:2018-08-21 01:28:04

# Python @ Windows 如何处理字符编码

读到内存中的字符串都是Unicode编码吗?

只有在IO时才会编码解码?

> date:2018-08-20 18:08:19

