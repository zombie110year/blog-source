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

可以在 `/proc/sys/kernel/core_pattern` 文件中设置 core dump 的保存路径.
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
|/usr/lib/systemd/systemd-coredump %p %u %g %s %e %d %i
```

# Core Dump 怎么用

# 参考

- http://man7.org/linux/man-pages/man5/core.5.html
- https://zhuanlan.zhihu.com/p/24591108
- https://www.cnblogs.com/hazir/p/linxu_core_dump.html
