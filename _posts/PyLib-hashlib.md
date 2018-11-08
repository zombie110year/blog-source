---
comments: true
title:  Python 的 hashlib 库
data:   2018-10-05 14:34:19
mathjax:  false
tags:
    - Python
    - Note
categories:
    - Python
---

# 简介

`hashlib` 提供了 `md5`, `sha1` , `sha256` 等多种散列算法的支持. 要查看所有支持的算法, 可以查阅内置的集合 `algorithms_available`, 另外, `hashlib` 给出了推荐使用的算法, 查阅集合 `algorithms_guaranteed`.

```python
hashlib.algorithms_guaranteed
```

    {'blake2b',
     'blake2s',
     'md5',
     'sha1',
     'sha224',
     'sha256',
     'sha384',
     'sha3_224',
     'sha3_256',
     'sha3_384',
     'sha3_512',
     'sha512',
     'shake_128',
     'shake_256'}

<!--more-->

# 哈希函数通用操作

`hashlib` 中的 HASH 算法, 对于使用者来说很多操作都是一样的, 例如传入计算目标, 更新 hash 对象, 获取 16 进制表示等. 而且, 每一个 hash 算法, 都是用 `bytes(0)` 作初始值的.

- 所有 hash 函数都应该传入一个 `bytes` 类型的数据, 如果是字符串, 应使用 `encode()` 方法进行编码, 其他对象, 应使用 `bytes()` 函数编码.
- 所有 hash 函数都返回对应的 hash 对象实例, `md5()` 函数返回 `md5` 对象, 以此类推. 对于该实例, 可以进行 `update()` 操作, 用于更新 hash 对象. 此操作可用于分片计算 hash 目标, 效果和一次性传入是一样的.
- 所有 hash 对象, 都可以用 `hexdigest()` 方法获取其 16 进制表示(字符串格式).

`hashlib` 返回 hash 对象实例的这一特性, 可以很容易地运用到并行计算上.

以下将用 `"TestString"` 和 `"Test"` `"String"` 来演示 `md5`, `sha1` 算法的结果.


```python
x = "TestString".encode('utf-8')
x1 = "Test".encode('utf-8')
x2 = "String".encode('utf-8')
```

## md5

`md5` 是最常用的 HASH 算法, 具有速度快的特点. 生成值为一个 128bit 的二进制数, 常用 32 位的 16 进制数(字符串格式)表示.

`md5` 的全称是 "Message-digest Algorithm 5" (信息-摘要算法). 信息摘要算法能将任意长度的数据计算出固定长度的摘要. 对原数据进行的任何改动, 都会使摘要值发生变化. (能产生 $2^{128}$ 个不同的摘要, 如果有更多的原数据, 那么就一定会产生重复的摘要了, 不过在 $2^{128}$ 范围内, 遇到重复摘要的概率基本可以忽略)


```python
hashlib.md5(x).hexdigest() # 实例化时传入全部参数
```

    '5b56f40f8828701f97fa4511ddcd25fb'

```python
md5_ = hashlib.md5()  # 创建实例, 但是不传入参数
md5_.hexdigest() # 仍然会产生一个默认的 md5 值, 此默认值和传入 bytes(0) 的效果相同.
```

    '5b56f40f8828701f97fa4511ddcd25fb'

```python
hashlib.md5(bytes(0)).hexdigest()
```
    'd41d8cd98f00b204e9800998ecf8427e'

```python
md5_.update(x1)
md5_.hexdigest() # 用 "Test" 更新后, 产生了新的 md5 值
```

    '0cbc6611f5540bd0809a388dc95a615b'

```python
md5_.update(x2)
md5_.hexdigest() # 现在使用 "String" 再次更新, 产生的 md5 值和直接传入 "TestString" 一样了!
```

    '5b56f40f8828701f97fa4511ddcd25fb'

## sha1

sha1 生成值为一个 160bit 的二进制数据, 常用 40 位的 16 进制数(字符串格式)表示.

```python
hashlib.sha1(x).hexdigest()
```

    'd598b03bee8866ae03b54cb6912efdfef107fd6d'

```python
sha1_ = hashlib.sha1()
sha1_.update(x1)
sha1_.update(x2)
```

```python
sha1_.hexdigest()
```

    'd598b03bee8866ae03b54cb6912efdfef107fd6d'
