---
title: Docker笔记
mathjax: false
tags:  docker
category: 运维
date: 2019-04-18 12:54:11
---

# Docker 基本概念

Docker 和虚拟机有所相似也有所不同:

相似在于:

- Docker 与 虚拟机 都可以将任务所用的资源隔离开, 不同的 Docker 容器或虚拟机之间的进程互不干扰.

不同在于:

- Docker 使用的是系统内核, 而虚拟机则是使用虚拟化技术. 在运行过程中, Docker 对系统资源的占用是动态化的, 类似于一个特殊的"进程". 而虚拟机则是直接从系统中划走了额定的资源.
- Docker 只隔离了程序的依赖关系, 没有隔离主机对程序的监控. 而虚拟机创造了一个独立的操作系统, 主机对该系统是完全隔绝的.

引用官方提供的示意图:

|                                       Docker                                        |                                VM                                |
| :---------------------------------------------------------------------------------: | :--------------------------------------------------------------: |
| ![Docker Container](/assert/img/docker-containerized-appliction-blue-border_2.webp) | ![Vitual Machine](/assert/img/container-vm-whatcontainer_2.webp) |

<!--more-->

## Docker 镜像

Docker 镜像是一个特殊的文件系统, 提供了供容器运行所需的程序, 库, 配置等文件, 还包含了配置参数(如环境变量, 用户, 匿名卷等). 镜像里所有数据都是静态的, 在构建之后也不会改变.

## Docker 容器

容器和镜像关系, 就类似于面对对象编程中的 `实例` 与 `类` 一样. 镜像是静态的定义, 容器是运行的实体.

容器实质上是一个进程, 但是运行于独立的 `命名空间` . 容器可以有自己的用户, 系统配置, 文件系统. 当容器中的任务运行结束了, 此容器也会停止运行, 但是容器不会被自动删除.

每一个容器运行时, 是以镜像为 `基础层` , 在其上创建一个当前容器的 `存储层`, 我们可以称这个为容器运行时读写而准备的存储层为 `容器存储层`.

容器存储层的生存周期和容器一样, 容器被删除时, 容器存储层也随之被删除. 因此, 任何保存于容器存储层的信息都会随容器删除而丢失.

按照 Docker 最佳实践的要求, 容器不应该向其存储层内写入任何数据, 容器存储层要保持无状态化. 所有的文件写入操作, 都应该使用 `数据卷(Volume)`, 或者绑定 `宿主目录` , 在这些位置的读写会跳过容器存储层, 直接对宿主(或网络存储)发生读写, 其性能和稳定性更高.

数据卷的生存周期独立于容器, 容器删除, 数据卷不会删除. 因此, 使用数据卷后, 容器可以随意删除, 重新 run, 数据却不会丢失.

## Dockerfile

Dockerfile 是一个用于配置 image 生成的文件, 它可以配置哪些文件被忽略, image 的基本信息以及其他配置:

### .dockerignore

配置 `.dockerignore` 类似于 `.gitignore`, 语法是相同的, 在其中的文件不会被打包进 image 中.

### Dockerfile

在项目的根目录下创建一个 `Dockerfile`, 这里就是 image 的所有配置了:

```
# 继承自 DockerHub 中的 image, <image> 为完整的 image 路径, <tag> 则是标签, 如果留空
# 则默认为 latest
FROM <image>:<tag>

# 将 <dir> (主机文件系统) 中的文件复制到 <container_dir> (容器内部文件系统) 中,
# .dockerignore 中的文件将被排除
COPY <dir> <container_dir>

# 设置容器的工作目录, 也就是当容器运行时, 进程的 cwd
WORKDIR <container_dir>

# 在 build image 之前运行的命令, 如果会下载或者生成新的文件, 则这些文件也会被打包
# 如果有多个命令要在构建前运行, 可以使用多条 RUN 命令
RUN <command0>
RUN <command1>

# 容器启动时运行的命令, 一个容器只能运行一个命令; 如果需要运行多个任务, 应当使用多个容器.
CMD <command>

# 配置容器开放的端口
EXPOSE <port>
```

