---
comments: true
title: Termux-Api
tags:
  - termux
categories: 日常
date: 2018-08-23 23:55:44
---

Termux: API
===========

附加应用程序, 它将设备功能作为 API 公开给 Termux 中的命令行程序.

安装
====

`F-Droid <https://f-droid.org/packages/com.termux.api/>`__

`Google
Play <https://play.google.com/store/apps/details?id=com.termux.api>`__

**重要提示: 请勿在 Google Play 和 F-Droid 之间混合安装 Termux
和它的扩展程序.** 从这些 Internet 门户混合安装时存在兼容性问题.
这是因为每个下载站都使用一个特定的密钥来安装 Termux 及其扩展.

安装 Termux-api 包
------------------

在安装了 ``Termux: API`` 的 ``.apk`` 包之后, 还需要在 Termux 中安装
``termux-api``.

.. code:: sh

   pkg install termux-api
   # 或者使用 apt
   apt install termux-api

设置
----

在 Android 7 上, 必须通过进入 “设置/受保护的应用程序” 菜单来来保护
“Termux: API”, 否则, 调用像 ``termux-battery-status`` 这样的 API
将永远挂起.

当前的 API 实例
===============

-  ``termux-battery-status`` 获取设备的电池信息.
-  ``termux-brightness`` 设置屏幕亮度, 值域为 [0, 255].
-  ``termux-call-log`` 列出历史通话记录.
-  ``termux-camera-info`` 获取设备摄像头的信息.
-  ``termux-camera-photo`` 调用相机拍摄照片, 保存为 ``JPEG`` 格式.
-  ``termux-clipboard-get`` 获取系统剪贴板.
-  ``termux-clipboard-set`` 设置系统剪贴板.
-  ``termux-contact-list`` 列出联系人信息.
-  ``termux-dialog`` 显示文本输入对话框.
-  ``termux-download`` 使用系统下载器下载资源.
-  ``termux-fingerprint`` 在设备上使用指纹传感器验证身份.
-  ``termux-infrared-frequencies`` 查询红外发射器支持的载波频率.
-  ``termux-infrared-transmit`` 传输红外图案.
-  ``termux-location`` 获取地理位置信息.
-  ``termux-media-player`` 播放媒体文件.
-  ``termux-media-scan`` MediaScanner 界面, 使 Android
   相册可以看到文件更改.
-  ``termux-microphone-record`` 使用设备上的麦克风录制.
-  ``termux-notification`` 显示系统通知.
-  ``termux-norification-remove`` 删除之前使用
   ``termux-notification --id`` 显示的通知.
-  ``termux-sensor`` 获取有关传感器类型和实时数据的信息.
-  ``termux-share`` 共享参数指定的文件或在 stdin 上接收的文本.
-  ``termux-sms-inbox`` 列出收到的短信.
-  ``termux-sms-send`` 将 SMS 信息发送到指定号码.
-  ``termux-storage-get`` 从系统请求文件, 并将其输出到指定的文件.
-  ``termux-telephony-call`` 拨打电话号码.
-  ``termux-telephony-cellinfo``
   从设备上的所有无线电获取有关所有观察到的小区信息的信息,
   包括主要和相邻小区.
-  ``termux-telephony-deviceinfo`` 获取有关设备的信息.
-  ``termux-toast`` 显示临时弹出通知.
-  ``termux-torch`` 在设备上切换 LED 灯.
-  ``termux-tts-engines`` 获取可用的TTS引擎的相关信息.
-  ``termux-tts-speak`` 使用系统 TTS 转换文本到语音.
-  ``termux-vibrate`` 振动设备.
-  ``termux-volume`` 更改系统音量.
-  ``termux-wallpaper`` 更改桌面壁纸.
-  ``termux-wifi-connectioninfo`` 获取当前连接的 WIFI 信息.
-  ``termux-wifi-enable`` 连接/断开 WIFI.
-  ``termux-wifi-scaninfo`` 获取上次 WIFI 扫描信息.

用法
====

可以在脚本或者交互式 Shell 中使用 API 命令.

一个使用 ``termux-clipboard API`` 的例子:

.. code:: sh

   $ termux-clipboard-set 'Hello World'    # 写入剪贴板
   $ termux-clipboard-get                  # 读取剪贴板
   Hello World
