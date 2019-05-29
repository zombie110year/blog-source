---
layout: posts
title: 段错误与Coredump
date: 2019-05-25 16:14:23
tags:
-   C/C++
---

# Core Dump 是什么

Core Dump 是 Linux 系统在进程出现错误而中断时会产生的一种文件,
在其中储存了进程的内存状态, 寄存器状态, 调用栈等信息.

# Core Dump 如何产生

当程序访问到不属于该进程的内存地址时, 就会产生 Core Dump 包括:

- 内存访问越界:
1. 数组下标越界.
2. 字符串未以 `\0` 结尾的情况下被读写.
3. 使用 `strcpy` 等函数时输出缓冲区溢出, 最好使用 `strncpy` 等函数代替, 设定最大写入字符数.
- 非法指针:
1. 读写 NULL 指针所指的地址.
2. 错误的指针类型转换. 由于内存的对齐方式不一致而导致 bus error 触发 core dump
- 堆栈溢出

当触发 Core Dump 条件时, 系统会自动在进程的 "当前工作目录" 产生一个名为 `core` 的文件(可配置).

有些 Linux 发行版会将这个功能禁用, 可以在 `/etc/security/limits.conf` 这个配置文件中设置:

```
# /etc/security/limits.conf
#
#Each line describes a limit for a user in the form:
#
#<domain>   <type>   <item>   <value>
    *          soft     core   unlimited
```

然后, 查看当前会话的 `ulimit -c` 的输出, 如果为 `0`, 也不会产生 core dump.
这个选项其实是查看或设定 core dump 文件大小限制, 单位是 KB.
可以设置为 `unlimited`, 从而产生不限大小的 core dump.

可以在 `/proc/sys/kernel/core_pattern` 文件中设置 core dump 的保存路径
(每次重启, 这个文件都会被重置).
以 `|` 开头的行会被认为是要执行的命令.
设置将 core dump 文件保存为:

```sh
echo "/tmp/coredump/%u.%e.%p" > /proc/sys/kernel/core_pattern
```

这样, 将会把产生的 core dump 文件保存在 `/tmp/coredump` 目录下,
文件名由进程的 UID, 可执行文件名, 进程的 PID 组成.

core dump 程序不会自动创建目录, 所以需要先创建目录:

```sh
mkdir /tmp/coredump
```

这样文件才能保存.

对使用 systemd 的 coredump 管理工具的发行版, 可以不用更改以上设置, 因为 systemd 提供了方便的工具.

首先, 保证 `/proc/sys/kernel/core_pattern` 的内容为

```
|/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h %e
```

每次发生 coredump 时, 都会在 systemd 所管理的日志中增加一条记录.
可以使用 coredumpctl 进行管理, 基本指令如下:

```sh
# 查看记录
coredumpctl -r
# 或 coredumpctl list -r
# 使用 -r 选项是为了把最新记录排前面

# 将最后一条记录保存到文件 name.core 中
coredumpctl dump -o name.core

# 打开 GDB 开始调试最后一次 coredump
coredumpctl debug

# 查看最后一次 coredump 的详细信息
coredumpctl info

# 操作指定的记录
coredumpctl <cmd> [MATCHS...]
# MATCHS 可以是 PID 或 可执行文件名
```

# Core Dump 怎么用

coredump 只保留了中断前的状态, 不可能当成一个运行至断点的程序, 所以它只适合用 debugger 查看以下本地变量, 调用栈, 寄存器状态等等.

对于 gdb, 使用命令加载可执行文件与 coredump, (编译时需开启 `-g` 选项):

```sh
gdb ./a.out ./a.out.coredump
```

然后, 使用 `info` 指令查看想要观察的信息.

如果使用 Visual Studio Code, 并且安装了 C/C++ 插件的话, 可以将 vscode 与 gdb 连起来, 在 `launch.json` 中的调试配置中增加:

```json
    "coreDumpPath": "${fileDirname}/a.out.coreDump",
```

就会在调试器启动时加载 coredump 文件.

# 参考

- http://man7.org/linux/man-pages/man5/core.5.html
- https://zhuanlan.zhihu.com/p/24591108
- https://www.cnblogs.com/hazir/p/linxu_core_dump.html
