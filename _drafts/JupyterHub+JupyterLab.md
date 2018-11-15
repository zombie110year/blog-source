---
title:  JupyterHub+JupyterLab
date:   2018-10-01 15:49:44
mathjax:  false
tags:
    - Python
    - Jupyter
categories:
    - 日常
---

# 简介

Jupyter Hub 是一个多用户的 Jupyter Notebook 环境, 而 Jupyter Lab 类似一个 Jupyter Notebook 的插件, 提供了更优美的界面以及编辑方式.

Jupyter Lab 和 Jupyter Notebook 可以同时运行, 在输入 URL 时, 以 `lab?` 结尾, 则进入 Jupyter Lab, 以 `tree?` 结尾, 则进入原版的 Jupyter Notebook, 因此, 推断 Jupyter Lab 也是可以用于 Jupyter Hub 的.

# Jupyter Hub

为了免去安装 Python, Numpy, Matplotlib ... 等依赖项的麻烦, 先 [安装 Anaconda](https://anaconda.com). Anaconda 中自带了 Jupyter Notebook 以及 Jupyter Lab, 我们要做的就是下载并安装 Jupyter Hub.

## 安装 Jupyter Hub

可以直接使用 conda 下载安装, 会安装这些包:

```
user@machine:~$ conda install -c conda-forge jupyterhub
Solving environment: done

## Package Plan ##

  environment location: /home/jupyter/anaconda3

  added / updated specs:
    - jupyterhub


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    async_generator-1.10       |             py_0          18 KB  conda-forge
    certifi-2018.4.16          |           py36_0         142 KB  conda-forge
    alembic-0.9.9              |             py_0         104 KB  conda-forge
    python-oauth2-1.0.1        |           py36_0          86 KB  conda-forge
    conda-4.5.11               |           py36_0         625 KB  conda-forge
    prometheus_client-0.3.1    |             py_1          27 KB  conda-forge
    pamela-0.3.0               |           py36_0          11 KB  conda-forge
    jupyterhub-0.9.4           |           py36_0         1.7 MB  conda-forge
    libgcc-7.2.0               |       h69d50b8_2         304 KB  conda-forge
    nodejs-8.10.0              |                0        14.9 MB  conda-forge
    python-editor-1.0.3        |             py_0           8 KB  conda-forge
    mako-1.0.7                 |             py_1          57 KB  conda-forge
    configurable-http-proxy-3.1.0|          node8_1         247 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        18.1 MB

The following NEW packages will be INSTALLED:

    alembic:                 0.9.9-py_0       conda-forge
    async_generator:         1.10-py_0        conda-forge
    configurable-http-proxy: 3.1.0-node8_1    conda-forge
    jupyterhub:              0.9.4-py36_0     conda-forge
    libgcc:                  7.2.0-h69d50b8_2 conda-forge
    mako:                    1.0.7-py_1       conda-forge
    nodejs:                  8.10.0-0         conda-forge
    pamela:                  0.3.0-py36_0     conda-forge
    prometheus_client:       0.3.1-py_1       conda-forge
    python-editor:           1.0.3-py_0       conda-forge
    python-oauth2:           1.0.1-py36_0     conda-forge

The following packages will be UPDATED:

    certifi:                 2018.4.16-py36_0             --> 2018.4.16-py36_0 conda-forge
    conda:                   4.5.4-py36_0                 --> 4.5.11-py36_0    conda-forge

Proceed ([y]/n)?
```

## 配置 Jupyter Hub

安装之后, 使用 `jupyterhub --generate-config` 来创建配置文件. 默认创建到当前目录下的 `jupyterhub_config.py`.

修改一下设置以便使用:

(建议在 Vim 中使用 `:/xxxx` 来搜索相关设置项, 使用 `yy` 复制光标当前行, 使用 `p` 粘贴到光标下一行. 因为根据版本的不同, 一些设置项的名称可能会发生变化, 本文使用的 Jupyter Hub 版本为 `0.9.4`, 使用 `jupyterhub --version` 查询)

```python
c.JupyterHub.ip = '*'   # 设置为 * 以允许以该主机的任意 IP 访问.
c.JupyterHub.hub_port = 80 # 如果有一个域名的话, 设置为 80 端口, 可以用 http 协议通过域名访问, 如果使用 https, 设置为 443 端口.
c.PAMAuthenticator.encoding = 'utf8' # 设置为 utf-8 就好, 如果是在 Windows 上开服务器, 得考虑考虑 gbk 编码
c.LocalAuthenticator.create_system_users = False # 是否允许在主机上创建不存在的系统用户, 就是是否在 JupyterHub 的网页上开放注册的意思.
c.Authenticator.whitelist = set() # 用户白名单, 但是我管理多用户的方式是将它们添加到 jupyter 组, 所以这一项就没有设置
c.JupyterHub.admin_users = set('jupyter') # 管理员用户
c.LocalAuthenticator.group_whitelist = set('jupyter') # 用户组白名单, 此设置优先级高于用户白名单
c.JupyterHub.statsd_prefix = 'jupyterhub'
c.Spawner.notebook_dir = '/home/jupyter/notebooks/{username}' # Jupyter Hub 的工作目录, 其中 {username} 会被替换为登陆用户名
```

## 使用 Jupyter Hub

Jupyter Hub 需要使用 Linux 用户登陆, 并且使用的也是 Linux 用户的密码.

按照上面的配置, 应当使用 `jupyter` 组的用户 `jupyter` 作为管理员登陆, 并且使用 `/home/jupyter/notebooks/*` 作为工作目录.

因此, 首先创建用户组, 再创建管理员用户, 还得创建 Jupyter 的用户目录并配置权限.

```sh
groupadd jupyter  # 创建 jupyter 用户组
useradd jupyter -g jupyter -m -d /home/jupyter -s /bin/bash # 创建用户
```

运行了以上两个命令, 就会创建 `jupyter` 组和属于 `jupyter` 组的用户 `jupyter`. `useradd` 指令的各选项解释如下:

- `-g jupyter` 指定该用户属于 `jupyter` 用户组.
- `-m` 生成用户家目录.
- `-d /home/jupyter` 指定用户家目录, 如果没有指定, 但有 `-m`, 那么会将家目录生成在默认路径 `/home/{username}`.
- `-s /bin/bash` 指定该用户登陆使用的 Shell, 默认也是 `/bin/bash`, 为了安全, 将会在配置完成后改为 `/usr/sbin/nologin` 以禁止使用 Shell.

使用 **Root** 用户执行 `jupyterhub --no-ssl --config=/home/jupyter/jupyterhub_config.py` 启动, 可以使用 HTTP 协议连接, 登陆看看.

> **Jupyter Hub** 只能使用 Root 用户运行, 否则创建用户等操作时会因权限不足而报错.

## 配置网络连接

使用 `ifconfig` 查看主机 IP, 结果只是内网 IP, 无法在外网访问.

```
root@iZwz9cixaslir6cf0zd9lyZ:/home/jupyter# jupyterhub --no-ssl --config=/home/jupyter/jupyterhub_config.py
[I 2018-10-01 16:42:27.072 JupyterHub app:1673] Using Authenticator: jupyterhub.auth.PAMAuthenticator-0.9.4
[I 2018-10-01 16:42:27.072 JupyterHub app:1673] Using Spawner: jupyterhub.spawner.LocalProcessSpawner-0.9.4
[I 2018-10-01 16:42:27.076 JupyterHub app:1016] Loading cookie_secret from /home/jupyter/jupyterhub_cookie_secret
[I 2018-10-01 16:42:27.096 JupyterHub proxy:431] Generating new CONFIGPROXY_AUTH_TOKEN
[W 2018-10-01 16:42:27.097 JupyterHub app:1159]
    JupyterHub.admin_users is deprecated since version 0.7.2.
    Use Authenticator.admin_users instead.
[I 2018-10-01 16:42:27.131 JupyterHub app:1201] Not using whitelist. Any authenticated user will be allowed.
[I 2018-10-01 16:42:27.153 JupyterHub app:1855] Hub API listening on http://127.0.0.1:80/hub/
[W 2018-10-01 16:42:27.154 JupyterHub proxy:472] Found proxy pid file: /home/jupyter/jupyterhub-proxy.pid
[W 2018-10-01 16:42:27.154 JupyterHub proxy:489] Proxy still running at pid=3493
[W 2018-10-01 16:42:28.157 JupyterHub proxy:509] Stopped proxy at pid=3493
[W 2018-10-01 16:42:28.159 JupyterHub proxy:565] Running JupyterHub without SSL.  I hope there is SSL termination happening somewhere else...
[I 2018-10-01 16:42:28.159 JupyterHub proxy:567] Starting proxy @ http://172.16.32.55:8000/
16:42:28.570 - info: [ConfigProxy] Proxying http://172.16.32.55:8000 to (no default)
16:42:28.573 - info: [ConfigProxy] Proxy API at http://127.0.0.1:8001/api/routes
```

将 `ip` 设置为 `0.0.0.0`, 却无法运行.

```
root@iZwz9cixaslir6cf0zd9lyZ:/home/jupyter# jupyterhub --no-ssl --config=/home/jupyter/jupyterhub_config.py
[I 2018-10-01 16:55:00.642 JupyterHub app:1673] Using Authenticator: jupyterhub.auth.PAMAuthenticator-0.9.4
[I 2018-10-01 16:55:00.642 JupyterHub app:1673] Using Spawner: jupyterhub.spawner.LocalProcessSpawner-0.9.4
[I 2018-10-01 16:55:00.646 JupyterHub app:1016] Loading cookie_secret from /home/jupyter/jupyterhub_cookie_secret
[I 2018-10-01 16:55:00.668 JupyterHub proxy:431] Generating new CONFIGPROXY_AUTH_TOKEN
[W 2018-10-01 16:55:00.669 JupyterHub app:1159]
    JupyterHub.admin_users is deprecated since version 0.7.2.
    Use Authenticator.admin_users instead.
[I 2018-10-01 16:55:00.704 JupyterHub app:1201] Not using whitelist. Any authenticated user will be allowed.
[I 2018-10-01 16:55:00.727 JupyterHub app:1855] Hub API listening on http://127.0.0.1:80/hub/
[W 2018-10-01 16:55:00.729 JupyterHub proxy:565] Running JupyterHub without SSL.  I hope there is SSL termination happening somewhere else...
[I 2018-10-01 16:55:00.729 JupyterHub proxy:567] Starting proxy @ http://0.0.0.0:8000/
[E 2018-10-01 16:55:00.732 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:00.830 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:01.173 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
16:55:01.176 - info: [ConfigProxy] Proxying http://0.0.0.0:8000 to (no default)
16:55:01.179 - info: [ConfigProxy] Proxy API at http://127.0.0.1:8001/api/routes
[E 2018-10-01 16:55:01.676 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:01.676 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:01.825 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:02.058 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:02.132 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
[E 2018-10-01 16:55:02.764 JupyterHub utils:68] Unexpected error connecting to iZwz9cixaslir6cf0zd9lyZ:8000 [Errno -2] Name or service not known
```

TODO:
