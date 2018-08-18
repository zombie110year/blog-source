---
title: '[PyNote]-类的定义与继承'
mathjax: false
tags:
  - null
categories:
  - null
date: 2018-08-14 00:35:35
---

# 定义一个类

```py
class ClassName(object):
    def __init__(self):
        pass
```

以上代码定义了一个什么都没有的类.

- `ClassName` 按照代码规范, 应使用 `驼峰命名法`.
- `CLassName(object)` 是一个继承自 `object` 的类. `object` 是 Python 中的基类, 可以留空, 默认值就是它.
- `__init__()` 方法用于初始化. 一旦为该类创建了一个实例, 就会调用该方法. 该方法中的参数可以在定义实例时传递.
- `self` 变量代表了属于该类的实例.

```py
class RandomNumber():
    def __init__(self, count):
        from random import randint
        self.body = []
        for i in range(0, count):
          self.body.append(randint(0, 100))
c = RandomNumber(100)
```

在定义实例 `c` 时, `100` 作为 `count` 的实际参数传递给了 `__init__()` 方法. 而 `c` 传递给了 `self` 参数.