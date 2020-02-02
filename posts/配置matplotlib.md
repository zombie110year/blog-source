---
comments: true
title:  配置matplotlib
date:   2018-09-29 01:25:26
mathjax:  false
tags:
    - python
    - matplotlib
categories:
    - 日常
---

# 图片显示中文

## 问题原因

在 `matplotlib` 中作图, 一旦遇到中文就会出现方块符号, 表示无法显示.

出现这个问题的原因只可能有两种: 字符编码不对, 没有支持的字体.

现在字符编码都是标准的 `utf-8` 了, 并且 Python 运行时处理字符都会转换为 Unicode, 因此这个问题只可能是没有支持的字体了.

在网上找到的很多解决方案, 都提到要绘制中文需要使用 `u'中文'` 这样的语句, 猜测这个是 Python2 的遗留, Python3 实测不需要这么做.

<!--more-->

## matplotlib 字体设置

**需要注意! matplotlib 只支持 `ttf` 格式的字体!** 也就是 `truetype` 字体.

如果要用其他格式字体, 需要将其转换为 `ttf`, 否则就算设置了也不会启用!

### 配置文件 matplotlibrc

[官方文档: 自定义 matplotlib](https://matplotlib.org/users/customizing.html)

matplotlib 启动时, 会读取以下路径的几个配置文件:

0. `./matplotlibrc` 当前路径下的配置文件
0. `$HOME/.config/matplotlib/matplotlibrc` *nix 系统家目录下的配置文件
    - 其他系统是这个路径: `$HOME/.matplotlib/matplotlibrc`
0. `site-packages/matplotlib/mpl-data/matplotlibrc` 安装路径下的配置文件

matplotlib 读取配置将数据以字典的形式载入程序, 配置文件中的条目都是这样的格式:

```
配置组.配置项: value1, value2, ...
```

对于设置的字体, 就设置这么一项即可:

```
font.family: Inziu Iosevka SC, other fonts,
```

注意, 不能加引号, 这个配置文件的解析会将引号也作为字体名的一部分, 就无法找到字体了.

`matplotlib.font_manager._rebuild()` 用于重新生成缓存. 在安装完字体或修改了设置之后运行一次才能生效.

如果 `_rebuild()` 后仍无效, 可能需要手动删除 `.cache/matplotlib` 下的缓存. 再 `_rebuild()`.

### 程序内动态设置

matplotlib 中提供了几个函数, 用于动态设置.

#### `matplotlib.rcParams['font.family'] = 'Inziu Iosevka SC'`

此语句在程序中运行, 就相当于修改了配置文件中的对应项.

#### `matplotlib.rc(group:str, **kwargs)`

此语句和 `rcParams` 类似, 其第一个参数为修改的配置组, 修改项需要以关键词参数的形式传入, 可以利用 `**dict` 的方式:

```python
font = {
    'family': 'Inziu Iosevka SC',
    'weight': 'regular', # 可用选项可以通过 matplotlib.font_manager.weight_dict 查看.
    'size': 12,
}
matplotlib.rc('font', **font)
```

```python
weight_dict = {'ultralight': 100,
 'light': 200,
 'normal': 400,
 'regular': 400,
 'book': 400,
 'medium': 500,
 'roman': 500,
 'semibold': 600,
 'demibold': 600,
 'demi': 600,
 'bold': 700,
 'heavy': 800,
 'extra bold': 800,
 'black': 900}
```

#### `matplotlib.font_manager.FontProperties(fname="/path/to/font.ttf")`

此方法会返回一个 "字体" 对象(实际上我不知道该怎么称呼它), 用一个变量接收它, 然后在调用函数时传入给 `fontproperties` 关键词参数.

```python
fontsetting = matplotlib.font_manager.FontProperties(fname="/path/to/font.ttf")
matplotlib.pyplot.plot(X,Y, fontproperties=fontsetting)
```

不过有些作图函数不接受 `fontproperties` 参数, 比如 `matplotlib.pyplot.bar()` (做条形图).

## 安装字体

[Inziu](https://be5invis.github.io/Iosevka/inziu.html) 系列字体是我目前发现的唯一一个中文英文宽度严格 2:1 的字体, 并且开源, 强烈推荐.

不过它下载下来是 `ttc` (True Type Collection) 格式的, 需要转换为 `ttf` 才能使用.

推荐使用 [FontForge](https://fontforge.github.io/en-US/) 来转换格式. 这是一个开源的字体制作工具, 其他的工具只找到个 FontCreater, 但是是商业软件, 不打算用破解版.

FontForge 在 Windows 上是通过开 X server 来显示的, 有以下表现:

- 需要为 X server 开放防火墙.
- 不支持 Windows 高分屏 (也许可以改设置, 但是我不会).
- GUI 有明显的 Gnome 风格.

发现下载速度简直和渗透作用差不多(1 KB/s 左右), 最后我是上了梯子的服务器, 下载完之后 `scp` 下来的... (两秒钟就进 VPS 了, `scp` 速度大约 300 KB/s)

转换为 `ttf` 后, 将字体文件上传并放置在 `/usr/share/fonts/truetype/inziu` 目录下, `inziu` 目录是自己创建的.

然后使用 `fc-cache` 更新字体缓存.

要查看字体名, 在 `Linux` 系统中, 使用命令 `fc-list` 来查看, 一般会返回这些信息:

```
/usr/share/fonts/truetype/inziu/Inziu-Iosevka-SC-Regular.ttf: Inziu Iosevka SC:style=Regular
```

可以看到, 返回信息有三条, 用 `:` 分隔: `文件路径: 字体名: 字体默认风格`. 在设置中用到的应是字体名.

要指定搜索中文字体, 可以使用

```sh
fc-list :lang=zh
```

```
/usr/share/fonts/truetype/arphic/uming.ttc: AR PL UMing TW MBE:style=Light

......

/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK KR,Noto Sans CJK KR Bold:style=Bold,Regular
```

如果是在 `Windows` 或 `MacOS` 系统, 用相应的图形化工具看就行了.

## 参考

- [我们来解决一下 matplotlib 的中文显示问题](https://www.jianshu.com/p/15b5189f85a3)
- [matplotlib图例中文乱码? - 知乎](https://www.zhihu.com/question/25404709)

# 在 Jupyter Notebook 中的设置

在 `ipython_config.py` 中添加

```python
c.InteractiveShellApp.matplotlib = 'inline'     # 自动显示图片
c.InlineBackend.figure_formats = ['svg']        # 生成 svg 矢量图
```
