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

讲解案例:

```python
```
## 首先当然得 `import argparse`.

```python
import argparse
```

## 使用时, 先创建一个解析器实例

```python
parser = argparse.ArgumentParser(description="选择运行模式")
```

这是这个函数的原型:

```python
argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=<class 'argparse.HelpFormatter'>, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)
```

- `prog` 该程序的名字, 默认为 `sys.argv[0]`
- `usage` 帮助信息, 默认自动生成(由后续的每个参数设置)
- `description` 该程序的描述
- `epilog` 
- `parents` 
- `formatter_class` 用于格式化帮助信息的类
- `prefix_chars` 用于标识选项的前缀字符, 默认为 `-`
- `fromfile_prefix_chars`
- `argument_default` 所有参数的默认值
- `conflict_handler`
- `add_help` 添加 `-h/--help` 选项, 默认为 `True`
- `allow_abbrev` 允许长选项的简写, 例如, 在无歧义时, `--target` 可以简写为 `--t` 或 `--ta` 或 `--tar` ...

## 为解析器实例添加属性

```python
parser.add_argument('-t', '--target', metavar='/path/to/target', required=True,
                    dest='target', action='append', help="定位目标")

parser.add_argument(dest='rest', metavar='剩下的参数', nargs='*')
```

以上两个方法, 将为该程序添加一个选项: `-t`(其长选项为 `--target`), 至于另一个 `rest` 则可以接收剩余参数.

```python
add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

- `name` 或 `flags`: 

### name or flags

