---
title:  Linux搭建AnkiServer
data:   2018-8-24 20:11:31
mathjax:  false
tags:
    - Linux
    - Anki
categories:
    - 日常
---

<!--more-->

# 下载 AnkiServer

[AnkiServer](https://pypi.org/project/AnkiServer/2.0.6/) 基于 Python2 运行, 但幸好有人写了 Python3 的版本.

[tsudoko/anki-sync-server](https://github.com/tsudoko/anki-sync-server). 不过作者没有提供简单的安装办法, 

首先克隆 Git 仓库:

```sh
git clone https://github.com/tsudoko/anki-sync-server.git ~/anki-sync-server
```

仓库里有这些东西:

```
-rw-------    1 u0_a174  u0_a174    33.7K Aug 25 01:21 COPYING
-rw-------    1 u0_a174  u0_a174     3.1K Aug 25 01:21 README.md
drwx------    2 u0_a174  u0_a174     4.0K Aug 25 01:21 anki-bundled
-rwx------    1 u0_a174  u0_a174     2.7K Aug 25 01:21 ankisyncctl.py
drwx------    2 u0_a174  u0_a174     4.0K Aug 25 01:21 ankisyncd
-rw-------    1 u0_a174  u0_a174      303 Aug 25 01:21 ankisyncd.conf
drwx------    4 u0_a174  u0_a174     4.0K Aug 25 01:21 tests
```

接着用 pip 安装以下依赖项:

```
bs4
send2trash
pyaudio         # 这个是用于语音处理的一个库. 可以不要, 处理方法见后文.
requests
decorator
markdown
webob
```

另外, 在机器上必须有 anki 客户端, 否则 Python 会报没有 `anki` 这个模块的错误.

## 安装 pyaudio 的依赖.

先来看看安装过程中报了什么错:

```
gcc -pthread -B /root/anaconda3/compiler_compat -Wl,--sysroot=/ -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/root/anaconda3/include/python3.7m -c src/_portaudiomodule.c -o build/temp.linux-x86_64-3.7/src/_portaudiomodule.o
  src/_portaudiomodule.c:29:10: fatal error: portaudio.h: No such file or directory
   #include "portaudio.h"
            ^~~~~~~~~~~~~
  compilation terminated.
  error: command 'gcc' failed with exit status 1

  ----------------------------------------
    src/_portaudiomodule.c:29:10: fatal error: portaudio.h: No such file or directory
     #include "portaudio.h"
              ^~~~~~~~~~~~~
    compilation terminated.
    error: command 'gcc' failed with exit status 1

    ----------------------------------------
```

发现就是 GCC 编译的时候出现了缺少 `portaudio.h` 库的问题. 这个库的官网为: [portaudio.com](http://portaudio.com) 需要将文件下载到 GCC 的 lib/ 里.

先去 [下载页](http://portaudio.com/download.html) 查看最新版本. 下载之后解压.

```sh
tar -xvf XXXXXX
```

进入解压后的目录.

由于官网推荐先安装 `ALSA`, 所以先通过 `apt install libasound-dev` 安装. 之后使用目录中的 `configure` 进行配置, 配置完成就 `make`.

```sh
cd ~/portaudio
apt install libasound-dev       # 这将下载 ALSA
configure && make               # 这将编译 PortAudio 的运行库
make install                    # 这将把运行库安装到系统 /usr/local/lib
```

但是这只将运行库安装到 `/usr/local/lib` 中了, 头文件还得自己移动. 将头文件放在 `/usr/include` 中, 最好先创建对应目录.

```sh
mkdir /usr/include/portaudio && cp ~/portaudio/include/* /usr/include/portaudio
mkdir /usr/include/pablio && cp ~/portaudio/pablio/* /usr/include/pablio       # 这是 Portaudio 中的另一个装满 .h 文件的目录, 不知道干嘛的. 但还是放进去吧
```
需要将对应路径添加到编译器搜索路径.

```sh
export C_INCLUDE_PATH=/usr/include:$C_INCLUDE_PATH      # 头文件路径
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH  # 动态库路径
export LIBRARY_PATH=/usr/local/lib:$LIBRARY_PATH        # 静态库路径
```

再进行安装.

## 排除 pyaudio

[作者在GitHub上介绍了方法](https://github.com/tsudoko/anki-sync-server#running-ankisyncd-without-pyaudio)

# 配置 AnkiServer

`ankisyncd.conf`

```
[sync_app]
# change to 127.0.0.1 if you don't want the server to be accessible from the internet
host = 127.0.0.1
port = 18123            # 使用的端口
data_root = ./collections
base_url = /sync/               # 同步数据的目录, 通过 http://IP:18123/sync/ 来访问.
base_media_url = /msync/        # 同步媒体的目录.
auth_db_path = ./auth.db
# optional, for session persistence between restarts
session_db_path = ./session.db
```

# 使用 AnkiSyncd

添加用户:

```sh
ankisyncctl adduser <username>           # 添加用户, 与 anki app 上的用户保持一致
```

启动服务:

```sh
python3 -m ankisyncd ankisyncd.conf
```

注意, 克隆 anki 客户端之后注意调整目录结构, 使其与 ankisyncd 目录同级, 否则仍然会发生找不到模块的错误.

<!--
# 下载 AnkiServer

[AnkiServer](https://pypi.org/project/AnkiServer/2.0.6/) 基于 Python2 运行. 

```sh
pip2 install AnkiServer
```

# 配置 AnkiServer

0. 首先, 创建一个单独的目录, 要同步的文件存储在此.
0. 从 `python_prefix/lib/python2.X/site-packages/AnkiServer-2.X.X-py2.X.egg/examples` 复制一个配置文件模板. 不过在下载的发行版中没有发现该文件, 于是去 [GitHub 项目页](https://github.com/dsnopek/anki-sync-server) 找了. 注意有两个重要的配置文件. 使用方法如下:

> 无意间发现模板被放在这个目录下了. `/data/data/com.termux/files/usr/examples`

```ini
# example.ini 需要重命名为 production.ini 并移动到为 AnkiServer 创建的目录

[server:main]
use = egg:AnkiServer#server
host = 127.0.0.1        # 运行服务的主机 IP 地址
port = 27701            # 服务使用的端口

[filter-app:main]
use = egg:Paste#translogger
next = real

[app:real]
use = egg:Paste#urlmap
/ = rest_app
/msync = sync_app
/sync = sync_app

[app:rest_app]
use = egg:AnkiServer#rest_app
data_root = ./collections
allowed_hosts = 127.0.0.1       # 允许使用服务的客户机的 IP 地址, 可设置为 0.0.0.0 以允许任何 IP 连接.
;logging.config_file = logging.conf

[app:sync_app]
use = egg:AnkiServer#sync_app
data_root = ./collections
base_url = /sync/
base_media_url = /msync/
session_db_path = ./session.db
auth_db_path = ./auth.db
```

如果是在 Termux 中运行 AnkiServer 的话, 以下文件中的路径都要改!
不知道路径在哪里的话, 用 `locate -r XXX$` 通过正则表达式搜索. (`$` 匹配字符串末尾.)

```conf
; supervisor-anki-server.conf , 这是个监控服务的配置文件, 需要放在 supervisor/conf.d/ 目录中.
[program:anki-server]


; The command used to execute the Anki Server. If you setup a virtualenv like described
; in the README.md, then be sure to point to the "paster" command inside of it! All files
; are relative to the "directory" variable given below
; command=/usr/local/bin/paster serve production.ini
command= /data/data/com.termux/files/usr/bin/paster serve production.ini    ; 用于运行服务的命令

; This is the directory to execute the Anki Server from. All files will be relative to this
; directory. This includes arguments to the "command" above and in the configuration files.
directory=/var/lib/anki

; This is the user the Anki Server will run as. It should have permission to read and write
; the Anki collections referred to in the configuration file, but, for security reasons it
; shouldn't be "root"!
user=u0_174     ; 需要配置为运行 AnkiServer 的 Linux 用户名

autostart=true
autorestart=true
redirect_stderr=true

; Sometimes necessary if Anki is complaining about a UTF-8 locale. Make sure
; that the local you pick is actually installed on your system.
;environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8,LC_LANG=en_US.UTF-8
```

但是我的手机没法使用 `supervisor` 而现在大多数 Linux 系统都使用 `systemd` 了. 所以这个文件的东西看看就好.

## 小结

需要注意的几条配置:

```ini
# 在 production.ini 中
allowed_hosts = 0.0.0.0       # 允许使用服务的客户机的 IP 地址, 可设置为 0.0.0.0 以允许任何 IP 连接.
host = 127.0.0.1        # 运行服务的主机 IP 地址
port = 18909            # 服务使用的端口

# 在 supervisor-anki-server.conf 中
# 这项内容可在配置 systemd 时用于参考
; command=/usr/local/bin/paster serve production.ini
command= /data/data/com.termux/files/usr/bin/paster serve production.ini    ; 用于运行服务的命令
```

# 使用 AnkiServer

Anki server 主要通过 `/data/data/com.termux/files/usr/bin/ankiserverctl.py` 文件来运行.

添加用户:

```sh
ankiserverctl.py adduser <username>           # 添加用户, 与 anki app 上的用户保持一致
```

测试服务:

```sh
ankiserverctl.py debug
```

启动服务:

```sh
ankiserverctl.py start
```

停止服务:

```sh
ankiserverctl.py stop
```

-->

# 连接个人 AnkiServer

(我 Aliyun 服务器备案还没批下来, 除了 22 端口其他端口都给封着, 没法在客户端上做实验....)

## PC 端

[作者告知](https://github.com/dsnopek/anki-sync-server#point-the-anki-desktop-program-at-it) , PC 端没有相关设置, 必须自己编写插件.

在 Anki 插件目录中创建一个 `myankisync.py` 文件. Anki 插件目录入口在此:

![Snipaste_2018-08-25_00-19-23.png](https://i.loli.net/2018/08/25/5b80302f5bfb8.png)

在其中创建 `AnkiSyncMaster.py`, myankisync 太蠢了, 换个帅点的名字. 注意, Anki 运行插件时不允许任何注释.

```py
import anki.sync
anki.sync.SYNC_BASE = 'http://127.0.0.1:27701/'
anki.sync.SYNC_MEDIA_BASE = 'http://127.0.0.1:27701/msync/'

# 原地址:
#anki.sync.SYNC_BASE = 'https://ankiweb.net/'
#anki.sync.SYNC_MEDIA_BASE = 'https://msync.ankiweb.net/'
```

需要重启客户端生效. 注意填对端口号, 并且开放防火墙对应端口.

当然, 可以只让媒体文件走自己的服务器, 只需要将 `SYNC_BASE` 设为原 AnkiWeb 即可.

## 连接 AnkiDroid

![Screenshot_2018-08-25-00-43-38-070_com.ichi2.anki.png](https://i.loli.net/2018/08/25/5b8036260dc7f.png)

## iOS

据说没有任何办法.