---
title: HTTP 和 HTTPS
date: 2019-04-28 12:56:49
tags:
- Network
- HTTP
---

# HTTP 协议

HTTP (Hypertext Transfer Protocol) 超文本传输协议, 是一个应用层协议.

它通过客户端 Client 和 服务端 Server 建立一个 TCP 链接, 从而进行数据的传输.

HTTP 所传输的数据称为 [HTTP 报文](#HTTP-报文), 在一个报文中, 报文分为 请求(Request) 和 响应(Response) 两种类型, 这两种类型都可以在数据段中携带任意数据.

为了安全(security), HTTP 协议可以和 TLS 或者 SSL 结合, 为报文的传输添加 加密/解密 功能. 这样的 HTTP 协议被称为 HTTPS.

HTTP 协议的版本经过了以下发展历程:

|   版本   | 文档     | 备注                                                         |
| :------: | -------- | ------------------------------------------------------------ |
| HTTP/1.0 | RFC 1945 |                                                              |
| HTTP/1.1 | RFC 2616 | HTTP/1.1 2019 年也是使用最多的协议版本, 尽管它是在 1997 年被标准化的. 它在 1999 年升级了一次, 在 2000 年被添加了 TLS 功能. |
| HTTP/2.0 | RFC 7540 | HTTP/2.0 是对 HTTP/1.1 协议的升级, 它在 2015 年被标准化; 最大的特点就是支持一个 HTTP 连接的复用. |
| HTTP/3.0 |          | 目前仍为草案                                                 |

> HTTP/1 版本, 是一个 HTTP 连接传输一个资源, 而 HTTP/2 允许一个 HTTP 连接传输多个资源.

## HTTP 连接过程

在一次 HTTP 链接中, 客户端与服务端进行了如下行为:

1. 客户端与服务端的一个端口端口(HTTP标准要求为 80, 可设置为任意端口) 初始化一个 TCP 连接. (TCP 属于传输层协议, 不在应用层讨论)
2. 客户端发送请求报文.
3. 服务端返回响应报文.
4. 完成一次 HTTP 连接, 根据设置, 关闭或维持此 TCP 连接以便下次 HTTP 连接.

### 长连接与短连接

一次 HTTP 连接, 会在开始时建立 TCP 连接, 结束时关闭 TCP 连接, 如果要多次传输资源, 就会导致 TCP 连接多次建立与关闭.
这种连接方式被称作 *短连接*.

而 *长连接* 呢, 则是建立一次 TCP 连接后, 在同一个 TCP 连接中完成多次 HTTP 连接, 直到最后才将其关闭.

在 HTTP 报文中, 可以通过 `Connection` 关键字来设置连接方式.
在 HTTP/1.0 中, 默认采用短连接方式, 而在 HTTP/1.1 后, 就默认采用长连接了.

在请求报文中, 设置 `Connection` 关键字为 `keep-alive` 或者 `close` 来显示地声明连接方式:

```http
# 保持连接
Connection: keep-alive

# 响应完成后关闭连接
Connection: close
```

> 参考 http://www.firefoxbug.com/index.php/archives/2806/

# HTTP 报文

## 请求报文

```http
${method} ${uri} ${http_version}
${headers}

${datum}
```

一个请求报文由三个段落组成:

1. 请求语句, 需要三个要素: HTTP 方法, 资源标识符, HTTP 协议版本
2. 请求头, 是一系列键值对.
3. 请求体, 是将会传输给服务端的数据. POST 方法可以携带请求体. 对于其他不接待数据的方法, `${datum}` 段为空.

一次典型的 GET 请求是这样的:

```http
GET https://github.com/dashboard/recent-activity HTTP/1.1
Host: github.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: */*
Accept-Language: zh,en-US;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://github.com/
X-Requested-With: XMLHttpRequest
DNT: 1
Connection: keep-alive
Cookie: logged_in=yes; user_session=atPhqIFY6tL1eW4... # Cookie 剩下的值被隐藏了
If-None-Match: W/"2501550c7b185e7ec3d68484f0c37165"
```



# HTTP 方法

# HTTPS

# HTTP 调试工具

# Cookie
