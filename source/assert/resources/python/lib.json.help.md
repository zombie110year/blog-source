[Origin-File](/assert/repos/python/json.__doc__)

> Help on package json:

# NAME

    json

# 描述

[JSON(JavaScript Object Notation)](http://json.org) 是用作轻量级数据交换格式的JavaScript语法(ECMA-262第3版)的子集.

`json` 向用户公开了一个类似于标准库模块 `marshal` 和 `pickle` 的 API. 它源自外部维护的 simplejson 库的一个版本.

## 对基本 Python 对象层级结构编码

```python
>>> import json
>>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]' 
# json.dumps() 函数返回序列化 json 字符串
>>> print(json.dumps("\"foo\bar"))
"\"foo\bar"
>>> print(json.dumps('\u1234'))
"\u1234"
>>> print(json.dumps('\\'))
"\\"
>>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
{"a": 0, "b": 0, "c": 0}
>>> from io import StringIO
>>> io = StringIO()
>>> json.dump(['streaming API'], io)
# json.dump(obj, io) 将 obj 序列化后输出到 io
>>> io.getvalue()
'["streaming API"]'
```

### 紧凑编码

```py
>>> import json
>>> mydict = {'4': 5, '6': 7}
>>> json.dumps([1,2,3,mydict], separators=(',', ':'))
'[1,2,3,{"4":5,"6":7}]'
```

### 漂亮的打印输出

```py
>>> import json
>>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}
```

## 解码 JSON

```py
>>> import json
>>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
>>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
True
>>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
True
>>> from io import StringIO
>>> io = StringIO('["streaming API"]')
>>> json.load(io)[0] == 'streaming API'
True
```

### 指定 JSON 对象解码

```py
>>> import json
>>> def as_complex(dct):
...     if '__complex__' in dct:
...         return complex(dct['real'], dct['imag'])
...     return dct
...
>>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
...     object_hook=as_complex)
(1+2j)
>>> from decimal import Decimal
>>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
True
```

### 指定 JSON 对象编码

```py
>>> import json
>>> def encode_complex(obj):
...     if isinstance(obj, complex):
...         return [obj.real, obj.imag]
...     raise TypeError(f'Object of type {obj.__class__.__name__} '
...                     f'is not JSON serializable')
...
>>> json.dumps(2 + 1j, default=encode_complex)
'[2.0, 1.0]'
>>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
'[2.0, 1.0]'
>>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
'[2.0, 1.0]'
```

### 使用shell中的 `json.tool` 来验证和美化打印输出

```sh
$ echo '{"json":"obj"}' | python -m json.tool
{
    "json": "obj"
}
$ echo '{ 1.2:3.4}' | python -m json.tool
Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
```

# 包内容

- `decoder`
- `encoder`
- `scanner`
- `tool`

# CLASS

- `builtins.ValueError(builtins.Exception)`
    - `json.decoder.JSONDecodeError`
- `builtins.object`
    - `json.decoder.JSONDecoder`
    - `json.encoder.JSONEncoder`

```
    class JSONDecodeError(builtins.ValueError)
     |  JSONDecodeError(msg, doc, pos)
     |
     |  Subclass of ValueError with the following additional properties:
     |
     |  msg: 未格式化的错误信息
     |  doc: 正在解析的JSON文档
     |  pos: 解析失败处的 index
     |  lineno: 对应于 pos 的行
     |  colno: 对应于 pos 的列
     |
     |  方法解析顺序:
     |      JSONDecodeError
     |      builtins.ValueError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  这里定义的方法:
     |
     |  __init__(self, msg, doc, pos)
     |      初始化 self.  参阅 help(type(self)) 得到准确的 signature.
     |
     |  __reduce__(self)
     |      Helper for pickle.
     |
     |  ----------------------------------------------------------------------
     |  这里定义的数据描述符:
     |
     |  __weakref__
     |      对象的弱引用列表(如果定义)
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.ValueError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      创建并返回一个新对象. 参阅 help(type) 获得准确的 signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      执行 delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      返回 getattr(self, name).
     |
     |  __repr__(self, /)
     |      返回 repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      执行 setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      返回 str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause     例外原因
     |
     |  __context__
     |      exception context   例外内容
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class JSONDecoder(builtins.object)
     |  JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
     |
     |  Simple JSON <http://json.org> decoder
     |
     |  解码时默认进行以下转换:
     |
     |  +---------------+-------------------+
     |  | JSON          | Python            |
     |  +===============+===================+
     |  | object        | dict              |
     |  +---------------+-------------------+
     |  | array         | list              |
     |  +---------------+-------------------+
     |  | string        | str               |
     |  +---------------+-------------------+
     |  | number (int)  | int               |
     |  +---------------+-------------------+
     |  | number (real) | float             |
     |  +---------------+-------------------+
     |  | true          | True              |
     |  +---------------+-------------------+
     |  | false         | False             |
     |  +---------------+-------------------+
     |  | null          | None              |
     |  +---------------+-------------------+
     |
     |  它还将 ``NaN``, ``Infinity`` 和 ``-Infinity`` 理解为对应的浮点数, 这超出
     |  了 JSON 的规范.
     |
     |  Methods defined here:
     |
     |  __init__(self, *, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
     |      ``object_hook``, 如果指定, 将调用每个JSON对象的结果, 并使用其返回值
     |      代替给定的 ``dict``. 这可用于提供自定义反序列化 (例如, 支持
     |      JSON-RPC 类提示).
     |
     |      ``object_pairs_hook``, 如果指定将被调用, 每个 JSON 对象的结果都使用
     |      有序的对列表进行解码. 将使用 ``object_paires_hook`` 的返回值, 
     |      而非 ``dict``. 此特性可用于实现自定义解码器. 如果还定义了
     |      ``object_hook`` , 则 ``object_hook`` 优先.
     |
     |      ``parse_float``, 如果指定, 将使用要解码的每个 JSON float 的字符串调用. 
     |      默认情况下, 这相当于 float(num_str). 这可用于为 JSON 浮点数使用另一
     |      种数据类型或解析器(例如 decimal.Decimal).
     |
     |      ``parse_int``, 如果指定, 将使用要解码的每个 JSON int 的字符串调用. 
     |      默认情况下, 这相当于 int(num_str). 这可用于为 JSON 浮点数使用另一种
     |      数据类型或解析器(例如 float).
     |
     |      ``parse_constant``, if specified, will be called with one of the
     |      following strings: -Infinity, Infinity, NaN.
     |      This can be used to raise an exception if invalid JSON numbers
     |      are encountered.
     |
     |      If ``strict`` is false (true is the default), then control
     |      characters will be allowed inside strings.  Control characters in
     |      this context are those with character codes in the 0-31 range,
     |      including ``'\t'`` (tab), ``'\n'``, ``'\r'`` and ``'\0'``.
     |
     |  decode(self, s, _w=<built-in method match of re.Pattern object at 0x00000175F1020F30>)
     |      Return the Python representation of ``s`` (a ``str`` instance
     |      containing a JSON document).
     |
     |  raw_decode(self, s, idx=0)
     |      Decode a JSON document from ``s`` (a ``str`` beginning with
     |      a JSON document) and return a 2-tuple of the Python
     |      representation and the index in ``s`` where the document ended.
     |
     |      This can be used to decode a JSON document from a string that may
     |      have extraneous data at the end.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class JSONEncoder(builtins.object)
     |  JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
     |
     |  Extensible JSON <http://json.org> encoder for Python data structures.
     |
     |  Supports the following objects and types by default:
     |
     |  +-------------------+---------------+
     |  | Python            | JSON          |
     |  +===================+===============+
     |  | dict              | object        |
     |  +-------------------+---------------+
     |  | list, tuple       | array         |
     |  +-------------------+---------------+
     |  | str               | string        |
     |  +-------------------+---------------+
     |  | int, float        | number        |
     |  +-------------------+---------------+
     |  | True              | true          |
     |  +-------------------+---------------+
     |  | False             | false         |
     |  +-------------------+---------------+
     |  | None              | null          |
     |  +-------------------+---------------+
     |
     |  To extend this to recognize other objects, subclass and implement a
     |  ``.default()`` method with another method that returns a serializable
     |  object for ``o`` if possible, otherwise it should call the superclass
     |  implementation (to raise ``TypeError``).
     |
     |  Methods defined here:
     |
     |  __init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
     |      Constructor for JSONEncoder, with sensible defaults.
     |
     |      If skipkeys is false, then it is a TypeError to attempt
     |      encoding of keys that are not str, int, float or None.  If
     |      skipkeys is True, such items are simply skipped.
     |
     |      If ensure_ascii is true, the output is guaranteed to be str
     |      objects with all incoming non-ASCII characters escaped.  If
     |      ensure_ascii is false, the output can contain non-ASCII characters.
     |
     |      If check_circular is true, then lists, dicts, and custom encoded
     |      objects will be checked for circular references during encoding to
     |      prevent an infinite recursion (which would cause an OverflowError).
     |      Otherwise, no such check takes place.
     |
     |      If allow_nan is true, then NaN, Infinity, and -Infinity will be
     |      encoded as such.  This behavior is not JSON specification compliant,
     |      but is consistent with most JavaScript based encoders and decoders.
     |      Otherwise, it will be a ValueError to encode such floats.
     |
     |      If sort_keys is true, then the output of dictionaries will be
     |      sorted by key; this is useful for regression tests to ensure
     |      that JSON serializations can be compared on a day-to-day basis.
     |
     |      If indent is a non-negative integer, then JSON array
     |      elements and object members will be pretty-printed with that
     |      indent level.  An indent level of 0 will only insert newlines.
     |      None is the most compact representation.
     |
     |      If specified, separators should be an (item_separator, key_separator)
     |      tuple.  The default is (', ', ': ') if *indent* is ``None`` and
     |      (',', ': ') otherwise.  To get the most compact JSON representation,
     |      you should specify (',', ':') to eliminate whitespace.
     |
     |      If specified, default is a function that gets called for objects
     |      that can't otherwise be serialized.  It should return a JSON encodable
     |      version of the object or raise a ``TypeError``.
     |
     |  default(self, o)
     |      Implement this method in a subclass such that it returns
     |      a serializable object for ``o``, or calls the base implementation
     |      (to raise a ``TypeError``).
     |
     |      For example, to support arbitrary iterators, you could
     |      implement default like this::
     |
     |          def default(self, o):
     |              try:
     |                  iterable = iter(o)
     |              except TypeError:
     |                  pass
     |              else:
     |                  return list(iterable)
     |              # Let the base class default method raise the TypeError
     |              return JSONEncoder.default(self, o)
     |
     |  encode(self, o)
     |      Return a JSON string representation of a Python data structure.
     |
     |      >>> from json.encoder import JSONEncoder
     |      >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
     |      '{"foo": ["bar", "baz"]}'
     |
     |  iterencode(self, o, _one_shot=False)
     |      Encode the given object and yield each string
     |      representation as available.
     |
     |      For example::
     |
     |          for chunk in JSONEncoder().iterencode(bigobject):
     |              mysocket.write(chunk)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  item_separator = ', '
     |
     |  key_separator = ': '
```

# FUNCTIONS

```py
    dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
        Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
        ``.write()``-supporting file-like object).

        If ``skipkeys`` is true then ``dict`` keys that are not basic types
        (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
        instead of raising a ``TypeError``.

        If ``ensure_ascii`` is false, then the strings written to ``fp`` can
        contain non-ASCII characters if they appear in strings contained in
        ``obj``. Otherwise, all such characters are escaped in JSON strings.

        If ``check_circular`` is false, then the circular reference check
        for container types will be skipped and a circular reference will
        result in an ``OverflowError`` (or worse).

        If ``allow_nan`` is false, then it will be a ``ValueError`` to
        serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)
        in strict compliance of the JSON specification, instead of using the
        JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).

        If ``indent`` is a non-negative integer, then JSON array elements and
        object members will be pretty-printed with that indent level. An indent
        level of 0 will only insert newlines. ``None`` is the most compact
        representation.

        If specified, ``separators`` should be an ``(item_separator, key_separator)``
        tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
        ``(',', ': ')`` otherwise.  To get the most compact JSON representation,
        you should specify ``(',', ':')`` to eliminate whitespace.

        ``default(obj)`` is a function that should return a serializable version
        of obj or raise TypeError. The default simply raises TypeError.

        If *sort_keys* is true (default: ``False``), then the output of
        dictionaries will be sorted by key.

        To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
        ``.default()`` method to serialize additional types), specify it with
        the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.

    dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
        Serialize ``obj`` to a JSON formatted ``str``.

        If ``skipkeys`` is true then ``dict`` keys that are not basic types
        (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
        instead of raising a ``TypeError``.

        If ``ensure_ascii`` is false, then the return value can contain non-ASCII
        characters if they appear in strings contained in ``obj``. Otherwise, all
        such characters are escaped in JSON strings.

        If ``check_circular`` is false, then the circular reference check
        for container types will be skipped and a circular reference will
        result in an ``OverflowError`` (or worse).

        If ``allow_nan`` is false, then it will be a ``ValueError`` to
        serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in
        strict compliance of the JSON specification, instead of using the
        JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).

        If ``indent`` is a non-negative integer, then JSON array elements and
        object members will be pretty-printed with that indent level. An indent
        level of 0 will only insert newlines. ``None`` is the most compact
        representation.

        If specified, ``separators`` should be an ``(item_separator, key_separator)``
        tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
        ``(',', ': ')`` otherwise.  To get the most compact JSON representation,
        you should specify ``(',', ':')`` to eliminate whitespace.

        ``default(obj)`` is a function that should return a serializable version
        of obj or raise TypeError. The default simply raises TypeError.

        If *sort_keys* is true (default: ``False``), then the output of
        dictionaries will be sorted by key.

        To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
        ``.default()`` method to serialize additional types), specify it with
        the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.

    load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
        Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
        a JSON document) to a Python object.

        ``object_hook`` is an optional function that will be called with the
        result of any object literal decode (a ``dict``). The return value of
        ``object_hook`` will be used instead of the ``dict``. This feature
        can be used to implement custom decoders (e.g. JSON-RPC class hinting).

        ``object_pairs_hook`` is an optional function that will be called with the
        result of any object literal decoded with an ordered list of pairs.  The
        return value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders.  If ``object_hook``
        is also defined, the ``object_pairs_hook`` takes priority.

        To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
        kwarg; otherwise ``JSONDecoder`` is used.

    loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
        Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
        containing a JSON document) to a Python object.

        ``object_hook`` is an optional function that will be called with the
        result of any object literal decode (a ``dict``). The return value of
        ``object_hook`` will be used instead of the ``dict``. This feature
        can be used to implement custom decoders (e.g. JSON-RPC class hinting).

        ``object_pairs_hook`` is an optional function that will be called with the
        result of any object literal decoded with an ordered list of pairs.  The
        return value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders.  If ``object_hook``
        is also defined, the ``object_pairs_hook`` takes priority.

        ``parse_float``, if specified, will be called with the string
        of every JSON float to be decoded. By default this is equivalent to
        float(num_str). This can be used to use another datatype or parser
        for JSON floats (e.g. decimal.Decimal).

        ``parse_int``, if specified, will be called with the string
        of every JSON int to be decoded. By default this is equivalent to
        int(num_str). This can be used to use another datatype or parser
        for JSON integers (e.g. float).

        ``parse_constant``, if specified, will be called with one of the
        following strings: -Infinity, Infinity, NaN.
        This can be used to raise an exception if invalid JSON numbers
        are encountered.

        To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
        kwarg; otherwise ``JSONDecoder`` is used.

        The ``encoding`` argument is ignored and deprecated.
```

# DATA

```py
__all__ = ['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecod...
```

# VERSION

2.0.9

# AUTHOR

```
Bob Ippolito <bob@redivi.com>
```

# FILE

```
python3\lib\json\__init__.py
```