---
title:  解决 Conda SSLError 问题
date:   2019-02-17 19:11:08
comments: true
mathjax:  false
tags:
    - anaconda
---

在我重装了一次系统之后,
我发现 Anaconda 用不了了.

```
> conda update conda
Solving environment: failed

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/win-64/repodata.json>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.
SSLError(MaxRetryError('HTTPSConnectionPool(host=\'mirrors.ustc.edu.cn\', port=443): Max retries exceeded with url: /anaconda/cloud/conda-forge/win-64/repodata.json (Caused by SSLError("Can\'t connect to HTTPS URL because the SSL module is not available."))'))
```

<!--more-->

我最开始还以为是安装包出错, openssl 模块文件损坏了.
为此还多次重装, 甚至回滚到旧版本.
但是问题依然没有解决.
令人恶心万分.

好在, 在 [这个issue](https://github.com/conda/conda/issues/8046) 得知,
需要安装 openSSL.

我跑 C:\WINDOWS\System32 里面一看,
果然没有任何 openssl 相关的东西.

看来是需要链接一个 openssl 的动态链接库,
而不是操作 Python 的 openssl 标准库.

在 [https://slproweb.com/products/Win32OpenSSL.html](https://slproweb.com/products/Win32OpenSSL.html)
下载 OpenSSL 的 Windows 安装包.

对于 Win10 64bit 的,
应当选择 Win64 开头的版本,
例如本文撰写时最新的 Win64 OpenSSL v1.1.1a.

Win32 开头的版本是 32bit 系统使用的.

运行下载的 exe 或 msi 安装包,
发现协议里要求捐款,
不过也可以不管.

根据提示一路 "next",
当 "安装 DLL 到 System 目录" 的选项出现时,
勾选它.

安装了 OpenSSL 之后,
弹出了请求捐款的选项,
如果没兴趣的话,
可以取消掉再点 finish,
否则会弹出一个支付网页.

安装 OpenSLL 之后, conda 的运行就正常了.

想起之前重装的过程,
感觉我的 SSD 在疯狂 -1s. 😭
