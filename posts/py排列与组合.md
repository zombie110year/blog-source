---
comments: true
title:  py排列与组合
date:   2018-9-15 15:45:58
mathjax:  true
tags:
    - Algorithm
    - Python
categories:
    - 算法
---

<!--more-->

# 排列 Permutation

假设有这么一条列表, 其中的元素有:

```
ABCDEFG
```

那么, 要生成规律的排列, 很明显得靠递归, 需要

1. 从上次传入的待处理列表中除去一个元素(按顺序循环)
2. 将除去的元素写入已处理列表
3. 将列表传入递归
4. 直到待处理列表为空或取元素的数目达到条件, 就终止递归, 并将已处理的元素写入存储池

当所有递归步骤结束后, 存储池中就存储了目标序列的排列.

排列的数目, 就是数学中的 `排列数`:

$$A_m^n = \frac{m!}{n!}$$

以举例的列表为例,

```
ABCDEFG
-> A BCDEFG
--> ...
-> B ACDEFG
--> ...
-> C ABDEFG
...
-> E ABCDFG
--> EA BCDFG
--> EB ACDFG
...
```

Python 标准库

```python
itertools.permutations(iterable:iter[, r:int])->itertools.permutations:
    """输入可迭代对象与层数(默认为总长), 返回一个排列实例,
    不可用对其他可迭代对象的方法取出其中元素, 除了 for 循环.
    但是可先将其转换为 list 或 tuple.
    (每一个元素为一个排列)"""
```


```python
def myperm(Iter:list, Count:int)->list:
    result = []
    def _trueAlgo(done:list, rest:list, count:int)->list:
        if count == 0:
            nonlocal result
            result.append(tuple(done))
        else:
            for index in range(len(rest)):
                _rest = rest[:]
                _del = _rest.pop(index)
                _trueAlgo([*done, _del], _rest, count-1)
    _trueAlgo(done=[], rest=Iter, count=Count)
    return result
```

# 组合 Combination

组合与排列的算法大同小异, 只不过组合需要注意, 组合是无序的, AB 与 BA 是同一个组合.

因此, 只需要对排列的代码进行一点小修改, 把已经使用过的列表截断即可.

组合的数目就是 `组合数`:

$$C_m^n = \frac{m!}{n!(m-n)!}$$

同样, 以例子来说明.

```
ABCDEFG

-> A BCDEFG
--> AB CDEFG
--> AC DEFG
--> AD EFG
--> AE FG
--> ...
-> B CDEFG
--> BC DEFG
--> ...
--> BE FG
...
```

Python 标准库

```python
itertools.combinations(iterable:iter, r:int) -> itertools.combinations:
    """输入可迭代对象与层数(必选), 返回一个组合实例,
    不可用对其他可迭代对象的方法取出其中元素, 除了 for 循环.
    但是可先将其转换为 list 或 tuple.
    (每一个元素为一个组合)"""
```


```python
def mycombi(Iter:list, Count:int)->list:
    result = []
    def _trueAlgo(done:list, rest:list, count:int)->list:
        if count == 0:
            nonlocal result
            result.append(tuple(done))
        else:
            for index in range(len(rest)):
                _rest = rest[index:] #!免逆序重复
                _del = _rest.pop(0)
                _trueAlgo([*done, _del], _rest, count-1)
    _trueAlgo(done=[], rest=Iter, count=Count)
    return result
```
