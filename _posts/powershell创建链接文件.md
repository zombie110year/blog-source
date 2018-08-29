---
title: PowerShell创建链接文件
date: 2018-07-24 21:01:59
tags:
  - PowerShell
categories:
  - 日常
---
# PowerShell 创建链接文件

Linux 系统中, 用户可以随意创建软连接( SymbolicLink) 或 硬链接( HardLink). 而 Windows 好像就只能创建 "快捷方式" 了?

事实上, Windows 系统同样可以创建链接文件, 并且其效果和 Linux 下的 *Link 完全相同.

Windows 下链接文件的格式可以有:

- 软连接 SymbolicLink
- 硬链接 HardLink
- "Junction"

## 创建链接文件的 PowerShell 命令

**创建链接文件需要管理员权限** .

创建链接文件和创建普通文件使用的 PowerShell 命令相同, 只是需要加上特定的参数.

```powershell
New-Item -ItemType SymbolicLink -Path D:\Link -Value D:\Target #创建符号链接 D:\Link -> D:\Target
New-Item -ItemType HardLink -Path D:\Link -Value D:\Target #创建硬链接 D:\Link -> D:\Target. 注意, 硬链接只能链接两个文件, 不能链接两个目录
New-Item -ItemType Junction -Path D:\Link -Value D:\Target #创建 Junction D:\Link -> D:\Target
```

<!--more-->

在创建链接时, 可以使用 `-Force` 参数. 如果在创建链接之前, 目录中已经存在一个与链接同名的文件或子目录, 那么系统会报错 "NewItemError, resource exists", 并不会创建该链接. 那么, 就得使用 `-Force` 参数强行创建, 覆盖已经存在的文件或子目录.

## 移除/修改链接文件

我创建完一个从本博客所在目录到 Document 目录的符号链接之后, 发现该目录深度少了两级. 当我想要删除已经创建的链接时, 系统提示我"将删除其下所有子项, 是否继续?". 吓得我赶紧按下 N + 回车, 逃之夭夭.

我为此查询了微软的官方文档, 又 Google 了一翻. 结果发现这东西只管拉屎不管填坑啊! 连猫都不如啊混蛋! 😡

幸好经 [StackOverflow 上的这个回答](https://stackoverflow.com/questions/45536928/powershell-remove-symbolic-link-windows) 提示, 我想到了一个变通方案.

```powershell
New-Item -ItemType SymbolicLink -Path D:\Link -Value 'D:\$Recycle.Bin' -Force
```

我将该链接重新指向了一个空目录, 然后把它 `Remove-Item` 掉了, 之后重新创建了一个新的链接.

刚才在知乎提了一个问, [轮子哥回答](https://www.zhihu.com/question/286730188/answer/451072733) 说可以用 cmd 的 `rmdir` 命令来删除该链接. 经测试, 的确能删除, 并且文件依然存在于原目录.

PowerShell 到底有没有此功能? 在 [PowerShell在GitHub上的一个issue](https://github.com/powershell/powershell/issues/621) 里了解到微软正在解决这个问题. 但是根据实测的结果来看, 恐怕还是只能靠 cmd 来完成这个任务...

```powershell
PS D:\> Remove-Item .\LinkTest\

确认
D:\LinkTest\ 处的项具有子项，并且未指定 Recurse
参数。如果继续，所有子项均将随该项删除。是否确实要继续?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助
(默认值为“Y”):Y
rm : D:\LinkTest\ 是 NTFS 交接点。请使用 Force 参数删除或修改该对象。
所在位置 行:1 字符: 1
+ Remove-Item .\LinkTest\
+ ~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (D:\LinkTest\:DirectoryInfo) [Remove
   -Item], IOException
    + FullyQualifiedErrorId : DirectoryNotEmpty,Microsoft.PowerShell.Commands.
   RemoveItemCommand

PS D:\> Remove-Item .\LinkTest -Force

确认
D:\LinkTest 处的项具有子项，并且未指定 Recurse
参数。如果继续，所有子项均将随该项删除。是否确实要继续?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助
(默认值为“Y”):Y
rm : 请求中指定的标记与重分析点中存在的标记不匹配。
所在位置 行:1 字符: 1
+ rm .\LinkTest -Force
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Remove-Item], Win32Exception
    + FullyQualifiedErrorId : System.ComponentModel.Win32Exception,Microsoft.P
   owerShell.Commands.RemoveItemCommand
```

出现了 "请求中指定的标记与重分析点中存在的标记不匹配" 的问题... 等我搞明白这句话用英语怎么说就去 [GitHub](https://github.com/powershell/powershell/issues) 提 issue 去...

知乎上 [Gee Law的回答](https://www.zhihu.com/question/286730188/answer/451095023) 提出的方法:

```powershell
(Get-Item D:\LinkDir).Delete($false) # 无参数也行
```

调用 `DirectotyInfo.Delete()` 方法进行删除. 实测有效.

## 创建链接的用处

0. 区分对待同一根目录下的不同子目录使用 OneDrive 的策略.
    OneDrive 只能同步一个目录之下的所有子项. 若有一些经常变动且无关紧要的文件与需要注意保存和备份的文件处于同一目录下, 就可以通过在 OneDrive 目录之外创建目录, 并将其中需要同步的目录链接到 OneDrive 目录内的方式来达成目的.

## 小结

0. 使用 `New-Item -ItemType xxx -Path Link -Value Target` 创建链接.
0. 使用 `-Force` 参数使创建的链接覆盖同名文件/目录.
0. 使用 `(Get-Item .\Link).Delete()` 方法删除链接, 而不影响被链接的文件.