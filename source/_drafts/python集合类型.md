---
comments: true
title: '[PyNote]-3.2-Python集合类型'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-07-29 21:37:35
---

- 集合类型
  - 列表 list
  - 元组 tuple
  - 字典 dict
  - 集合 set

集合类型由称 "容器" 类型, 它们的特征是拥有一个 `__iter__()` 方法, 用于获取容器中的下一个元素.

字符串也应当归于集合(不是 `set`)类型之中. 集合类型的切片方法和字符串的切片方法一致, 不再赘述.

# 列表与元组

## 创建列表与元组

创建一个列表与元组可分别调用 `list()` 和 `tuple()` 函数. 如果不传入参数, 将生成空列表 (元组), 如果传入参数, 将会将其转化为对应的列表 (元组).

除了调用 `list()` `tuple()` 函数之外, 还可以直接通过 `[]` 生成列表, `()` 生成元组. 这两种不同的括号正好代表了其对应类型的输出.

```py
In [1]: LIST = list()

In [2]: LIST
Out[2]: []      # 列表的代表为方括号.

In [3]: LIST = list("zombie110year")

In [4]: LIST
Out[4]: ['z', 'o', 'm', 'b', 'i', 'e', '1', '1', '0', 'y', 'e', 'a', 'r']
In [5]: LIST = [1,]     # 最好添加一个逗号, 表示结束输入.

In [6]: LIST
Out[6]: [1]
```

对于元组也同样.

Python 中的列表与元组, 其中的元素类型可以不同.

### 列表生成式

可以用 `[x for x in range(0,10)]` 来生成列表. 并且可以使用多层 `for` 循环, 还能使用 `if` 判断语句.

**不可用于生成元组, 因为元组对象一创建便不可变.**

```py
In [1]: [x for x in range(10)]
Out[1]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [2]: [x**3 for x in range(10)]
Out[2]: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

In [3]: [x+y for x in "ABC" for y in "abc"]
Out[3]: ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']

In [4]: [x for x in range(10) if x % 2 == 0]
Out[4]: [0, 2, 4, 6, 8]
```

## 操作列表与元组

### 通过 index 索引

列表与元组都可以通过 `index` 进行操作. 在此种操作上, 比较类似于字符串. 与字符串稍有不同的是, 每一项的元组不一定是单个字符.

```py
In [1]: LIST = [1,2,3,4,5]

In [2]: LIST[::-1]      # 最简单的取倒序
Out[3]: [5, 4, 3, 2, 1]
```

而元组与列表有不同的一点是, 元组的每一项不可修改.

```py
In [11]: TUPLE = (1, 2, 3, 4)

In [12]: TUPLE[1] = 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-645a8d4a3749> in <module>()
----> 1 TUPLE[1] = 2

TypeError: 'tuple' object does not support item assignment
```

### 列表与元组类型的方法

