---
layout: posts
title: LLDB 使用教程
date: 2019-08-12 20:22:10
tags:
-   LLDB
---

# LLDB 使用教程

LLDB 是 LLVM 项目下的一个调试器，它可以使用 Python 编写脚本，
脚本所用到的 Python 包也叫 lldb，可以通过 pip 安装。

在 Windows 平台上，LLVM 预编译包中的 lldb 不支持脚本，所以这里会介绍怎么自己编译它。
另外，8.0.0 版本的 LLDB 需要使用 3.6.x 版本的 Python。

<!-- more -->

## 编译 LLVM

先下载依赖项:

- git
- llvm 源码, clone LLVM 官方 git 仓库, 目前最新版本为 8.0.1
  - `git clone https://github.com/llvm/llvm-project.git` 可以下载到全部源码.
- cmake 工具, 到 https://cmake.org/download/ 下载最新版本即可.
- python 3.6.x 安装, 到 https://www.python.org/ftp/python/3.6.6/ 下载预编译包, 也可以下载 3.6.9 的源码自己编译.
- MSVC 编译器，如果不想要整个 IDE，可以仅安装 Build Tools。
  下载链接位于 [https://aka.ms/buildtools](https://aka.ms/buildtools) 中的 "所有下载" -> "Visual Studio 20xx 工具" -> "VS 20xx 生成工具"

> - http://llvm.org/docs/GettingStarted.html#checkout
> - http://lldb.llvm.org/resources/build.html#windows

在确保已经安装了 Python 3.6.x 和 cmake 后，就可以根据官方文档中的描述编辑 cmake 参数, 以生成合适的工程配置文件了:

```powershell
# powershell
cmake `
<# 构建 64 位程序 #> `
-Thost=x64 `
<# 生成 VS 2019 可用的工程文件 #> `
-G "Visual Studio 16" `
<# 指定 Python 解释器路径 #> `
-DPYTHON_HOME='C:\Program Files\Python36' `
<# 在无法找到 -DPYTHON_HOME 设置的解释器路径的情况下使用环境变量 PYTHONHOME 指定的路径或 PATH 中的路径 #> `
-DLLDB_RELOCATABLE_PYTHON=1 `
<# 因为没有编译 lld, 因此不运行测试 #> `
-DLLDB_ENABLE_TESTS=OFF `
<# 以 Release 模式编译 #> `
-DCMAKE_BUILD_TYPE=Release `
<# 指定安装路径 #> `
-DCMAKE_INSTALL_PREFIX='C:\Program Files\LLVM' `
<# 指定 CMakeLists.txt 所在路径 #> `
..
```

先打开 MSVC 提供的开发者命令行 *x64 Native Tools Command Prompt for VS 2019*, 在进入到指定位置后运行 msbuild 命令即可:

```powershell
msbuild -p:Configuration=Release -m <# 并行线程数 #> LLVM.sln
```

为了方便, 我是在国外的云服务商开了一台 Windows 虚拟机编译的.
使用了 scoop 作为软件管理工具. 为此, 编写了一个脚本来完成以上工作:

```powershell
# 下载 scoop
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
# 安装目标软件
scoop install git
scoop install cmake


# git 基本配置
git config core.username zombie110year
git config core.email zombie110year@outlook.com
git config core.autocrlf false

# 继续下载 Python
scoop bucket add versions
scoop install python36

# 克隆源码
git clone "https://github.com/llvm/llvm-project.git"
cd llvm-project
git checkout llvmorg-8.0.1 # 跳到最近的一个稳定版

# 然后需要手动下载并安装 MSVC
echo "https://aka.ms/buildtools"
```
