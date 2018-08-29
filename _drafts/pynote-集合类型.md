---
title: '[PyNote]-3.2-Python集合类型'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-07-29 21:37:35
---

- 集合
  - 列表
  - 元组
  - 字典

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

### 列表与元组对象的方法

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