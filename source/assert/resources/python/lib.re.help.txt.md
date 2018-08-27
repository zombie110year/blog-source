[Origin-File](/assert/repos/python/lib.re.help.txt)

> Help on module re:

# 名称

re - 提供正则表达式支持.

# 描述

此模块提供类似于 Perl 的正则表达式 (regular expression) 匹配操作. 它同时支持 8-bit 和 Unicode 字符串; 被处理的 pattern 与 strings 都可以包含空字符与非 ASCII 字符.

正则表达式可以同时包含特殊字符与普通字符. 大多数普通字符, 例如 "A", "a", 或者 "0", 是最简单的正则表达式; 它们只陪陪其自身. 你可以组合普通字符, 例如 "last" 匹配字符串 "last".

特殊字符如下:

```
"."      匹配除换行符外的任意字符.
"^"      匹配字符串头部.
"$"      匹配字符串尾部, 或匹配字符串末尾行的尾部(如果字符串末尾为换行符的话).
"*"      匹配 0 或多次(贪婪). 贪婪的意思是会尽可能多地匹配重复结构.
"+"      匹配 1 或多次(贪婪).
"?"      匹配 0 或 1 次.
*?,+?,?? 上面三种特殊字符的非贪婪版本.
{m,n}    匹配 m 到 n 次(贪婪).
{m,n}?   上一条的非贪婪版.
"\"     要么转义特殊字符, 要么声明特殊序列. Either escapes special characters or signals a special sequence.
[]       表示一个字符集合, 若 `^` 为第一个字符, 将表示其补集.
"|"      `A|B` 将创建一个匹配 A 或 B 的正则表达式.
(...)    匹配括号内的正则表达式. 其内容可以在稍后被恢复或匹配. Matches the RE inside the parentheses. The contents can be retrieved or matched later in the string.
(?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
(?:...)  Non-grouping version of regular parentheses.
(?P<name>...) The substring matched by the group is accessible by name.
(?P=name)     Matches the text matched earlier by the group named name.
(?#...)  一个注释, 将被忽略. A comment; ignored.
(?=...)  Matches if ... matches next, but doesn't consume the string.
(?!...)  Matches if ... doesn't match next.
(?<=...) Matches if preceded by ... (must be fixed length).
(?<!...) Matches if not preceded by ... (must be fixed length).
(?(id/name)yes|no) Matches yes pattern if the group with id/name matched, the (optional) no pattern otherwise.
 ```

下列这些由 `\` 与一个字符组成的特殊序列. 如果这些普通字符不在此列表中, 最终的正则表达式将会匹配第二个字符.

```
\number  匹配分组中对应编号的内容.
\A       只匹配字符串头部.
\Z       只匹配字符串尾部.
\b       匹配处于单词头部或尾部的空字符.
\B       匹配处于单词内部的空字符.
\d       匹配任何十进制数字(digit), 等价于处于字节模式或带有 ASCII 标志的集合 `[0-9]`. 处于不带有 ASCII 标志的单元时, 将会在整个 Unicode 范围内匹配数字.
         Matches any decimal digit; equivalent to the set [0-9] in
         bytes patterns or string patterns with the ASCII flag.
         In string patterns without the ASCII flag, it will match the whole
         range of Unicode digits.
