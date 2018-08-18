---
title: HTML5-link标签
date: 2018-08-18 21:29:36
tags:
    - HTML5
categories:
    - 网站
---

# <link> 是干什么用的?

希望在一个网页中嵌入其他网页的文本, 上网搜了不少, 先是搜了 Hexo 是否有相关的功能, 发现并没有. 然后又考虑使用 JavaScript, 但对于一个从来没学过 HTML+CSS+JavaScript 的新手来说, 根本看不懂...

后来看了博客的 public 文件夹, 发现首页的 `index.html` 通过 

```html
<link itemprop="mainEntityOfPage" href="https://zombie110year.github.io/public/public/2018/08/docker笔记/">
```

来插入文章. 于是针对性地搜索了一番.

---

- `<link>` 标签定义两个连接文档的关系
- `<link>` 元素是空元素, 它只有属性
> 也就是说 `<link>` 标签总是这样子的: `<link 属性列表 />`
- `<link>` 元素有以下属性:
    - `href` 定义目标文档或资源的位置. 可使用绝对路径或相对路径.
    - `hreflang` 定义目标 URL 的基准语言
    - `media` 规定文档显示设备.
    - `rel`  定义当前文档与目标的关系
        - `alternate` 
        - `author`
        - `dns-prefetch`
        - `help`
        - `icon`
        - `license`
        - `next`
        - `pingback`
        - `preconnect`
        - `prefetch`
        - `preload`
        - `prerender`
        - `prev`
        - `search`
        - `stylesheet` 表明目标是当前文档的样式表
    - `type` 规定目标 URL 的 MIME 类型
        - `text/css` 表明是一个 CSS 文件