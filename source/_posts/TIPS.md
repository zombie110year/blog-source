---
title: 'Tips'
date: 2018-08-28 20:05:52
categories: Tips
---

# Python 文档翻译

https://pythoncaff.com/docs/tutorial/3.7.0

> date:2018-08-28 20:05:52

<!--more-->

# encode, decode

```
str   --encode()--> bytes
bytes --decode()--> str
```


> date:2018-08-28 15:33:37

# VsCode中取正则表达式的子表达式

```
$number
```

> date:2018-08-27 18:23:27

# Vim

添加折叠 za
打开折叠 zo
关闭折叠 zc

> date:2018-08-27 00:22:28

# Vscode 调试 Python模块时的 launch.json 设置

```
            cwd: 模块所在路径,
            module: ModuleName,
            args: [],
```

> date:2018-08-25 16:57:29

# locate找不到数据库的解决办法

`updatedb` 指令生成数据库

> date:2018-08-25 00:05:02

# FireFox config 设置

about:config页面:

```
view_source.editor.external             允许使用外部编辑器
view_source.editor.path                 编辑器路径
security.enterprise_roots.enabled       固定根证书
```

> date:2018-08-24 20:40:31

# Linux 用户, 用户组 权限管理

指定 /usr/sbin/nologin 使用户无法登陆 shelll

useradd userdel usermod

groupadd groupdel groupmod

passwd

> date:2018-08-24 03:59:13

# Linux 添加 sudoer

 编辑 `/etc/sudoers`

```sh
chmod 600 /etc/sudoers    #获取写权限
echo 'username ALL=(ALL) ALL' >> /etc/sudoers
chmod 200 /etc/sudoers
```

```
username ALL=(ALL:ALL) ALL
        可切换至所有用户, 用户组, 可使用所有命令
```

> date:2018-08-24 02:30:19

# CSS 选择器


`.` 选择类 `class`

`#` 选择 `id`


> date:2018-08-24 01:49:01

# PowerShell rm

可以向 -Exclude (忽略) 传递多个值, 使用逗号 , 分割. -Include 同理.

> date:2018-08-24 00:22:24

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

但是这效果...... 应该需要改 CSS 把 post 部分弄宽一点吧... 但是不会改... 暂时放弃.

![Snipaste_2018-08-24_01-36-38.png](https://i.loli.net/2018/08/24/5b7ef0c9cb183.png)

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

