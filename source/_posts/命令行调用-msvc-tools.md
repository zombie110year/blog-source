---
comments: true
title:  命令行调用 MSVC Tools
date:   2018-11-05 15:52:13
mathjax:  false
tags:
    - C/C++
    - MSVC
categories:
    - 日常
---

> Visual Studio 2017 Comunity 版

在学习 C/C++ 时, 需要编译源文件, 但是不希望为此而打开这个庞大的 IDE, 所以研究如何在命令行中调用它的编译工具链:

```
cl.exe      编译
link.exe    连接
lib.exe     加载 lib
nmake.exe   Makefile 的解析器
```

但是, 即便找到了这些可执行文件的路径, 还需要解决一大堆 include, lib 等等的搜索路径, 非常麻烦.
<!--more-->
# 使用官方提供的 bat 脚本

[微软为开发者准备了命令提示符](https://msdn.microsoft.com/zh-cn/library/f2ccy3wt.aspx?f=255&MSPPError=-2147217396)不过, 这些命令提示符打开的是 cmd, 没有 tab 补全, 体验还是不太好, 在进入后通过 `powershell -NoExit` 进入 PowerShell 环境就舒服多了.

# 自行配置环境变量

要自行配置环境变量, 需要进行这些步骤:

0. 将 MSVC 编译工具的路径添加到 `PATH` 环境变量中
0. 添加 `include`, `lib` 环境变量.

MSVC 的编译工具分布比较分散, 在 IDE 中, 就有 "32位机器编译32位程序", "64位机器编译32位程序", "64位机器编译64位程序" 等配置, 在学习 C/C++ 的时候, 随意选择一项即可, 比如选择 `Hostx64/x64`(64位机器编译64位程序) 这个配置, 就需要把对应的路径添加到 `PATH` 中.

而 lib, include 的路径也分为 VS 目录下, Microsoft SDKs 中以及 Windows Kit 中. 也分了多个目录. 在使用了官方提供的脚本后, 查看到环境变量发生了后面的变化, 因此将这些变量设置为对应的值应该就能正常工作了.

在配置了环境变量之后, 可以使用 `refreshenv` 指令在当前终端里刷新, 但是如果要每个终端都能使用, 则需要重启一下.

## VS_DIR WIN_KIT WIN_SDK

为了方便, 首先定义几个常用的路径为环境变量.

- `VS_DIR` 是 Visual Studio 的安装目录, 使用默认安装的话是在 `C:\Program Files (x86)\Microsoft Visual Studio` 中, 需要选择版本, 社区版则将这个变量设置为 `C:\Program Files (x86)\Microsoft Visual Studio\2017\Community`.
- `WIN_KIT` 则是编译 Windows 应用程序所需的头文件与库文件的目录, `C:\Program Files (x86)\Windows Kits`, 该目录下的子目录是各个版本的 Windows Kit, win10 的 Kit 命名为 `10`, win8 的则是 `8.1` 等等.
- `WIN_SDK` 是一系列开发工具包, 路径为 `C:\Program Files (x86)\Microsoft SDKs`, 其下也有一个 `Windows Kits` 目录, 不过里面是 `ExtensionSDKs` 暂时不知道是干什么的, 不过也添加上吧.

在 "环境变量编辑器" 里把这些变量各自赋值为:

```
VS_DIR=C:\Program Files (x86)\Microsoft Visual Studio\2017\Community
WIN_KIT=C:\Program Files (x86)\Windows Kits
WIN_SDK=C:\Program Files (x86)\Microsoft SDKs
```

## PATH

将 VS 的编译工具路径添加到 `PATH` 中, 在环境变量 `PATH` 中添加这些项目:

```batch
%VS_DIR%\VC\Tools\MSVC\14.15.26726\bin\Hostx64\x64;
::--------------------这里的数字是版本号, 最好在设置时到对应目录看一下
%VS_DIR%\Common7\IDE;
```

## include

```batch
%VS_DIR%\VC\Tools\MSVC\14.15.26726\lib\x64;
%WIN_KIT%\NETFXSDK\4.6.1\lib\um\x64;
%WIN_KIT%\10\lib\10.0.17134.0\ucrt\x64;
%WIN_KIT%\10\lib\10.0.17134.0\um\x64;
```

同样的, 不要搞错版本号.

## lib

```batch
%VS_DIR%\VC\Tools\MSVC\14.15.26726\include;
%WIN_KIT%\NETFXSDK\4.6.1\include\um;
%WIN_KIT%\10\include\10.0.17134.0\ucrt;
%WIN_KIT%\10\include\10.0.17134.0\shared;
%WIN_KIT%\10\include\10.0.17134.0\um;
%WIN_KIT%\10\include\10.0.17134.0\winrt;
%WIN_KIT%\10\include\10.0.17134.0\cppwinrt
```

# 使用 cl 编译器

可以通过 `cl -help` 查看帮助信息. 其中比较另人在意的部分有:

## 预处理

```
               -预处理器-

/AI<dir> 添加到程序集搜索路径           /FU<file> 强制使用程序集/模块
/C 不抽出注释                           /D<name>{=|#}<text> 定义宏
/E 预处理到 stdout                      /EP 预处理到 stdout，无行号
/P 预处理到文件                         /Fx 将插入的代码合并到文件中
/FI<file> 命名强制包含文件              /U<name> 移除预定义的宏
/u 移除所有预定义的宏                   /I<dir> 添加到包含搜索路径
/X 忽略“标准位置”                     /PH 在预处理时生成 #pragma file_hash
```

## 语言

```
                -语言-

/std:<c++14|c++17|c++latest> C++ 标准版
    c++14 – ISO/IEC 14882:2014 (默认)
    c++17 – ISO/IEC 14882:2017
    c++latest – 最新草案标准(功能集可更改)
/Zs 只进行语法检查
```

## 链接

```
                -链接-

/LD 创建 .DLL                           /LDd 创建 .DLL 调试库
/LN 创建 .netmodule                     /F<num> 设置堆栈大小
/link [链接器选项和库]                  /MD 与 MSVCRT.LIB 链接
/MT 与 LIBCMT.LIB 链接                  /MDd 与 MSVCRTD.LIB 调试库链接
/MTd 与 LIBCMTD.LIB 调试库链接
```

## 杂项

```
               - 杂项 -

@<file> 选项响应文件                    /?, /help 打印此帮助消息
/bigobj 生成扩展的对象格式              /c 只编译，不链接
/errorReport:option 将内部编译器错误报告给 Microsoft
    none - 不发送报告                       prompt - 提示立即发送报告
    queue - 在下一次管理员登录时，提示发送报告(默认)
    send - 自动发送报告                 /FC 诊断中使用完整路径名
/H<num> 最大外部名称长度                /J 默认 char 类型是 unsigned
/MP[n] 最多使用“n”个进程进行编译      /nologo 取消显示版权信息
/showIncludes 显示包含文件名            /Tc<source file> 将文件编译为 .c
/Tp<source file> 将文件编译为 .cpp      /TC 将所有文件编译为 .c
/TP 将所有文件编译为 .cpp               /V<string> 设置版本字符串
/utf-8 集源和到 UTF-8 的执行字符集
/validate-charset[-] 验证 UTF-8 文件是否只有合法字符

/Wall 启用所有警告                      /w   禁用所有警告

/Zi 启用调试信息                        /Z7 启用旧式调试信息
/Zo[-] 为优化的代码生成更丰富的调试信息(默认开启)
/ZH:SHA_256             在调试信息(实验)中将 SHA256 用于文件校验和
/Zp[n] 在 n 字节边界上包装结构          /Zl 省略 .OBJ 中的默认库名
/vd{0|1|2} 禁用/启用 vtordisp           /vm<x> 指向成员的指针类型
/ZI 启用“编辑并继续”调试信息          /openmp 启用 OpenMP 2.0 语言扩展
```

## 输出文件

```
               -输出文件-

/Fa[file] 命名程序集列表文件            /FA[scu] 配置程序集列表
/Fd[file] 命名 .PDB 文件                /Fe<file> 命名可执行文件
/Fm[file] 命名映射文件                  /Fo<file> 命名对象文件
/Fp<file> 命名预编译头文件              /Fr[file] 命名源浏览器文件
/FR[file] 命名扩展 .SBR 文件            /Fi[file] 命名预处理的文件
/Fd: <file> 命名 .PDB 文件              /Fe: <file> 命名可执行文件
/Fm: <file> 命名映射文件                /Fo: <file> 命名对象文件
/Fp: <file> 命名 .PCH 文件              /FR: <file> 命名扩展 .SBR 文件
/Fi: <file> 命名预处理的文件
/doc[file] 处理 XML 文档注释，并可选择命名 .xdc 文件
```

# 一些常用的命令

## 编译多个文件

```powershell
cl /Fe可执行文件名 ${files}     编译多个文件, 将最终生成的可执行文件命名
```

## 控制编译的进度

```powershell
cl /P ${files}  # 只进行预处理
cl /c ${files}  # 编译至 .obj 文件而不链接
```

## 保留汇编文件

```powershell
cl /FAs ${files} # 在完全编译之后保留汇编语言文件
```

> 暂时记录这么多

# 使用 nmake

据称 nmake 和 GNUmake 的语法一致, 可通过 [跟我一起写 Makefile](https://github.com/seisman/how-to-write-makefile) 学习

# 参考

- [带你玩转Visual Studio--命令行编译C/C++程序](https://blog.csdn.net/luoweifu/article/details/49847749)
