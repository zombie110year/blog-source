---
title: 基于 aliyun OSS+Serverless 搭建图床服务
date: 2020-02-29 18:51:00
tags:
  - 阿里云
  - 对象存储
  - Serverless
  - python
categories: 记录
---

准备
====

1. 一个域名：用作图床的管理界面和图片的链接
2. 一批 Serverless 函数：用于接受请求、查找图片、返回响应
3. 一个数据库：用于存储图片信息，以及可能会有的用户管理信息
4. 一个 OSS：存储图像文件
5. 一个服务器：（后续再选，如果有 Serverless
   函数处理不了的业务，再考虑）

域名准备
========

1. 购买
2. 解析
3. 备案

准备存储空间 —— 『OSS bucket』
==============================

在阿里云的 OSS 管理控制台创建一个新的 bucket， bucket
名不能与其他用户创建的重复，但由于最高支持 63 个字符，
我们可以以自身的用户名为前缀创建一个：\ ``zom-imgs``\ 。

其他需要注意的选项有：

1. 存储类型：图床服务一般适用 『标准存储』
2. 读写权限：私有，避免自己的图床上线后被人白嫖
3. 服务端加密：又不是什么机密数据，就不用加密了
4. 实时日志查询：开通！

防止白嫖：Referer 控制
----------------------

在创建好 bucket
后，可以在『权限管理』标签下的『防盗链』设置中配置允许访问的 HTTP
Referer。 阿里云 OSS 使用白名单模式配置。 我们在这里配置
**只允许图床的域名访问**\ 。

