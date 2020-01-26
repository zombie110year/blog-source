---
title:  git 中文出现乱码的解决方案
date:   2019-02-17 19:26:54
comments: true
mathjax:  false
tags:
    - git
    - encoding
categories:
    - null
---

`git log` 与 `git status` 时, 如果文件与 commit message 中含有中文,
那么就可能出现乱码.


```
    # git status 中的乱码

        new file:   "\350\247\243\345\206\263-conda-sslerror-\351\227\256\351\242\230.md"
```

```
    # git log 中的乱码

        <E4><BD><A0><E5><A5><BD><E4><B8><96><E7><95><8C>
```


对于 `git status` 中的乱码, 使用

```
    git config --global core.quotepath false
```

来解决.

对于 `git log` 中的乱码, 使用

```
    git config --global i18n.commitEncoding utf-8
    git config --global i18n.logOutputEncoding utf-8
```

解决.

前者设置提交时, message 以什么编码保存.
后者设置查看时, message 以什么编码传递给查看器.

在 Windows 中文版系统中,
由于系统编码为 gbk (cp936).
虽然可以通过注册表修改 (最新的 Win10 将这个功能放进了 语言与区域 设置面板中)
但是很多上年纪的程序 (比如各种破解版商业软件) 可能会因此崩溃或乱码,
所以不建议更改.

对于 Windows 可以单独设置.

```
    git config --global i18n.commitEncoding utf-8
    git config --global i18n.logOutputEncoding gbk
```

如果对 utf-8 有特别的执念, 一定要设置 logOutputEncoding 为 utf-8 的话,
就修改查看器的编码, 定义环境变量

```
    LESSCHARSET=utf-8
```

如果, 安装的 Git for Windows 是最小安装,
那么是不包含 less 程序的.
这样的话 `LESSCHARSET` 当然不起作用.
git log 会直接输出到终端.
这就必须设置为 gbk 才不会乱码了.

如果使用其他查看器,
从 less 类推, 修改相关的字符编码设置即可.
