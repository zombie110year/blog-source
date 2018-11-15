---
title:  利用 Windows.h 编写一个恶作剧弹窗
date:   2018-11-01 13:44:53
mathjax:  false
tags:
    - C/C++
    - 恶搞
categories:
    - 日常
---

# 不弹出控制台

使用编译器指令:

```c
#pragma comment(linker, "/subsystem:windows /entry:mainCRTStartup") // no console
```

# MessageBox 函数

## 函数原型

```c
int WINAPI MessageBox(HWND hWnd, LPCTSTR lpText, LPCTSTR lpCaption, UINT uType);
```

`WINAPI` 其实是宏定义 `#define WINAPI __stdcall`, 用于规定该函数的调用方式.

## 传递参数

- 第一个参数 `hWnd`, 表示该窗口的父窗口句柄, 如果没有父窗口, 则传入 `NULL`
- 第二个参数 `lpText` 传入一个字符串的首地址, 这个字符串将被显示在消息框中. 可以使用原声方法获得字符串的首地址, 也可使用 windows.h 提供的 `TEXT()` 函数来对一个字符串进行处理.
- 第三个参数 `lpCaption` 则是显示在标题栏的字符串.
- 第四个参数 `uType` 则是定义了 UI 的样式, 传入的无符号整数应当使用 [以下宏定义](#MessageBox-Flags):

如果要同时定义按钮以及图标的话, 可以对相应代码进行 "或" 位运算. 按钮都只使用了 16 进制的最后一位, 图标则只使用 16 进制的倒数第二位, 它们不会重合.

```c
#define MB_OK                           0x00000000L     // 一个 "确认" 按钮
#define MB_ICONEXCLAMATION              0x00000030L     // 警告标记 "!"
// 以上是 WinUser.h 中的宏定义

// 以下是在 main.cpp 中调用函数
MessageBox(hWnd, lpText, lpCaption, MB_OK | MB_ICONEXCLAMATION);
// 同时定义了 OK 按钮以及 ! 图标
```

## 返回值

当调用了 `MessageBox()` 函数后, 程序会在此处暂停, 直到按下 GUI 上的一个按钮才行.

按下一个按钮后, `MessageBox()` 函数会返回一个值, 这些值如下表:

```c
/*
 * Dialog Box Command IDs
 */
#define IDOK                1   // "确认"
#define IDCANCEL            2   // "取消"
#define IDABORT             3   // "中止"
#define IDRETRY             4   // "重试"
#define IDIGNORE            5   // "忽略"
#define IDYES               6   // "是"
#define IDNO                7   // "否"
#if(WINVER >= 0x0400)
#define IDCLOSE         8       // "关闭" 右上角
#define IDHELP          9       // "帮助" 工具栏
#endif /* WINVER >= 0x0400 */

#if(WINVER >= 0x0500)
#define IDTRYAGAIN      10
#define IDCONTINUE      11
#endif /* WINVER >= 0x0500 */

#if(WINVER >= 0x0501)
#ifndef IDTIMEOUT
#define IDTIMEOUT 32000
#endif
#endif /* WINVER >= 0x0501 */
```

<div id="MessageBox-Flags">

> 定义在头文件 `WinUser.h` 中

```c
/**
 * MessageBox() Flags
 */

/* 按钮 */
#define MB_OK                           0x00000000L     // 一个 "确认" 按钮
#define MB_OKCANCEL                     0x00000001L     // "确定" "取消"
#define MB_ABORTRETRYIGNORE             0x00000002L     // "终止" "重试" "跳过"
#define MB_YESNOCANCEL                  0x00000003L     // "是" "否" "取消"
#define MB_YESNO                        0x00000004L     // "是" "否"
#define MB_RETRYCANCEL                  0x00000005L     // "重试" "取消"
#if(WINVER >= 0x0500)
#define MB_CANCELTRYCONTINUE            0x00000006L     // "取消" "重试" "继续"
#endif /* WINVER >= 0x0500 */

/* 显示图标 */
#define MB_ICONHAND                     0x00000010L     // 错误标记 "X"
#define MB_ICONQUESTION                 0x00000020L     // 问题标记 "?"
#define MB_ICONEXCLAMATION              0x00000030L     // 警告标记 "!"
#define MB_ICONASTERISK                 0x00000040L     // 消息标记 "i"

#if(WINVER >= 0x0400)
#define MB_USERICON                     0x00000080L
#define MB_ICONWARNING                  MB_ICONEXCLAMATION
#define MB_ICONERROR                    MB_ICONHAND
#endif /* WINVER >= 0x0400 */

#define MB_ICONINFORMATION              MB_ICONASTERISK
#define MB_ICONSTOP                     MB_ICONHAND

#define MB_DEFBUTTON1                   0x00000000L
#define MB_DEFBUTTON2                   0x00000100L
#define MB_DEFBUTTON3                   0x00000200L
#if(WINVER >= 0x0400)
#define MB_DEFBUTTON4                   0x00000300L
#endif /* WINVER >= 0x0400 */

#define MB_APPLMODAL                    0x00000000L
#define MB_SYSTEMMODAL                  0x00001000L
#define MB_TASKMODAL                    0x00002000L
#if(WINVER >= 0x0400)
#define MB_HELP                         0x00004000L // Help Button
#endif /* WINVER >= 0x0400 */

#define MB_NOFOCUS                      0x00008000L
#define MB_SETFOREGROUND                0x00010000L
#define MB_DEFAULT_DESKTOP_ONLY         0x00020000L

#if(WINVER >= 0x0400)
#define MB_TOPMOST                      0x00040000L
#define MB_RIGHT                        0x00080000L
#define MB_RTLREADING                   0x00100000L

#endif /* WINVER >= 0x0400 */

#ifdef _WIN32_WINNT
#if (_WIN32_WINNT >= 0x0400)
#define MB_SERVICE_NOTIFICATION         0x00200000L
#else
#define MB_SERVICE_NOTIFICATION         0x00040000L
#endif
#define MB_SERVICE_NOTIFICATION_NT3X    0x00040000L
#endif

#define MB_TYPEMASK                     0x0000000FL
#define MB_ICONMASK                     0x000000F0L
#define MB_DEFMASK                      0x00000F00L
#define MB_MODEMASK                     0x00003000L
#define MB_MISCMASK                     0x0000C000L
```

</div><!--id=MessageBox-Flags-->

# 
