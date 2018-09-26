---
title:  python生成器与可迭代对象
data:   2018-09-22 23:43:30
mathjax:  false
tags:
    - Python
    - Note
categories:
    - Python
---

# 列表生成式

在 Python 中, 可以使用 `[x for x in range(10)]` 来快速创建一个列表, 它将会按照 `[表达式 for 变量 in 范围]` 的方式来创建一个列表, 其中的每一个元素都是按照 `范围` 与 `表达式` 来计算得到的, 例如以下的列表生成式与定义的函数作用相同. 但是不管是从简洁性还是代码的复用性来说, 都是列表生成式更胜一筹.

```python
def generateList(l_range):
    the_list = []
    for var in l_range:
        the_list.append(2*var)
    return the_list
generateList(range(10))
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```python
[2*x for x in range(10)]
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

不过, 由于列表生成式会一次性将列表完整地生成出来, 所以对于一些对内存要求高的计算过程, 这就太过于奢侈了.

对于这种情况, 最好是使用生成器 (`generator`)

# 列表式生成器

一个生成器, 只储存了生成输出的算法, 而在实际使用中需要一个个计算出来.

创建一个生成器, Python 提供了简便的方法: 与列表生成式类似, 不过将方括号 `[]` 更换为圆括号 `()`

而要使用此生成器, 需要首先创建一个 **实例**.

```python
ge = (2*x for x in range(10))
ge
```

    <generator object <genexpr> at 0x7f34a425e990>

可以看到, 这是创建了一个 `<generaotr boject>` . 有两种方式得到其中的元素:

## 1.使用 `next()` 函数

```python
next(ge)
```

使用 `next(ge)` 函数, 将会调用生成器实例的 `__next__()` 方法, 返回生成器的下一次输出, 每次调用都会修改生成器的步数. 当生成器步数到达其末尾时 (本例的 `ge` 生成器末尾为 `range(10)` 的最后一项 `x=9`), 将会抛出 `StopIteration` 错误. 并且, 要得到一次输出, 就得使用一次 `next()`, 非常麻烦, 因此, 更建议使用 `for` 循环.

## 2. 使用 `for` 循环

使用 `for` 循环对于得到生成器的输出非常方便, 并且也不会抛出 `StopIteration` 错误, 能遍历所有元素.

```python
for item in ge:
    item
```

如果在一个程序中同时使用了 `next()` 与 `for`, 那么它们对生成器的修改是相关的.

# 函数式生成器

上文提到了 "列表式生成器", 这是一种简洁的生成器表示法, 但是, 如果计算对象比较复杂, 有相当多的逻辑判断, 那么使用函数式的生成器是一个更好的选择.

总的来说, 函数式生成器与定义一个函数差不多, 只不过将 `return` 语句替换为 `yield` 语句.

下面以一个得到质数的粗暴算法为例:

要得到一个质数, 可以:

0. 从整数 2 开始, 依次递增
0. 判断当前整数是否能被从 2 到其自身 -1的整数整除
    - 判断为 `True` 则返回当前整数
    - 判断为 `False` 则将当前整数 +1, 进入下一次运算

```python
def generatePrime():
    yield 2
    yield 3 # 先把前两个质数输出
    cur = 3 # 当前整数
    while True:
        var = 2 # 每次外层循环初始化检验数
        cond = False
        cur += 2 # 因为除了 2 之外的所有偶数都可以排除
        while True:
            if cur <= var:  # 检查是否已经通过检查
                cond = True
                break
            elif cur%var == 0:
                break
            elif cur%var != 0:
                var += 1
        if cond:
            yield cur
gen =  generatePrime() # 创建生成器实例
```

```python
n = 0
while n < 10:
    print(next(gen), end=' ')
    n += 1
```

```
2 3 5 7 11 13 17 19 23 29
```

在定义了一个函数式的生成器时, 与列表式生成器相同, 需要首先创建一个 **生成器实例**.

在每次使用 `next` 或 `for` 循环时, 生成器都会运行到 `yield` 语句并返回对应值, 而在下一次调用时从上次的 `yield` 语句开始.

# 可迭代对象与迭代器

Python 中, 可迭代对象 `Iterable` 包括了 列表,元组,集合,字典,生成器 等概念, 它们的共同特点是可以实际地或者概念上地表示一个集合.

列表,元组,集合,字典 都包含了真实存在的所有元素, 需要占用真实的空间, 因此其可以包含的元素是有限的. 可以通过 index 或者 key 来随时取出其中的元素.

而生成器 `generator` 属于迭代器 `Iterator`, 这是一种惰性运算的序列, 它只存储了给出下一个元素的算法. 因此可用来表示一个概念上的序列和无限的元素. 不过, 它必须通过一次次计算才能依次得到目标. `Iterator` 类定义了 `__next__()` 方法, 用来取得下一个元素, 而 `next()` 函数正是调用了对应实例的此方法.

Python 中的 `for` 循环是通过 `Iterator` 的 `__next__()` 方法来遍历整个可迭代对象的. 实际上, 有这么一个函数 `iter()` 用来创建或转换一个可迭代对象. `for` 循环的机制可以通过利用该函数和 `while` 循环来实现:

```python
for item in range(10):
    item
```

```python
n_iter = iter(range(10))
while True:
    try:
        n_iter.__next__()
    except StopIteration:
        break
```

# 小结

## 列表生成式

```python
[x*x for x in range(100) if x%2 != 0]
```

生成一个列表, 其中的每一项元素都是由生成式最前方的表达式 `x*x` 计算而来, `x` 的值则由后方的逻辑结构决定.

逻辑结构由前向后解释, 可以连用多个.

## 生成器

### 列表式生成器

```python
(x*x for x in range(100) if x%2 !=0)
```

### 函数式生成器

```python
def generator1():
    for x in range(100):
        if x%2 != 0:
            yield x*x
```

### 使用生成器

0. 创建生成器实例

```python
ge = (x*x for x in range(100) if x%2 !=0)
ge = generator1()
```

1. 使用 `next()` 函数或生成器的 `__next__()` 方法

```python
next(ge)
ge.__next__()
```

2. 使用 `for` 循环

```python
for item in ge:
    item
```

## 迭代器与 for 循环

使用函数 `iter()` 创建一个可迭代对象.

`for` 循环可以利用 `while` 循环实现:

```python
the_iter = iter([x*x for x in range(100) if x%2 != 0])
while True:
    try:
        item = the_iter.__next__()
    except StopIteration:
        break
```
