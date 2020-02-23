---
title: 远程下载站配置
slug: yuan-cheng-xia-zai-zhan-pei-zhi
date: 2020-02-02 02:36:38 UTC+08:00
tags:
  - aria2
  - linux
  - rclone
link:
description: |
  通过 aria2 与 rclone 配合，实现将 VPS 下载文件自动上传至 OneDrive 的功能。
type: text
---

# 预期目标

1. aria2 + RPC 支持
2. 自动将下载的文件上传到 OneDrive
3. 自动清理已上传到 OneDrive 的文件

<!-- more -->

# （下载器）aria2 配置

用一个脚本来安装：

```bash
#! /usr/bin/env bash

#! 此脚本只适用于使用 apt 软件包管理器的 debian、 ubuntu 等系统
# 外部变量说明
# 当前用户名： $UID
# 当前用户组： $GID
# 当前用户家目录： $HOME
# Aria2 RPC 密码： $ARIA2_SECRET
# 额外的 trackers：$ARIA2_TRACKERS
# 指定下载保存目录：$ARIA2_DATADIR

# 方便地彩色打印
function say()
{
  echo -e "[\033[33m$*\033[0m]"
}
function sayres() {
  echo -e "\033[32m$*\033[0m"
}
function sayerr() {
  echo -e "\033[31m$*\033[0m"
}

if [[ $1 = *help ]]; then
  echo "安装并配置 aria2 RPC 服务的脚本"
  echo "可以设置外部环境变量以控制行为："
  echo "*   ARIA2_SECRET   - aria2 rpc 密码（默认：无）"
  echo "*   ARIA2_TRACKERS - 额外的 Tracker 列表，每一项用英文逗号 , 分隔（默认：无）"
  echo "*   ARIA2_DATADIR  - 下载保存目录（默认：/aria2-data）"
  echo
  exit
fi

# ==== START ====
say "安装 aria2"
sudo apt install -y aria2 >/dev/null 2>/dev/null
sayres "$(aria2c --version | grep 'aria2 version')"

say "准备数据目录"
if [[ $ARIA2_DATADIR ]]; then
  DDIR=$ARIA2_DATADIR
else
  DDIR=/aria2-data
fi
[[ ! -d $DDIR ]] && sudo mkdir $DDIR && sudo chown -R $UID:$GID $DDIR
sayres "$DDIR"

say "准备 aria2 配置文件"
CONF_DIR=$HOME/.aria2
CONF_FILE=$CONF_DIR/aria2.conf
CONF_CONTENT="# Aria2 配置文件\n
# 保存在路径 $HOME/.aria2 之下时会自动加载\n
\n
# 允许rpc\n
enable-rpc=true\n
# 允许向任意地址响应\n
rpc-allow-origin-all=true\n
# 允许接收任意地址的请求\n
rpc-listen-all=true\n
# rpc 端口，约定俗成为 6800\n
rpc-listen-port=6800\n
# 不保存上传的种子/元数据文件\n
rpc-save-upload-metadata=false\n
\n
# rpc 密码(新特性, 旧的 rpc-user,passwd 已被抛弃)\n
rpc-secret=$ARIA2_SECRET\n
\n
### 速度相关\n
## 最大同时下载数(任务数)\n
max-concurrent-downloads=5\n
## 断点续传\n
continue=true\n
## 同服务器连接数\n
max-connection-per-server=5\n
##最小文件分片大小, 下载线程数上限取决于能分出多少片, 对于小文件重要\n
min-split-size=2M\n
##单文件最大线程数, 路由建议值: 5\n
split=4\n
## 下载速度限制 0 不限制\n
max-overall-download-limit=0\n
## 单文件速度限制\n
max-download-limit=0\n
## 上传速度限制\n
max-overall-upload-limit=0\n
## 单文件速度限制\n
max-upload-limit=0\n
## 断开速度过慢的连接\n
lowest-speed-limit=0\n
## 验证用，需要1.16.1之后的release版本\n
## referer=*\n
\n
### 进度保存相关\n
# input-file 在启动时加载其中的任务并执行\n
input-file=$CONF_DIR/sessions.txt\n
save-session=$CONF_DIR/sessions.txt\n
# 定时保存会话，需要1.16.1之后的release版\n
save-session-interval=60\n
# 自动保存 .aria2 控制文件, 设为 0 取消\n
auto-save-interval=0\n
\n
### 磁盘相关\n
# 文件保存路径, 默认为当前启动位置\n
dir=$DDIR\n
# 文件缓存, 使用内置的文件缓存, 如果你不相信Linux内核文件缓存和磁盘内置缓存时使用, 需要1.16及以上版本\n
disk-cache=0\n
# 另一种Linux文件缓存方式, 使用前确保您使用的内核支持此选项, 需要1.15及以上版本\n
enable-mmap=true\n
# 文件预分配, 能有效降低文件碎片, 提高磁盘性能. 缺点是预分配时间较长\n
# 所需时间 none < falloc ? trunc << prealloc, falloc和trunc需要文件系统和内核支持\n
file-allocation=falloc\n
\n
### BT相关\n
# 分离做种，不占用同时下载任务数限制\n
bt-detach-seed-only=true\n
# 启用本地节点查找\n
bt-enable-lpd=true\n
# 添加额外的tracker\n
bt-tracker=$ARIA2_TRACKERS\n
# 单种子最大连接数\n
bt-max-peers=50\n
# 强制加密, 防迅雷必备\n
bt-require-crypto=true\n
# 当下载的文件是一个种子(以.torrent结尾)时, 自动下载BT\n
follow-torrent=true\n
# BT监听端口, 当端口屏蔽时使用\n
listen-port=6881-6999\n
# aria2亦可以用于PT下载, 下载的关键在于伪装\n
# 不确定是否需要，为保险起见，need more test\n
enable-dht=true\n
bt-enable-lpd=true\n
enable-peer-exchange=false\n
# 修改 HTTP 请求特征（Windows 10 Firefox）\n
user-agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0\"\n
peer-id-prefix=Aria2-\n
# 修改做种设置, 允许做种\n
seed-ratio=2.0\n
# 保存会话\n
force-save=true\n
bt-hash-check-seed=true\n
bt-seed-unverified=true\n
bt-save-metadata=true\n
# 加载 cookie 文件, 支持 Firefox3 (SQLITE3),\n
# Chromium/Google Chrome (SQLite3) 或\n
# Mozilla/Firefox(1.x/2.x)/Netscape (TXT) 格式\n
# load-cookies=$CONF_DIR/cookies.sqlite3\n
\n
## 自动化相关\n
on-download-complete=/usr/local/bin/on-download-complete.sh\n
on-bt-download-complete=/usr/local/bin/on-download-complete.sh\n
on-download-stop=/usr/local/bin/on-download-stop.sh\n
"

[[ ! -d $CONF_DIR ]] && mkdir -p $CONF_DIR
printf %b $CONF_CONTENT > $CONF_FILE
touch $CONF_DIR/sessions.txt
sayres "$CONF_DIR"
```