更多的 Dockerfile 语法可以参考 [官方文档](https://docs.docker.com/engine/reference/builder/).

配置完成后, 构建 image:

```sh
# -t 参数指定 image 名字, tag 是可选的, 如果留空则默认为 latest.
docker image build -t <name>:<tag>
```

# 在 Linux 上安装 Docker

[GetDocker](https://get.docker.com) 准备了一个安装脚本.

```sh
wget -qO- https://get.docker.com | sh
```

对于 ArchLinux, 可以直接安装 pacman 的 docker 组.

```sh
sudo pacman -S docker
```

然后启用 `docker.service`:

```sh
sudo systemctl enable docker.service
```

等到配置完成了再运行服务:

```sh
sudo systemctl start docker.service
```

## 配置

1. 将当前用户添加到 docker 用户组, 否则只能通过 root 用户操作 docker:

```sh
# 1. 查询用户组中是否已添加了 docker 组. 若已有, 则跳到第 3 步.
sudo cat /etc/group | grep docker
# 2. 创建 docker 用户组
sudo groupadd -g docker
# 3. 将当前用户添加到 docker 用户组
sudo usermod -aG docker <当前用户>
# 4. 重启 主机, 使用户配置生效
sudo reboot
```

使用 `docker info` 查询当前 docker 信息.

```sh
docker info
```

2. 修改 Docker Hub 镜像

由于在国内访问 Docker Hub 十分不便, 因此, 最好设置镜像站点.

在 `/etc/docker/daemon.json` (如果文件不存在则新建)中添加一个键值对:

```json
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
```

然后重启 docker 服务:

```sh
sudo systemctl restart docker.service
```

然后就可以使用了.

# Docker 使用

## 根据镜像新建容器并运行

```sh
docker container run [image] [command]
```

- `docker container run` 如果成功, 就会创建一个容器, 此容器基于 `image` 建立. `command` 是在容器中执行的指令.
- 如果未在本地找到 `image` , docker 会自动前往官方仓库下载. 每次运行此命令都会生成新的容器.
- 通过 run 新建的容器会保存下来, 如果停止后希望恢复, 应当使用 `start` 命令启动, 而不是 run 再创建一个.

一些持久运行的服务类容器, 需要手动 [停止](#停止容器)

如果 image 的 Dockerfile 中已经定义了 `CMD` 命令, 那么 `[command]` 可以省略以运行设定的 `CMD` 命令.

## 重新运行已有容器

使用 `docker container start [ID] [command]` 运行.

## 查看容器日志输出

```sh
docker container logs [ID]
```

其实是查看容器内的 `stdout` 与 `stderr`.

## 进入一个非交互式容器

```sh
docker container exec -it [ID] /bin/bash
```

如果容器在运行时没有指定 `-it`(`--interactive` 和 `--tty`) 参数, 那么需要手动进入容器的 Shell.

## 从容器中复制文件

```sh
docker container cp [ID]:[/container_path] [localpath]
```

语法类似于 `scp`, 从容器的文件系统中复制文件到主机中.

## 停止容器

```sh
docker container stop [ID]
docker container kill [ID]
```

它们之间是发出 `SIGTERM` 或者 `SIGKILL` 信号的区别.

容器 ID 可以通过 `docker container ps` 或者 `docker container ls` 查询, 它们是一样的, 互为别名.
在没有歧义的情况下, 可以缩写 ID, 只输入前几位即可.

## 使用参数运行容器

```sh
docker container run [options] [image] [command]
```

一些有用的参数:

- `-a` 连接至一个 docker 容器, 开放其 stdin, stdout 和 stderr. `--attach`
- `-d` 后台运行, 并打印容器 ID, 长参数形式为 `--detach`
- `-i` 开放容器的 stdin, 长参数形式为 `--interactive`
- `-t` 创建一个终端(tty), `--tty`
- `-h` 指定容器的 hostname, `--hostname`, 例如, `-h MyC` 或 `--hostname MyC` 将容器的 hostname 设置为 "MyC"
- `--env` 设置环境变量
- `--memory (int)bytes` 限制容器使用的内存, 例如 `--memory 1024m` 限制容器最多使用 1024MB 内存
- `-p`, `--publish list` 公开容器内部端口, 并将其映射到对应主机端口. 例如 `-p [80:80, 8080:8080]` 或 `--publish=[80:80, 8080:8080]` 每一项都是 `主机端口号:容器端口号` 的组合.
- `-P` 公开容器内部所有使用的端口, 随机映射到主机的空闲端口.
- `-v` 挂载容器的数据卷: `-v [/path:/container_path, /path1:/container_path1]`

### 交互式容器

```sh
docker container run -i -t ubuntu /bin/bash
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
docker container run -d [image] [command]
```

- `-d` 参数会将此容器放在系统后台运行.

### 容器数据卷

假设要将目录 `/home/docker/.datum/example` 作为容器的数据卷, 将其挂载到容器内部的 `/data` 目录上:

```sh
docker container run -v /home/docker/.datum/example:/data
```

如果要挂载多个目录, 可以使用列表:

```sh
docker container run -v [/path0:/cpath0, /path1:/cpath1]
```

- 每一组为 `主机路径:容器路径`
- 必须使用绝对路径

### 容器端口

假设在容器中, 有一个 Web 应用运行在 **容器内** 的 8080 端口, 现在要把它与主机的 80 端口连接起来:

```sh
docker container start -p 80:8080 [ID]
```

# Docker 管理

## 添加容器

使用 `docker container run [image]` 根据镜像创建容器.

## 列出容器

使用 `docker container ls --all` 列出所有容器. 默认列出 容器 ID, 使用的 image, 启动使用的命令, 创建时间, 当前状态, 命名 这几个参数.

```
$ docker container ls --all
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES
```

如果希望列出更详细的信息, 或者过滤一些无用的信息, 可以使用 `--format` 或 `--filter` 参数.

`--format` 参数接受的模板字符串使用 Go Template 语法. 传入的 `formatter.containerContext` 结构体具有以下字段:

- `Command`: 启动的命令
- `CreatedAt`: 容器创建时间
- `ID`: 容器 ID
- `Image`: 容器使用的镜像 ID
- `Labels`: 该容器的标签, 一般是镜像维护者编辑的
- `LocalVolumes`: 绑定的宿主数据卷数目
- `Mounts`: 数据卷挂载点
- `Names`: 该容器的命名
- `Networks`: (与宿主机的)网络连接模式
- `Ports`: 端口映射信息
- `RunningFor`: 运行时间
- `Size`: 容器占用空间
- `Status`: 当前状态



## 移除容器

```sh
docker container ls --all
docker container rm -f [ID]
```

## 添加镜像

可以通过 DockerHub 下载镜像

```sh
docker image pull [image]:[tag]
```

也可以构建镜像:

```sh
docker image built -t [name]:[tag]
```

前提是当前项目完整配置了 Dockerfile.

## 列出镜像

```sh
docker image ls --all
```

## 移除镜像

```sh
docker image ls                 # 列出本地镜像
docker image rm -f [images]     # 强制删除镜像
```

如果 `docker image rm [images]` 没有 `-f` 参数的话, 则只有在没有任何容器正在使用此镜像的情况下才能成功删除, 加上 `-f` 参数强制删除, 并且删除对应容器. 下面是一个无 `-f` 参数时报错的例子:

```sh
Error response from daemon:
conflict: unable to remove repository reference "hello-world:latest" (must force) - container 79a139769099 is using its referenced image 2cb0d9787c4d
```

# docker-compose

docker-compose 是一个 Python 编写的 docker 命令解析器，用于将一些 docker 命令写为 yaml 格式的配置文件，以便复制、保存、和方便地执行。

将 docker 命令以一定的形式保存到 `docker-compose.yml` 文件中，然后执行 `docker-compose up` 命令解析并运行它们。也可以将文件命名为其他名称，然后使用 `-f <filename>` 参数来指定。

```sh
docker-compose -f <filename> <command> [options...]
```

注意顺序，docker-compose 解析参数是有一定顺序的， `-f` 参数必须在 `command` 参数之前。

# 推荐阅读

- [阮一峰 Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [阮一峰 Docker 微服务教程](http://www.ruanyifeng.com/blog/2018/02/docker-wordpress-tutorial.html)
- [慕课网的 Docker 概念讲解](https://zhuanlan.zhihu.com/p/38552635)
