---
title:  PyLib-argparse
data:   2018-10-11 23:19:04
mathjax:  false
tags:
    - Python
    - Note
categories:
    - Python
---

# 基本使用

```python
import argparse
parser = argparse.ArgumentParser(
    prog="这个程序叫什么名字",
    description="这是一个怎样的程序",
    argument_default=argparse.SUPPRESS  # 在没有对应参数传入时, 不向结果中添加对应属性.
)
parser.add_argument(...)
args = parser.parseargs()
```

# 使用时, 先创建一个解析器实例

```python
argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class='argparse.HelpFormatter', prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)
```

- `prog` 该程序的名字, 默认为 `sys.argv[0]`, 在后续设置 `add_argument()` 的 `help` 参数时, 可以使用 `%(prog)s` 作为格式化占位符.
- `usage` 帮助信息中第一行的 `Usage: ...` 信息, 默认自动生成(根据参数设置而不同)
- `description` 该程序的描述
- `epilog` 在帮助信息最后一行的额外声明
- `parents` 
- `formatter_class` 用于格式化帮助信息的类
- `prefix_chars` 用于标识可选参数的前缀字符, 默认为 `-`, 当该项设置为一个长字符串时, 其中的每一个字符都可以当前缀使用.
- `fromfile_prefix_chars` 从文件读取参数! 定义此项后, 例如 `@`, 那么在命令行中输入参数 `prog.py @file.args` 将会从文本文件 `file.args` 中读取参数, 其他命令行参数会被忽略. 文件中的参数必须一项一行.
- `argument_default` 解析参数的默认行为
    - `argparse.SUPPRESS` 当命令行中没有传入对应参数时, 不向解析结果中添加对应属性
    - `None` 当命令行中没有传入对应参数时, 将解析结果中对应属性的值设为 None
    - `其他 Python 对象` 当命令行中没有传入对应参数时, 将解析结果中对应属性的值设为 该值(和 None 的表现一致)
- `conflict_handler` 通常, argparse 不允许对一个参数重复添加, `error` 表示直接报错, `resolve` 则允许覆写.
- `add_help` 添加 `-h/--help` 选项, 默认为 `True`
- `allow_abbrev` 允许长选项的简写, 例如, 在无歧义时, `--target` 可以简写为 `--t` 或 `--ta` 或 `--tar` ...

# 为解析器实例添加属性

```python
parser.add_argument('-t', '--target', metavar='/path/to/target', required=True,
                    dest='target', action='append', help="定位目标")

parser.add_argument(dest='rest', metavar='剩下的参数', nargs='*')
```

以上两个方法, 将为该程序添加一个选项: `-t`(其长选项为 `--target`), 至于另一个 `rest` 则可以接收剩余参数.

```python
add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

位置参数之间在命令行中的相对位置与定义时的顺序一致, 和选项之间没有顺序要求.

选项有长选项与短选项两种类型, 它们可以在同一个 `add_argument()` 函数中定义, 当定义长选项或两者共存时, `dest` 由长选项决定, 当只有短选项时, `dest` 由短选项决定, 当然, 也可以手动设置 `dest` 的值.

选项可以在命令行中以 `--option value` `--optioin=value` 两种方式使用. 对于短选项也是同样.

- `name` 或 `flags`: 参数名, 有 位置参数和可选参数(选项) 两种类型, 和 短选项,长选项 两种形式
    - 定义位置参数: 不使用前缀字符例如 `add_argument("name")` 
    - 定义选项: 使用一个或两个前缀字符. `-h`, `--help` 分别为短/长选项.
- `action`      : 参数解析行为, 默认为 'store', 表示保存参数值. (详解见下文 [action](#action))
- `nargs`       : 选项接收值的数目. 默认为 None. (详解见下文 [nargs](#nargs))
- `const`       : 配合 `action='store_const`, `nargs='?'` 等使用.
- `default`     : 输入参数的默认值, 会覆盖掉解析器中该项参数的 `argument_default`. 配合 `nargs`, `action` 等使用.
- `type`        : 输入参数的解析类型, 默认为 str
- `choices`     : 命令行参数接受的值的范围.
- `required`    : 用于选项, 使该选项为必选. `required=True`.
- `help`        : 该项参数的帮助信息.
- `metavar`     : 帮助信息中的参数值示例
- `dest`        : 保存值的属性名