# （文件保存）OneDrive rclone 客户端配置

使用 rclone 挂载 OneDrive。

## 安装 rclone

对于 Debian 系统，可以执行 `apt install rclone` 即可安装。

对于 Windows 系统，推荐用 [lukesampson/scoop](https://github.com/lukesampson/scoop/) 来管理软件： `scoop install rclone`。

## 在本地主机取得 OneDrive API 授权

首先，你得在 **安装了浏览器** 的日常使用主机上安装 rclone，这样才能弹出一个页面进入 OneDrive 网站上获取授权。

在 Windows 系统上用 `scoop install rclone` 安装了 rclone 后，运行 `rclone authorize onedrive`，然后会弹出浏览器窗口，进入微软登录页面用 OAuth2 验证。

输入你的微软帐号密码登录后，rclone 就取得了微软授权，在终端中显示授权码。这个授权码可以保存下来给其他 rclone 程序使用（例如我们要作为下载服务器的主机）。

```
# rclone authorize onedrive
2020/02/02 00:22:07 NOTICE: Config file "C:\\Users\\zom\\.config\\rclone\\rclone.conf" not found - using defaults
If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=_yOQ6xvaun9P7FSOIj-2aw
Log in and authorize rclone for access
Waiting for code...
Got code
Paste the following into your remote machine --->
{"access_token":"EwCAA8l6BAAUO9**************************************************************防止泄漏************************************************************************DAs$","expiry":"2020-02-02T01:27:49.2021085+08:00"}
<---End paste
```

可以看到， rclone 用 JSON 配置它自己，并且从 `expiry` 字段读取到，这个授权码有有效期限。
TODO: 查微软官网

将其保存下来，命名为 onedrive.json。

## 远程服务器配置 rclone

rclone 在 `~/.config/rclone/rclone.conf` 中保存配置。

由于 rclone 通过 stdin 获取用户输入，因此这里只能手动配置了。

执行 `rclone config` 进入配置流程，下面会先介绍输入，然后展示当时的终端情况。

1. rclone 询问你的意图

我们选择 `n`，新建一个 remote。

```
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> n
```

2. 设置新 remote 的名字

随便起一个就好，例如，因为 OneDrive 是微软家的，就取名叫 `ms` 了。

```
name> ms
```

3. 选择服务提供方

选择 `22`，微软 OneDrive。

**注意，如果 rclone 版本不同，编号可能不一样，记得看准了选**

```
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Citrix Sharefile
   \ "sharefile"
 9 / Dropbox
   \ "dropbox"
10 / Encrypt/Decrypt a remote
   \ "crypt"
11 / FTP Connection
   \ "ftp"
12 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
13 / Google Drive
   \ "drive"
14 / Google Photos
   \ "google photos"
15 / Hubic
   \ "hubic"
16 / JottaCloud
   \ "jottacloud"
17 / Koofr
   \ "koofr"
18 / Local Disk
   \ "local"
19 / Mail.ru Cloud
   \ "mailru"
20 / Mega
   \ "mega"
21 / Microsoft Azure Blob Storage
   \ "azureblob"
22 / Microsoft OneDrive
   \ "onedrive"
23 / OpenDrive
   \ "opendrive"
24 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
25 / Pcloud
   \ "pcloud"
26 / Put.io
   \ "putio"
27 / QingCloud Object Storage
   \ "qingstor"
28 / SSH/SFTP Connection
   \ "sftp"
29 / Transparently chunk/split large files
   \ "chunker"
30 / Union merges the contents of several remotes
   \ "union"
31 / Webdav
   \ "webdav"
32 / Yandex Disk
   \ "yandex"
33 / http Connection
   \ "http"
34 / premiumize.me
   \ "premiumizeme"
storage> 22
```

特别说明一下，`drive_id` 是微软给你的 OneDrive 帐号分配的 ID，可以在网页登录 OneDrive 时从 URL 中获取：``

4. 询问 Microsoft App Clinet ID，由于没有，所以留空。

```
** See help for onedrive backend at: https://rclone.org/onedrive/ **

Microsoft App Client Id
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_id>
```

5. Microsoft App Client Secret，同样留空。

```
Microsoft App Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret>
```

6. 询问是否进阶编辑，选择是。

```
Edit advanced config? (y/n)
y) Yes
n) No
y/n> y
```

7. Chunk Size，保持默认即可。

```
Chunk size to upload files with - must be multiple of 320k (327,680 bytes).

Above this size files will be chunked - must be multiple of 320k (327,680 bytes). Note
that the chunks will be buffered into memory.
Enter a size with suffix k,M,G,T. Press Enter for the default ("10M").
chunk_size>
```

8. 是否自动配置 remote，选择 `n`，因为远程服务器没有浏览器。

```
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes
n) No
y/n> n
```

9. 输入我们之前获取的 onedrive.json 文件内容。

```
For this to work, you will need rclone available on a machine that has a web browser available.
Execute the following on your machine (same rclone version recommended) :
        rclone authorize "onedrive"
Then paste the result below:
result> {******* 敏感信息，已隐藏 ********}
```

10. 选择 OneDrive 服务类型，个人版就选 1，persional 或 bussiness 这一类。

```
Choose a number from below, or type in an existing value
 1 / OneDrive Personal or Business
   \ "onedrive"
 2 / Root Sharepoint site
   \ "sharepoint"
 3 / Type in driveID
   \ "driveid"
 4 / Type in SiteID
   \ "siteid"
 5 / Search a Sharepoint site
   \ "search"
Your choice> 1
```

11. rclone 通过之前的配置，查询到微软服务器上你的 OneDrive 帐号对应的 ID，让你选择

如果买了多个 OneDrive 计划的话，可能有多种选择，选其中一个方便的就好。

```
Found 1 drives, please select the one you want to use:
0:  (personal) id=c***********0
Chose drive to use:> 0
```

12. 配置基本完成，接下来一路 `y` 过去就好了，问的问题都是「你的配置是不是这样？」、「还要继续配置其他 remote 吗？」这样的问题。

**如果在不同机器间迁徙的话，可以直接复制生成的 `~/.config/rclone/rclone.conf` 文件。**

# （下载后自动上传并删除本地文件）aria2 hook 配置

aria2 提供了 hook 功能，见 [官方文档 event-hook 章节](https://aria2.github.io/manual/en/html/aria2c.html#event-hook)，aria2 在完成下载后，根据普通下载或 BT 下载的区别会调用 `on-download-complete`、`on-bt-download-complete` 配置的脚本。传入的参数分别是 GID、文件数目、文件路径。我们用到最后一个就好。前面的我们就统计在 log 里好了。

这里创建我们之前 `aria2.conf` 中配置为 event hook 的脚本。
保存到 `/usr/local/bin/` 中，并给予 `+x` 权限。

1. on-download-complete.sh

```bash
#! /usr/bin/env bash

now=$(date '+%Y-%m-%d %H:%M:%S')
log=/tmp/aria2-onedrive.log
remote_savedir=/aria2-data
# $1: GID, $2: 文件数目, $3: 文件路径
rclone copy "$3" "ms:$remote_savedir/"
if [[ $? -ne 0 ]]; then
  echo "[$now] ERROR rclone copy $3 ms:$remote_savedir/ failed, files still save in local" >> $log
  exit
fi

echo "[$now] INFO save $3, numbers: $2" >> $log
```

2. on-download-stop.sh

```bash
#! /usr/bin/env bash

now=$(date '+%Y-%m-%d %H:%M:%S')
log=/tmp/aria2-onedrive.log

#? 删除本地文件
rm -rf "$3"
#? 删除 .aria2 进度文件
rm "$3.aria2"

echo "[$now] INFO cleanup $3, numbers: $2" >> $log
```