[方法和函数有什么区别?](/2018/08/pynote-函数.html#方法)

#### 列表

```py
append(...)
    L.append(object) -> None -- 在末尾添加 object

clear(...)
    L.clear() -> None -- 清空所有元素

copy(...)
    L.copy() -> list -- 复制出一个新的列表, 和赋值不同, 赋值不产生新列表, 仅仅创建一个新的指向此列表的变量.

count(...)
    L.count(value) -> integer -- 返回列表中 value 元素出现的次数

extend(...)
    L.extend(iterable) -> None -- 将 iterable 添加到列表的最后来扩展该列表

index(...)
    L.index(value, [start, [stop]]) -> integer -- 返回 value 在列表中第一次出现时的 index, 如果不存在则抛出异常 ValueError,
    可选参数 start, stop 分别指定扫描范围

insert(...)
    L.insert(index, object) -- 将 object 插入到 index 处, 原处于该处以及其后元素依次后延

pop(...)
    L.pop([index]) -> item -- 移除一个元素并返回其 index, 默认移除末尾元素.
    如果列表已空或 index 超出范围将抛出异常 IndexError.

remove(...)
    L.remove(value) -> None -- 移除 value 在列表中的第一次出现.
    如果 value 在列表中根本不存在, 则返回异常

reverse(...)
    L.reverse() -- **原地** 反转!

sort(...)
    L.sort(key=None, reverse=False) -> None -- **原地** 排序!
```

#### 元组

相比列表, 元组只有不修改其自身的方法.

```py
count(...)
    T.count(value) -> integer -- return number of occurrences of value

index(...)
    T.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
```

# 字典与集合

## 创建字典与集合

创建字典和集合分别使用 `dict()` 和 `set()` 函数. 也可以使用 `{}` 花括号来生成一个字典. 集合与字典都使用花括号来标识, 但是字典中的每一个元素都是 `key:value` 对, 而集合则是普通的无序集合.

### 字典

字典每一项的 `key` 都必须是不可变对象, 而 `value` 则没有限制. 另外, `key` 不能重复, 否则后方的 `key` 对应的 `value` 将会覆盖前方的.

```py
In [1]: dictionaty = {
   ...: "first":1,              # 字符串, 可
   ...: 2:"2",                  # 整数 , 可
   ...: 3.0:3,                  # 浮点数, 可
   ...: (1,3,5):(2,4,6),        # 元组, 可
   ...: (2,4,6):[1,3,5],        # value 可以是可变对象.
   ...: }

In [2]: dictionaty
Out[2]: {'first': 1, 2: '2', 3.0: 3, (1, 3, 5): (2, 4, 6), (2, 4, 6): [1, 3, 5]}
```

而试图以可变对象为键时, 就会出现这样的错误: (unhashable type)

```py
In [3]: dictionary = {[1,]:"You can't do it!"}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-22702d38b0b6> in <module>()
----> 1 dictionary = {[1,]:"You can't do it!"}

TypeError: unhashable type: 'list'
```

也可以调用 `dict()` 函数来得到一个字典, 不过限制挺多的.

```py
In [1]: dict(a=1,b=2,c=3)               # 使用关键词参数制造字典, 关键词会作为字符串形式的 key
Out[1]: {'a': 1, 'b': 2, 'c': 3}

In [2]: dict(5=1.0,2=a,1=3)                             # 不能用数字做关键词
  File "<ipython-input-2-13e421139ff8>", line 1
    dict(5=1.0,2=a,1=3)
        ^
SyntaxError: keyword can't be an expression


In [3]: dict(first=1, second=2, '3th'=3)                # 不能用字符串做关键词
  File "<ipython-input-3-15e990637fb4>", line 1
    dict(first=1, second=2, '3th'=3)
                           ^
SyntaxError: keyword can't be an expression


In [4]: dict(first=1, second=2, 3th=3)                  # 关键词必须为合法的变量
  File "<ipython-input-4-eee19b50a0c6>", line 1
    dict(first=1, second=2, 3th=3)
                              ^
SyntaxError: invalid syntax

In [5]: dict(th3=3)                                     # 关键词必须为合法的变量
Out[5]: {'th3': 3}

In [6]: dict(first=0, second=1, third=2)
Out[6]: {'first': 0, 'second': 1, 'third': 2}

In [7]: dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典, 前者为 Key, 后者为 value, 一一对应
Out[7]: {'three': 3, 'two': 2, 'one': 1} 

In [8]: dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典, item == (key,value)
Out[8]: {'three': 3, 'two': 2, 'one': 1}
```

### 集合

集合可以调用 `set()` 函数来创建, 也可以使用 `{}` 花括号, 只要不使用 `key:value` 这样的结构, 就不会被认为是字典.
但是创建空集合的时候不能使用 `{}`, 这会创建一个空字典.

```py
In [7]: se = {1,23,4}

In [8]: se
Out[8]: {1, 4, 23}
```

`set()` 函数可以接受任何带有 "集合" 性质的数据. 例如 字符串,列表,元组,字典,集合, 不过当接收字典时, 只会将 `key` 转化为集合中的元素, 而 `value` 不知所踪.
不过如果想要传递一个字符串, 需要使用类似于 `("string",)` 的形式, 否则, 会被拆分为一个个字符.
另外, 和数学上的集合一致, 同样的元素, 在集合中仅能存在一个.

```py
In [10]: se = set("test")       # 转化字符串

In [11]: se
Out[11]: {'e', 's', 't'}        # 两个 t 字符只留下来一个.

In [12]: se = set([23,32,23,])  # 转化列表

In [13]: se
Out[13]: {23, 32}               # 有个 23 重复了

In [14]: se = set((1,2,3,1))    # 转化元组

In [15]: se
Out[15]: {1, 2, 3}              # 重复的 1 只有一个保留

In [16]: set({1:2, 3:4})        # 转化字典
Out[16]: {1, 3}                 # 只收了 key.
```

## 可对字典进行操作

### 访问字典的值

可以通过 `dic[key]` 的方式访问字典中 key 对应的值. 可以通过 `dic[key] = new_value` 的方式为字典中某元素重新赋值. 但是不可以改变 key.

### 字典的方法

`dict` 类型的方法 (Method).

[Python 赋值, 浅拷贝, 深拷贝的关系](http://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html)

```py
clear(...)
    D.clear() -> None.  清除字典中所有元素.

copy(...)
    D.copy() -> dict.   复制一个新的字典, 如果不使用 new = old.copy(), 
    而使用 new = old, 那么 new 与 old 将会指向同一对象.

fromkeys(iterable, value=None, /) -> dict
    返回一个新的字典, key 与 iterable 参数传递的字典一致, 每一项的 value 与 value 参数一致.

get(...)
    D.get(key[,default=None]) -> D[key]
    如果 key 在字典 D 中存在, 那么返回对应的 value, 如果不存在, 返回 default 的值.

items(...)
    D.items()   -> a set-like object providing a view on D's items

keys(...)
    D.keys()    -> a set-like object providing a view on D's keys

values(...)
    D.values()  -> an object providing a view on D's values

In [1]: dictionaty
Out[1]: {'first': 1, 2: '2', 3.0: 3, (1, 3, 5): (2, 4, 6), (2, 4, 6): [1, 3, 5]}

In [2]: dictionaty.keys()
Out[2]: dict_keys(['first', 2, 3.0, (1, 3, 5), (2, 4, 6)])

In [3]: dictionaty.items()
Out[3]: dict_items([('first', 1), (2, '2'), (3.0, 3), ((1, 3, 5), (2, 4, 6)), ((2, 4, 6), [1, 3, 5])])

In [4]: dictionaty.values()
Out[4]: dict_values([1, '2', 3, (2, 4, 6), [1, 3, 5]])

In [5]: type(dictionaty.keys())
Out[5]: dict_keys

In [6]: type(dictionaty.items())
Out[6]: dict_items

In [7]: type(dictionaty.values())
Out[7]: dict_values

pop(...)
    D.pop(key [,default]) -> value
    移除指定的 key, 并返回对应的 value.
    如果 key 不存在, 则将会返回给定的默认值 default, 如果给 default 传递参数, 则会抛出 KeyError.

popitem(...)
    D.popitem() -> (key, value)
    随机移除并返回二元元组形式的 (key, value) 对.
    如果字典已经为空, 则抛出 KeyError.

setdefault(...)
    D.setdefault(key [,default]) -> D.get(key,defualt)
    如果 key 不存在, 则将 D[key] 设置为 default 参数传递的值.

update(...)
    D.update([E, ]**F) -> None.
    从另一字典 F 或可迭代对象 E 更新字典 D.
    将会把 E 或 F 的项以字典项的形式添加到字典 D 中.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
```

## 可对集合进行操作

### 不可直接访问集合中的元素

### 集合的数学运算

Python 中的集合可以进行数学中的交集,并集,补集等运算:

```py
In [1]: SET1 = {1,2,3,4}
In [2]: SET2 = {1,2}
In [3]: SET3 = {  2,  4,  6,  8}
In [4]: SET4 = {1,  3,  5,  7}
# 交集 使用 & 运算符
In [5]: SET1 & SET2
Out[5]: {1, 2}
# 并集 使用 | 运算符
In [6]: SET3 | SET4
Out[6]: {1, 2, 3, 4, 5, 6, 7, 8}
# 补集 使用 - 运算符
In [7]: FULL = SET3 | SET4
In [8]: FULL - SET2
Out[8]: {3, 4, 5, 6, 7, 8}
```

### 集合的方法

```py
add(element) -> None
    将元素添加入集合, 如果重复则无效.

clear() -> None
    移除集合中所有元素.

copy() -> set
    返回集合的浅复制.

difference(set) -> set
    返回两集合的补集. 以原集合为全集.

difference_update(set) -> None
    移除此集合中与输入集合相同的元素. 相当于将原集合设置为补集.
    Remove all elements of another set from this set.

discard(element) -> None
    从集合中移除指定元素, 如果不存在, 就不起作用.

intersection(set) -> set
    返回此集合与输入集合的交集.

intersection_update(set) -> None
    将原集合设置为两者的交集.

isdisjoint(set) -> bool
    如果两集合交集为空, 返回 True.

issubset(set) -> bool
    判断此集合是否是输入集合的子集.

issuperset(set) -> bool
    判断此集合是否包含输入集合.

pop([element]) -> element
    移除并返回集合中的某元素. 如果集合为空, 则抛出 KeyError.
    如不指定, 则会移除集合中按集合规律排序的第一个元素.

remove(element) -> None
    移除集合中的某元素, 其必须为集合中的成员.
    如果不是成员, 抛出 KeyError.

symmetric_difference(set) -> set
    返回两组的对称差异作为新集合.
    即, 总是返回两个集合中子集相对于全集的补集.
    如果原集合为子集, 则输入集合作为全集, 如果输入集合作为子集, 则原集合为全集.

symmetric_difference_update(set) -> None
    把 symmetric_difference(set) 的返回值赋值给原集合.

union(set) -> set
    返回两集合的并集.

update(set) -> None
    将两集合的并集赋值给原集合.
```

## 字典,集合生成式

```py
In [48]: {x:x*2 for x in range(5)}
Out[48]: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

In [49]: {x**3 for x in range(5)}
Out[49]: {0, 1, 8, 27, 64}
```

可以看出, 列表,字典,集合的生成式都是 "表达式" + `for` + "变量" + `in` + "容器对象" 的结构.

# in 运算符

集合类型的对象都可以使用 `in` 运算符判断某元素是否存在其中.

使用 `for ... in ...:` 迭代时也能遍历全部. 对于列表和元组, 按 index 顺序遍历, 而对于集合与字典, 则按其内部的排序遍历. 具体顺序与 HashTable 的性质有关. 对于字典, 遍历的对象为它的 `key`.

# *var 与 **var

如果为一个变量赋值了集合类型的对象, 则可用 `*var` 或 `**var` 来表示它.

- `*var`    可用于表示列表或元组.
- `**var`   可用于表示集合或字典.

函数的可变参数便是用集合类型对象来存储的.

# 字典与集合的本质

TODO: HashTable?
