---
comments: true
title: Hello World
date: 2018-07-23 22:12:38
mathjax: true
tags:
  - Hexo
---

# Hello World!

今天鼓起勇气创建了一个博客. 因为自己在计算机方面只能算个业余爱好者, 所以也就只能按照网上的教程一样地利用 GitHub 的公共仓库来承载这个博客.

我创建这个博客的用意何在呢? 我自己都得提醒自己多想一想.

首先, 我在计算机技术方面也有点兴趣, 很想亲身实践一下创建一个网站的过程. 而创建一个博客相对来说比较简单, 所以将其作为我实践的第一步.

另一方面呢, 也想要尝试一下将自己收集整理的资料和自己的想法放到互联网上给众人观摩. 尝试这么一种以前从来没试过的笔记方式.

最后, 也许是最重要的一个因素: 有个自己的博客是多酷的一件事啊. 2333😄

## 感谢指导我搭建博客的几篇博文

[HEXO博客搭建日记 - 青鸟晴空 - 博客园](http://www.cnblogs.com/airbird/p/6160209.html)

[教你免费搭建个人博客，Hexo&Github](https://zhangslob.github.io/2017/02/28/%E6%95%99%E4%BD%A0%E5%85%8D%E8%B4%B9%E6%90%AD%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2%EF%BC%8CHexo-Github/)

我搭建博客的步骤和这几篇教程基本一致, 没有什么区别. 只是在安装 Hexo 的时候犯了一个傻, 就是执行 `npm install hexo` 的时候, 会把 Hexo 安装到当前路径下, 而非另一个默认路径... 所以在安装的时候, 请注意切换到一个合适的路径吧.

顺便在这里记录一下 Hexo 的常用操作

|简写指令|完整指令|作用|
|-|-|-|
|`hexo n "标题"`|`hexo new`|创建一个 标题.md 文档在 /source/_posts 目录下|
|`hexo clean`||清楚缓存|
|`hexo g`|`hexo generate`|生成 public 下的文件|
|`hexo s`|`hexo server`|启动 hexo 服务器, 默认在 localhost 下的 :4000 端口|
|`hexo d`|`hexo deploy`|部署到远程服务器, 依据 _config.yml 的设置|

## 接下来打算干的事

准备在该博客上发布一些好玩的东西和学习笔记.

- [x] 更换主题, 感觉 [Next主题](https://github.com/iissnan/hexo-theme-next) 比较好看.
    - 更换主题, 将下载的主题包解压到 `/theme/` 目录下, 然后在 `/_config.yml` 中配置 `theme: landscape` 项(默认主题是 landscape) 为 `theme: 主题文件夹名` 即可.
- [x] TODO:添加支持 Markdown 甚至是渲染数学公式的评论框.
    - 选择了 [Gitalk](https://github.com/gitalk/gitalk)
    - {% post_link 配置Hexo-Gitalk %}
- [x] {2018.7.24更新}GitHub Page 只能显示一页?
    - 哇, 贼坑. 上传到 GitHub 之后, 文件名的大写字母全部变成小写了, 偏偏在 Archive 页面跳转的 url 又区分了大小写, 导致页面 404. 现尝试将文件名改成全小写, 再次尝试.(但是为什么混用中英文时就不会出现区分大小写导致的错误呢?)
        - 问题解决了.
