---
title: Windows汇编语言环境
mathjax: false
tags:
  - Assemble
categories:
  - Assemble
date: 2018-09-02 13:53:51
---

# 使用 GCC (MinGW-w64) + Vscode

GCC 的一些参数

编译一个 C 程序的过程.

C 源代码 -> 预处理后的 C 源代码 -> 汇编 -> 编译至机器码 -> 链接为可执行文件

|GCC 参数|作用|备注|
|-|-|-|
|`-E`|预处理, 但不编译, 生成`.i`文件|实际调用`cpp`|
|`-S`|生成至汇编代码, 但不汇编, 根据 `--masm` 参数的不同, 生成`.s`或`.asm`文件|实际调用` `|
|`-c`|汇编至机器码, 但不链接生成`.o`或`.obj`文件|实际调用`as`|
|`--masm=`|配置汇编格式|`intel`, Intel 格式; `att` AT&T 格式|

MinGW-w64 的 as.exe 对 intel 格式的汇编有问题, **不识别扩展名**, 所以编译 intel 格式的汇编文件时仍然使用 `.s` 扩展名. 经测试, 运行状况正常.

```
# 使用 .asm 扩展名时的报错.
ld.exe:./test.asm: file format not recognized; treating as linker script
ld.exe:./test.asm:1: syntax error
collect2.exe: error: ld returned 1 exit status
```

**未发现可行的图形化调试方法** 暂时放弃该方案.

# 使用 Vitual Studio

测试了一下书上抄来的代码:

```asm
	.386
	.model	flat
	.stack	100
	.data
num1	sdword	?
num2	sdword	?
	.code
main	proc
	mov	num1,	5
	mov	eax,	num1
	mov	num2,	eax
	ret
main	endp
	end
```

遇到以下错误, 正在寻找解决方案

```
LINK: error LNK2001 : 无法解析的外部符号 _mainCRTStartup
test.exe : fatal error LNK1120: 1 个无法解析的外部命令
```

[Visual Studio2017汇编环境教程](https://zhuanlan.zhihu.com/p/31918676)
[使用visual studio编译运行汇编程序](https://cfhm.github.io/2017/10/18/asm-1/)