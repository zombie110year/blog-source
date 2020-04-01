---
layout: posts
title: JavaScript ajax
date: 2019-06-25 20:12:47
tags:
-   javascript
categories: 笔记
---

Asynchronous Javascript And XML
===============================

如标题所述, ajax 就是 “异步的 JavaScript 与 XML”,
它的作用就是在当前页面打开的情况下,
通过异步的方式从其他地址获取数据并通过 JavaScript 运算.
常用于动态更新页面.

.. raw:: html

   <!-- more -->

要实现这一点, 可以使用浏览器内置对象 ``XMLHttpRequest`` (以后简称
``xhr``). 在使用时, 需要完成这些任务:

1. 实例化 xhr 对象.
2. 构造 HTTP 请求.
3. 发送 HTTP 请求.
4. 获取响应请求.

但是, 由于需要异步处理, 因此只能使用事件监听的方式使用.
在发送了请求之后, xhr 实例经历这些事件的发生:

1. ``loadstart`` 请求开始
2. ``progress`` 浏览器接收数据包(根据 HTTP 协议, 可能进行多次)
3. ``abort`` 调用了 ``xhr.abort()`` 方法而中止了请求
4. ``error`` 出现错误而终止请求
5. ``load`` 请求成功, 得到了服务器的响应
6. ``timeout`` 请求超时(在设置了 timeout 后才会生效)
7. ``loadend`` 请求完成
8. ``readystatechange`` 请求状态改变

在交互式的 console 中, 发出请求后可以随时查看 xhr 的状态.
而在编写的代码中, 由于请求与响应都是异步的, 如果不想写一个死循环不断查询
xhr 状态的话, 就需要重写这些事件的监听器, 让事件发生时, 自动进行处理.

要为事件添加监听器, 可以重写对象的 ``on*`` 属性, 也可以调用对象的
``addEventListener`` 方法.

.. code:: javascript

   // onload 监听 load 事件, 同理, 其他监听器名为 on*. 使用赋值的方式设置该监听器的事件处理函数
   xhr.onload = function(event) {/* 做点事情, 可以用 this 来指向 xhr 实例 */};

.. code:: javascript

   // 为 load 事件添加一个监听器, 其事件处理函数在第二个参数提供
   xhr.addEventListener("load", function(event) {/* 做点事情, 可以用 this 来指向 xhr 实例 */});

以上两种添加事件监听器的方法是一样的. 有两点需要注意:

1. 事件监听器在使用箭头函数的情况下, 用 ``event.target`` 指向对象本身.
   因为在 ``() => {}`` 箭头函数中使用 this 将会在对象的上下文中寻找,
   不是指向对象本身. 而根据 Event API 的要求, ``event.target``
   将指向触发事件的对象.
2. 事件处理函数接收 event 本身为参数, 但一般不会在函数体中处理它.
   关于它的详细信息, 参考 `MDN 文档 -
   Event <https://developer.mozilla.org/zh-CN/docs/Web/API/Event>`__.

对于一次典型的请求, 其代码可编写如下, 这里以请求本站的 ``robots.txt``
为例:

.. code:: javascript

   (() => {
       "use strict";
       // 实例化 xhr 对象
       let xhr = new XMLHttpRequest();

       // 为 load 事件添加监听器
       xhr.addEventListener("load", function (e) {
           if (this.status != 200) {
               console.error(`${this.status}: ${this.statusText}`);
           } else {
               console.log(this.responseText);
           }
       });

       // 设置请求参数, 使用 GET 方法, 请求 /robots.txt URL
       xhr.open("GET", "/robots.txt");
       // 发送请求
       xhr.send();

       // 等到服务器响应后自动调用 onload 函数
   })();

当一次请求完成后, xhr 的状态将会发生改变, 可以使用 ``open``
函数重新打开另外的请求并使用 ``send`` 发送. 不过更推荐一个 xhr
实例负责一个请求. 另外, 需要注意的是请求默认不能跨域.
也就是说在本站内发送的 ajax 请求之内请求同一域名下的资源.

`open 函数 <https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/open>`__
------------------------------------------------------------------------------------

xhr 的 open 函数只初始化请求, 要发送请求还需要调用 send 函数,
可接收这些参数:

.. code:: javascript

   xhr.open(method, URL, async, user, password)

除了 ``method`` 和 ``URL`` 是必须参数之外, 另外三个参数都是可选的.

-  ``method``: 本次请求使用的 HTTP 方法, 常用 GET, POST.
-  ``URL``: 统一资源定位符. 一般可理解成 “网址”
-  ``async`` \*: ``true`` 或 ``false`` 控制本次请求是异步还是同步.
   默认为 ``true``, 异步.
