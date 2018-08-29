[Origin-File](/assert/repos/python/buildin.open.help.txt)

Help on built-in function open in module io:

内容来自 `open.__doc__` 对象.

```py
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Open file and return a stream.  Raise OSError upon failure.
```

打开文件并返回流. 当打开失败时抛出 `OSError`.

```
file is either a text or byte string giving the name (and the path
if the file isn't in the current working directory) of the file to
be opened or an integer file descriptor of the file to be
wrapped. (If a file descriptor is given, it is closed when the
returned I/O object is closed, unless closefd is set to False.)
```

参数 `file` 是字符串类型数据, 可以是普通文本, 也可以是二进制编码的字符串. 给出需要打开的文件名 (如果文件不在当前目录, 需要给出文件的路径, 绝对路径或相对路径.) 或者要 wrap 的文件的整数文件描述符. (如果给出了文件描述符, 则在关闭 I/O 对象时关闭它, 除非设置 `closefd=False`).

```
mode is an optional string that specifies the mode in which the file
is opened. It defaults to 'r' which means open for reading in text
mode.  Other common values are 'w' for writing (truncating the file if
it already exists), 'x' for creating and writing to a new file, and
'a' for appending (which on some Unix systems, means that all writes
append to the end of the file regardless of the current seek position).
In text mode, if encoding is not specified the encoding used is platform
dependent: locale.getpreferredencoding(False) is called to get the
current locale encoding. (For reading and writing raw bytes use binary
mode and leave encoding unspecified.) The available modes are:
```

参数 `mode` 是一个字符串类型的数据, 用于指定文件的打开方式. 默认为 "r", 意味着文本以只读(text readonly) 模式打开. 其他常见值是 "w" 用于写入 (如果文件已存在则截断), "x" 用于创建和写入新文件, 和 "a" 用于追加 (在某些 Unix 系统上, 意味着所有写入都追加到末尾, 无论当前读写指针在何处.) 在文本模式 "t" 下, 如果未指定编码, 则使用系统编码, 通过调用 `locale.getpreferredencoding(False)` 获取当前语言环境编码. (对于读写原始字节, 使用二进制模式 "b", 此种模式不指定编码). 所有可用的模式有:

```
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       文本 只读. (默认模式)
'w'       文本 只写, 如果文本已存在则截断文件.
'x'       只创建新文件, 并以写模式打开它.
'a'       以写模式打开, 如果文件存在则在末尾添加
'b'       二进制模式
't'       文本模式
'+'       打开文件以更新 (读写)
'U'       universal newline mode (已弃用)
========= ===============================================================
```

```
The default mode is 'rt' (open for reading text). For binary random
access, the mode 'w+b' opens and truncates the file to 0 bytes, while
'r+b' opens the file without truncation. The 'x' mode implies 'w' and
raises an `FileExistsError` if the file already exists.
```

默认的模式是 "rt" (以读文本模式打开). 对任意的二进制访问, "w+b" 模式将会截断文件为 0 字节打开, 而 "r+b" 则不会截断. "x" 模式意味着 "w", 但如果文件已存在则抛出 `FileExistsError` 而不会截断文件, 当然也不会打开.

```
Python distinguishes between files opened in binary and text modes,
even when the underlying operating system doesn't. Files opened in
binary mode (appending 'b' to the mode argument) return contents as
bytes objects without any decoding. In text mode (the default, or when
't' is appended to the mode argument), the contents of the file are
returned as strings, the bytes having been first decoded using a
platform-dependent encoding or using the specified encoding if given.
```

Python 区分以二进制模式和文本模式打开的文件, 即使底层操作系统不区分. 以二进制模式打开(将 `b` 添加到 `mode` 参数)的文件返回内容为字节对象, 没有进行任何解码. 在文本模式(默认, 或者将 `t` 添加到 `mode` 参数), 文件的内容作为字符串返回, 首先使用依赖于系统平台的编码, 或使用 `encoding` 参数指定编码(如果有的话).

```
'U' mode is deprecated and will raise an exception in future versions
of Python.  It has no effect in Python 3.  Use newline to control
universal newlines mode.
```

"U" 模式已启用, 将在未来版本中引发异常. 它在 Python3 版本中不会生效. 使用 `newline` 参数来控制通用换行模式.

```
buffering is an optional integer used to set the buffering policy.
Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
line buffering (only usable in text mode), and an integer > 1 to indicate
the size of a fixed-size chunk buffer.  When no buffering argument is
given, the default buffering policy works as follows:
```

参数 `buffering` 是一个可选的整数, 用来设置缓冲策略. 

- `0` 关闭缓冲. (仅允许二进制模式下使用)
- `1` 选择行缓冲. (仅允许文本模式下使用)
- `值>1` 表示固定大小的块缓冲区大小.

没有给定缓冲参数时, 默认的缓冲策略如下:

```
* Binary files are buffered in fixed-size chunks; the size of the buffer
  is chosen using a heuristic trying to determine the underlying device's
  "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
  On many systems, the buffer will typically be 4096 or 8192 bytes long.

* "Interactive" text files (files for which isatty() returns True)
  use line buffering.  Other text files use the policy described above
  for binary files.
```

- 二进制文件以固定大小的块进行缓冲; 使用启发式方法选择缓冲区大小, 驶入确定底层设备的 "块大小" 并回调到 `io.DEFAULT_BUFFER_SIZE`. 在许多系统上, 缓冲区长度为 4096 或 8192 字节.

