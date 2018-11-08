---
comments: true
title: Regex 正则表达式
mathjax: false
tags:
  - Regex
  - Python
categories:
  - Context
date: 2018-08-10 16:24:09
---

# 正则表达式简介

正则表达式适用于匹配字符串.

正则表达式中拥有的元素有:

- 普通字符, 例如一般的 `abcd` 和 `中文字符` 等等.
- 元字符, 元字符起特殊的控制作用, 如果要匹配元字符本身, 需要使用反斜杠 `\` 转义.

# 术语解释

```
"[a-zA-Z]{5}" --> "This is a example string with a word which has only 5 letters." --> "which"
    pattern                    string                                                result   
pattern 表示一个          string 表示匹配的目标                                result 表示匹配到的结果.
用于匹配的正则表达式.
```

# 元字符介绍

## 表示字符(或字符集)

- `.` 点号, 表示一个任意符号(除了换行符).
- `\b` 匹配处于单词头部或尾部的空字符. 
如 `This is a high tower`, `hi\b` 将会匹配 `high` 中的 `hi`, 而 `This` 中的 `hi` 不会匹配
- `\B` 匹配处于单词内部的空字符.
- `\w` 匹配任何数字或字母.
- `\W` 匹配任何非数字或字母.
- `\d` 匹配任何数字.
- `\D` 匹配任何非数字.
- `\s` 匹配任何空白字符.
- `\S` 匹配任何非空白字符.
- `[]` 表示字符集, 在其中的任意一个字符, 都可被匹配.

## 限定符

在正则表达式中, 有这样几个有用的元字符用于指定重复次数:

- `*` 星号, 限定前方的那个字符将会重复 0 次以上.
- `+` 加号, 限定前方的那个字符将会重复 1 次以上.
- `?` 问好, 限定前方的那个字符将会出现 1 次或 0 次.

用这些元字符, 可以起到更高级的通配符功能.

例如

```
colou?r 可以匹配 colour 或 color
wtf+    可以匹配 wtf, wtff, wtfff, ...
wtf*    则可以匹配 wt, wtf, wtff, wtfff, ...
而 .*   的组合可以匹配任意字符串.
```

还可以自定义重复次数, 这些表达式都和花括号有关:

- `{n}`         指定重复 n 次.
- `{m,}`        指定重复 m 次及以上.
- `{,n}`        指定重复 n 次及以内.
- `{m,n}`       指定重复 m 次到 n 次.

## 定位符

除此之外, 还需要了解一下这些用于定位字符串的元字符:

- `^` 表示一个字符串的开始.
- `$` 表示一个字符串的结束.

例如

```
test a text

^t 将会匹配 test 的第一个 t
t$ 将会匹配到 text 的最后一个 t
```

而 `\b` 与 `\B` 也常用于定位单词.

- `\b` 将会匹配一个单词边界, 例如下划线 `_`, 空格 ` `, 标点符号等.
- `\B` 则匹配非边界.

**不能将限定符用在定位符之后!!! `\b` 与 `\B` 后也不能跟限定符.**

## 捕获组(子表达式)

在一个正则表达式中, 可以嵌入捕获组.

- `()`          捕获组. 在括号中的字符, 必须全部匹配, 才会匹配整个捕获组. 整个表达式作为一个字符串. 并且将能在之后再次取用.

捕获组和字符集是不同的概念.

例如:

```
Common plain text in windows notepad
[win] 将会匹配所有的 w, i, n
(win) 只会匹配 windows 中的 "win"
```

要取用匹配到的捕获组, 可以使用 `\1` 取出第一个, `\2` 取出第二个, 以此类推. 需要注意的是 `\0` 是整个表达式.

不过要在 Python 中对捕获组进行处理, 需要用到 [`Match_object.group()` 方法](#group()). 并不使用 `\number` 的方法.

而且 `\number` 的方法, 在各个编辑器中没有统一的标准. `Vim` 中使用 `\number`, 而 `VsCode` 中使用 `$number`... 对于其他编辑器, 可能各有各的不同.

## 命名捕获组

定义捕获组时可以像这样命名:

```re
(?<hello>\S+)
```

这样, 就为该捕获组取了一个 `hello` 别名. 当然, 匹配时依然只会匹配 `\S+`, 不过在这之后, 可以使用 `\k<hello>` 来获取此捕获组内容.

在 Python 中, 语法有所不同, 需要添加一个字母 `P`:

```python
pattern = r'(?P<hello>\S+)'
```

然后可使用 `group('hello')` 来获取此捕获组的值.

# 在 Python 中使用 re 模块

> [lib.re.help#函数](/assert/resources/python/lib.re.help.txt.html#函数)

`re` 模块中最常用的函数有:

- `compile()` 将一个 pattern 编译为正则表达式对象, 以提升匹配效率.
- `split()` 用于切分字符串, 与内建的 `split()` 不同的是, 它使用正则表达式作为分隔符.
- `search()` 搜索整个字符串中匹配的表达式.
- `match()` 用于检测目标字符串是否能被正则表达式匹配.
- `group()` 用于提取匹配到的捕获组.
- `findall()` 用于搜索目标字符串中能被正则表达式匹配的内容, 并存储到一个列表中返回.

## compile()

```py
compile(pattern, flags)
  --> pattern_object
