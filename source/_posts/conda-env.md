---
comments: true
title:  使用 conda 创建与管理虚拟环境
date:   2018-10-11 22:13:37
mathjax:  false
tags:
    - Python
categories:
    - Python
---

**不知道什么原因, 在 Windows 上, 必须在 cmd 中才能使用 conda 命令来管理虚拟环境, 在 PowerShell 中无法使用.**

<!--more-->

# 查看

使用 `conda list` 查看当前环境下安装的包, 使用 `conda env list` 查看已有的虚拟环境.

# 创建

使用 `conda create --name <环境名>` 创建一个虚拟环境, 至少需要指定一个 Python 的版本, 例如:

```sh
conda create --name <虚拟环境的名字> python=3.6 <安装的包的名字1> <安装的包的名字2> ...
```

创建的虚拟环境名能在 Anaconda 安装目录下的 `envs/` 下找到.

可以通过 `-p` 参数指定安装路径

```sh
conda create ... -p /path/to/target/dir
```

## 编写与读取 package 配置

可以将安装的环境编写到一个配置文件中, 方便一键安装.

配置文件 `.yml` 中可以设置环境的基础信息与安装包的列表.

使用 `-f` 参数指定配置文件.

```sh
conda env create -f=/path/to/environment.yml
```

一个 `.yml` 格式的配置文件, `name` 设置环境名, `dependencies` 设置创建环境时自动安装的包:

```yml
name: stats
dependencies:
  - numpy
  - pandas
  - ...
```

## 导出当前环境

使用 `conda env export --file <filename>` 将当前环境导出为 `.yml` 文件.
