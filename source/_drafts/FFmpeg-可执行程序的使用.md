---
title: FFmpeg 可执行程序的使用
date: 2019-05-13 11:23:58
tags: FFmpeg
categories: 日常
---

# 基础知识

## 视频编码格式与封装格式

## 比特率与帧率与分辨率

# ffmpeg 项目提供的可执行文件

- `ffmpeg`: 视频音频编码/解码
- `ffplay`: 基于 ffmpeg 构建的播放器
- `ffprobe`: 读取多媒体文件信息

## ffmpeg 参数

ffmpeg 常用参数:

```sh
ffmpeg -version # 查看 ffmpeg 版本以及可用的特性
```

ffmpeg 将命令行参数分为 "输入" 与 "输出" 两个分组, 以独立设置, 例如:

```sh
ffmpeg -vcodec libx264 -i input.mp4 -vcodec libvpx-vp9 -b:v 40000k -bufsize 40000k -y output.webm
```

- `-i input.mp4` 参数是输入文件, 在它之前的命令行参数在 "输入" 组,
- `-y output.webm` 参数是输出文件, 在它之前的命令行在 "输出" 组.
