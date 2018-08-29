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

# 列表-list

## 创建列表

创建列表可以调用 `list()` 函数, 也可以将一个列表表达式赋值给变量.

```py
new_list1 = list()
new_list3 = []
# 创建一个空列表

new_list2 = list(1,2,3,4,5,6)   # 此方法错误!, list() 函数仅接受一个参数.

new_list4 = [1,]
new_list5 = [2]
# 创建只含有一个元素的列表

new_list6 = [1,2,3,4,5,6]
# 创建含有多个元素的列表
```

`list()` 函数的作用是将一个其他类型的对象转化为列表, 返回此列表. 因此最多只接受一个参数, 若不传入参数, 则返回空列表.

可向 `list()` 函数传入 字符串, 元组, 字典, 集合等对象.

## 操作列表

### 列表类的方法

# 元组-tuple
# 字典-dict
# 集合-set