- "交互式" 文本文件, (调用 `isatty()` 方法, 返回 `True` 的文件. "is a tty") 使用行缓冲. 其他文本文件缓冲策略同二进制文件.


```
encoding is the name of the encoding used to decode or encode the
file. This should only be used in text mode. The default encoding is
platform dependent, but any encoding supported by Python can be
passed.  See the codecs module for the list of supported encodings.
```

参数 `encoding` 指定解码或编码文件使用的字符编码. 它只应用于文本模式. 默认编码取决于系统平台, 但可以向 Python 传递任何支持编码. 参阅 `codecs` 模块文档获取支持编码格式列表.

```
errors is an optional string that specifies how encoding errors are to
be handled---this argument should not be used in binary mode. Pass
'strict' to raise a ValueError exception if there is an encoding error
(the default of None has the same effect), or pass 'ignore' to ignore
errors. (Note that ignoring encoding errors can lead to data loss.)
See the documentation for codecs.register or run 'help(codecs.Codec)'
for a list of the permitted encoding error strings.
```

参数 `errors` 是一个可选的字符串, 用于指定如何处理编码错误---此参数不应用于二进制模式. 各值对应的策略:

- 默认值 "none", 如果存在编码错误则抛出 `ValueError` 异常. (同 "strict")
- "strict", 如果存在编码错误则抛出 `ValueError` 异常.
- "ignore", 忽略错误. (注意, 忽略编码错误可能导致数据丢失.)

参阅 `codecs.register` 模块文档或运行 `help(codecs.Codec)` 获取有效的编码错误字符串列表.

```
newline controls how universal newlines works (it only applies to text
mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
follows:
```

参数 `newline` 控制通用换行工作方式(仅应用于文本模式). 仅接受 `None`, `""` (空), "\n"(换行符, Unix, 推荐), "\r\n"(回车换行, MS-DOS). 工作方式如下:

```
* On input, if newline is None, universal newlines mode is
  enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
  these are translated into '\n' before being returned to the
  caller. If it is '', universal newline mode is enabled, but line
  endings are returned to the caller untranslated. If it has any of
  the other legal values, input lines are only terminated by the given
  string, and the line ending is returned to the caller untranslated.

* On output, if newline is None, any '\n' characters written are
  translated to the system default line separator, os.linesep. If
  newline is '' or '\n', no translation takes place. If newline is any
  of the other legal values, any '\n' characters written are translated
  to the given string.
```

输入(读取)时:

- 如果 `newline` 的值为 `None`, 通用换行模式被启用. 输入的各行可以以 "\n", "\r" 或 "\r\n" 结尾, 并且它们在被返回给函数调用前将被翻译成 "\n".
- 如果值为 `""`, 则通用换行模式被启用, 但输入的换行符不会被翻译. 
- 如果为其他合法的值, 输入的各行将会以规定字符结尾, 且换行符不会被翻译. (就是说以 `newline` 参数规定的字符作为换行符, 识别一行字符串)

输出(写入)时:

- 如果 `newline` 的值为 `None`, 任何 `"\n"` 换行符将被翻译为系统默认换行符(即 `os.linesep`).
- 如果 `newline` 的值是 `""` 或 `"\n"`, 输出时不会翻译换行符.
- 如果为其他合法的值, 任何 `"\n"` 都会被翻译为指定字符.

**注**: Python 在处理文本时, 内部使用 `\n` 作为换行符.

```
If closefd is False, the underlying file descriptor will be kept open
when the file is closed. This does not work when a file name is given
and must be True in that case.
```

如果参数 `closefd` 的值为 `False`, 则在关闭文件后, 基础文件描述符将保持打开状态. 这在给出文件名时不起作用, 在此情况下必须为 `True`.

```
A custom opener can be used by passing a callable as *opener*. The
underlying file descriptor for the file object is then obtained by
calling *opener* with (*file*, *flags*). *opener* must return an open
file descriptor (passing os.open as *opener* results in functionality
similar to passing None).
```

可以通过传递可调用的 `*opener*` 来使用自定义的 opener. 通过使用 `(*file*, *flags*)` 调用 `*opener*` 获取文件对象的基础文件描述符. `*opener*` 必须返回一个打开的文件描述符(将 `os.open` 传递给 `*opener*` 会产生类似于传递 `None` 的功能).

```
open() returns a file object whose type depends on the mode, and
through which the standard file operations such as reading and writing
are performed. When open() is used to open a file in a text mode ('w',
'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
a file in a binary mode, the returned class varies: in read binary
mode, it returns a BufferedReader; in write binary and append binary
modes, it returns a BufferedWriter, and in read/write mode, it returns
a BufferedRandom.
```

`open()` 返回一个文件对象, 类型取决于 `mode`, 并且通过它执行标准文件操作例如读写. 当 `open()` 用于以文本模式打开文件(例如 `r`, `wt`, `rt` 等), 它将会返回一个 `TextIOWrapper`. 当以二进制模式打开文件, 返回的类会有所不同: 在 `rb` 模式, 返回 `BufferedReader`; 在 `wb` 和 `ab` 模式, 返回 `BufferedWriter`, 在 `+b` 模式, 返回 `BufferedRandom`.

```
It is also possible to use a string or bytearray as a file for both
reading and writing. For strings StringIO can be used like a file
opened in a text mode, and for bytes a BytesIO can be used like a file
opened in a binary mode.
```

也可以使用字符串或字节数组作为读取和写入的文件. 对于字符串, `StringIO` 可以像在文本模式下打开的文件一样使用; 对于字节, `BytesIO` 可以像在二进制模式下打开的文件一样使用.
