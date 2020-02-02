---
title: C 语言动态链接库
date: 2019-04-10 21:03:32
tags: c/c++
---

# 什么是动态链接库

DLL(Dynamic Linked Library) 是一种可在运行时被其他程序链接并执行的代码.

<!--more-->

# GNU 工具链

## 如何创建动态链接库

先以单个源文件为例, 可以使用 `-fPIC`, `-shared` 等参数直接创建 `.so` (Shared Object) 文件:

```sh
gcc -fPIC -shared -Wl,-soname,libswap.so -o libswap.so swap.c
# 得到 libswap.so 文件
```

-   `-fPIC`: `-f` 选项是很多拥有长名称的 flag 的前缀, PIC(Position Independent Code) 表示生成的代码不依赖于绝对地址, 这样生成的可执行程序可以在一个动态的内存空间中执行相关的代码. 与之相对的还有 `PIE` (Position Independent Executable)
-   `-shared`: 表示创建共享库.
-   `-Wl,-soname,libswap.so`: `-Wl` 表示之后的参数传递给链接器, 用逗号作为分隔符; 而 `-soname,libswap.so` 则是命名动态库, 这不是命名生成的文件, 而是填写生成文件中的一个字段, 以便调用者识别动态库的版本. <sup>[wiki - soname](https://en.wikipedia.org/wiki/Soname)</sup>
-   `-o libswap.so` 将输出写入到此文件中.

```c
/* swap.c 内容 */

void swap(int* a, int* b)
{
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}
```

### 多源文件情形

类似于单源文件, 只不过将编译和链接步骤分开执行:

```sh
    # 以 PIC 模式生成代码
    gcc -c -fPIC *.c
    # 将所有代码链接成动态链接库
    gcc -shared -Wl,-soname,libexample.so -o libexample.so *.o
```

## 如何调用动态链接库

主要还是 gcc 参数的使用, 下面以显示数字的程序为例.

新建一个 `main.c` 文件, 在其中定义:

```c
#include <stdio.h>

// 外部引用函数声明, 这会创建一个在链接时指向 libswap.so 中 swap 函数的符号.
extern void swap(int*, int*);

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    swap(&a, &b);
    printf("%d %d\n", a, b);
    return 0;
}
```

在编译时, 动态链接:

```sh
    gcc -o main.out -L. -lswap main.c
```

-   `-L.`: `-L` 是添加链接库搜索路径, `.` 表示当前路径, 如果把 `.so` 文件保存到其他地方了, 就设置为对应的路径.
-   `-lswap`: `-l` 表示链接某库. 无论是动态还是静态链接都使用同一选项. `swap` 是链接库的名字. 命名规则为 `lib{name}.so.{version}`. 链接时参数中使用 `name`.

要运行程序, 还需要定义环境变量 [LD_LIBRARY_PATH](#LD_LIBRARY_PATH), 将 `libswap.so` 的路径添加到其中, 否则 `main.out` 仍然无法找到动态库:

```sh
    export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
```

然后直接运行 `main.out` 查看效果吧.

## 查看动态库信息

使用 `nm` 指令, 通过 `man nm` 得知, `nm` 可用于列出 object 中的符号, 显示三个字段:

```sh
    nm libswap.so
```

```
<value>         <type>          <name>
0000000000004020 b completed.7287
                 w __cxa_finalize@@GLIBC_2.2.5
0000000000001020 t deregister_tm_clones
0000000000001090 t __do_global_dtors_aux
0000000000003e48 t __do_global_dtors_aux_fini_array_entry
0000000000004018 d __dso_handle
0000000000003e50 d _DYNAMIC
0000000000001134 t _fini
00000000000010e0 t frame_dummy
0000000000003e40 t __frame_dummy_init_array_entry
0000000000002050 r __FRAME_END__
0000000000004000 d _GLOBAL_OFFSET_TABLE_
                 w __gmon_start__
0000000000002000 r __GNU_EH_FRAME_HDR
0000000000001000 t _init
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
0000000000001050 t register_tm_clones
00000000000010e9 T swap
0000000000004020 d __TMC_END__
```

-   `value` 都是无符号整数, 默认 16 进制显示, 对一些特殊的类型, 可能有不同的基数.
-   `type` 该符号的类型:
    -   `A` 此符号的值是绝对的, 在之后的链接中也不会改变
    -   `b`, `B` 符号位于BSS数据部分, 此部分通常包含零初始化或未初始化的数据, 但确切的行为取决于系统.
    -   `C` 普通符号, 是未初始化的数据, 在链接时, 多个普通符号可能同名. 此符号被视作未定义的引用.
    -   `D`, `d` 此符号在初始化数据段.
    -   `G`, `g` 符号位于小对象的初始化数据部分中. 某些目标文件格式允许更有效地访问小数据对象, 例如全局 int 变量而不是大型全局数组.
    -   `i` 对于PE格式文件, 这表示该符号位于特定于DLL实现的部分中.  对于ELF格式文件, 这表示该符号是间接函数.  这是标准ELF符号类型集的GNU扩展.  它表示一个符号, 如果由重定位引用, 则不会计算其地址, 而是必须在运行时调用.  然后, 运行时执行将返回要在重定位中使用的值.
    -   `I` 此符号是其他符号的间接引用.
    -   `N` 这是一个调试符号
    -   `p` 符号位于堆栈展开部分
    -   `R`, `r` 符号位于只读数据段
    -   `S`, `s` 符号位于小对象的未初始化或零初始化数据段
    -   `T`, `t` 符号在 text(code) 数据段中. 这是机器指令数据段, 虽然它起了个令人误会的 "text" 名字.
    -   `U` 未定义符号
    -   `u` 这是一个独特的全局符号。 这是标准ELF符号绑定集的GNU扩展。 对于这样的符号，动态链接器将确保在整个过程中只有一个符号具有此名称和类型。
    -   `V`, `v` 不报错的弱对象
    -   `W`, `w` 未被标记的弱对象
    -   `-` stabs 对象, 只会在 `.out` 文件中定义, 提供调试信息.

使用 `ldd` 命令, 查看库的依赖:

```sh
    ldd libswap.so
```

```
        linux-vdso.so.1 (0x00007ffcbed0d000)
        libc.so.6 => /usr/lib/libc.so.6 (0x00007f316de60000)
        /usr/lib64/ld-linux-x86-64.so.2 (0x00007f316e042000)
```

## LD_LIBRARY_PATH

在未设置的情况下, `echo $LD_LIBRARY_PATH` 得到的是空值, 在网上搜索一番, 得到了以下答案:

> 一般来讲，linux系统的 `LD_LIBRARY_PATH` 都是未设置的，echo 出来也是空值；这个环境变量其实是程序员添加 “额外的” so 查找路径时使用，并不会影响到系统默认的 so 查找路径;
> 真正的系统默认查找路径是配置在文件里的：看看你的 `/etc/ld.so.conf` , 里面就配置了系统安装时，默认的 so 查找路径，不过这个文件一般都不直接配置查找路径，而是简单地 import 了 `/etc/ld.so.conf.d` 下的所有配置文件；
> 你再去 `/etc/ld.so.conf.d` 目录下看，就会有一些 `.conf` 配置文件了, 这些文件里记载的路径，就是你当前系统的 so 默认查找路径了，这些配置跟 `LD_LIBRARY_PATH` 是无关的
>
> 当然，除了设置 `LD_LIBRARY_PATH` 之外，你还可以自己编辑一个 `.conf` 文件，扔到 `/etc/ld.so.conf.d` 目录下, 也能达到添加别的路径到 `so` 默认查找路径的目的， 记得文件扔过去之后以 root 权限执行 `ldconfig` 以刷新配置
> -- [segmentfault 问答](https://segmentfault.com/q/1010000003506264/a-1020000003506326)

# MinGW 工具链

MinGW 是在 Windows 系统中可用的最小 GNU 实现. 在动态链接库方面, 它与 Linux 上的 GNU 的差别仅在于 Windows 上对 DLL 文件的搜索策略.

将上述命令行选项改为:

```sh
gcc -fPIC -shared "-Wl,-soname,swap.dll" -o swap.dll swap.c
gcc -L. -lswap main.c -o main.exe
```

1.  Windows 上 DLL 文件的命名为 `{name}.dll` 没有 `lib` 前缀.
2.  以可执行程序所在目录为第一搜索路径, 之后按 PATH 环境变量中的路径依次搜索.

其他内容查看 [MSVC 工具链](#MSVC-工具链).

# MSVC 工具链

MSVC 编译 C 程序的最小要求是 "C++ 桌面开发" 以及 "单个组件 -> SDK 库和框架 -> Windows 通用 C 运行时"

你可能会看到 `_declspec(dllexport)` 或者 `_declspec(dllimport)` 这两种声明, 它们是 Microsoft 的 C++ 扩展, 不在 C 或 C++ 的标准之内. 如果要求代码平台无关, 使用标准的 `extern` 声明就好了.

`dllMain`?

# 参考

-   https://medium.com/@Cu7ious/how-to-use-dynamic-libraries-in-c-46a0f9b98270
-   https://docs.microsoft.com/en-us/cpp/cpp/declspec
