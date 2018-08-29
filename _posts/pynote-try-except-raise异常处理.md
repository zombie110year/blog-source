---
title: '[PyNote]-try..except..raise异常处理'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-08-15 22:39:39
---

- [`try...except`](#try...except)
- [`try...except{ErrorType}`](#try...except{ErrorType})
- [`try...except...else`](#可以使用-else-关键词)
- [`raise`](#raise-抛出异常)
- [`try..finally`](#异常清理行为)
- [`with...as`](#使用-with...as-语句)

<!--more-->

# 语法

## `try...except`

```py
b = 10
c = 0
a = b / c
print("a=%d, b=%d, c=%d"%(a, b, c))
```

以上代码, 如果直接执行的话会报一个[错误](#ZeroDivisionError), 然后整个程序就中断了. 如果要让程序错误了也能继续执行, 就需要用到 `try...except` 语句进行错误处理.

```py
try:
    b = 10
    c = 0
    a = b / c
    print("a=%d, b=%d, c=%d"%(a, b, c))
except:
    c = 2
    a = b / c
```

但是使用了 `try...except` 语句后, 如果有任何错误, Python 会执行 `except:` 后的语句, 然后继续. 具体的执行顺序:

0. 执行 `try:` 后语句, 直到遇到错误部分
0. 在错误处中断, 执行 `except:` 后语句
0. 在错误处重启, 继续执行 `try:` 后剩余部分(发生错误的那一行会被忽略)

<div id="ZeroDivisionError"></div>

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
## `try...except{ErrorType}`

在 `try...except` 语句中可以指定错误类型:

```py
try:
    a = 1 / 0
except ZeroDivisionError:
    print(ZeroDivisionError.__doc__)
```

以上语句可以特异性处理 `ZeroDivisionError` 类型的错误, 但是在 `try:` 中遇到其它类型的错误, 程序依然会终止.

### 可以在一个 `except` 中处理多种异常

需要在 `{ErrorType}` 中使用一个元组来包括需要的异常类型. 只要发生其中一种异常, 就会触发此异常处理.

```py
try:
    a = 1 / 0
    def hei()
        pass
except (ZeroDivisionError, SyntaxError):
    print(ZeroDivisionError.__doc__)
    print(SyntaxError.__doc__)
```

### 可以使用多个 `except` 关键词

```py
try:
    a = 1 / 0
    def hei()
        pass
except ZeroDivisionError:
    print(ZeroDivisionError.__doc__)
except SyntaxError:
    print(SyntaxError.__doc__)
except:
    print("Unknown")
```

- 发生某种异常时, 按顺序核对异常类型, 触发对应的异常处理.
- 可以在最后使用无指定类型的 `except:` 任何异常类型都可以触发它.
- 在一个 `try...except` 结构中, 最多触发一次 `except`, 之后便会退出该结构.

### 可以使用 `as` 关键字给 `except` 后的错误类型取别名.如:

```py
try:
    a = 1 / 0
except ZeroDivisionError as z:
    print(z.__doc__)
```

### 可以使用 `else` 关键词

```py
try:
    a = 1 / 0
except ZeroDivisionError as z:
    print(z.__doc__)
else:
    print("Everything is OK!")
```

如果没有异常, 则会运行 `else` 后的语句.

## `raise` 抛出异常

使用语句

```py
raise ErrorType('提示字符串')
```

抛出一个异常.

- 抛出异常之后, 程序将停止运行.
- `raise` 可以不接参数, 这将抛出当前异常(只能运用在`except`后)
- `raise` 后接的参数必须是一个异常的 `类` 或 `实例`.

# Python 中存在的异常类型

## Python 中的基本异常类型

|异常类型|说明|
|:-:|-|
|Exception|**所有异常的基类**|
|AttributeError|特性应用或赋值失败时触发|
|IOError|试图打开不存在的文件时触发|
|IndexError|在使用序列中不存在的索引时触发|
|KeyError|在使用映射不存在的键时触发|
|NameError|在找不到名字(变量)时触发|
|SyntaxError|代码出现语法错误时触发|
|TypeError|在内建操作或者函数应用于错误类型的对象时触发|
|ValueError|在内建操作或者函数应用于正确类型的对象, 但是该对象使用不合适的值时触发|
|ZeroDivisionError|在除法或者地板除操作的第二个操作数为 0 时触发|

## 自定义异常类型

可以通过创建一个继承了 `Exception` 的子类的方式来创建自定义异常类.

```py
class MyError(Exception):
    def __init__(self, expression, suggestion):
        self.expression = expression
        self.suggestion = suggestion
    def __str__(self):
        print("MyError: %s\n\tSuggestion: %s"%(self.expression, self.suggestion))
```

注意定义一个 `__str__` 方法, 这个方法定义了抛出异常时进行的动作.

# 异常清理行为

```py
try:
    pass
finally:
    pass
```

无论 `try` 中是否有异常, `finally` 后的语句一定会执行.

## 使用 `with...as` 语句

`with...as` 语句可以调用对象预定义的清理行为. 如:

```py
with open('./test.txt', 'r') as f:
    for i in f:
        print(i)
```

将会保证 `with..as:` 后的语句块执行完毕后调用 `close()`(文件对象的预定义清理行为). 