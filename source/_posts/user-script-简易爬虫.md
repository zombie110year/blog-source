---
comments: true
title: User-Script 简易爬虫
tags:
categories:
date: 2019-09-11 16:22:44
---

# User-Script 简易爬虫

一个爬虫至少需要完成这两个任务：

1. 获取资源
2. 解析资源

获取资源，我们可以用 `fetch` API 或更旧的 XHR API，解析资源则有 DOM API、JSON API、和 RegExp 对象。但这些工具进行解析的话步骤都比较复杂，只适合简单的数据处理。

而且由于浏览器的同源政策，绝大多数网页都是不能在异源站点抓取的。

因为以上提到的这两个劣势：

- 弱数据处理
- 同源政策

原生 API 爬虫的适用场景其实是基于 User Script 管理器运行的 **页面增强工具**。例如页面不提供一些资源的便捷下载方法，于是我们自己实现一个。

我们需要搞定这些问题：

1. 利用浏览器的开发者工具抓包，确定需要请求的资源
2. 用 fetch 请求资源
3. 用原生 DOM API、JSON API 或 RegExp 解析数据
4. 对于单独的文件，可以使用 Blob API 将数据下载；如果是文件，也可以将内容显示在页面上的新建元素中，或复制到剪贴板。
5. 如果有多个文件，且存在文件夹，可以依次下载，也构造 zip 压缩文件。只是原生 JavaScript 不支持 zipfile，得找到一个读写 zip 文件的轮子，例如 [JSZip](https://github.com/Stuk/jszip)。
6. 如果希望将数据发送到特定服务器，那么需要考虑同源政策、解决跨域问题。

并且希望依赖越少越好。

本文的使用环境为：

- 浏览器：FireFox 68.*
- 脚本管理器：Tampermonkey

<!-- more -->

## 抓包

按 F12 打开开发者工具，在 “网络” （Network）选项卡中就是当前页面所发送的请求与响应。开发者工具只有在打开的情况下才会记录网络请求，应当先打开开发者工具，再访问网站。

在其中我们感兴趣的资源有：

- `.html`, `.aspx`, `.php` 等 HTML 页面模板。
- `.js` `.json` 等请求的脚本或数据。

浏览器的开发者工具/网络选项卡提供了过滤器，我们可以分别用 `HTML`, `JS`, 来筛选出以上请求。

另外还有两个有用的过滤器：`XHR` 和 `WS`。前者是当前页面用 Ajax 手段请求的资源，大多数响应是很有用的 JavaScript 脚本或 JSON 数据。后者是通过 WebSocket 连接传输的数据，虽然少见，但是由于 WS 连接效率比 HTTP 高，一些需要持续传输的大文件有可能是通过它传输的。

在抓包时需要关注 4 个信息：

1. HTTP 请求类型。
2. HTTP 请求头，主要是看 User-Agent、Cookies、Referer 三个字段，服务器一般都用这三个字段（或其中几个）来确认用户身份。
3. HTTP 请求参数，一般是 POST 请求才查看，如果是 GET 请求的话，参数直接在 URL 里（`?name=value&n2=v2` 这样的字串就是 GET 参数，用 `?` 将它与 URL 其他部分分开，用 `key=value` 键值对设置数据，用 `&` 分隔各键值对）。
4. HTTP 响应体，查看其响应数据格式，以确定资源的解析方案。

## fetch API

fetch API 是异步并且 Promise 风格的，它接受两个参数，第一个参数是 `URL`, 第二个是可选的 `init` 参数，是一个 JSON，在其中可对请求方案进行详细的设置。

```javascript
fetch("http://example.com/", {
    method: "GET"
}).then(response => {
    // 每一次 .then 方法中，参数是自动解析的上个 Promise 的数据，
    // 返回值会自动打包进当前 Promise 的数据中。
    return response.text();
}).then(html => {
    // 将当前页面的 body 替换为请求的页面
    let x = document.createElement("html");
    x.innerHTML = html;
    let body = x.querySelector("body");
    document.body = body;
})
```

`fetch` 规范与 `jQuery.ajax` 在规范上有两点不同：

1. 只要服务器响应了，不管是 40x 还是 50x， fetch 都会 resolve （但是 resolve 的 ok 属性被设为 false），只有等待超时也没有收到响应才会 reject。
2. fetch 默认不会发送或接收 cookies，如果需要通过 cookies 进行认证，必须设置 credentials 选项，并且遵守同源政策。

如果能 resolve， fetch 将返回一个 Response 对象，一般可以通过调用 `.text()` 方法解析为纯文本、`.json()` 方法解析为 JSON 对象、`.blob() ` 解析二进制数据、`.arrayBuffer()` 解析为字节数组或者 `.formData()` 解析为 FormData。

要发送定制的请求，可以设置 `init` 参数的值，这是一个 JSON，可以设置这些键值：

- `method`: HTTP 方法，如 `GET`、 `POST`。
- `headers`: 请求的头信息，形式为 [`Headers`](https://developer.mozilla.org/zh-CN/docs/Web/API/Headers) 的对象或包含 [`ByteString`](https://developer.mozilla.org/zh-CN/docs/Web/API/ByteString) 值的对象字面量。
- `body`: 请求的 body 信息：可能是一个 [`Blob`](https://developer.mozilla.org/zh-CN/docs/Web/API/Blob)、[`BufferSource`](https://developer.mozilla.org/zh-CN/docs/Web/API/BufferSource)、[`FormData`](https://developer.mozilla.org/zh-CN/docs/Web/API/FormData)、[`URLSearchParams`](https://developer.mozilla.org/zh-CN/docs/Web/API/URLSearchParams) 或者 [`USVString`](https://developer.mozilla.org/zh-CN/docs/Web/API/USVString) 对象。注意 GET 或 HEAD 方法的请求不能包含 body 信息。
- `mode`: 请求的模式，如 `cors`、 `no-cors` 或者 `same-origin`。
- `credentials`: 请求的 credentials，如 `omit`、`same-origin` 或者 `include`。为了在当前域名内自动发送 cookie， 必须提供这个选项，从 Chrome 50 开始， 这个属性也可以接受 [`FederatedCredential`](https://developer.mozilla.org/zh-CN/docs/Web/API/FederatedCredential) 实例或是一个 [`PasswordCredential`](https://developer.mozilla.org/zh-CN/docs/Web/API/PasswordCredential) 实例。
- `cache`:  请求的 cache 模式: `default `、 `no-store` 、 `reload `、 `no-cache` 、 `force-cache` 或者 `only-if-cached`。
- `redirect`: 可用的 redirect 模式: `follow` (自动重定向), `error` (如果产生重定向将自动终止并且抛出一个错误), 或者 `manual` (手动处理重定向). 在Chrome中，Chrome 47之前的默认值是 follow，从 Chrome 47开始是 manual。
- `referrer`: 一个 [`USVString`](https://developer.mozilla.org/zh-CN/docs/Web/API/USVString) 可以是 `no-referrer`、`client`或一个 URL。默认是 `client`。
- `referrerPolicy`: 如何指定 HTTP 头中的 `referer` 字段。可以是 `no-referrer`、 `no-referrer-when-downgrade`、 `origin`、 `origin-when-cross-origin`、 `unsafe-url`。
- `integrity`: 包括请求的  [subresource integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) 值 （ 例如： `sha256-BpfBw7ivV8q2jLiT13fxDYAe2tJllusRSZ273h2nFSE=`）。

### 读取当前页面的 HTTP 头信息并设定请求头

#### Referer

此字段的值保存在 `document.referrer` 中。注意 `r` 的数量，在 HTTP 标准中，少了一个 r，这属于拼写错误，但已经无法修改了。而在 JavaScript 中却使用了正确的拼写。这常常引起混淆。

|   HTTP    | JavaScript |
| :-------: | :--------: |
| `referer` | `referrer` |

#### Cookie

此字段的值保存在 `document.cookie` 中，是一个用 `; ` 分隔的键值对（`k=v`）。

#### User-Agent

这个无法通过 JavaScript 动态获取。不过对于一个浏览器而言，这是一个常量字符串。复制粘贴即可。

#### 设置请求头

在 `fetch` 的 init 参数中设置：

```js
let init = {
    headers: {
        "referer": document.referrer,
        "cookie": document.cookie,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
}
```

其他头也可以这么设置在其中。

### 设定请求参数

GET 和 HEAD 方法不能设置请求参数，它们的参数是在 URL 中的。

body 的值可以是 [`Blob`](https://developer.mozilla.org/zh-CN/docs/Web/API/Blob)、[`BufferSource`](https://developer.mozilla.org/zh-CN/docs/Web/API/BufferSource)、[`FormData`](https://developer.mozilla.org/zh-CN/docs/Web/API/FormData)、[`URLSearchParams`](https://developer.mozilla.org/zh-CN/docs/Web/API/URLSearchParams) 或者 [`USVString`](https://developer.mozilla.org/zh-CN/docs/Web/API/USVString) 对象。

```js
let init = {
    body: JSON.stringify({"a": "b"})
}
```

对于用 JSON 传输数据的请求、可以用 `JSON.stringify` 将对象打包成字符串。

> JSON.parse 可以将字符串解析为对象。

## 资源解析

### 用 DOM API 解析 HTML

在知道响应体是 HTML 时，调用 `response.text()` 得到 HTML 文本，然后通过

```js
fetch("http://example.com/")
	.then(resp => {
    	return resp.text();
	})
	.then(text => {
    	let html = document.createElemnt("html");
    	let html.innerHTML = text;
     	return html;
	}).then(process_with_dom);
```

通过 `document.createElement` 可以创建一个未渲染的 HTML 元素，将内部 HTML 内容编辑为 HTML 文本，就可以创建一个可操作的 DOM。

这个 DOM 可以使用 `querySelector` 或 `querySelectorAll` 等方法来通过 CSS 选择器查找元素。

### JSON API

```js
let obj = {
    name: "object",
    value: 10,
    lists: [1,2,3,4,5,6,7,8,9]
};
JSON.stringify(obj);
// "{\"name\":\"object\",\"value\":10,\"lists\":[1,2,3,4,5,6,7,8,9]}"
JSON.parse("{\"name\":\"object\",\"value\":10,\"lists\":[1,2,3,4,5,6,7,8,9]}");
// Object { name: "object", value: 10, lists: (9) […] }
```

### 正则表达式

正则表达式可以用 `//` 定义，也可以用 `RegExp`，但由于前者经常需要转义 `/`，看起来太丑，因此我偏好使用 `RegExp`。

```js
let text = "zombie110year@outlook.com";
let re = RegExp("(\\S+)@(\\S+)");
// .test 测试 re 能否全文匹配 text
re.test(text);
// true
// .exec 搜索并得到捕获组列表
let m = re.exec(text);
// 捕获组列表 0 为全文
m[0];
// 1 为第一个子表达式
m[1];
```

在定义时，可以设置 flag：

- `g`: 全局匹配，而不是找到第一个匹配就停止
- `i`: 忽略大小写
- `m`: 多行模式， `^`, `$` 将匹配行的首尾，而不是整个字符串的首尾
- `u`: Unicode 模式
- `y`: 粘性匹配; 仅匹配目标字符串中此正则表达式的lastIndex属性指示的索引(并且不尝试从任何后续的索引匹配)
- [`dotAll`模式](https://github.com/tc39/proposal-regexp-dotall-flag)，匹配任何字符（包括终止符 `\n`）

## 获取结果

### 文件下载法

JavaScript 原生提供了 [Blob](https://developer.mozilla.org/zh-CN/docs/Web/API/Blob) API 用于存储不可变的二进制数据。类似的还有个可变的 [ArrayBuffer](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) 对象，ArrayBuffer 长度固定，且需要使用视图去修改它。但我们关注文件操作的话，就使用 Blob 的子类 [File](https://developer.mozilla.org/zh-CN/docs/Web/API/File) 好了。

File 对象的构造函数的形参为

```js
File(bits, name[, options]);
```

- *bits* [`ArrayBuffer`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)，[`ArrayBufferView`](https://developer.mozilla.org/zh-CN/docs/Web/API/ArrayBufferView)，[`Blob`](https://developer.mozilla.org/zh-CN/docs/Web/API/Blob)，或者 [`DOMString`](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMString) 对象的 [`Array`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Array) — 或者任何这些对象的组合。这是 UTF-8 编码的文件内容。对于文本文件，
- *name* [`USVString`](https://developer.mozilla.org/zh-CN/docs/Web/API/USVString)，表示文件名称，或者文件路径。
- *options* （可选） 选项对象，包含文件的可选属性。可用的选项如下：    
  -  `type`: [`DOMString`](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMString)，表示将要放到文件中的内容的 MIME 类型。默认值为 `""` 。  
  - `lastModified`: 数值，表示文件最后修改时间的 Unix 时间戳（毫秒）。默认值为 [`Date.now()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Date/now)。    

得到了 File 对象，接下来考虑下载的问题。可以利用 `a` 元素，构造这样的 HTML 元素插入页面：

```html
<a href="blob:https://example.com/********" download="example.txt">下载</a>
```

然后点击它，就能触发浏览器的下载功能。JavaScript 无法触发，应该是浏览器的安全功能。下面是一个实例，blob URL 的创建方法是 `URL.createObjectURL`。

```js
let myfile = new File(["Hello World"], "hello.txt", {type: "text/plain"});
let blob_url = URL.createObjectURL(myfile); // 生成 UUID 风格的路径
let a = document.createElement("a");
a.href = blob_url;
a.download = myfile.name;
a.innerText = "下载 Hello World";
document.body.appendChild(a);
```

Blob URL 只在本机有效，文件也是储存在浏览器中的，关闭标签页就会自动清理，也可以手动清理，用

```js
URL.revokeObjectURL("blob:**************");
```

> 参考 https://javascript.ruanyifeng.com/htmlapi/file.html

### textarea

文本数据可以直接显示在 textarea 中，只是要注意， textarea 的内容不在 `textarea.innerText` 中，而是 `textarea.value`。这会在页面底端新增一个文本编辑框，可以框选并复制，或者进行简单的编辑。

```js
let ta = document.createElement("textarea");
ta.value = "Hello World";
document.body.appendChild(ta);
```

### 剪贴板法

剪贴板法需要用到 textarea，因为浏览器的安全策略，复制行为需要用户手动触发，例如点击一个按钮等。

```js
// 创建 textarea
let ta = document.createElement("textarea");
ta.id = "zxcv_textarea";
ta.value = "Hello World";
document.body.appendChild(ta);
// 创建一个按钮
let btn = document.createElement("button");
btn.innerText = "复制";
document.body.appendChild(btn);
btn.addEventListener("click", function(event) {
    let ta = document.querySelector("#zxcv_textarea");
    ta.focus();
    ta.select();
    document.execCommand("copy");
});
```

### 构建 zip 文件

我们使用 [JSZip](https://github.com/Stuk/jszip) 包，在浏览器中，可以通过用户脚本管理器来引用。

```js
// 创建 Zip 文件
let zip_root = new JSZip();
// 创建新的文件以及内容
zip_root.file("hello.txt", "Hello World!");
// 创建新的目录
example_menu = zip_root.folder("example_menu");
// 子目录可以进行任何与根目录相同的操作
example_menu.file("aaaaa.txt", "in example_menu");
// 路径参数可以写为 POSIX 路径
zip_root.file("example_menu/bbbbb.txt", "POSIX path");
// 删除文件/目录
zip_root.remove("hello.txt");
zip_root.remove("example_menu/aaaaa.txt");
zip_root.folder("example_menu").remove("bbbbb.txt");
```

JSZip 中的 `file` 函数可以传入可选参数以指定文件的类型：https://stuk.github.io/jszip/documentation/api_jszip/file_data.html 这里列举一些在写入二进制数据时可能用到的参数：

| name   | type    | default | description                                                  |
| ------ | ------- | ------- | ------------------------------------------------------------ |
| base64 | boolean | `false` | 如果数据已经用 base64 编码，则设置为 `true`。例如由 `<canvas>` 元素生成的图像数据。文本数据不需要此选项。 [More](https://stuk.github.io/jszip/documentation/api_jszip/file_data.html#base64-option). |
| binary | boolean | `false` | 如果数据需要被当作原始数据处理，则设置为 `true`，如果是文本，则设置为 `false`。如果使用了 base64 选项，则此选项也默认为 true。如果输入的 data 参数不是字符串，此项也自动设为 `true`。[More](https://stuk.github.io/jszip/documentation/api_jszip/file_data.html#binary-option). |

## 其他工具的使用方法

### DOM API

1. CSS 选择器
	- 第一个匹配的元素： `.querySelector`，
	- 所有匹配的元素（列表）： `.querySelectorAll`。
2. 当前节点的属性： `.attributes`（映射）
3. 子节点：`.children` 中是有 HTML 标签的子节点，`.childNodes` 还包含了标签之外的文本。
4. 父节点：`.parentNode` 或 `.parentElement`，是一样的。
5. 附加：`.append` 可以将一个节点附加到子节点列表的末尾
6. 插入：`.insertBefor(el, pos_el)` 将 el 插入到 `pos_el` 前面。
7. 内容：`.innerHTML` HTML 格式，`.innerText` 去除了 HTML 标签。

### 字符串 split, join

在对 GET 请求的参数处理，或者 Cookie 的处理，都涉及到字符串与分隔符的问题。可以使用 **字符串** 的 `.split` 方法，把字符串按分隔符分割成列表。要将列表中的元素组合成字符串，也可以调用 **列表** 的 `.join` 方法，用分隔符隔开每一项。

```js
"1,2,3".split(",")
// ["1,", "2", "3"]
["1", "2", "3"].join(".")
// "1.2.3"
```

## 缓存数据

就用 `localStorage`/`sessionStorage` ，现成的键值对数据库。

## TamperMonkey require API

TamperMonkey 脚本管理器可以加载额外的脚本。

```js
// ==UserScript==
// @name          Hello jQuery
// @namespace     http://www.example.com/
// @description   jQuery test script
// @include       *
// @require       http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js
// ==/UserScript==
```

只是它不处理依赖关系。
