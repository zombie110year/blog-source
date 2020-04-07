---
comments: true
title:  py排列与组合
date:   2018-9-15 15:45:58
has_math: true
tags:
    - python
categories: 笔记
---

排列 Permutation
================

假设有这么一条列表, 其中的元素有:

::

    ABCDEFG

那么, 要生成规律的排列, 很明显得靠递归, 需要

1.  从上次传入的待处理列表中除去一个元素(按顺序循环)
2.  将除去的元素写入已处理列表
3.  将列表传入递归
4.  直到待处理列表为空或取元素的数目达到条件, 就终止递归,
    并将已处理的元素写入存储池

当所有递归步骤结束后, 存储池中就存储了目标序列的排列.

排列的数目, 就是数学中的 ``排列数``:

.. math::

    A_m^n = \frac{m!}{n!}

以举例的列表为例,

::

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

Python 标准库::

    itertools.permutations(iterable, r=None)
        :param iterable: 可迭代对象
        :type iterable: Iterable[T]
        :param r: 长度
        :returns: 一组排列的迭代器
        :rtype: Iterator[tuple]

        输入一个可迭代对象和排列的长度，返回一组排列的迭代器。
        迭代返回的每一个对象都是一个元组，记录一种排列方式。

标准库的中排列算法由 C 语言实现。

组合 Combination
================

组合与排列的算法大同小异, 只不过组合需要注意, 组合是无序的, AB 与 BA
是同一个组合.

因此, 只需要对排列的代码进行一点小修改, 把已经使用过的列表截断即可.

组合的数目就是 ``组合数``:

.. math:: C_m^n = \frac{m!}{n!(m-n)!}

同样, 以例子来说明.

::

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

Python 标准库::

    itertools.combinations(iterable, r=None)
        :param iterable: 可迭代对象
        :type iterable: Iterable[T]
        :param r: 长度
        :returns: 一组组合的迭代器
        :rtype: Iterator[tuple]
