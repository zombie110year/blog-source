---
comments: true
title: PowerShell 安装 Chocolatey/Scoop
date: 2018-08-19 17:23:15
tags:
    - powershell
categories:
    - 日常
---

   更新：现在更推荐 `scoop <https://scoop.sh>`__

--------------


`Chocolatey <https://chocolatey.org/>`__

按官网指示下载安装
==================

首先需要检查 PowerShell 的脚本安全政策.

.. code:: powershell

   Get-ExecutionPolicy     # 查看当前政策

然后使用 ``Set-ExecutionPolicy`` 设置, 可以有以下选项:

.. code:: powershell

   有效值包括:

   -- Restricted:不加载配置文件或运行脚本. 默认值为"Restricted".

   -- AllSigned:要求所有脚本和配置文件由可信发布者签名, 包括在本地计算机编写的脚本.

   -- RemoteSigned:要求从 Internet 下载的所有脚本和配置文件均由可信发布者签名.

   # 我喜欢设置为 Unrestricted
   -- Unrestricted:加载所有配置文件并运行所有脚本. 如果运行从 Internet 下载的未签名脚本, 则系统将提示您需要相关权限才能运行该脚本.

   -- Bypass:不阻止任何执行项, 不显示警告和提示.

   -- Undefined:从当前作用域删除当前分配的执行策略. 此参数将不会删除在组策略作用域中设置的执行策略.

之后就运行
`官方提供的命令行 <https://chocolatey.org/install#install-with-powershellexe>`__

.. code:: powershell

   iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   # 其中 iex 通过 Get-Alias 查询到是 Invoke-Expression 的别名, 作用是之后的字符串识别为命令.

等待安装完成后, ``choco --help`` 检查安装是否成功.


先安装一个 Vim 试试
===================

   初次使用, 发现 chocolatey 貌似是通过发布安装脚本的形式来分发软件的.

下载时发现 ``choco`` 只能在管理员权限下使用, 在其他 shell
中会提示没有这个东西.

::

   Downloading vim
     from 'https://sourceforge.net/projects/cream/files/Vim/8.0.604/gvim-8-0-604.exe/download'
   Progress: 100% - Completed download of C:\Users\xxxxx\AppData\Local\Temp\chocolatey\vim\8.0.604\gvim-8-0-604.exe (9.22 MB).
   Download of gvim-8-0-604.exe (9.22 MB) completed.
   Installing vim...
   vim has been installed.
   Adding the vim installation directory to PATH …
   PATH environment variable does not have C:\Program Files (x86)\Vim\vim80 in it. Adding...
     vim may be able to be automatically uninstalled.
   Environment Vars (like PATH) have changed. Close/reopen your shell to
    see the changes (or in powershell/cmd.exe just type `refreshenv`).
    The install of vim was successful.
     Software installed as 'exe', install location is likely default.

   Chocolatey installed 1/1 packages.
    See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

虽然 ``choco`` 口口声声说了将 Vim 添加到 PATH 环境变量中了,
但是实测并没有, 还是需要手动添加… ``refreshenv`` 之后也无效… Vim
安装路径在第八行提示, 手动将这个路径添加进PATH.

……

发现路径被自动添加到系统环境变量了, 但是没有添加进用户环境变量,
但是按理说当前的环境变量是用户变量和系统变量的叠加才对啊,
难道需要重启才生效? 正好 Win10 有系统更新要安装, 先重启看看.

   重启之后就行了, Why?
