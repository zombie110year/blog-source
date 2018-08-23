---
title: SSH 使用
tags:
  - SSH
categories:
  - 日常
date: 2018-08-22 00:18:20
---

# ssh-keygen

使用 ssh-keygen 生成 公钥-私钥对.



<!--
# ssh 命令的参数

- `-b`
- `-c`
- `-D`
- `-E`
- `-e`
- `-F`
- `-I`
- `-e`
- `-J`
- `-L`
- `-l`
- `-m`
- `-O`
- `-o`
- `-p`
- `-Q`
- `-R`
- `-S`
- `-W`
- `-w`
-->

# ~/.ssh 下的配置文件

## `known_hosts`

位于客户端.

记录 SSH 连接过的主机, 如果发现本次连接的主机在此有记录, 但有不符之处 (例如连接已有域名, 但 IP 地址不同) , 就会打印安全警报并退出.

## `config`

位于客户端.

配置连接选项, 格式为:

```
Host mysite                     # 在本机登陆时使用的别名
        HostName 192.168.1.2    # 连接目标的 IP 地址或域名
        PreferredAuthentications publickey  # 连接方式, 采用 公钥-私钥对 方式
        IdentityFile ~/.ssh/id-rsa      # 身份文件, 私钥文件的路径.
        User root               # 登陆的用户
        Port 8022               # 登陆的端口
```

从此, 以下两命令起到相同效果:

```sh
ssh root@192.168.1.2 -p 8022 -i ~/.ssh/id-rsa
ssh mysite
```

## `authorized_keys`

位于服务端.

记录允许使用 公钥-私钥对 连接本机此用户的客户端的公钥.

# /etc/ssh/ 下的配置文件

此处配置文件用于配置服务端.

# scp 与 sftp