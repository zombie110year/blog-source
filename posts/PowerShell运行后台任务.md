---
comments: true
title:  PowerShell运行后台任务
date:   2018-9-10 19:33:31
mathjax:  false
tags:
    - PowerShell
    - Windows
categories:
    - 日常
---

在 Linux 下, 我知道要运行一个 长期运行的, 不随当前终端的退出而结束的, 输出被重定向的后台任务, 可以使用 `nohup` 命令.

但是在 Windows 的 PowerShell 中, 有什么命令可以起到这样的效果呢?

<!--more-->

# `Start-Job`

```powershell
Cmdlet          Start-Job                                          3.0.0.0    Microsoft.PowerShell.Core
```

> `Start-Job` 在本地计算机上启动 PowerShell 后台任务.
>
> PowerShell 后台任务运行命令而不与当前会话交互. 当启动后台任务时, 任务对象会立即返回, 即使任务需要较长时间才能完成.
>
> 任务运行时, 您可以在不中断的情况下继续在会话中工作. 任务对象包含有关任务的有用信息, 但不包含任务结果. 任务完成后, 使用 > `Receive-Job` 获取任务的结果.

从描述上看, `Start-Job` 完全符合需求, 但是, 对于需要在后台一直运行的任务, 它总是会在运行之后很短的一段时间就结束了.

`Start-Job` 的一些有用的参数:

```powershell
-Name <string>          # 为任务取一个别名
-FilePath <string>      # 运行指定脚本
-LiteralPath <string>   # 与 -FilePath 作用相同, 只是禁止了通配符
-ScriptBlock {scripts}  # 运行指定代码块, 用花括号{} 包括的部分是代码块
```

## 管理 `Job`

```powershell
Get-Job     # 获取任务列表(包括已完成的或失败的), 可总览任务的运行情况.
Stop-Job    # 停止指定任务, 可用 -Name 或 -Id 指定
Remove-Job  # 将任务从任务列表中删除(否则它不会自己删除的)
Receive-Job # 获取任务运行结果, 如果是已经完成的任务, 会在获取后删除, 如果不想删除, 加 -Keep 参数
Suspend-Job # 将任务挂起
Resume-Job  # 恢复挂起的任务
```

# `Runspace`

参考:

- [从Powershell ***脚本学到的如何执行后台runspace~](http://blog.51cto.com/beanxyz/1787607)

对 Runspace 的一般使用方法就是:

```powershell
$scripts = {python pydrcom.py}  # 准备一个代码块(如果很短的话也可以直接写在后面的方法调用里)
$job = [powershell]::create()   # 从 PowerShell 类里创建一个实例 (这个实例就是 runspace 了?)
$job.addscript($scripts)        # 向 runspace 实例中加入将运行的代码
$job.begininvoke()              # 开始运行
```

要管理 Runspace, 使用 `Get-Runspace` cmdlet. 可以使用 `-Name` 或 `-Id` 或 `-InstanceId` 检索.

要关闭一个 runspace, 调用其 `close()` 方法即可. 一般来说, 会使用 `(Get-Runspace -Id 2).close()` 这样的语句, 用于将确定的 runspace 关闭.

当直接使用 `Get-Runspace` 的时候, 总会在 PowerShell 中发现早已存在的一个 Id 为 1 的 Runspace, 在关闭它之后, 整个终端就无响应了. 猜测, 从 `[powershell]` 创建的 Runspace 就是一个 PowerShell 的进程, 而一个 PowerShell 中 Id 为 1 的 Runspace 就是此终端本身.

# `Start-Process`

```powershell
Start-Process   # 启动进程
Stop-Process    # Kill 进程
Wait-Process    # 等待进程, 一般在 Stop-Process 之后使用, 等待进程确定被终止了再继续之后的语句
Get-Process     # 查询进程, 类似于 Linux 中的 ps
Debug-Process   # 调试进程, 会打开一个调试器附加到目标进程(需要安装 Visual Studio 或者其他调试器)
```

`Start-Process` 命令可用的参数有:

```powershell
-Filepath # 指定程序的路径，如果程序在 $env:Path 中，那么可以省略完整的路径
-ArgumentList # 一个使用逗号 , 分隔的列表。其中的每一个项应当为字符串。
# 如果使用 Linux 的参数风格， `-xxx` 则短线会与 Powershell 命令的参数前缀冲突，
# 需要显式使用引号 `''` 表明为字符串。
-WorkingDirectory # 工作目录，默认为 $pwd 得到的路径，可以修改为其他路径
-NoNewWindow # 不打开新的窗口，默认情况下是打开一个新的 conpty.exe 窗口执行命令的。
-RedirectStandardError
-RedirectStandardInput
-RedirectStandardOutput
# 三个标准流的重定向。

# 设定窗口风格
## 可选项 Hidden Maximized Minimized Normal
-WindowStyle
# 当选择 Hidden 的时候，不会出现窗口
```

例如，要在隐藏的窗口中启动 aria2c 进程:

```powershell
Start-Process -FilePath aria2c.exe -ArgumentList '-c','-D' -RedirectStandardError '$env:USERPROFILE/.aria2/err.log' -RedirectStandardOutput '$env:USERPROFILE/.aria2/out.log' -WindowStyle Hidden
```

如果不使用 `-WindowStyle Hidden` 的话, 任何进程都会新建一个窗口并运行.

由 `Start-Process` 命令启动的进程将拥有与当前 PowerShell 相同的父进程。

# 总结

使用 Runspace, 虽然成功让脚本在后台持续运行了起来, 但是脚本仍然不是独立于终端的, 当前会话一退出, Runspace 也关闭了. (并且我找不到 stdout 了)

三个需求只解决了一个, 但实在没有情报了. 因此, 该问题暂时搁置.

(凑合着用吧...)

TODO:

- `[class]::method()` 这样的语法是 `.NET` 的内容.
- [.NET教程](https://docs.microsoft.com/zh-cn/dotnet/standard/tour)
