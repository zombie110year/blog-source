---
comments: true
title: 使用Brook翻墙
date: 2018-07-24 18:12:38
tags:
  - brook
  - 翻墙
categories: 教程
---


部署翻墙工具 Brook
==================

`Brook@GitHub <https://github.com/txthinking/brook>`__

租赁 VPS
--------

在国内, 要租赁到一个外国 VPS 还是比较麻烦的, 在付款方式上就能拦住不少人.

我选择的是 vultr 这个服务商, 因为他支持使用 PayPal 甚至 支付宝 付款.

.. figure:: https://i.loli.net/2018/07/24/5b56e6795aa58.png
   :alt: Vultr Billing

只是为了翻墙的话, 购买倒数第二 $5/mon 五美元每月的套餐即可.
虽然有更便宜的 $2.5/mon 但是这个服务器将无法分配到公网 IPv4 地址, 只有
IPv6…

测试 VPS 连接稳定性与速度
~~~~~~~~~~~~~~~~~~~~~~~~~

首先用 ``ping`` 的方式测试 vultr 各机房的网络状况.

vultr 机房一览:

============== =================================================================
地理位置       域名
============== =================================================================
Tokyo          `hnd-jp-ping.vultr.com <https://hnd-jp-ping.vultr.com>`__
Singapore      `sgp-ping.vultr.com <https://sgp-ping.vultr.com>`__
Amsterdam      `ams-nl-ping.vultr.com <https://ams-nl-ping.vultr.com>`__
Paris          `par-fr-ping.vultr.com <https://par-fr-ping.vultr.com>`__
Frankfurt      `fra-de-ping.vultr.com <https://fra-de-ping.vultr.com>`__
London         `lon-gb-ping.vultr.com <https://lon-gb-ping.vultr.com>`__
New York       `nj-us-ping.vultr.com <https://nj-us-ping.vultr.com>`__
Chicago        `il-us-ping.vultr.com <https://il-us-ping.vultr.com>`__
Dallas         `tx-us-ping.vultr.com <https://tx-us-ping.vultr.com>`__
Atlanta        `ga-us-ping.vultr.com <https://ga-us-ping.vultr.com>`__
Los Angeles    `lax-ca-us-ping.vultr.com <https://lax-ca-us-ping.vultr.com>`__
Miami          `fl-us-ping.vultr.com <https://fl-us-ping.vultr.com>`__
Seattle        `wa-us-ping.vultr.com <https://wa-us-ping.vultr.com>`__
Silicon Valley `sjo-ca-us-ping.vultr.com <https://sjo-ca-us-ping.vultr.com>`__
Sydney         `syd-au-ping.vultr.com <https://syd-au-ping.vultr.com>`__
============== =================================================================

用下面这个脚本:

.. gist:: zombie110year/c0e26f4b9d7376489688fb264e3d9e3b

先把这个文件保存到本地的 ``vultr_ping.py``，或者直接在 REPL
中运行，在按照文档注释中的例子用就可以了。 因为 ``show_ping`` 函数是用
ANSI Color Sequence
将结果在终端里打印成表的，如果终端不支持，可能会很难看。

部署 Brook 服务
---------------

Brook 开发了各个平台的版本, 随便选择一个熟悉的操作系统即可. 我这里选择了
Ubuntu 18.04, 因为我日常使用的就是它. 如果你不差钱的话, 也可以选择
Windows Server ( $16/mon 呢 😏)

安装 Brook
~~~~~~~~~~

部署 brook 可以先到 Github 项目主页
`txthinking/Brook <https://github.com/txthinking/brook>`__
下载相关的可执行文件.

64 位桌面 Linux 系统一般下载 arm64 版本

.. code:: sh

   wget "https://github.com/txthinking/brook/releases/download/v20180707/brook_linux_arm64"

下载完成之后, 直接得到一个可执行文件 (Go 语言编译得到的文件都是这样.) ,
可以先将其重命名 ``mv ./brook_linux_amd64 ./brook`` 之后可以将其链接到
``*/bin`` 文件夹, 以便在全局使用 ``brook`` 指令控制 brook 的运行.
否则你必须 ``cd`` 到 brook 所在的文件夹才能操作.
注意文件是否有可执行权限, 如果没有, 使用 ``chmod +x ./brook``
给它添加可执行权限.

另一种方法, 在 snap 商店中已经提供了 brook 程序, 直接下载安装即可.
我知道在 Ubuntu 18.04 有 snap 商店, 其他发行版不知道有没有.

.. code:: sh

   sudo snap install brook