\D       匹配任何非数字字符, 等价于 `[^\d]`.
\s       匹配任何空白字符. 等价于处于字节模式或带有 ASCII 标志的 `[ \t\n\r\f\v]`. 处于不带有 ASCII 标志的单元时, 将会匹配整个 Unicode 范围内的空白字符.
\S       匹配任何非空白字符, 等价于 `[^\s]`.
\w       匹配任何数字或字母, 等价于处于字节模式或带有 ASCII 标志的 `[a-zA-Z0-9_]`. 处于不带有 ASCII 标志的单元时, 将会匹配整个 Unicode 范围内的数字或字母符号(字母加数字加下划线). 处于 LOCALE 环境中时, 将会匹配在此语言中被定义为数字的字母.
\W       Matches the complement of \w.
\\       匹配一个反斜杠.
```

此模块开放如下函数:

```
match     匹配处于字符串头部的表达式.
fullmatch 匹配整个字符串中的表达式.
search    搜索整个字符串中出现的表达式.
sub       Substitute occurrences of a pattern found in a string.
subn      Same as sub, but also return the number of substitutions made.
split     Split a string by the occurrences of a pattern.
findall   Find all occurrences of a pattern in a string.
finditer  Return an iterator yielding a match object for each match.
compile   将一个 pattern 编译为正则对象(RegexObject)
purge     Clear the regular expression cache.
escape    Backslash all non-alphanumerics in a string.
```


    Some of the functions in this module takes flags as optional parameters:
        A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                       match the corresponding ASCII character categories
                       (rather than the whole Unicode categories, which is the
                       default).
                       For bytes patterns, this flag is the only available
                       behaviour and needn't be specified.
        I  IGNORECASE  Perform case-insensitive matching.
        L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
        M  MULTILINE   "^" matches the beginning of lines (after a newline)
                       as well as the string.
                       "$" matches the end of lines (before a newline) as well
                       as the end of the string.
        S  DOTALL      "." matches any character at all, including the newline.
        X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
        U  UNICODE     For compatibility only. Ignored for string patterns (it
                       is the default), and forbidden for bytes patterns.
    
    This module also defines an exception 'error'.

# CLASSES

```
    builtins.Exception(builtins.BaseException)
        sre_constants.error
    
    class error(builtins.Exception)
     |  Exception raised for invalid regular expressions.
     |  
     |  Attributes:
     |  
     |      msg: The unformatted error message
     |      pattern: The regular expression pattern
     |      pos: The index in the pattern where compilation failed (may be None)
     |      lineno: The line corresponding to pos (may be None)
     |      colno: The column corresponding to pos (may be None)
     |  
     |  Method resolution order:
     |      error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, msg, pattern=None, pos=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
```

# 函数

```py
compile(pattern, flags=0)
    """编译一个正则表达式 pattern, 返回一个 pattern 对象"""

escape(pattern)
    """转义除了 ASCII 字母, 数字, 与下划线 `_` 之外的所有字符."""

findall(pattern, string, flags=0)
    """返回字符串中所有非重复匹配项的列表.
    如果 pattern 中存在一个或多个捕获组, 将返回捕获组列表, 如果 pattern 中有多个捕获组, 将返回一个元组列表.
    结果中包含空匹配项"""
finditer(pattern, string, flags=0)
    """Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a match object.
    
    Empty matches are included in the result."""

fullmatch(pattern, string, flags=0)
    """Try to apply the pattern to all of the string, returning
    a match object, or None if no match was found."""

match(pattern, string, flags=0)
    """尝试在字符串的开头匹配 pattern, 返回一个 Match 对象. 找不到匹配项时返回 None"""

purge()
    """清楚正则表达式缓存"""

search(pattern, string, flags=0)
    """扫描整个字符串以寻找匹配 pattern 的部分, 若成功则返回一个 Match 对象, 否则返回 None"""

split(pattern, string, maxsplit=0, flags=0)
    """Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list."""

sub(pattern, repl, string, count=0, flags=0)
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used."""

subn(pattern, repl, string, count=0, flags=0)
    """Return a 2-tuple containing (new_string, number).
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the match object and must
    return a replacement string to be used."""

template(pattern, flags=0)
    """Compile a template pattern, returning a pattern object"""
```

# DATA

    A = <RegexFlag.ASCII: 256>
    ASCII = <RegexFlag.ASCII: 256>
    DOTALL = <RegexFlag.DOTALL: 16>
    I = <RegexFlag.IGNORECASE: 2>
    IGNORECASE = <RegexFlag.IGNORECASE: 2>
    L = <RegexFlag.LOCALE: 4>
    LOCALE = <RegexFlag.LOCALE: 4>
    M = <RegexFlag.MULTILINE: 8>
    MULTILINE = <RegexFlag.MULTILINE: 8>
    S = <RegexFlag.DOTALL: 16>
    U = <RegexFlag.UNICODE: 32>
    UNICODE = <RegexFlag.UNICODE: 32>
    VERBOSE = <RegexFlag.VERBOSE: 64>
    X = <RegexFlag.VERBOSE: 64>
    __all__ = ['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'fi...

# VERSION

    2.2.1

# FILE

    lib\re.py



