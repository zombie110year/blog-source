---
title: '[PyNote]-json解析'
tags:
  - Python
  - Note
  - json
categories:
  - Python
date: 2018-08-20 09:39:14
---

# JSON

`json` 是 Python 的标准库之一, 用于解析 JSON 格式的文本.

- JSON 指的是 JavaScript 对象表示法( JavaScript Object Notation )
- JSON 是轻量级的文本数据交换格式
- JSON 独立于语言: JSON 使用 Javascript 语法来描述数据对象, 但是 JSON 仍然独立于语言和平台
- JSON 解析器和 JSON 库支持许多不同的编程语言. 目前非常多的动态( PHP, JSP,. NET )编程语言都支持 JSON
- JSON 具有自我描述性, 更易理解

JSON 常用于浏览器的发送或接收报文中. 一个典型的 JSON 大概为以下格式:

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "sex": "male",
    "age": 25,
    "address": 
    {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021",  //! 注意, JSON 不能有多余的尾随逗号!!! 我还以为是什么玄学 BUG 呢, 
    },                          // 写完了上面那个注释, 才得知 JSON 不允许注释, Why?!!!
    "phoneNumber":
    [
        {
          "type": "home",
          "number": "212 555-1234"
        },
        {
          "type": "fax",
          "number": "646 555-4567"
        }
    ]
}
```

以下这个 JSON 才是格式正确的.

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "sex": "male",
    "age": 25,
    "address": {
        "streetAddress": "212ndStreet",
        "city": "NewYork",
        "state": "NY",
        "postalCode": "10021"
    },
    "phoneNumber": [
        {
            "type": "home",
            "number": "212555-1234"
        },
        {
            "type": "fax",
            "number": "646555-4567"
        }
    ]
}
```

可以看到, 
- JSON 中存在着类似于字典的 `key-value` 对, 其中 key 一定有双引号, 是字符串类型, 而 value 则可为任意类型.
- 花括号 `{}` 表示一个对象(类的实例), 方括号 `[]` 保存数组(多个实例).
- 最终, JSON 会被 Python 的 json 模块解释为字典,

# Python json 模块

```py
import json
```

---

## JSON 的编码与解码

json 模块中提供了 `dump()` 与 `dumps()` 用于编码(`Python object` -> `JSON string`); `load()` 与 `loads()` 用于解码(`JSON string`->`Python object`)

其中, `dumps()` 将 Python 对象编码为 JSON 的字符串, 而 `dump()` 则将 Python 对象编码为 JSON 字符串并写入一个文件之中. 类似的, `loads()` 是将一个 JSON 字符串解析为 Python 对象, 而 `load()` 则从文件中读取并解析.

```python
dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw) -> str
loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) -> obj
```