```

在每次使用正则表达式匹配 pattern 的时候都有

```
pattern-string --编译--> pattern-object ----> 用于匹配
```

的过程. 

对于同一个表达式需要使用多次的情况, 用 `compile()` 函数将 pattern 编译, 之后使用编译后的 pattern-object 进行匹配, 可以提高效率.

## split()

```py
split(pattern, string)
  --> list(cut_string)
```

例如:

```py
In [0]: import re
In [1]: STRING = "a, b, c,  ,d,e f"
In [2]: STRING.split(", ")
Out[2]: ['a', 'b', 'c', ' ,d,e f']      # 未能正确处理错误的情况
In [3]: re.split("[, ]+", STRING)
Out[3]: ['a', 'b', 'c', 'd', 'e', 'f']
```

## search()

```py
search(pattern, string, flags=0)
  --> Match_object
```

`search()` 将在整段 string 中搜索 pattern 匹配的字符串, 如果匹配成功, 则返回一个 `Match` 对象, 否则返回 `None`.

## match()

```py
match(pattern, string, flags=0)
  --> Match_object
```

`match()` 会尝试在字符串的开头匹配 pattern, 返回一个 `Match` 对象. 找不到匹配项时返回 `None`. 与 `search` 不同之处在于, `match` 不会扫描整个字符串, 它只从给定字符串的开头进行匹配.

一般来讲, `match` 常用于检测输入是否合法, 或者用于从一个整理好的字符串中提取捕获组.

## group()

```py
Match_object.group(index)
  --> str
```

`group()` 常与 `search` 或 `match` 连用, 对于其返回的 `Match` 对象, 可用 `group` 方法取出匹配到的捕获组内容.

```py
In [1]: import re
In [2]: Match_object = re.match("This is (\S+), Hello!","This is Mike, Hello!")
In [3]: Match_object.group(0)
Out[3]: 'This is Mike, Hello!'
In [4]: Match_object.group(1)
Out[4]: 'Mike'
```

`group(0)` 为表达式自身, `group(1)` 开始则按顺序为对应的捕获组.

要提取命名捕获组, 向 `group()` 中传递对应命名的字符串即可.

## findall()

```py
findall(pattern, string, flags=0)
  --> list(matched)
  --> list(tuple(matched groups))
```

`findall()` 函数会以列表的形式返回 string 中所有与 pattern 向匹配的字符串. 如果在 pattern 中定义了捕获组, 则将会返回以元组的形式组织起来的捕获组匹配项列表.

## sub() 与 subn()

```py
sub(pattern, repl, string, count=0, flags=0)
  --> str(替换后字符串)
subn(pattern, repl, string, count=0, flags=0)
  --> tuple(str(替换后字符串), int(替换次数))
```

`sub()` 函数用于搜索替换字符串. 它将 `string` 中被 `pattern` 匹配到的部分用 `repl` 替换. 在 `pattern` 中匹配的捕获组可被 `repl` 取用.

`count` 参数决定替换次数, 若为 0 则会全部替换.

以下为实例:

```py
In [1]: import re
   ...: FROM = """\
   ...: Name:           Mike Donald
   ...: Age:            18
   ...: Address:        Earth
   ...: """
   ...:
   ...: pattern = r"Name:\s*([\S ]+)\s*Age:\s*([ \S]+)\s*Address:\s*([\S ]+)"
   ...: repl    = r"""姓名: \1
   ...: 年龄: \2
   ...: 地址: \3
   ...: """
   ...:
   ...: TO = re.sub(pattern, repl, FROM)
   ...:
   ...: print(TO)
   ...:
   ...:
