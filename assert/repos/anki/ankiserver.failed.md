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