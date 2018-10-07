---
title: Hexo配置过程
date: 2018-07-25 21:30:45
mathjax: true
tags:
  - Hexo
categories:
  - 网站
---
# Hexo 配置过程

## 配置目标

**一期目标**

- [x] 启用 `tag`, `category` 等页面.
- [x] 使用 `MathJax` 渲染 LaTeX 公式.
- [x] 使用 `Gitalk` 作为评论系统.
  - [x] 使用 [MD5](https://github.com/blueimp/JavaScript-MD5/blob/master/js/md5.min.js#L1) 的标签, 以规避由于文章标题过长而无法正常创建 GitHub issue 的问题.

**二期目标**

- [x] 在网站内保存图片等文件, 而非使用第三方图床.

闹了半天, 原来直接把图片存在 `/source` 目录的随意子目录下, 然后引用相对链接即可...

## 步骤

<!--more-->

### 开始使用 Hexo

这部分内容有很多其他的博主都介绍过了, 我参考了这几篇文章:

[HEXO博客搭建日记 - 青鸟晴空 - 博客园](http://www.cnblogs.com/airbird/p/6160209.html)

[教你免费搭建个人博客，Hexo&Github](https://zhangslob.github.io/2017/02/28/%E6%95%99%E4%BD%A0%E5%85%8D%E8%B4%B9%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%EF%BC%8CHexo-Github/)

这些文章介绍了下载安装 Node.js 到生成 Hexo 静态博客, 并部署到 GitPage 的步骤.

补充说一点, 我使用的是 [NexT 主题](https://hexo.io/zh-cn/) . 在配置网站语言为简体中文的时候, 应在 Hexo 的 `_config.yml` 里配置 `language:` 为 `language: zh-CN`. 尽管依据国际标准应为 zh-Hans , 但是在 /theme/next/languages/ 目录下只有 zh-CN.yml 文件...

## 启用 "tags" 页面

要使用 tags 页面, 先得确保 **主题** 的 _config.yml 文件里 `menu:` 项中 `tags` 选项被启用. 例如

```yml
menu:
  home: / || home
  #about: /about/ || user
  tags: /tags/ || tags
  #categories: /categories/ || th
  archives: /archives/ || archive
  #schedule: /schedule/ || calendar
  #sitemap: /sitemap.xml || sitemap
  #commonweal: /404/ || heartbeat
```

`||` 前的部分表示路径, 后面表示在页面上显示的图标, 使用的是 [font-awesome](http://fontawesome.dashgame.com/).

然后, 需要创建一个 "Page" 类型的页面.

```sh
hexo new page "tags"
```

之后会在 /source/ 目录下出现一个 tags/ 目录, 里面有一个 index.md 文件. 其内容为:

```markdown
---
title: tags
date: 2018-07-25 21:21:00
---
```

需要稍微修改一下, 

```markdown
---
title: 标签
date: 2018-07-25 21:21:00
type: "tags"
comments: false
---
```

`conmments: false` 表示在此页面禁用评论功能.

在发布的博文的 front-matter 中使用

```yml
---
tags:
  - tagname1
  - tagname2
  ...
---
```

来给文章添加标签.

其他同理.

### 启用 MathJax

根据 NexT 提供的 [文档](https://github.com/theme-next/hexo-theme-next/blob/master/docs/zh-CN/MATH.md)

$$ Hello \; MathJax $$

### 启用 Gitalk

[Blog](/2018/10/配置Hexo-Gitalk/)

## 参考资料

[NexT 已适配MathJax](https://theme-next.iissnan.com/third-party-services.html#mathjax)

[NexT 添加Gitalk](https://github.com/gitalk/gitalk/blob/master/readme-cn.md)

[NexT 官网](https://hexo.io/zh-cn/)

[NexT 使用文档](https://theme-next.iissnan.com/)

[Gitalk 官网](https://gitalk.github.io/)
