---
layout: posts
title: nodejs HTTP 客户端与 HTML 解析
date: 2019-07-29 16:56:15
tags:
  - nodejs
  - axios
  - cheerio
---
# Node.js HTTP 客户端与 HTML 解析

和 Python 下载器相比，Node.js 下载器在获取需要运行 JavaScript 代码才能得到的数据时更加方便，
毕竟它自身就是一个 JavaScript 解释器。

要使用 Node.js 编写爬虫应用，一般可以使用 `axios` 和 `cheerio` 两个 npm 包，前者是一个易用的 ajax 封装，
后者则是简单化的 jQuery，用来查询 DOM。

另外，由于 axios 是异步执行的，一处异步，处处异步，需要将编码的思维和一般的 Python 有显著差异。

<!-- more -->

## axios 的用法

axios 的 GitHub 上的 [README](https://github.com/axios/axios#example) 介绍了它的详细用法。

简单总结一下，就是：

axios 的基本 API 是

```javascript
axios({/* config */})
```

在 config 对象中可以进行如下配置:

|        字段         |               类型               |      必填/默认值      | 用途                                                                                               |
| :-----------------: | :------------------------------: | :-------------------: | -------------------------------------------------------------------------------------------------- |
|        `url`        |              String              |         必填          | 请求资源的 URL                                                                                     |
|      `method`       |              String              |         `get`         | HTTP 请求方法                                                                                      |
|      `baseURL`      |              String              | 当 `url` 不完整时必填 | 连接在 `url` 之前，补全为完整的 URL                                                                |
| `transformRequest`  | `Array[function(data, headers)]` |  原样返回数据的函数   | 在发送之前根据 headers 转换 data                                                                   |
| `transformResponse` |     `Array[function(data)]`      |  原样返回数据的函数   | 在响应之后转换 data                                                                                |
|      `headers`      |              Object              |         `{}`          | 设置 HTTP 请求头                                                                                   |
|       `param`       |              Object              |         `{}`          | URL 参数                                                                                           |
|       `data`        |      Object, ArrayBuffer 等      |         `{}`          | HTTP 请求体                                                                                        |
|      `timeout`      |              Number              |         1000          | 超时极限                                                                                           |
|  `withCredentials`  |               Bool               |         false         | 允许跨域                                                                                           |
|       `auth`        |  `{username: "", password: ""}`  |                       | 基本的 HTTP 认证                                                                                   |
|   `responseType`    |              String              |         json          | 响应体类型, 可选 arraybuffer, document, json, text, stream 等，在未设置 `transformResponse` 时有效 |
| `responseEncoding`  |              String              |         utf8          | 响应体的字符编码                                                                                   |

还有其他的一些参数, 不太常用, 因此不在此列出, 需要的自己去 GitHub 上看。

根据不同的 HTTP 方法， axios 提供了简写, 常用的有 get 和 post, 其他方法也有, 但不在此列出:

```javascript
axios.get(url, {/* config */})
axios.post(url, data, {/* config */})
axios.delete(url, {/* config */})
// 等
```

每一个 axios 调用都会返回 Promise, 因此需要用 `.then` 链式调用。它的返回值为这样的一个对象：

```javascript
{
  // data 是服务端返回的响应体
  data: {},

  // `status` 是响应的 HTTP 状态码
  status: 200,

  // `statusText` 是 HTTP 状态码对应的消息
  statusText: 'OK',

  // `headers` 是响应头，所有字段都是小写字母
  headers: {},

  // `config` 是原样的请求的设置
  config: {},

  // `request` 是发起这次请求的对象，在浏览器，是一个 XMLHttpRequest，
  // 在 node.js， 是最后一个 ClientRequest
  request: {}
}
```

在确认返回正常后，可以直接取用 `resp.data` 数据，它的类型根据发出请求时 `responseType` 的设置不同而不同，或者
通过 `transformResponse` 自行转换（比如解密等，此时的类型为默认的 json）。

## cheerio 使用方法

https://github.com/cheeriojs/cheerio

cheerio 用来解析 html 文本，将其转化为一个 DOM 对象，然后可以使用 CSS 选择器来查找元素。
通常会将解析的 DOM 命名为 `$`，这是 jQuery 的命名习惯。

```javascript
let $ = cheerio.load(/* html text */)
```

然后

```javascript
$(/* CSS 选择器 */)
```

查找元素。

## 几种页面的示例

todo
