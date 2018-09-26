---
title:  Jupyter添加C++内核
data:   2018-09-23 11:47:11
mathjax:  false
tags:
    - Jupyter
    - C/C++
categories:
    - 日常
---

Jupyter Notebook 可以更换笔记本使用的内核, 除了 Python 之外, 还可以支持 C++!

要添加其他支持的语言, 在 [此链接](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) 查看支持的语言内核.

这些内核中, 有些是基于 Ipython Kernel 开发的, 因此需要在运行时指定, 并且在保存时为 `.ipynb` 文件, 例如 [bash kernel](https://github.com/takluyver/bash_kernel), [IOctave kernel](https://github.com/calysto/octave_kernel)(基于 Oct2Py) 等.

详细的方法见 [此文档](https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html).

# 安装 xeus-cling

[xeus-cling@GitHub](https://github.com/QuantStack/xeus-cling).

此仓库可以使用 `conda` 安装. 但是因为国内无此仓库(QuantStack)的镜像, 所以安装速度很慢.

## 从源代码安装 xeus-cling

经过一下午的尝试, conda 安装法失败了, 因为总是会遇到网络连接中断的问题, 所以这次从 [GitHub xeus-cling]() 下载源代码来安装.

# 安装 cling

[Cling kernel](https://github.com/root-project/cling/tree/master/tools/Jupyter) 是使 Jupyter Notebook 支持 C/C++ 语言的内核.

Cling 依赖于 Python3, 如果机器上没有安装, 需要先安装:

```sh
apt install python3 python3-pip
pip3 install ipykernel --user   # 将 ipython 内核安装到 Jupyter 中
```

然后就从源码构建 Cling 内核, 需要机器上安装由 cmake, git 工具. 如果没有就用 `apt` 安装.

0. 克隆代码仓库

```sh
git clone https://github.com/root-project/cling.git
```

1. 进到目录 `cling/tools/packaging/` 目录下, 利用 `cpt.py` 工具来安装.

```sh
./cpt.py --check-requirements # 检查依赖
./cpt.py --create-dev-env Debug --with-workdir=./cling-build/
```

检查依赖后, 会从 `http://root.cern.ch/git/llvm.git` 获取源码;
随后使用 cmake 编译, 以我的网络条件, 下载源码花费约 30 分钟, 编译约 50 分钟.

2. 全部编译安装完成后, 进入 `cling/tools/Jupyter/` 目录, 执行以下命令安装内核.

```sh
pip3 install kernel/
```

3. 之后使用 `jupyter kernelspec install kernel/cling-cpp17` 注册对应 C++ 标准的内核.

但是发现此方法安装的 cling 内核无法连接. 原因不明, 无法解决.

推荐使用 [xeus-cling](#安装-xeus-cling).

# 内核的安装位置

- 使用 Anaconda 安装的情况: `anaconda3/share/jupyter/kernels/`.
- 其他方法安装的情况: `.local/share/jupyter/kernels/`.

# jupyter kernelspec

`jupyter kernelspec` 是 Jupyter 的内核管理工具.

0. `jupyter kernelspec list` 列出已有内核.
0. `jupyter kernelspec install XXXX` 安装目标内核.
0. `jupyter kernelspec remove XXXX` 移除目标内核.
