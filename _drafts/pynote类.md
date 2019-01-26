---
comments: true
title: '[PyNote]-类'
mathjax: false
tags:
  - Python
  - Note
categories:
  - Python
date: 2018-08-14 00:35:35
---

# 创建一个类

创建一个类的语法:

```py
class NewClass():
    ...
```

便可以从 Python 的基类 `object` 创建一个新类. 括号可以舍去, 也可以将 `object` 写明, 它们的意思都是一样的.

可以在类中定义变量, 函数.

```py
class NewClass(object):
    VAR = "这是类的变量"
    LIST = [1,]                 # 将一个可变对象作为类的属性
    def __init__(self):         # __init__ 方法在实例化的过程中自动运行
        self.var = "这是类的实例的变量"

    def instance_method(self, *parameters):     # 这是实例的方法
      print("这是实例的方法")

    @classmethod                        # 这是类的方法
    def class_method(*parameters):
      print("这是类的方法")

    @staticmethod                       # 这是静态方法
    def static_method(*parameters):
      print("这是静态方法")
```

# 类,属性,实例

一个类, 可以认为是一个模板, 在这个模板上, 有着这个类所有的属性, 包括类的方法, 类的数据(成员).

而类的实例化, 则是以类为模板, 创建了一个具体的对象. 这个对象就是这个类的一个实例. 一个类可以创建多个实例.

例如一个简单的类, 可以通过 `.` 点运算符访问类中的成员.

```py
In [1]: class NewClass(object):
   ...:     VAR = "这是类的变量"
   ...:     LIST = [1,]                 # 将一个可变对象作为类的属性
   ...:     def __init__(self):         # __init__ 方法在实例化的过程中自动运行
   ...:         self.var = "这是类的实例的变量"
   ...:
   ...:     def instance_method(self, *parameters):     # 这是实例的方法
   ...:       print("这是实例的方法")
   ...:
   ...:     @classmethod                        # 这是类的方法
   ...:     def class_method(*parameters):
   ...:       print("这是类的方法")
   ...:
   ...:     @staticmethod                       # 这是静态方法
   ...:     def static_method(*parameters):
   ...:       print("这是静态方法")
   ...:

In [2]: test = NewClass()       # 实例化, 此时执行了 test.__init__() 方法.

In [3]: test.VAR                # 实例可以访问类的成员
Out[3]: '这是类的变量'

In [4]: test.LIST               # 这是一个可变对象, 但是它是在类中共享的!
Out[4]: [1]

In [5]: test.var                # 这是实例的成员, 不能通过类来访问
Out[5]: '这是类的实例的变量'

In [16]: NewClass.var
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-16-5e75d95acd75> in <module>()
----> 1 NewClass.var

AttributeError: type object 'NewClass' has no attribute 'var'

In [6]: test.instance_method()
这是实例的方法

In [7]: test.class_method()
这是类的方法

In [8]: test.static_method()
这是静态方法

In [9]: NewClass.VAR
Out[9]: '这是类的变量'

In [10]: NewClass.LIST
Out[10]: [1]

In [11]: NewClass.instance_method()     # 不能通过类来访问实例的方法
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-0d34494c2d05> in <module>()
----> 1 NewClass.instance_method()

TypeError: instance_method() missing 1 required positional argument: 'self'

In [12]: NewClass.class_method()
这是类的方法

In [13]: NewClass.static_method()
这是静态方法
```

如果为一个类创建了复数实例, 那么每一个实例都可以修改在类中共享的成员, 但不会影响其他实例.

每创建一个实例, 那么类的成员都会被复制一份, 各个实例之间是独立的.

```py
In [17]: test2 = NewClass()     # 创建了一个新的实例 test2

In [18]: test2.VAR              # 现在它的 VAR 和类一致
Out[18]: '这是类的变量'

In [19]: test2.VAR = "改了它!"

In [20]: test2.VAR
Out[20]: '改了它!'

In [21]: test.VAR               # 其他实例不受影响
Out[21]: '这是类的变量'

In [25]: NewClass.VAR           # 类本身也不受影响
Out[25]: '这是类的变量'

In [22]: test2.LIST.append(2)

In [23]: test2.LIST
Out[23]: [1, 2]
                                # 哪怕成员为可变对象也是如此
In [24]: test.LIST
Out[24]: [1]
```

可以为实例创建新的属性, 这并不会影响到类, 也不会影响到其他实例.

```py
In [26]: test.newitem = "newitem"

In [27]: test.newitem
Out[27]: 'newitem'

In [28]: test2.newitem
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-28-7293e2cbcdbe> in <module>()
----> 1 test2.newitem

AttributeError: 'NewClass' object has no attribute 'newitem'

In [29]: NewClass.newitem
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-29-0b5a924363d7> in <module>()
----> 1 NewClass.newitem

AttributeError: type object 'NewClass' has no attribute 'newitem'
```

# 类的方法

类的方法, 其实就是函数. 只不过传递了特殊的参数罢了.

## 实例方法

对于实例方法, 参数中的 `self` 其实并不是关键字, 可以是任何合法的变量名. 当调用方法的时候, 实例自身被作为参数传递过去了.

所以, 当调用一个实例方法时, 可以有以下形式:

```python
test = NewClass()
test.

## 类方法

## 静态方法