运行 Brook 服务端
~~~~~~~~~~~~~~~~~

brook 在安装完成之后, 就可以使用 ``brook <args>`` 启动运行,
最简单的方法是

.. code:: sh

   nohup brook server -l :port -p password &

-  ``server`` 参数, 表示将其作为服务运行
-  ``-l :port`` 参数将 ``brook`` 运行到服务器的某个端口, 将 ``port``
   替换为任意一个空闲端口即可.
-  ``-p password`` 设置一个密码.
-  ``nohup`` 是一个 Linux 系统指令, 将进程放到 shell 之外运行,
   否则你一断开 ssh , 包括 brook 在内的所有在此 shell
   中运行的程序都会停止.
-  命令最末尾的 ``&`` 符号表示后台运行.

Brook 还有其他的运行模式. 比如 ``raw Socks5``, ``shadowsocks`` 等.
具体可以看\ `项目Wiki <https://github.com/txthinking/brook/wiki>`__.

根据我的了解, Sock5 是一种网络协议, ,它的工作就是把 A
机器接受/发送的数据原封不动地传输给 B 机器. 对于翻墙来说,
因为此协议没有对数据进行加密和混淆, 被 GFW 抓住封 IP 是必然的,
对于翻墙来说没什么用. 而
`Shadowsocks <https://github.com/shadowsocks/shadowsocks>`__
作者已经喝茶, 代码已被删除, 虽然有其他的分支保留了下来,
但是最近的代码更新也隔了好几个月了. 我在 V2ex
论坛上听说(原谅我地址已经找不到了) SS 的加密混淆特征已经被 GFW 掌握, IP
封锁越来越迅速了. 所以使用 SS 的效果可能会很差. 不知道 Brook 的
ShadowSocks 模式和原 Shadowsocks 有什么区别,
但是我认为这种方式可能会比较危险.

系统配置: 端口与防火墙
~~~~~~~~~~~~~~~~~~~~~~

注意, 如果你的系统有防火墙, 需要允许 brook 通过设置的端口,
并且需要同时允许 TCP/UDP 端口.

例如 Ubuntu 使用的防火墙是 ``ufw`` , 使用以下指令对 ``9999``
端口(就是运行 brook 时设定的端口) 放行:

.. code:: sh

   sudo ufw allow 9999
   sudo ufw allow 9999/tcp
   sudo ufw allow 9999/udp

使用 Brook 客户端
-----------------

Windows GUI
~~~~~~~~~~~

该 GUI 界面傻瓜式操作, 将对应值填进输入栏里, 然后点击 Save 就可以用了.
在托盘区会有一个小钥匙的图标, 右键 ``troggle`` 可以开关. 不过 GUI
程序没有设计作为服务端的功能.

.. figure:: https://i.loli.net/2018/07/13/5b48411dba980.png
   :alt: Brook Windows GUI 界面

   Brook Windows GUI 界面

实际上，目前我更喜欢使用命令行版客户端。用法和 `Linux
CLI <#linux-cli>`__ 几乎一样，只是不能用 Linux 特性：

.. code:: powershell

   brook client -l 127.0.0.1:1080 -i 127.0.0.1 -s server_address:port -p password

之后得一直开着命令行窗口。

或者用 PowerShell 提供的进程管理指令：

.. code:: powershell

   Start-Process -FilePath brook.exe -ArgumentList "client","-i","localhost","-l","localhost:1080","-s","远程:9999","-p","********" -WindowStyle Hidden

这样将不会有窗口。

Android GUI
~~~~~~~~~~~

一样的, 安装了 apk 包, 把服务器 IP 地址, 端口, 用户名和密码一填,
点击“开始” 就可以用了.

Linux CLI
~~~~~~~~~

Brook 没有提供 Linux 下的 GUI 程序, 只能通过命令行使用. 不过对于 Linux
用户来说并不是什么难事. Brook 各种意义上都非常简单.

.. code:: sh

   nohup brook client -l 127.0.0.1:1080 -i 127.0.0.1 -s server_address:port -p password >> ./brook.log 2>&1 &

这将把 brook 运行时的信息输出到当前目录下的 brook.log 文件,
虽然我从来没看过, 但是如果出了问题, 有这个文件应该能有所帮助. 命令行里的
``2>&1`` 表示把 stderr 也输出到 stdout 流中.

设置 systemd 守护进程
---------------------

使用 Brook 的过程中, 我经常是隔 2~3 天就发现 brook 这个进程在 VPS
上被结束掉了. 正在研究利用 systemd 进程监控守护的方法.

[TODO:挖坑待填]
