---
title: 为 Hexo 博客添加自动集成
date: 2019-04-09 10:49:53
tags:
    - hexo
    - ci
    - travis
---

# Travis CI

Travis CI 是 GitHub 上非常流行的 CI 工具.

在 Travis 中添加项目, 可以直接登录 GitHub 并添加公开仓库.
除了在 Travis 中配置项目之外, 还需要在仓库中添加 `.travis.yml` 配置文件.

每次 push 代码后, 就会触发 Travis 的检测, 根据 `.travis.yml` 文件的配置, 进行自动化的构建与发布.
构建和发布的命令行以 YAML 列表的形式写入 `.travis.yml` 中.

可以在 Travis 的网页上定义一些不希望公开的环境变量, 并在 `.travis.yml` 中以 `${varname}` 的形式引用.

<!--more-->

# 为 Hexo 添加 CI

首先, 需要完整的 hexo 应用. 并且将其配置完善.

在根目录, 由于 `package.json` 文件的存在, node js 的各种依赖可以依靠简单的 `npm install` 指令进行安装.

由于 hexo 的发布页是写入 GitHub 的仓库中的, 因此, 需要在 GitHub 上配置, 允许 Travis 拥有写仓库的权限.

在 `Settings -> Developer settings -> Personal access tokens` 中生成一个仓库写权限的 token, 在 Travis 中配置为环境变量.
例如 `${github_token}` 以便在 `.travis.yml` 中引用.
这个 token 的用法就是添加在 HTTP 链接前: `https://example_token@github.com/user/repo.git`, 这样就能直接写对应的仓库.

然后配置 `.travis.yml` 为:

```yml
# 定义 CI 类型, Travis 会按照此项配置安装对应的环境
language: node_js
node_js: stable

# 保存每次 npm install 的缓存.
cache:
  directories:
    - node_modules

# install 阶段
install:
  - npm install

script:
  - hexo g

after_script:
  - cd ./public
  - git init
  - git config user.name "zombie110year"
  - git config user.email "zombie110year@outlook.com"
  - git add .
  - git commit -m "update blog"
  - git push --force --quiet "https://${github_token}@${github_url}" master:master


env:
  global:
    - github_url: github.com/zombie110year/zombie110year.github.io.git
```

Travis 的 CI 流程大致可以分为三个阶段:

1.  环境安装
2.  install 阶段
3.  script 阶段

环境安装阶段的主配置项是 `language`, 根据语言的不同会有其他需要配置的项, 建议参考官方文档.

install 阶段将在环境安装完成后运行, 有 `before_install`, `install`, `after_install` 三个子阶段, 但是可以只配置 `install` 阶段, 其他两个阶段在未配置的情况下不会执行.
install 下用 YAML 列表的形式配置构建命令行. 这个阶段应该做的事情, 顾名思义, 是安装项目的开发环境, 和 `language` 阶段相比, 这个阶段做的是针对当前项目的环境.

script 阶段将在 install 阶段 **成功** 后运行, 如果前一阶段失败, 则整个流程失败. 和 `install` 类似, 同样有 `before_script`, `script`, `after_script` 三个子阶段.
script 阶段则是配置构建当前项目的命令, 比如测试, 打包, 发布 等等. 同样采用 YAML 列表的形式编写.

另外, 还有一个 env 项, 可以在 global 子项下配置一组键值对, 设置为可被其他项使用的环境变量.
在 Travis 网页中配置的环境变量也可以使用.

# 还能在 Hexo 的 config 里增加一个 Travis 的小徽章

被我用 html 的形式添加到 _config.yml 里了, 用于查看构建状态:

```yml
# Hexo Configuration
## Docs: https://hexo.io/docs/configuration.html
## Source: https://github.com/hexojs/hexo/

# Site
title: ZomHub
subtitle: Mo
description: '<a src="https://travis-ci.org/zombie110year/blog-source.svg?branch=master"><img alt="Travis Status" src="https://travis-ci.org/zombie110year/blog-source.svg?branch=master"</a>'
keywords:
author: Zombie110year
language: zh-CN # themes/next/language/zh-CN.yml
timezone: Asia/Shanghai
```