## action

- `store` 保存参数值
- `store_const` 只能用于选项. 当选项存在时, 保存 `add_argument()` 中 `const` 参数定义的值.

```python
In [6]: parser.add_argument("--set10", dest="num", action="store_const", const=10)
Out[6]: _StoreConstAction(option_strings=['--set10'], dest='num', nargs=0, const=10, default=None, type=None, choices=None, help=None, metavar=None)
In [8]: parser.parse_args(['--set10'])
Out[8]: Namespace(num=10)
```

- `store_true`, `store_false` 只能用于选项. 将参数保存为布尔值. 对于 `store_true`, 若参数存在, 则保存为 `True`, 否则 `False`;`store_false` 和 `store_true` 行为相反.
- `append` 只能用于选项. 将参数值添加到 list 中, 若参数重复出现, 则保存多个值. 目标 list 就是该参数对应的 dest 属性
- `append_const` 只能用于选项. 将选项出现, 则将 `const` 的值添加到 `dest` 指定的属性中. 只能设置一个选项.
- `count` 只能用于选项. 记录此参数的个数, 将数目储存. 对于短选项, 可以这么用: `-v`, `-vvvv`=4.
- `help` 只能用于选项. 打印帮助信息, 然后退出.
- `version` 只能用于选项. 打印程序的版本信息, 然后退出. 必须同时定义 `version` 的值. 
```python
parser.add_argument('--version', action='version', version="%(prog)s v0.0")
```

可以自定义 Action 类, 需要继承 `argparse.Action`.

```python
class BuiltfulVersion(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(BuiltfulVersion, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print("%r %r %r" % (namespace, values, option_string))
        setattr(namespace, self.dest, values)
```

## nargs

`nargs` 参数只能对选项使用. 设置选项接收值的数目. 默认为 None.

0. 当为 None 时, 该选项的 dest 只接受一个值.

1. 当为一个整数 n 时, 该选项的 dest 为一个长度为 n 的列表, 并且必须接受同等数目的值

2. 当为 `?` 问号时, 需要定义 `const` 与 `default`, 有以下可能:
    - `--foo` 未出现, 则值为 const
    - `--foo` 出现, 但没有指定值, 则值为 default
    - `--foo=value` 则值为 `value`

```python
parser.add_argument('--foo', nargs='?', const='const', default='default')
```

3. `*`. 将会把从选项所在位置之后的所有值存入列表, 直到下一个选项.
4. `+`. 将会把从选项所在位置之后的所有值存入列表, 直到下一个选项. 但至少需要一个值.
5. `argparse.REMAINDER` 储存所有未解析的参数.

# 帮助信息

help=`argparse.SUPPRESS` 将会使该条 help 不显示.

在实例化解析器 或者 调用 `add_argument` 时, 都可以指定 `help` 参数用于编写帮助信息中, 其中可以使用以下格式控制符:

- `%(prog)s` 程序名
- `%(default)s` 只能用于参数. 默认值
- `%(type)s` 只能用于参数. 参数类型
- `%(nargs)s`

... 以此类推

`argparse.add_argument` 和 解析器 `argparse.ArgumentParser` 的每一项参数都有对应的格式化字符串.

# 让解析器进行参数解析

在定义了各项参数之后, 对解析器 `parser` 调用方法 `parse_args()` 令其解析参数.

`parse_args()` 解析参数后, 会把各对应的值储存在一个  实例中返回, 实例的每一个属性对应一个参数项目, 属性名由 `add_argument()` 的 `dest` 参数决定, 如果没有传入此参数的话, 会由该参数的 `name` 决定.

```python
args = parser.parse_args()
args.xxx    # 通过对 args 的属性访问命令行参数的解析值
```