姓名: Mike Donald
年龄: 18
地址: Earth
```

TODO: 另外还有一些函数, 留待日后讲解.

```
escape(pattern)
    """转义除了 ASCII 字母, 数字, 与下划线 `_` 之外的所有字符."""

finditer(pattern, string, flags=0)
    """Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a match object.
    Empty matches are included in the result."""

fullmatch(pattern, string, flags=0)
    """Try to apply the pattern to all of the string, returning
    a match object, or None if no match was found."""

purge()
    """清除正则表达式缓存"""

template(pattern, flags=0)
    """Compile a template pattern, returning a pattern object"""
```

## re.flags

对于 re 模块中的一些函数, 有一个可选参数为 `flags`, 该参数用于决定函数解析表达式时的一些策略, 其值的含义如下.

这些参数都是 re 模块下的一级数据. `import re` 的情况下以 `re.X` 的方式使用, `from re import *` 的情况下以 `X` 的方式使用.

```
A           = <RegexFlag.ASCII: 256>
ASCII       = <RegexFlag.ASCII: 256>
DOTALL      = <RegexFlag.DOTALL: 16>
I           = <RegexFlag.IGNORECASE: 2> # 忽略大小写
IGNORECASE  = <RegexFlag.IGNORECASE: 2>
L           = <RegexFlag.LOCALE: 4>
LOCALE      = <RegexFlag.LOCALE: 4>     # 使用本地化时间日期表示法
M           = <RegexFlag.MULTILINE: 8>
MULTILINE   = <RegexFlag.MULTILINE: 8>  # 多行模式
S           = <RegexFlag.DOTALL: 16>
U           = <RegexFlag.UNICODE: 32>   # 使用 Unicode 识别
UNICODE     = <RegexFlag.UNICODE: 32>
VERBOSE     = <RegexFlag.VERBOSE: 64>
X           = <RegexFlag.VERBOSE: 64>
```

# Regex 语法列表

|表达式|含义|备注|
|:-:|-|-|
|`\`|转义字符||
|`.`|任意字符(不包括换行符)|要匹配换行符, 使用 `[.\n]`|
|定位符|||
|`^`|字符串首|匹配字符串开始位置, 如果设置了 multiline, 也可匹配换行符之后的位置|
|`$`|字符串尾|匹配字符串结束位置, 如果设置了 multiline, 也可匹配换行符之前的位置|
|限制符|||
|`{}`|限制符|限制字符重复次数|
|`{n}`|字符正好出现 n 次||
|`{n,}`|字符至少出现 n 次||
|`{m,n}`|字符出现 m 到 n 次||
|`*`|字符出现 0 次或任意次|`{0,}`|
|`+`|字符至少出现一次|`{1,}`|
|`?`|字符出现 0 次或 1 次|`{0,1}`|
|`?`|贪婪设置符|当 `?` 紧跟某限制符时, 匹配使用非贪婪模式|
|字符集合|||
|<code>&#124;</code>|表示"或"|这东西优先级不高|
|`()`|捕获组||
|`[]`|字符集|表示包括其中字符|
|`[^]`|负值字符集合|不包括其中字符|
|`[-]`|字符范围|`[a-z]` 包括所有小写字母, 顺序按照 Unicode 排序(包含了 ASCII)|
|特殊元字符|||
|`\s`|任意数量的空白字符|如空格, 换行符等|
|`\S`|任意数量的可见字符|如普通字母, 汉字等|
|`\b`|匹配一个单词边界|如 `This is a high tower`, `hi\b` 将会匹配 `high` 中的 `hi`, 而 `This` 中的 `hi` 不会匹配|
|`\B`|匹配一个非单词边界||
|`\d`|匹配数字字符|等价于 `[0-9]`|
|`\D`|匹配非数字字符|等价于 `[^0-9]`|
|`\w`|匹配字母, 数字, 下划线|等价于 `[A-Za-z0-9_]`|
|`\W`|匹配非字母, 数字, 下划线|等价于 `[^A-Za-z0-9_]`|
|`\x`|匹配一个 16 进制编码字符, 使用 ASCII编码|例如 `\x048` 表示 `0`|
|`\u`|匹配一个 16 进制编码字符, 使用 Unicode编码||
|`\num`|引用前方获取的捕获组||
|`\c`|匹配 [控制字符](#值得在意的控制字符)|例如 `\cM` 匹配回车 `\r`(`Control-M`)|

## 值得在意的系统控制字符

- 换行符, `\n`, `control-J`
- 回车符, `\e`, `control-M`
- 换页符, `\f`, `control-L`
