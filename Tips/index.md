---
title: Tips
type: "tips"
---

# Git Log 乱码

Git 默认使用 less 作为 log 的查看器, 在有中文时乱码, 一般都是因为字符编码对不上的原因.

乱码看起来是这样:

```
\123\321 ......
<A3><E8> ......
```

1. 设置 git 的 i18n

```sh
git config --global i18n.commitencoding = utf-8
git config --global i18n.logoutputencoding utf-8
```

2. 设置环境变量 LESSCHARSET

```
export LESSCHARSET=utf-8 # Bash

$env:LESSCHARSET = "utf-8" # PowerShell
# 或者直接在设置环境变量的 GUI 中设置
```

问题解决

> date: 2018-12-08 00:18:34

<!--more-->

# Python 运行一个包

```sh
python -m package.__main__ ...args
```

> date: 2018-11-17 21:15:41

# Linux rename 指令

Linux rename 指令用于重命名文件

```sh
rename <pattern> <target>
```

- `<pattern>` 是重命名时的模式字符串, 采用正则表达式:
    - `s/原名/更名/作用域` 作用域留空则只更改匹配到的第一个文件, `g` 则表示更改所有.
- `<target>` 指明操作目标文件, 支持通配符.

```sh
rename 's/(.*)\.c/\.cpp/g' *
# 将当前目录下所有 .c 文件重命名为 .cpp文件
```

> date: 2018-11-01 21:33:26

# Pandoc 提取 docx 中媒体文件

使用参数 `--extract-media=DIR` 提取 source 中的媒体文件.

会在指定的 `DIR` 下创建一个 `media` 目录. 例如

```sh
pandoc test.docx -f docx+style -t markdown --extract-media=DIR -o test.md
```

将会产生以下文件

```
cwd/
    test.md
    DIR/
        media/
            figure1.png
            figure2.png
            ...
```

根据需要指定, 一般 `--extract-media=.` 即可.

> date: 2018-10-21 17:40:46

# 一些 css 样式

- `opacity` 控制元素透明度, 子元素必定继承父元素的透明度, 无法切断继承. 可以考虑: 用插入透明图片的方式代替透明背景.
- `border-radius` 控制边框圆角, 应有一个圆角半径值.
- 将 `background-size` 设为 `cover`, 使背景图片完全展开, 覆盖当前页面.

## css 盒子模型

- `margin` 外边距. 处于最外层, 用于控制元素与元素之间的间隔.
- `border` 边框. 处于外边距与内边距之间.
- `padding` 内边距. 处于内容与边框之间, 用于控制父元素与子元素块的间隔.
- `content` 内容. 盒子的内容, 可嵌入图片, 文本, 子元素等等.

一个盒子的 `width`, `height` 等属性的值, 是 `margin`, `border`, `padding`, `content` 各元素的尺寸之和. (一个盒子有两个边距,边框, 只有一个内容)

> date: 2018-10-18 00:22:47

# Python 出现 PermissionError [Errno 13]

一个数据科学的同学试图将一个 DataFrame 保存到一个目录中:

```python
daylinedates.to_csv("D:\新建文件夹")
```

而 Python 也毫不怜惜地报了错:

```
PermissionError: [Errno 13] Permission denied : 'D:\\新建文件夹'
```

问题原因就是 **试图将一个文件夹打开为一个目录**.

在 Windows 下, 这将报错 `PermissionError [Errno 13]`, 在 Linux 下, 将报错 `IsADirectoryError: [Errno 21] Is a directory: './xxx'`.

> date: 2018-10-16 12:56:10

# 使用 `refreshenv` 刷新Windows环境变量

> date: 2018-10-11 22:48:19

# 猜测GBK还是UTF8?

使用汉字 "的" 的UTF8编码来判断. 

的 的 UTF8 编码为 `0xe79a84`, 而 GBK 字符集中只有 "鐨" `0xe79a`, "殑" `0x9a84` 可能造成误判, 而此两个生僻字出现频率极低, 可以忽略.

缺点: 万一 "的" 字不出现就没用了.

> date: 2018-10-10 17:08:47

# 使用 xelatex 而非 xetex

`xelatex` 和 `xetex` 将以不同方式调用 XeLaTeX 引擎, 后者将使用 LaTeX 格式, 使用 GBK 编码

> date: 2018-10-07 19:54:55

# Conda 更换清华镜像

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

> date: 2018-09-23 17:38:57

# BiliBili查看失效收藏

在收藏夹页面, 在这个路径下是收藏视频条目, 其下 `class` 属性为 `small-item disabled` 的 `li` 元素就是失效条目.

```
#page-fav > div.col-full.clearfix.master > div.fav-main.section > div.fav-content.section > ul.fav-video-list.clearfix.content
```

失效条目依然保留了封面与标题, 可在对应 `li` 元素下的 `li.small-item.disabled > a.cover.cover-normal.disabled > img` 中查看. `src` 属性是封面的路径, 而 `alt` 属性是标题.

