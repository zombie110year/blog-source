---
title: Docker笔记
mathjax: false
tags:
  - Docker
categories:
  - Linux
date: 2018-08-18 03:09:11
---

# 在 Linux 上安装 Docker

[GetDocker](https://get.docker.com) 准备了一个安装脚本.

```sh
wget -qO- https://get.docker.com | sh
```

# Docker 基本概念

Docker 和虚拟机有所相似也有所不同:

相似在于:

- Docker 与 虚拟机都可以将任务所用的资源隔离开, 不同的 Docker 容器或虚拟机之间的进程互不干扰

不同在于:

- Docker 使用的是系统内核, 而虚拟机则是使用虚拟化技术. 在运行过程中, Docker 对系统资源的占用是动态化的, 类似于一个特殊的"进程". 而虚拟机则是直接从系统中划走了额定的资源.
- Docker 只隔离了程序的依赖关系, 没有隔离主机对程序的监控. 而虚拟机创造了一个独立的操作系统, 主机对该系统是完全隔绝的.

![Docker](https://www.docker.com/sites/default/files/Container%402x.png)
![Vitual Machine](https://www.docker.com/sites/default/files/VM%402x.png)

## Docker 镜像

Docker 镜像是一个特殊的文件系统, 提供了供容器运行所需的程序, 库, 配置等文件, 还包含了配置参数(如环境变量, 用户, 匿名卷等). 镜像里所有数据都是静态的, 在构建之后也不会改变.

## Docker 容器

容器和镜像关系, 就类似于面对对象编程中的 `实例` 与 `类` 一样. 镜像是静态的定义, 容器是运行的实体.

容器实质上是一个进程, 但是运行于独立的 `命名空间` . 容器可以有自己的用户, 系统配置, 文件系统.

每一个容器运行时, 是以镜像为 `基础层` , 在其上创建一个当前容器的 `存储层`, 我们可以称这个为容器运行时读写而准备的存储层为 `容器存储层`.

容器存储层的生存周期和容器一样, 容器消亡时, 容器存储层也随之消亡. 因此, 任何保存于容器存储层的信息都会随容器删除而丢失.

按照 Docker 最佳实践的要求, 容器不应该向其存储层内写入任何数据, 容器存储层要保持无状态化. 所有的文件写入操作, 都应该使用 `数据卷(Volume)`, 或者绑定 `宿主目录` , 在这些位置的读写会跳过容器存储层, 直接对宿主(或网络存储)发生读写, 其性能和稳定性更高.

数据卷的生存周期独立于容器, 容器消亡, 数据卷不会消亡. 因此, 使用数据卷后, 容器可以随意删除, 重新 run, 数据却不会丢失. 

## DockerFile

# Docker 使用

**运行 Docker 必须要有 root 权限, 除非将当前用户添加到 docker 用户组**

```sh
# 1. 查询用户组中是否已添加了 docker 组. 若已有, 则跳到第 3 步.
sudo cat /etc/group | grep docker
# 2. 创建 docker 用户组
sudo groupadd -g docker
# 3. 将当前用户添加到 docker 用户组
sudo usermode -aG docker current_user
# 4. 重启 docker 服务, 使权限生效
sudo systemctl restart docker
# 如果提示get ......dial unix /var/run/docker.sock权限不够, 则修改/var/run/docker.sock权限
sudo chmod a+rw /var/run/docker.sock
```

## 根据已有镜像运行容器

```sh
docker run [image] [command]
```

- `docker run` 如果成功, 就会创建一个容器, 此容器基于 `image` 建立. `command` 是在容器中执行的指令.
- 如果未在本地找到 `image` , docker 会自动前往官方仓库下载.

一些有用的参数 [^docker.run.help]

- `-a` 连接至一个 docker 容器, 开放其 stdin, stdout 和 stderr. `--attach`
- `-d` 后台运行, 并打印容器 ID, 长指令形式为 `--detach`
- `-i` 开放容器的 stdin, 长指令形式为 `--interactive`
- `-t` 创建一个终端(tty), `--tty`
- `-h` 指定容器的 hostname, `--hostname`, 例如, `-h MyC` 或 `--hostname MyC` 将容器的 hostname 设置为 "MyC"
- `--env` 设置环境变量
- `--memory (int)bytes` 限制容器使用的内存, 例如 `--memory 1024m` 限制容器最多使用 1024MB 内存
- `-p`, `--publish list` 公开容器内部端口, 并将其映射到对应主机端口. 例如 `-p [80:80, 8080:8080]` 或 `--publish=[80:80, 8080:8080]` 每一项都是 `主机端口号:容器端口号` 的组合.
- `-P` 公开容器内部所有使用的端口, 随机映射到主机.

## 使用参数运行容器

```sh
docker run [options] [image] [command]
```

- 对 docker 使用的参数必须紧挨着 `docker run ` .

### 交互式容器

```sh
docker run -i -t ubuntu /bin/bash
```

- `-i` 参数表示允许向容器内的 stdin 输入.
- `-t` 参数表示向容器外部生成一个终端.

当运行完上面的指令后, 系统返回如下信息, 然后进入了容器内的 bash 环境.
输入 `exit` 返回主机的 Shell, 同时, 容器被停止.

```
c64513b74145: Already exists
01b8b12bad90: Already exists
c5d85cf7a05f: Already exists
b6b268720157: Already exists
e12192999ff1: Already exists
Digest: sha256:3f119dc0737f57f704ebecac8a6d8477b0f6ca1ca0332c7ee1395ed2c6a82be7
Status: Downloaded newer image for ubuntu:latest
root@43912502ede1:/#
```

### 后台运行容器

```sh
docker run -d [image] [command]
```

- `-d` 参数会将此容器放在系统后台运行.

## 停止容器

要停止容器, 需要先获取容器 ID

```sh
docker ps       # 列出当前正在运行的容器
docker ps -a    # 列出所有容器
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
5512151d0144        training/webapp     "python app.py"     5 seconds ago       Up 4 seconds        5000/tcp            relaxed_roentgen
```

之后使用

```sh
docker stop [ID]
```

停止容器. ID 可以不输完, 在没有歧义的情况下, 只输入 ID 的前半段也能停止目标容器.

# Docker 管理

## 添加容器
## 添加镜像
## 列出容器
## 列出镜像
## 移除容器
## 移除镜像

```sh
docker image ls                 # 列出本地镜像
docker image rm -f [images]     # 强制删除镜像
```

如果 `docker image rm [images]` 没有 `-f` 参数的话, 删除操作无法成功, 且报错:

```sh
Error response from daemon:
conflict: unable to remove repository reference "hello-world:latest" (must force) - container 79a139769099 is using its referenced image 2cb0d9787c4d
```

---

[^docker.run.help]: [Docker.run.help](/public/assert/resources/docker.run.help.html)