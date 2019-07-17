---
comments: true
title: 布置PowerShell工作环境
tags:
  - PowerShell
categories:
  - 日常
date: 2018-08-21 14:00:46
---

<!--more-->

# 推荐 ConEmu

原生 PowerShell 的使用体验... 怎么说呢, 只谈工作肯定是没问题的, 但是它不好看啊.

首先, 一旦将 PowerShell 字符集切换到 UTF8 , 就会出现输入中文字符时只显示一半的毛病;

其次, 一旦启用 `oh-my-posh` 的 `Agnoster` 主题, 就会发生光标错位的问题.

但是, ConEmu 就没有这些问题...

因为要同时使用 ConEmu 与 Terminal on VsCode, 需要让 ConEmu 启动时启用 `oh-my-posh` 但是使用 VsCode 时不启用.

在 ConEmu 的 task 设置中, 如果直接设置

```
powershell Start-ConEmu
```

会导致执行完命令就退出. 需要加上参数 `-NoExit`

```
powershell -NoExit Start-ConEmu
```

这样, 执行完我自定义的函数后, PowerShell 就不会退出了.

> 2019 年, 微软也要做个新终端了, 来看看吧: https://github.com/microsoft/terminal

# Git

## Git Windows version

在 [官网](https://git-scm.com/downloads) 安装对应版本.

## posh-git

[posh-git](https://www.preview.powershellgallery.com/packages/posh-git) 是一个 PowerShell 模块, 主要有以下功能:

- 提供了 PowerShell 下 git 命令的补全功能;
- cmdlet 格式的 git 命令; (并不打算用...)
- PowerShell 中的 Git 状态提示符.(oh-my-posh 的依赖)

需要使用 `Import-Module` 启用.

# Vim

## 使用安装包安装

[参考官网](https://www.vim.org/download.php#pc)

## 使用 chocolatey 安装

[我的上篇文章](/2018/PowerShell-安装-Chocolatey/#先安装一个-vim-试试)

# oh-my-posh

喜欢 `oh-my-zsh` 的终端风格, 在网上了解到 PowerShell 也有一款叫做 `oh-my-posh` 的模块.

这里是它的官网: [oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh) .

安装该模块, 先在 PowerShell 中使用 `Find-Module oh-my-posh` 查找是否能连接上 [PowerShell Gallery](https://www.powershellgallery.com).

如果输出以下信息,

```powershell
Version    Name                                Repository           Description
-------    ----                                ----------           -----------
2.0.223    oh-my-posh                          PSGallery            Theming capabilities for the PowerShell prompt in ConEmu
```

就直接使用 `Install-Module oh-my-posh` 安装. 之后可以使用 `Import-Module oh-my-posh` 载入模块, 使用 `Set-Theme XXX` 设置主题.

<!--最好看的主题是 Agnoster-->

建议在 ConEmu 中使用.

# user.poshrc

要想让 PowerShell 执行用户编辑的脚本, 需要设置安全策略:

```powershell
# 查询当前安全策略
Get-ExecutionPolicy
# 设置当前安全策略
Set-ExecutionPolicy XXX
## 可设置的策略:
### Restricted          不运行任何脚本, 包括配置文件
### AllSigned           所有脚本必须签名
### RemoteSigned        不限制本地编辑的脚本, 但是从网络下载的脚本必须有签名
### Unrestricted        完全不受限制, 但是如果运行从网络下载的脚本, 系统会提示
### Bypass              啥都不管, 随便你运行什么也一句话都不说
### Default             Restricted
### Undefined           从当前作用域删除当前分配的执行策, 此参数将不会删除在组策略作用域中设置的执行策略. (没接触过相关领域, 这个看不懂了...)
```

## 编辑 $PROFILE

PowerShell 的 `$PROFILE` 变量存储它的配置文件路径(这个配置文件对本机所有用户生效, 不过很多 Windows 都是单用户吧), 在 PowerShell 启动时便会运行. 如果没动过它的话, 它就是空的.

最好将自己的设置项放在用户目录中, `$PROFILE` 里只需要放一句 "执行对应脚本" 就好了.

我自己的 `$PROFILE` 里只有这个内容:

```powershell
. $HOME\.psconfig\poshrc.ps1
```

意思是执行 `poshrc.ps1` 脚本, 那是个自己编辑的文件. (注意有个点号 `.`, 这是为了导出变量的作用域!)

## 组织配置目录

按照自己的习惯, 我在自己的 `$HOME` 目录下新建了一个目录 `.psconfig` . 这个目录有着如下结构:

```
.psconfig/
    poshrc.ps1      //存放用户配置, 主要
    alias.ps1       //存放 alias
    userfunc.ps1    //存放 自定义函数
```

### poshrc.ps1

这是 `.psconfig` 的主要部分, 要设置什么就都写进这个文件里. 为了方便清晰, 我将设置别名(alias)和定义函数的文件分开了, 就是同路径下的 `alias.ps1` 和 `userfunc.ps1` 文件.

我的 `poshrc.ps1` 内容大概为以下部分

```powershell
# Define functions
. $Home/.psconfig/userfunc.ps1

# Set alias
Import-Alias $Home/.psconfig/alias.ps1

# Set variabilities
# ...

# Others
```

0. 首先, 定义函数(放在一个单独的文件里了);
0. 之后, 设置别名, 这里有两种办法, 一种是 `Set-Alias 别名 原名`, 一种是 `Import-Alias`. 如果是前者, 就像普通的脚本一样运行它就好, 如果是后者, 虽然不限制文件后缀名, 只要是个纯文本就行, 但是需要特殊的语法:
0. 再之后, 就设定一些经常使用的变量. 如果很多, 又有针对性, 也可以单独放一个文件.
0. 最后, 就是其他要设置的东西.

### alias.ps1

这个文件里存放定义的别名, 可以使用 `Set-Alias XXX YYY` 的语法一个个设置, 也可以写成 CSV 格式通过 `Import-Alias` 导入.

#### csv(逗号分割值) 文件格式

```powershell
# Import-Alias 需要使用以下语法:
#别名   原名             鬼知道什么东西   作用域
#====== =============== =============== =======
"grep", "findstr.exe",  "" ,            "AllScope"
# 一行一条, 空格可忽略.
# 第三项实在不知道是什么, 但是又必须要有...
```

### userfunc.ps1

```powershell
function name($args) {
  ...
}
```

定义函数. 对于函数名, 官方建议使用驼峰命名法, 就和其他 cmdlet 差不多. 确实很好看.

比如, 我写这个博客, 觉得每次 `Hexo generate` 生成的文件里空行太多了, 而且文本位置也不固定, 导致每次 `git push` 的时候都有大量不必要的修改被上传, 再加上想要把 HTML 文档格式化. 于是想要重新定义一个工作流:

```powershell
function Make-Blog() {
  $origin_location = Get-Location       # 获取当前路径, 做完事跳回来
  Set-Location $Blog                    # 这个变量定义在 poshrc 里了, 是博客的根目录
  hexo g
  jdf format ./public                   # 调用 jdf 对 html 文档进行格式化
  git add *
  git commit
  git push                              # 把博客的所有东西存到 GitHub(public/ 和 themes/ 设置了 gitignore)
  cp -Force ./public/* ../.hexo.deploy  # 把要发布的内容复制到另一目录.
  Set-Location ../.hexo.deploy
  git add *
  git commit -m "Uploaded"
  git push                              # 把发布的页面推送到这个博客的仓库
  Set-Location $origin_location
}
```

> 因为用了 Travis-CI {% post_link 为-Hexo-博客添加自动集成 为 Hexo 博客添加了自动集成 %}, 这个函数被弃用了.