不过 B 站收藏夹是动态页面, 无法用静态爬虫获取.

> date: 2018-09-23 16:36:32

# 配置 Hexo NexT Page

在 next 的 `_config.yml` 中的

```yml
menu:
  your_page: /path/ || fontawesome-code
# 该页面使用的代号: 该页面的 index.md 所处路径(相对) || 使用的图标(fontawesome代码)
```

之后去到使用的页面国际化(翻译) 配置, 如 `themes/next/languages/zh-CN.yml` 中, 也在 `menu:` 项下添加对应代码

```yml
menu:
  your_page: 显示名
```

> date: 2018-09-19 19:32:23

# Windows不在乎文件后缀名

所以要注意, 命名脚本文件时去除后缀的部分不要与调用程序的命名相同.

[关于此事的记录](https://www.zhihu.com/question/21747929/answer/494153996)

> date: 2018-09-19 00:04:39

# #Python locals() 函数

此函数将会返回命名空间

> date: 2018-09-18 00:13:21

# # Python代码风格

我认为, 编写代码的时候, 拥有良好的编码风格是很有必要的, 而且越早决定采用的标准越好.

我决定, 采用如下标准:

- 拥有特殊意义的常量: `UPPER_LETTER` 使用大写字母+下划线的组合.
- 全局变量, `gUPPER_LATTER` 使用 g+大写字母+下划线的组合.
- 局部变量; 如果为一般对象, 则用 `lowwer_letter` 小写字母+下划线, 如果为容器对象, 则用 `lowwer_Upper_Letter` 小驼峰命名法+下划线
- 函数, 方法名: `lowwerUpperLetter` 使用小驼峰命名法
- 类: `UpperUpperLetter` 使用驼峰命名法

> date: 2018-09-17 13:12:20

# Vim 块操作模式

在 Windows 系统, 使用 <kbd>Ctrl</kbd> + <kbd>q</kbd>

在 Linux 系统, 使用 <kbd>Ctrl</kbd> + <kbd>v</kbd>

进入 Vitual-Block 模式

> date: 2018-09-15 17:14:49

# python子进程与多线程基本用法

分别使用 subprocess 和 threading 模块

```python
# 使用 run 函数
x = subprocess.run(*popenargs:tuple, shell:bool[, stdout]) -> Popen
# popenargs 是通过列表或元组组织起来的命令行, 第 0 项为可执行文件, 其余项为传递给可执行文件的参数.
# shell=True, 则会新开一个 Shell 运行命令, 否则就只是新开一个进程运行, 不会读取用户为 Shell 设置的配置.
# 如果要捕获输出, 务必将 stdout=subprocess.PIPE, 这样, 标准输出就会被重定向到 Popen 实例 x 的 stdout 属性中
## 该属性是字节流类型的, 需要根据字符编码进行解码. x.stdout.decode('gbk')

# 创建线程
x = threading.Thread(target:<python funcion>, *args:tuple) -> Thread
# 使用此函数创建一个线程实例, target 函数应该为 Python 中定义的函数, 这会使得该函数在新的线程中运行.
# 启动线程
x.start()
# 线程被创建出来后, 不会立刻运行, 需要使用 start() 方法, 才会启动相应的线程
# 等待线程
x.join()
# 线程启动之后, 会立即执行接下来的 Python 语句, 如果需要在某处等待某线程完成, 就使用 join() 方法
```

> date: 2018-09-15 16:05:37

# LaTeX `\displaystyle` 使行内公式具有行间样式

> date: 2018-09-04 17:16:42

# Pandoc转换行内公式不允许空格

```
$This is a in-line math$
$ 这个不行 $
```

> date: 2018-09-04 12:51:46

# Python Import 模块会将模块文件执行一遍

> date: 2018-09-02 21:46:22

# LaTex 学习资料. 顺便, 在 HTML 中嵌入 PDF

<iframe src="/assert/repos/latex/lnotes2.pdf" style="width:800px; height:600px;" frameborder="0">
  <p>
看来你的浏览器不支持 iframe 标签... 咋不更新呢?
算了, 给你个链接你自己下载吧: <a src="/assert/repos/latex/lnotes2.pdf"></a>
  </p>
</iframe>

```html
<iframe src="/assert/repos/latex/lnotes2.pdf" style="width:800px; height:1200px;" frameborder="0"></iframe>
```

> date: 2018-09-02 14:49:48

# Python可以使用中文作为变量名

```
In [8]: 中文变量名 = 1

In [9]: 中文变量名
Out[9]: 1
```

> date:2018-09-01 23:57:17

# 拼音注音字符

```
āáǎàōóǒòêēéěèīíǐìūúǔùüǖǘǚǜ
```

> date:2018-08-31 22:31:32

# Dos clip 程序

可以使用 `string | clip ` 将文本内容放入剪贴板, 但是不能有任何非 ASCII 字符, 否则变为问号 ?

> date:2018-08-31 20:04:58

# Markdown插入图片Base64

```
![](data:image/png;base64,ILENFLKSNGEJ...)
或者
![][id]

...

[id]: data:image/png;base64,IJLKDFSK...
```

> date:2018-08-30 21:02:28

# 字符串 `translate()` 与 `maketrans()` 方法

Python

```py
string.maketrans(FROM, TO) --> dict(原字符串: 目标字符串)

string.translate(dict(FROM:TO)) --> new_string
```

> date:2018-08-29 11:35:56

# 匹配Markdown图片链接的正则表达式

```
!\[[^\[\]\(\)]+\]\(([\S\./]+)\)
```

> date:2018-08-28 21:12:58

# encode, decode

```
str   --encode()--> bytes
bytes --decode()--> str
```

> date:2018-08-28 15:33:37

# VsCode中取正则表达式的子表达式

```
$number
```

> date:2018-08-27 18:23:27

# Vscode 调试 Python模块时的 launch.json 设置

```
cwd: 模块所在路径,
module: ModuleName,
args: [],
```

> date:2018-08-25 16:57:29

# locate找不到数据库的解决办法

`updatedb` 指令更新数据库

> date:2018-08-25 00:05:02

# FireFox config 设置

about:config页面:

```
view_source.editor.external             允许使用外部编辑器
view_source.editor.path                 编辑器路径
security.enterprise_roots.enabled       固定根证书
```

> date:2018-08-24 20:40:31

# Linux 用户, 用户组 权限管理

指定 /usr/sbin/nologin 使用户无法登陆 shelll

useradd userdel usermod

groupadd groupdel groupmod

passwd

> date:2018-08-24 03:59:13

# Linux 添加 sudoer

 编辑 `/etc/sudoers`

```sh
chmod 600 /etc/sudoers    #获取写权限
echo 'username ALL=(ALL) ALL' >> /etc/sudoers
chmod 200 /etc/sudoers
```

```
username ALL=(ALL:ALL) ALL
        可切换至所有用户, 用户组, 可使用所有命令
```

> date:2018-08-24 02:30:19

# CSS 选择器

```css
html {}         /*      选择 HTML 元素          */
.class {}       /*      选择 class              */
#id {}          /*      选择 id                 */
[src] {}        /*      选择属性, 例如 src      */
@media          /*      at-rule                 */
```

- [MDN:CSS at-rule](https://developer.mozilla.org/zh-CN/docs/Web/CSS/At-rule)

> date:2018-08-24 01:49:01

# PowerShell rm

可以向 -Exclude (忽略) 传递多个值, 使用逗号 `,` 分割. -Include 同理.

> date:2018-08-24 00:22:24

# 检查翻墙VPS是否被封的办法

## 首先, `ping` 测试.

- 检查能否 `ping` 通.

## 其次, 端口测试

国内端口测试:

[站长工具/port](http://tool.chinaz.com/port)

国外端口测试:

[Open Port Finder](https://www.yougetsignal.com/tools/open-ports/)

> date:2018-08-23 03:39:16

# 更换Hexo主题的背景图

将喜欢的背景图放到 `project-->themes-->next-->source-->images` 目录下。
打开 `project-->themes-->next-->source-->css-->_custom-->custom.styl` 文件，加入代码

```
body { background:url(/images/imagename.jpg);}
```

重新编译项目就OK了。

[参考](http://www.lieeber.com/2016/05/15/Hexo%E4%BD%BF%E7%94%A8%E4%B8%8A%E7%9A%84%E4%B8%80%E4%BA%9B%E5%B0%8Ftips/#%E6%9B%B4%E6%8D%A2next%E4%B8%BB%E9%A2%98%E7%9A%84%E8%83%8C%E6%99%AF)

但是这效果...... 应该需要改 CSS 把 post 部分弄宽一点吧... 但是不会改... 暂时放弃.

> date:2018-08-22 18:48:02

# PowerShell 中的转义字符

PowerShell 使用反引号作为转义字符;

```
所以如果要在终端中使用反引号, 就打两个反引号就好了
```

> date:2018-08-22 18:07:10

# Linux BBR

内核版本必须大于 4.9.

[升级内核](https://www.google.com/search?q=Linux+升级内核)

检查是否已开启:

```sh
uname -r # 查看内核版本
sysctl net.ipv4.tcp_avaliable_congestion_control # 查看内核是否启用 BBR 算法
lsmod | grep bbr    # 如果有 tcp_bbr 说明启动成功
```

通过写入配置文件开启 BBR

```sh
echo net.core.default_qdisc=fq >> /etc/sysctl.conf
echo net.ipv4.tcp_congestion_control=bbr >> /etc/sysctl.conf
```

> date:2018-08-21 22:11:40

# Android 刷机包结构?

> date:2018-08-21 10:01:46

# Python @ Windows 如何处理字符编码

`sys.getdefaultencoding()`.

读到内存中的字符串都是Unicode编码吗?

> 是的.

只有在IO时才会编码解码?

> Python3 在读写文件时的默认编码是 `utf-8`

> date:2018-08-20 18:08:19
