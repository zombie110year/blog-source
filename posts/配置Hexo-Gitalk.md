---
title:  Hexo 配置 Gitalk 的过程
date:   2018-10-03 23:36:45
mathjax:  false
comments: true
tags:
    - hexo
categories:
    - 网站
---

# 在 Hexo 站点上布置 Gitalk

安装 Gitalk, 实际上就是为博客添加了一些 JavaScript 代码, 只有在浏览器上发生访问时才会运行.

本文介绍 Hexo 的 NexT 主题安装 Gitalk 的方法.

Gitalk 官方提到的一种安装方式是通过 npm install 安装, 但是我根本不知道应该在哪里添加 `import gitalk` 代码, 所以就按在页面引用 `gitalk.js` 的方法安装了.

<!--more-->

## 申请 GitHub Repo issue 的读写权限

Gitalk 是利用 GitHub 的 issue 工作的, 要使用 Gitalk, 需要先在 GitHub 创建一个仓库(博客仓库可以, 空仓库也可以), 并注册一个 [Github Application](https://github.com/settings/applications/new), 需要填写以下项目:

- `Application Name`: 填写应用名称, 可以随便填.
- `Homepage URL`: 用于展示此应用的主页, 因为我们是用的别人开发的 Gitalk, 可以随便填.
- `Application Description`: 填写对该应用的描述, 将会展示给别人看, 不过反正是自己用, 随便写.
- `Authorization callback URL`: 授权回调, 也就是允许此应用运行的页面, 只有在这个授权的页面中, 才允许应用访问 GitHub.

URL 是包含了 协议, 域名, 路径 的, 不要只填域名, 需要填诸如 `https://zombie110year.top` 这样的值.
(路径默认为 `/`, 可以省略).

以上信息在创建后都可以改, 随意.

GitHub 会生成两个信息:

- `Client ID`
- `Client Secret`

这两个信息很重要, 将在之后填入到配置文件中.

## 修改文件

> {2019 年更新}: 目前 NexT 已经将改动合并了, 不需要手动更改.

在 Google 时, 发现 [官方 wiki](https://github.com/gitalk/gitalk/wiki/在hexo-next主题上使用gitalk) 提示 [根据这个 Pull Request 改动](https://github.com/iissnan/hexo-theme-next/pull/1814/files).

于是就照着改.

### 在 NexT 主题的 `_config.yml` 配置中添加 Gitalk 的设置项

> {2019 年更新}: 目前 NexT 的配置文件中已经提供了此模板

文件位于 `/themes/next/_config.yml`. 不是 `/_config.yml`, 根目录下的是 Hexo 的配置, 不是 NexT 主题的.

这个更改不要求位置如何, 添加到文件最后就行:

```yml
# Gitalk
# Demo: https://gitalk.github.io
gitalk:
  enable: true
  github_id: zombie110year # Github repo owner
  repo: blog-source # Repository name to store issues
  client_id: "***********" # Github Application Client ID
  client_secret: "**************" # Github Application Client Secret
  admin_user: zombie110year # GitHub repo owner and collaborators, only these guys can initialize github issues
  distraction_free_mode: true # Facebook-like distraction free mode
  # Gitalk's display language depends on user's browser or system environment
  # If you want everyone visiting your site to see a uniform language, you can set a force language value
  # Available values: en, es-ES, fr, ru, zh-CN, zh-TW
  language: zh-CN
```

### 在 `comments.swig` 模板文件中添加 Gitalk 的 HTML 容器元素

> {2019 年更新}: 官方支持, 无需再改.

文件位于 `/themes/next/layout/_partials/comments.swig`.

这个文件就是一个 `if-elseif` 结构的判断, 先判断页面的 `comments` 设置是否为 `true`, 然后依次判断配置文件 `_config.yml` 中的各评论系统设置, 插入对应的 `<div>` 元素.

对于 Gitalk, 只要放入这个 `if-elseif` 结构的开头就可以了, 并将原本是开头的 `facebook` 选项的 `if` 改成 `elseif`, 添加到这个位置:

```swig
{% if page.comments %}

  {% if theme.gitalk.enable %}
      <div id="gitalk-container"></div>
      <link rel="stylesheet" href="https://unpkg.com/gitalk/dist/gitalk.css">

  {% elseif theme.facebook_sdk.enable and theme.facebook_comments_plugin.enable %}
```

按照我的猜想, 应该可以把其他不用的删掉, 只要不破坏 `if .... endif` 结构就好. 不过我并不知道会不会导致超出我认知世界范围的 Bug, 所以就不妄动了.

### 新增 Gitalk 的 swig 文件

> {2019 年更新}: 官方支持, 无需再改.

文件位于 `/theme/next/layout/_third-party/comments/gitalk.swig`.

原本在最外层有一个 `duoshuo` 的 `if...endif` 感觉实际上这个设置并不起作用, 所以删掉了.

这个文件其实就是向页面添加 Gitalk 运行需要的 js 代码.

**需要注意**! GitHub 的 issue 对 label 的长度有 50 个字符的限制, 如果 GitTalk 的 id 为 `location.pathname` (也就是 `2018/09/filename.html`) 的话, 只要文件名中含有中文, 一旦经过了 URL 编码, 一下子就超过 50 字符了, 所以最好对 `location.pathname` 进行编码, 比如 md5 编码就只输出 32 个字符, 并且保留了文件与 id 的唯一对应性.

但是 JavaScript 没有原生支持的 `md5` 函数, 我在 [这里](https://github.com/blueimp/JavaScript-MD5/tree/master/js) 找到了一个 `md5` 的实现. 还需要将其添加到博客中, 并在下面的 swig 文件中引用.

因为 Hexo 的渲染机制, 在 `/source` 目录下的非 md, html 文件都只是简单地复制到 `/public` 目录中, 所以创建自己的文件夹 `/source/assert/js/src` 然后将下载的 `md5.js` 放入其中即可. 随后, 在 `gitalk.swig` 中按照 `/assert/js/src/md5.js` 的路径引用.

```swig
{% if theme.gitalk.enable %}
  {% if page.comments %}
    <script src="https://unpkg.com/gitalk/dist/gitalk.min.js"></script>
    <script src="/assert/js/src/md5.js"></script>
    <script type="text/javascript">
      const gitalk = new Gitalk({
        clientID: '{{theme.gitalk.clientID}}',
        clientSecret: '{{theme.gitalk.clientSecret}}',
        repo: '{{theme.gitalk.repo}}',
        owner: '{{theme.gitalk.owner}}',
        admin: '{{theme.gitalk.admin}}',
        pagerDirection: '{{theme.gitalk.pagerDirection}}',
        id: md5(location.pathname),
        labels: "Gitalk",
        // facebook-like distraction free mode
        distractionFreeMode: false
      })
      gitalk.render('gitalk-container')
    </script>
  {% endif %}
{% endif %}
```

> `admin` 那一项也是改过的, 去掉了 `.split()`, 因为我在配置文件中传入的是一个字符串, 而非数组.

# 修改 `index.swig`

> {2019 年更新}: 官方支持, 无需再改.

在 `/themes/next/layout/_third-party/comments/index.swig` 中添加:

```swig
{% include 'gitalk.swig' %}
```

在 [这个 PR](https://github.com/iissnan/hexo-theme-next/pull/1814/files) 中竟然没提到, 坑啊, 我是搜到 [这篇文章](https://iochen.com/2018/01/06/use-gitalk-in-hexo/) 才知道的.

# 小结

经过了

1. 申请 Github 应用
2. 修改 `_config.yml`
3. 修改 `comments.swig`
4. 增添 `gitalk.swig`

等操作后, 只需要 `hexo clean`, `hexo generate` 重新生成静态页面, 部署到 GitHub 上就可以配置评论系统了.

之后需要手动进入每一个页面, 登陆评论, 才能在 GitHub 上创建 issue. 因为我博文不多, 所以这个过程我就手动完成了.

可喜可贺~

# 参考

- [Gitalk 中文说明](https://github.com/gitalk/gitalk/blob/master/readme-cn.md)
- [为博客添加-Gitalk-评论插件](https://knightcai.github.io/2017/12/19/%E4%B8%BA%E5%8D%9A%E5%AE%A2%E6%B7%BB%E5%8A%A0-Gitalk-%E8%AF%84%E8%AE%BA%E6%8F%92%E4%BB%B6/)
- [Gitalk 选项说明](https://github.com/gitalk/gitalk#options)
- [JavaScript md5 的一个实现](https://github.com/blueimp/JavaScript-MD5)
- [如何向 NexT 中添加 js 文件](https://github.com/iissnan/hexo-theme-next/issues/1436)
- [Hexo中Gitalk配置使用教程-可能是目前最详细的教程](https://iochen.com/2018/01/06/use-gitalk-in-hexo/)
