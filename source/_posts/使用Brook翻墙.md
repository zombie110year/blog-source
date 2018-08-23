---
title: 使用Brook翻墙
date: 2018-07-24 18:12:38
tags:
  - Brook
  - 翻墙
categories:
  - 日常
---

<!--more-->

# 部署翻墙工具 Brook

[Brook@GitHub](https://github.com/txthinking/brook)

## 租赁 VPS

在国内, 要租赁到一个外国 VPS 还是比较麻烦的, 在付款方式上就能拦住不少人.

我选择的是 vultr 这个服务商, 因为他支持使用 PayPal 甚至 支付宝 付款.

[![Vultr-Billing.png](https://i.loli.net/2018/07/24/5b56e6795aa58.png)](https://i.loli.net/2018/07/24/5b56e6795aa58.png)

只是为了翻墙的话, 购买倒数第二 \$5/mon 五美元每月的套餐即可. 虽然有更便宜的 \$2.5/mon 但是这个服务器将无法分配到公网 IPv4 地址, 只有 IPv6...

### 测试 VPS 连接稳定性与速度

首先用 `ping` 的方式测试 vultr 各机房的网络状况.

vultr 机房一览:

|地理位置|域名|
|:--:|:--|
|Tokyo|[hnd-jp-ping.vultr.com](hnd-jp-ping.vultr.com)|
|Singapore|[sgp-ping.vultr.com](sgp-ping.vultr.com)|
|Amsterdam|[ams-nl-ping.vultr.com](ams-nl-ping.vultr.com)|
|Paris|[par-fr-ping.vultr.com](par-fr-ping.vultr.com)|
|Frankfurt|[fra-de-ping.vultr.com](fra-de-ping.vultr.com)|
|London|[lon-gb-ping.vultr.com](lon-gb-ping.vultr.com)|
|New York|[nj-us-ping.vultr.com](nj-us-ping.vultr.com)|
|Chicago|[il-us-ping.vultr.com](il-us-ping.vultr.com)|
|Dallas|[tx-us-ping.vultr.com](tx-us-ping.vultr.com)|
|Atlanta|[ga-us-ping.vultr.com](ga-us-ping.vultr.com)|
|Los Angeles|[lax-ca-us-ping.vultr.com](lax-ca-us-ping.vultr.com)|
|Miami|[fl-us-ping.vultr.com](fl-us-ping.vultr.com)|
|Seattle|[wa-us-ping.vultr.com](wa-us-ping.vultr.com)|
|Silicon Valley|[sjo-ca-us-ping.vultr.com](sjo-ca-us-ping.vultr.com)|
|Sydney|[syd-au-ping.vultr.com](syd-au-ping.vultr.com)|

下面这个脚本会将这些机房的域名挨个 ping 20次, 使用 python3 运行它. 不是我不提供操作系统自带的脚本, 只是因为我不会 bash 编程, 也不会 PowerShell 或 Batch. 不过幸好 Python 有 os 与 sys 模块可以调用外部命令.

- (Windows PowerShell) `Start-Job -ScriptBlock {python3 ./ping-vultr.py >> ./ping-vultr-out.txt}` 将这个脚本放到后台运行, 输出重定向至 `ping-vultr-out.txt` 文件. (实测发现在 Windows 下后台无法运行, 一开启则停止, 使用绝对路径也不行, 不知道是什么问题, 还是使用前台进程吧, 大不了多开个窗口) 
- (Linux) 使用 `nohup python3 ./ping-vultr.py >> ./ping-vultr-out.txt &` 将这个脚本放到后台运行, 输出重定向至 `ping-vultr-out.txt` 文件.
	- 注意, 需要将第 15 行的 `os.system("ping " + domains[a] + " -n 20")` 改为 `os.system("ping " + domains[a] + " -c 20")`

```py
# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
# 创建一个列表, 储存 vultr 各机房的域名.
names = ["Tokyo", "Singapore", "Amsterdam", "Paris", "Frankfurt", "London", "New York",
         "Chicago", "Dallas", "Atlanta", "Los Angeles", "Miami", "Seattle", "Silicon Valley", "Sydney", ]
domains = ["hnd-jp-ping.vultr.com", "sgp-ping.vultr.com", "ams-nl-ping.vultr.com", "par-fr-ping.vultr.com", "fra-de-ping.vultr.com", "lon-gb-ping.vultr.com", "nj-us-ping.vultr.com",
           "il-us-ping.vultr.com", "tx-us-ping.vultr.com", "ga-us-ping.vultr.com", "lax-ca-us-ping.vultr.com", "fl-us-ping.vultr.com", "wa-us-ping.vultr.com", "sjo-ca-us-ping.vultr.com", "syd-au-ping.vultr.com"]
j = 0
while j < 14:
    print("\n\n========================")
    print("正在 ping 位于 \"%s\" 的机房" % names[j], end='\n')
    sys.stdout.flush()
    os.system("ping " + domains[j] + " -n 20")
    j = j + 1
print("Done\a")
```

从结果中选择一个连接成功次数最多, 丢包率最小的区域, 购买此处机房.

## 部署 Brook 服务

Brook 开发了各个平台的版本, 随便选择一个熟悉的操作系统即可. 我这里选择了 Ubuntu 18.04, 因为我日常使用的就是它. 如果你不差钱的话, 也可以选择 Windows Server ( $16/mon 呢 😏)

### 安装 Brook

部署 brook 可以先到 Github 项目主页 [txthinking/Brook](https://github.com/txthinking/brook) 下载相关的可执行文件.

64 位桌面 Linux 系统一般下载 arm64 版本

```sh
wget "https://github.com/txthinking/brook/releases/download/v20180707/brook_linux_arm64"
```

下载完成之后, 直接得到一个可执行文件 (Go 语言编译得到的文件都是这样.) , 可以先将其重命名 `mv ./brook_linux_amd64 ./brook`
之后可以将其链接到 `*/bin` 文件夹, 以便在全局使用 `brook` 指令控制 brook 的运行. 否则你必须 `cd` 到 brook 所在的文件夹才能操作.
注意文件是否有可执行权限, 如果没有, 使用 `chmod +x ./brook` 给它添加可执行权限.

另一种方法, 在 snap 商店中已经提供了 brook 程序, 直接下载安装即可. 我知道在 Ubuntu 18.04 有 snap 商店, 其他发行版不知道有没有.

```sh
sudo snap install brook
```

### 运行 Brook

brook 在安装完成之后, 就可以使用 `brook <args>` 启动运行, 最简单的方法是

```sh
nohup brook server -l :port -p password &
```

- `server` 参数, 表示将其作为服务运行
- `-l :port` 参数将 `brook` 运行到服务器的某个端口, 将 `port` 替换为任意一个空闲端口即可.
- `-p password` 设置一个密码.
- `nohup` 是一个 Linux 系统指令, 将进程放到 shell 之外运行, 否则你一断开 ssh , 包括 brook 在内的所有在此 shell 中运行的程序都会停止.
- 命令最末尾的 `&` 符号表示后台运行.

Brook 还有其他的运行模式. 比如 `raw Socks5`, `shadowsocks` 等. 具体可以看[项目Wiki](https://github.com/txthinking/brook/wiki).

根据我的了解, Sock5 是一种网络协议, ,它的工作就是把 A 机器接受/发送的数据原封不动地传输给 B 机器. 对于翻墙来说, 因为此协议没有对数据进行加密和混淆, 被 GFW 抓住封 IP 是必然的, 对于翻墙来说没什么用. 而 [Shadowsocks](https://github.com/shadowsocks/shadowsocks) 作者已经喝茶, 代码已被删除, 虽然有其他的分支保留了下来, 但是最近的代码更新也隔了好几个月了. 我在 V2ex 论坛上听说(原谅我地址已经找不到了) SS 的加密混淆特征已经被 GFW 掌握, IP 封锁越来越迅速了. 所以使用 SS 的效果可能会很差. 不知道 Brook 的 ShadowSocks 模式和原 Shadowsocks 有什么区别, 但是我认为这种方式可能会比较危险.

### 系统配置: 端口与防火墙

注意, 如果你的系统有防火墙, 需要允许 brook 通过设置的端口, 并且需要同时允许 TCP/UDP 端口.

例如 Ubuntu 使用的防火墙是 `ufw` , 使用以下指令对 `9999` 端口(就是你运行 brook 使用的端口) 放行:

```sh
sudo ufw allow 9999
sudo ufw allow 9999/tcp
sudo ufw allow 9999/udp
```

## 使用 Brook

### Windows GUI

在 GitHub 项目主页上下载时经常遇到莫名失败, 并且速度奇慢无比, 我好不容易下载好了, 在这里放一个度盘吧. (不保证最新) 事实上, 这里提到的使用方法对应的可执行文件我都放到了一个压缩包里, 上传到度盘.

解压密码是: 执掌好运的黑黄之王

PS: 我可喜欢这本小说了.😀

[密码: 3dpu](https://pan.baidu.com/s/1iXs5S_2i5m2_IZQT_0R66A)

该 GUI 界面傻瓜式操作, 将对应值填进输入栏里, 然后点击 Save 就可以用了. 在托盘区会有一个小钥匙的图标, 右键 `troggle` 可以开关. 不过 GUI 程序没有设计作为服务端的功能.

![Brook Windows GUI 界面](https://i.loli.net/2018/07/13/5b48411dba980.png)

### Android GUI

一样的, 安装了 apk 包, 把服务器 IP 地址, 端口, 用户名和密码一填, 点击"开始" 就可以用了. 

### Linux CLI

Brook 没有提供 Linux 下的 GUI 程序, 只能通过命令行使用. 不过对于 Linux 用户来说并不是什么难事. Brook 各种意义上都非常简单.

```sh
nohup brook client -l 127.0.0.1:1080 -i 127.0.0.1 -s server_address:port -p password >> ./brook.log 2>&1 &
```

这将把 brook 运行时的信息输出到当前目录下的 brook.log 文件, 虽然我从来没看过, 但是如果出了问题, 有这个文件应该能有所帮助. 命令行里的 `2>&1` 表示把 stderr 也输出到 stdout 流中.

## 设置 systemd 守护进程

使用 Brook 的过程中, 我经常是隔 2~3 天就发现 brook 这个进程在 VPS 上被结束掉了. 正在研究利用 systemd 进程监控守护的方法.

[TODO:挖坑待填]