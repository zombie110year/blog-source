---
title: '[PyNote]-3.1-Python中的数字与字符串'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-07-28 21:37:09
---

- 数字
  - 整数
  - 浮点数
  - 复数
- 字符串

> 可以使用 Python 内建函数 `type()` 来查看一个数据的类型

# 基本数据类型

## 整数-int

Python 中的整数与长整数没有什么区别 (Python3). 因为 Python3 会自动地处理整数的存储方式, 将整型与长整型互换. 从理论上讲, Python 中的整数的位数可以是无限长, 但实际上, 会受到内存空间的限制.

整数的相关信息可以从 `sys.int_info` 获得

```py
import sys
print(sys.int_info)

# 以下是经过整理的输出信息

sys.int_info(           # 长整数是普通整数的组合
  bits_per_digit=30,    # 每个整数占用 30 个 bit. 
  sizeof_digit=4        # 每个整数占用 4 个 byte (32 bit) 的内存空间.
  )
```

TODO: 为啥差 2 bit 呢?

### 布尔数-bool

布尔数是整数的一个子集. 它其实就是只有一个 bit 的整数. 其取值只有 `0`, `1` (二进制).
在 Python 中, 还可以用 `True`(1) `False`(0) 来表示它们.

## 浮点数-float

所谓的浮点数, 就是一种表示小数或按科学记数法记录的数字的数据类型. 计算机处理它和整数的方法有很大的区别.

- 首先, 浮点数的位数不可能无限. 或者说, 浮点数的分布不是稠密的. 它不能和数学上的实数等价.
- 其次, 浮点数的存储方法依然是二进制, 而人类所使用的十进制的基数是 $ 10=2 \\times 5 $ , 有个质因子, 因此, 浮点数在表现数字的时候, 总是会有无法避免的误差, 导致错误的四舍五入. 例如, 可以试一试将一个超出浮点数存储范围的小数赋值给一个变量, 会发现超出的部分直接消失了; 若将一个无法用二进制表示的十进制数赋值给变量, 会发现莫名的误差.
  - 这里随便尝试了一下:

```py
>>> a = 1.0000000000000006
>>> print(a)
1.0000000000000007
>>>
>>> a = 1.00000000000000006
>>> print(a)
1.0
```

浮点数的相关信息可以从 `sys.float_info` 对象获得.

