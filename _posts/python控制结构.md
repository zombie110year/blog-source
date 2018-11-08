---
comments: true
title: '[PyNote]-2-Python控制结构'
mathjax: False
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-07-27 22:05:51
---

<!--more-->

### 条件分支

#### 单分支结构

##### `if` 判断结构

```py
if condition:
	sentence1
	sentence2
```

- Python 首先判断 `condition` 的值, 若为 1 (True) 则执行接下来的语句块, 若为 0 (False) 则跳过.
	- 一切非零非空的 condition 都为 True, 一切为零为空的 condition 都为 False.
- Python 以缩进相同且连续的多个语句为一个语句块.
- 注意冒号 `:` !

#### 多分支结构

##### `if ... else` 判断结构

```py
if condition:
    True_block
else:
    False_block
```

- Python 首先判断 `condition` 的值, 若为 1 (True) 则执行接下来的语句块, 若为 0 (False) 则执行 `else` 后的语句块.
	- 一切非零非空的 condition 都为 True, 一切为零为空的 condition 都为 False.
- Python 以缩进相同且连续的多个语句为一个语句块.
- 注意冒号 `:`!

##### `if ... elif ... else` 判断结构

```py
if condition1:
	block 1
elif condition2:
	block 2
elif condition3:
	block 3
	.
	.
else:
	default_block
```

- Python 检查 conditionX ( X = 1, 2, 3, ...) 的值, 若为 True 则执行 blockX, **执行该分支之后, 退出整个分支结构** (注意此处与 C 语言的 `switch` 结构不同) . 若为 False , 则继续向下判断 condition(X+1), 直到最后的 `else` 为止.

### 循环结构

#### `while` 循环

```py
while condition:
	block
```

#### `for` 循环

```py
for element in list:
	block
```

- `for` 循环会遍历每一个处于 list 中的元素, 执行语句块.

#### 循环中起控制作用的关键字

|关键字|作用|
|:---:|:---|
|`break`|结束当前循环|
|`continue`|跳过后面语句, 进入下一次循环|
|`else`|在循环执行完毕之后执行|

- `else` 在循环中的使用举例:

```py
a = 0
while a < 10:
	a = a + 1
else:
	print("The all done")
```