-  ``user`` \*, ``password`` \*: HTTP 基本认证.

`send 函数 <https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/send>`__
------------------------------------------------------------------------------------

xhr 的 send 函数将发送请求. 它也可以接收一个参数用作请求体.
请求体可以是字符串, Blob 对象(二进制文件)或者一个 FormData
对象(用于发送表单数据).

.. code:: javascript

   xhr.send(body)

默认情况下, ``body === null``. 但也可以带上请求体, 可以是一个 Bolb 对象,
那样相当于发送了这个 Bolb 对象的二进制内容. 用 FormData
对象发送表单数据, 用字符串发送自定义数据. 如果要发送一个对象, 可以使用
``JSON.stringify`` 将之编码为字符串再发送.

请求头与响应
------------

在发送请求之前, xhr 对象可以通过 ``setRequestHeader`` 来设置请求头.
请求头是以键值对的方式存储的, 这个方法接受两个参数: ``header`` 和
``value``, 如果要设置多个请求头, 就需要多次调用此方法:

.. code:: javascript

   xhr.setRequestHeader(header, value)

这个方法需要在 **open之后, send之前** 调用.

在得到服务器响应之后, 可以使用 ``xhr.status`` 获取响应状态码(HTTP
状态码) 用 ``xhr.statusText`` 获取对应的文本. 至于响应内容, 可以通过
``xhr.responseText`` 获取其字符串形式, ``xhr.responseXML`` 获取其解析为
DOM 的形式, ``xhr.response`` 则是根据 ``xhr.responseType``
的值自动确定其形式. 可能是 ArrayBuffer, Blob, DOM, JSON, Text 等.

如果要得到响应头, 可以使用 ``xhr.getResponseHeader(name)``
来获取一个指定的头, 用 ``xhr.getAllResponseHeaders()``
获取用对象表示的所有响应头.

提交表单数据
------------

对于在 HTML 页面中的一个表单:

.. code:: html

   <form name="login">
     <input name="username"type="text">
     <input name="password" type="password">
   </form>

可以在提交时调用 ``new FormData`` 构造函数将之打包成 FormData 对象,
并直接通过 send 函数发送.

.. code:: javascript

   let data = new FormData(document.forms.login);
   xhr.send(data);

跨域访问
--------

出于网络安全的考虑, 发送 ajax 请求时, 只能请求同一域名下的资源,
要实现跨域访问, 需要先设置 ``xhr.withCredentials`` 为 ``true``:

.. code:: javascript

   xhr.withCredentials = true;
   xhr.open("GET", "https://github.com/");
   xhr.send();

当然, 还有另一个限制, 那就是目标的 ``Access-Control-Allow-Origin``
响应头. 在响应来自外部的请求时, 服务器会根据本地设置的
``Access-Control-Allow-Origin`` 响应头来决定是否响应请求,
这个响应头中设置了允许被跨域访问的站点, 例如在
``https://api.zombie110year.top`` 服务器上设置:

.. code:: http

   Access-Control-Allow-Origin: https://zombie110year.top

这个头设置了只允许从 ``https://zombie110year.top``
域名跨域访问该域名下的资源. 也可以将这个头设置为通配符 ``*``,
以此允许所有域名都可以跨域访问该域名下的资源.

这是通过后端的服务器设置的, JavaScript 对此无能为力.

playground
----------

用 node.js 搭建一个简单的服务器.
这个服务器的作用就是返回人类可读的请求头与请求体.
在本地搭建此服务器后自行实验 ajax 请求的细节吧.

.. code:: javascript

   //! node


   var http = require("http");
   var querystring = require("querystring");

   var server = http.createServer(function (require, response) {
       "use strict";
       // 从 require 中读取信息
       // https://nodejs.org/dist/latest-v10.x/docs/api/http.html#http_class_http_incomingmessage
       var method = require.method;
       var url = require.url;
       var header = require.headers;
       var body = '';

       // 向 response 写入信息
       // https://nodejs.org/dist/latest-v10.x/docs/api/http.html#http_class_http_serverresponse
       response.write(`${method} ${url}\n`);
       for (var key in header) {
           response.write(`${key}: ${header[key]}\n`);
       }

       require.on("data", function (chunk) {
           body += chunk;
       });

       require.on("end", function () {
           response.write("\n");
           response.write(body);
           response.end();
       });
   });


   server.listen(8080, "localhost");
   console.log("http://localhost:8080");