[Python 官方文档 对 sys.float_info 的解释](https://docs.python.org/3/library/sys.html#sys.float_info)

```py
import sys
print(sys.float_info)

# 以下是经过整理的输出信息

sys.float_info(         # 浮点数是以 2 进制储存的, 在需要时与 10 进制互相转换.
  max=1.7976931348623157e+308,  # 可表示的最大正数
  max_exp=1024,                 # < 2**1024
  max_10_exp=308,               # 十进制时可正常处理的最大指数
  min=2.2250738585072014e-308,  # 可表示的最小正数
  min_exp=-1021,                # > 2**-1021
  min_10_exp=-307,              # 十进制时可正常处理的最小指数
  dig=15,                       # 十进制下可正常处理的最大小数位数
  mant_dig=53,                  # 浮动精度, 二进制下表示有效数字的 bit 位数.
  epsilon=2.220446049250313e-16,# 十进制下 与 1 "相邻" 的浮点数与 1 的差. (浮点数的数量级不同, 这个值也不同, 详情...)
  radix=2,                      # "基数" 即指数部分的 "底数".
  rounds=1                      # 用于表示算术运算的舍入模式, 详情参见 C99 标准的5.2.4.2.2节
  )
```

对于一个

## 复数-complex

- 复数的概念与数学上的一致, 由 `实部+虚部j` 表示. 但是这里虚数单位的表示法是 `j` 不是 `i` , 需要注意别搞混淆了.
- 复数的实部与虚部都是浮点数.
- 可以使用 `complex.real` 和 `complex.imag` 分别取出复数的实部与虚部. (这里的 complex 是一个类型为复数的变量的变量名)

```py
test = 1.0 + 89.0j
print(str(test), end='=')
print(str(test.real), end='+')
print(str(test.imag)+'j')
```

输出为

```py
(1+89j)=1.0+89.0j
```

## 字符串-str

- Python 字符串用 `"字符串"` 引号括起来, 可以使用双引号也可以使用单引号. 双引号中可以嵌套单引号, 反过来也一样. 但如果要在双引号中表示双引号, 需要用 `\` 反斜杠转义 `\"`. 
  - 如果需要在字符串中表示反斜杠, 可以使用 `\\` 对反斜杠转义, 也可以使用 `r"不用\转义的原始字符串"` 在引号外使用字母 `r`.
  - 如果需要在字符串中使用 Unicode 编码插入 Unicode 字符, 可以在引号外使用字母 `u`. `u"这是一个\u0020字符"` (\u0020是空格).
  - 如果要将字符串转化为 `byte-like` 对象, 在引号外使用字母 `b`.
- Python 的字符串也可以使用成对的三引号`"""超级多的字符"""`. 这种方法标识的字符串中可以包含换行, 指标符和其他特殊字符.

```py
string = """测试三引号
包裹的字符
    是啥样的?
"""
print(repr(string))
```

输出了 `'测试三引号\n包裹的字符\n\t是啥样的?\n'` 可以看到, 特殊字符被识别并转换为对应的转义字符了.

- Python 没有单独的 "字符" 类型, 只有字符串. 但字符串中可以只有 1 个甚至 0 个字符.
- Python 字符串是只读的. 要更改, 可以创建并赋值一个新的字符串变量.
- Python 可用 `%` 符号表示格式化字符串. **其右侧本质上是一个元组(tuple)**

### 格式化字符串

|格式符|含义|
|-|-|
|`%c`|字符及其 ASCII 码|
|`%s`|字符串|
|`%d`|整数|
|`%o`|八进制整数|
|`%x`|十六进制整数|
|`%X`|十六进制整数(字母大写)|
|`%f`|小数表示的浮点数|
|`%e`|科学记数法表示的浮点数|
|`%E`|科学记数法表示的浮点数(字母大写)|
|`%g`|从 `%e` 和 `%f` 中选择输出短的|
|`%G`|从 `%E` 和 `%F` 中选择输出短的|

  - 传递多个格式化字符串需要使用 `()` 圆括号将参数括起来. 然后在内部用 `,` 逗号划分各参数. **元组**

```py
test1 = "hello"
test2 = "HELLO"
test3 = "WoRlD"
print("%s(%s) %s!"%(test1,test2,test3))
```

输出:

```
hello(HELLO) WoRlD!
```

  - 另一种格式化方法为 `"{}{}".format(a,b)`

```py
test1 = 1
test2 = 3.14
test3 = '哈哈哈'
# 按顺序
print("按顺序:{},{},{}".format(test1,test2,test3))
# 按索引号
print("按索引号:{2},{1},{0}".format(test1,test2,test3))
# 按参数名
print("按参数名:{a},{c},{b}".format(a=test1, b=test2, c=test3))
```

对格式化字符可以使用修饰符

|修饰符|含义|
|-|-|
|`#`|十六进制前添`0x`, 八进制前添`0`|
|`+`|在数字前添加正负号|
|`m.n`| `m`表示显示数字的总位数(整数部分+小数部分); `n` 表示保留小数点的位数, 若 `m` 的条件已达到, 则 `n` 将被忽略.|
|`0`|数字前填0, 默认空格|
|`-`|左对齐, 默认右对齐|

### 字符串的截取与分段

一个字符串变量, 实质上可以视作一个由字符拼接起来的 "元组", 可以在变量名后用 `[index]` 提取其中的一个元素, 或者使用 `[index1:index2]` 提取其中一段, 注意有一个 **要头不要腚** 的规则.

> 我突然想到用这个字符串来做例子也许会更形象...
> 
> ```py
> "_(:з」∠)_"    # 要头不要腚
> ```

```py
str = "abcdefg"
for i in range(7) # i = 0,1,2,3,4,5,6
    print(str[i], end=':index(%d)|'%(i))
print() # 换行
print(str[0:2]) # 打印 'ab\n'  (文雅点说"宁左毋右"吧).
```

index 号可以为非负数, 代表从左到右的索引号; 也可以为负数, 代表从右到左的索引号.

```
str     a  b  c  d  e  f  g
+       0  1  2  3  4  5  6
-      -7 -6 -5 -4 -3 -2 -1
```

index 可以留空一个, 表示从另一个开始一直取到末尾(或头部).

```py
print(str[2:]) # 打印 'cdefg\n' 从c开始向末尾
print(str[:4]) # 打印 'abcd\n'  从d开始向头部 (仍然不要腚)
```

无论正负, index 都是一个对字符位置的索引号而已. 所以它的大小关系和一般整数无关. 因此, 以下这些输出都是一样的.

```py
# 对照着上面那个表看
print(str[1:6])
print(str[-6:6])
print(str[1:-1])
# 都打印 'bcdef\n'

print(str[0:5])
print(str[:5])
print(str[:-2])
# 都打印 'abcde\n'
# ... 以此类推
```

### 字符串的"运算"

Python 中的字符串参与运算:

- `"str1" + "str2"` 拼接一个新的字符串 `"str1str2"`.
- `"str"*int` 重复一个字符串 `int` 次. 例如 `"str"*3` == `"strstrstr"` 

# 数据类型转换

## `int()`

`help(int())`:

```py
class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
```

- `int()` 可接受的参数有:
  - `x` 表示被转换的对象, 此参数未命名, 所以需要将对应实参放在参数表第一位.
  - `base` 表示转换时依据的进制基数, 默认 10 进制.
- 若 `x` 是一个整数, 返回其自身.
- 若 `x` 是一个浮点数, 其小数部分会被砍掉.
- 若 `x` 是一个字符串, 会将字符串中的字符依据定义的基数转换为对应的整数. 且该字符串中不能有基数表示范围以外的字符. 
  - 默认基数为 `base=10`, 可接受的基数值为 0 或 从 2 到 36. 
    - 就是说 10 进制下只能有 `0123456789`, 十六进制下可以有 `0123456789abcdef`, 最高可以在 36 进制下用 `z` 表示 `35`.
    - `base=0` 的情况下, 根据字符串内容猜测进制. 但适用情况较少:
      - `0x10` 会被识别为 16 进制的 `16`.
      - `f`    会被识别为 16 进制的 `15`.
      - `0o10` 会被识别为 8 进制的 `8`. (零后面是小写的字母O)
      - `29134` 会被识别为 10 进制.
      - `01423` 会被识别为 10 进制, 尽管没有任何大于 7 的数字, 在最前方也有个 `0`.
      - 只能从 `16` `8` `10` 中猜测.
  - 字符串中可以在前面有 `+ -` 正负号. 也可以在两侧有空格.
  - **规定了基数 `base` 时, 必须输入字符串.**

## `float()`

`help(float())`:

```py
class float(object)
 |  float(x=0, /)
 |
 |  Convert a string or number to a floating point number, if possible.
```

TODO: 文档说得这么简洁, 我也没啥好说的... 只能用多了再来说说感受了...

- `float.hex()` 返回一个用 16 进制表示的浮点数.
- `float.fromhex()` 从字符串转换一个 16 进制的浮点数. 形式为 `0xf.fp+1` 用 `p` 表示 16 为底的指数.

## `complex()`

`help(complex())`:

```py
class complex(object)
 |  complex(real=0, imag=0)
 |
 |  Create a complex number from a real part and an optional imaginary part.
 |
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.
```

## `str()`

```py
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
```

大意是说:

- 从给定对象创建一个新的字符串对象. 如果指定了 `encoding` 或 `errors`, 则必须公开 `bytes_or_buffer` 来编码字符串和处理错误信息.
- `str()` 可接受的参数有:
  - `object` 被转换的对象.
  - `bytes_or_buffer` 字节或缓冲区.
  - `encoding` 字符编码, 默认值由 `sys.getdefaultencoding()` 获得, 一般为 `utf-8`
  - `errors` 错误策略. 默认为 `strict`.

## 其他

- `hex()` 将整数转换为其 16 进制形式的字符串.
- `oct()` 将整数转换未其  8 进制形式的字符串.
- `chr()` 将整数按 ASCII 转换为字符. 若整数值超出了 255 , 则按 Unicode 转换. 整数可以是 10, 8, 16 进制. 范围为 `0<=i<=0x10ffff`.
- `ord()` 将字符 (单字符的字符串)转换为对应的 10 进制整数. 支持 Unicode .
- `repr()` 类似 `str()` 但返回的是一个字符串表达式.

```py
>>> repr('string')
"'string'"
>>> str('string')
'string'
```