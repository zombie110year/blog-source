---
title: C 与 C++ 使用正则表达式
date: 2019-04-25 23:25:22
tags:
- regex
- C/C++
---

# C 语言的正则表达式

GNU 为 C 语言提供了 `regex.h` 头文件, 其目标代码已经包含在 `glibc` 中了.

GNUC regex 提供了两类接口, 一类属于标准的 POSIX.2 接口, 另一类则是 GNUC 的历史实现. 这两种实现都包含在一个头文件中, 当定义了 `_POSIX_C_SOURCE` 宏时, 将只会编译 POSIX.2 接口实现.

<!--more-->

## 基本使用

```c
#include <regex.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
    /* 类型定义 */
    regex_t compiled_pattern;
    regmatch_t match_body[1];
    int regex_exec_error;

    char* const pattern = "[0-9]{1,}"; // 正则表达式
    char* string = (char*)calloc(bufsize, sizeof(char));
    fgets(string, bufsize, stdin);

    /* 编译表达式 */
    regcomp(&compiled_pattern, pattern, REG_EXTENDED);
    /* 进行匹配 */
    regex_exec_error = regexec(&compiled_pattern, string, 1, match_body, REG_NOTBOL | REG_NOTEOL);
    /* 清理现场 */
    regfree(&compiled_pattern);

    /* 验收结果 */
    if (!regex_exec_error) {
        for (regoff_t i = match_body[0].rm_so; i < match_body[0].rm_eo; ++i) {
            putchar(string[i]);
        }
        putchar('\n');
    } else if (regex_exec_error == REG_NOMATCH) {
        printf("没有有效匹配\n");
    }

    return 0;
}
```

在使用正则表达式之前, 必须先编译它. 这并不是将正则表达式编译成汇编指令, 而是产生一个可被 `regexec` 等函数解析的结构体.

总结一下上述流程：

1. 提前准备存储正则表达式以及匹配结果的变量 `compiled_pattern` 和 `match_body`。
2. 使用 `regcomp` 函数将表达式编译，得到一个可用于 `regexec` 的结构体。
3. 调用 `regexec` 函数以在字符串中匹配字符串，成功结果将存储在 `match_body` 中，而函数的返回值为状态码。
4. 释放 `regex_t` 结构体。
5. 验收结果：每一个成功的匹配将会存储在 `match_body` 中，其类型为 `regmatch_t`，最重要的两个成员是 `rm_so`, `rm_eo`，分别存储了匹配区域的 开始索引与结束索引。可理解为是 `regex match start offset` 以及 `regex match end offset`。并且，子表达式将按顺序存储在 `match_body` 的各个元素中。

## 详解

### 类型

在 C 语言中使用正则表达式, 需要用到下面两个结构体:

|     类型     | 作用                                                         |
| :----------: | ------------------------------------------------------------ |
|  `regex_t`   | 包含编译后的正则表达式, 是一个结构体, 对于用户来说, 只有一个需要访问的成员: `re_nsub` |
| `regmatch_t` | 传递给 `regexec` 的 `matchprt` 数组. 包含两个成员: `rm_so`, `rm_eo`. |

#### regex_t

这个结构体包含了编译后的正则表达式内容, 对于用户, 只需要访问 `re_nsub` 成员, 这个成员记录了正则表达式中子捕获组的数量.

此结构体在 `regcomp` 函数中进行设置, 在 `regexec` 中使用, 最后通过 `regfree` 释放.

#### regmatch_t

这个结构体包含了匹配的表达式信息, 可以用于提取子捕获组. 用在 `regexec` 函数中.

### regcomp 函数

```c
int regcomp (regex_t* restrict compiled, const char* restrict pattern, int cflags);
/**
 * 由于 C 编译器会转义一次转义符 `\`, 而正则表达式中又会转义一次, 
 * 因此, 注意使用双反斜杠 `\\` 来作为正则表达式的转义字符, 如:
 *
 *     pattern = "\\d";
 */
```

此函数将正则表达式的字符串写法 `pattern` 编译为可解析的结构体, 存入指针 `compiled` 所管理的内存空间之中. 可以使用 `cflags` 设置正则表达式的语法和语义:

- `REG_EXTENDED`:  使用扩展的正则表达式语法.
- `REG_ICASE`: 不区分大小写
- `REG_NOSUB`: 注销子捕获组所需的匹配信息, 将不进行子表达式的捕获. 也可以在 `regexec` 中为`matchptr` 和 `nmatch` 传递零参数. 如果不使用此选项, 那么可以进行子表达式的捕获, `compiled->re_nsub` 储存了多少个子捕获组.
- `REG_NEWLINE`: 进行多行匹配. 当匹配文本中包含换行符时, 会将整个字符串以换行符 `\n` 分割为多份. `^` 将匹配行首(`\n` 的下一位), `$` 将匹配行尾(`\n` 的上一位), 而默认情况下, 这两个字符将匹配整个字符串的首尾. 同时, 通配符 `.` 将不会包含 `\n`, 类似于 `[^...]` 这样的字符集也不会包含 `\n` 换行符.
- 如果要同时启用多个选项, 可以用位或运算: `REG_EXTENDED | REG_NEWLINE`; 如果不启用任何选项, 传入 `0` 即可.

此函数有可能返回以下错误码:

- `REG_BADBR`:  正则表达式中存在无效的 `{...}` 构造. 一个有效的 `{...}` 构造必须包含一个单独的数字, 或者一个用逗号 `,` 分隔的单调增加的数对: `{0}`, `{1,2}`
- `REG_BADPAT`: 正则表达式里有语法 (syntax) 错误.
- `REG_BADPRT`:  一个量词, 例如 `?` 或 `*`, 在错误的位置出现.
- `REG_ECOLLATE`: 正则表达式指向一个无效的 collating 元素, (未定义的为了字符串整理的当前区域设置). 参阅 [Locale Categories](https://www.gnu.org/software/libc/manual/html_node/Locale-Categories.html#Locale-Categories)
- `REG_ECTYPE`: 正则表达式引用了一个无效的字符类名.
- `REG_EESCAPE`: 正则表达式以转义符 `\` 结束.
- `REG_ESUBREG`: 在 `\数字` 构造中有无效的数字.
- `REG_EBRACK`: 正则表达式中存在不匹配的方括号.
- `REG_EPAREN`:  一个扩展的正则有不匹配的括号, 或者一个基本的正则表达式有不匹配的 `(` 或 `)`.
- `REG_EBRACE`: 正则表达式中有不匹配的 `{` 或 `}`.
- `REG_ERANGE`: 在范围表达式中有一个无效的终点.
- `REG_ESPACE`: 内存耗尽.

### regexec 函数

在字符串中匹配一个已编译的正则表达式结构体, pattern 将在字符串内任何位置进行匹配, 除非使用了 `^$` 锚字符. 支持的表达式特性较少, 类似于 `\d` 之类的字符集是没有的, 只能使用 `[]` 字符集自己定义.

```c
int regexec (const regex_t *restrict compiled, const char *restrict string, size_t nmatch, regmatch_t matchptr[restrict], int eflags);
```

参数解释:

- `compiled`: 用于匹配的 pattern
- `string`: 被匹配的字符串
- `nmatch`: 子捕获组的数目; 如果不想捕获, 传入 `0`.
- `matchptr[restrict]` 一个数组, 用于存储匹配到的子捕获组; 如果不想捕获, 传入 `NULL`.
- `eflags`: 为匹配过程设置选项.
    - `REG_NOTBOL` 不将字符串的开头视作行首, 也就是说, 不对此字符串之前的文本做任何假设.
    - `REG_NOTEOL` 不将字符串的末尾视作行尾, 也就是说, 不对此字符串之后的文本做任何假设.
    - 如果启用多个选项, 使用位或运算, 如果一个都不用, 传入 `0`.

返回的错误码:

- `REG_NOMATCH`: 没有任何有效匹配.
- `REG_ESPACE`: 内存耗尽.

#### regmatch_t 结构体

在 [`regexec`](#regexec-函数) 中使用的 `regmatch_t matchptr[restrict]` 是一个存储子捕获组的数组. 有 `rm_so`, `rm_eo` 两个成员. 分别存储了子捕获组在整个字符串中的起点和终点索引. 在调用 `regexec` 函数时, 用 `nmatch` 参数指定 `matchptr[]` 的长度, 如果实际的子捕获组比长度多, 那么多余的子捕获组将被忽略. 

#### regoff_t 结构体

`regmatch_t` 的 `rm_so`, `rm_eo` 两个成员都是 `regoff_t` 类型, 这个类型其实就是 `int` 的别名. 用于确定捕获组在源字符串中的位置, 其值为匹配到的捕获组的起始索引值. 如果匹配失败, 则此结构体中的成员值是无意义的垃圾值.

### 进行捕获

1. 构造一个长度等于 `compiled.re_nsub` 的 `matchptr` 数组. 
2. 将 `compiled.re_nsub` 与 `matchptr` 传入. 经过 `regexec` 执行后, `matchptr` 中的每一个 `regmatch_t` 都会储存匹配到的字符串在源字符串中的位置信息. 
3. 通过 `string.h` 中的 `memcpy` 函数, 将对应字节复制到另一个字符串中. 注意,  传入的字符串首地址为 `string + regmatch_t.rm_so`, 而字节长度为 `regmatch_t.rm_eo - regmatch_t.rm_so`.

### regfree 函数

释放编译后的正则表达式结构体.

```c
int regfree(const regex_t *restrict compiled);
```

# C++ 的正则表达式

> 参考 https://zh.cppreference.com/w/cpp/regex

C++ 在 C++ 11 之后提供了 `regex` 头文件，其中定义了正则表达式相关的功能。这里有四个主要概念：

- 源字串：将被正则表达式匹配的字符串，可以是两个字符串迭代器所限定的范围，一个 C-Style 字符串或 `std::string` 。
- 模式：正则表达式本身，是由特定语法的字符串构造的 `std::basic_regex` 。支持一些语法变体，见 [syntax_option_type](https://zh.cppreference.com/w/cpp/regex/syntax_option_type) 。
- 捕获组：正则表达式所匹配到的捕获组将被 `std::match_results` 存储。
- 替换字串：确定如何替换匹配的字符串，支持一些语法变体，见 [syntax_option_type](https://zh.cppreference.com/w/cpp/regex/syntax_option_type) 。

## 基本用例

这里以从文本中检索出电子邮箱地址为例

```cpp
#include <cassert>
#include <iostream>
#include <regex>
#include <string>
using namespace std;

string text = "这里有一些文本，但 zombie110year@example.com 是一个电子邮件地址";

int main(void) {
  /* 构造 regex 实例 */
  regex pattern("([a-z0-9A-Z]{1,})@([a-z\\.]{1,})", regex_constants::ECMAScript);

  /* 确认匹配/搜索 */
  cout << regex_search(text, pattern) << endl;

  /* 提取匹配文本 */
  smatch matches;
  regex_search(text, matches, pattern);

  for (auto m: matches) {
    cout << m.str() << endl;
  }
  return 0;
}
```

总结一下：

1. 构造 regex 实例。第一个参数是表达式语法，第二个则是语法选项。注意选择 `ECMAScript`（C++11可用），这将使用 JavaScript 的正则引擎，其他引擎也有，例如 awk, basic, grep 等等，但是由于和 ECMAScript 语法存在差异，没有学习，所以未使用。语法选项支持用位运算组合，它实际上也是一个无符号整数，用 bit 位进行设定，因此常用 `|` 位或运算组合一些选项，常用的有：
   1. `icase` 忽略大小写，默认不忽略。
   2. `nosubs` 不捕获子表达式。
2. 搜索/匹配。使用 `regex_search` 或 `regex_match` 函数进行搜索/匹配。这两个函数只会返回布尔值，即表达式是否能匹配源字串。`search` 是当模式在源字串中存在时便返回 true，`match` 则要求完全匹配。
3. 要提取捕获组，可以利用 `regex_search` 或 `regex_match` 的重载，将捕获组结果储存在 `smatch` （基类为 `match_results` ）实例中，对于得到的 match 对象，可以用 `.str()` 方法转换为 `std::string`。

这两个函数有 7 个重载（match 和 search 是对应的，下面只放 search）：

```cpp
/* 类型名这么长，真令人眼花缭乱啊 */
template <class BidirIt, class Alloc, class CharT, class Traits>
bool regex_search(BidirIt first /* 源串迭代器-首 */, BidirIt last /* 源串迭代器-尾 */,
                  std::match_results<BidirIt, Alloc> &m/* 收集捕获组的 match_results */,
                  const std::basic_regex<CharT, Traits> &e /* 正则表达式 */,
                  std::regex_constants::match_flag_type flags =
                      std::regex_constants::match_default/* 位设置项 */);
// (1) 	(C++11 起)
template <class CharT, class Alloc, class Traits>
bool regex_search(const CharT *str/* C-Style 字符串 */, 
                  std::match_results<const CharT *, Alloc> &m,
                  const std::basic_regex<CharT, Traits> &e,
                  std::regex_constants::match_flag_type flags =
                      std::regex_constants::match_default);
// (2) 	(C++11 起)
template <class STraits, class SAlloc, class Alloc, class CharT, class Traits>
bool regex_search(
    const std::basic_string<CharT, STraits, SAlloc> &s/* std::string 类型的源串 */,
    std::match_results<
        typename std::basic_string<CharT, STraits, SAlloc>::const_iterator,
        Alloc> &m,
    const std::basic_regex<CharT, Traits> &e,
    std::regex_constants::match_flag_type flags =
        std::regex_constants::match_default);
// (3) 	(C++11 起)
template <class BidirIt, class CharT, class Traits>
bool regex_search(BidirIt first, BidirIt last,
                  /* 省略掉 match_results 参数，不进行捕获组的捕获 */
                  const std::basic_regex<CharT, Traits> &e,
                  std::regex_constants::match_flag_type flags =
                      std::regex_constants::match_default);
// (4) 	(C++11 起)
template <class CharT, class Traits>
bool regex_search(const CharT *str,
                  /* 同上，不捕获 */
                  const std::basic_regex<CharT, Traits> &e,
                  std::regex_constants::match_flag_type flags =
                      std::regex_constants::match_default);
// (5) 	(C++11 起)
template <class STraits, class SAlloc, class CharT, class Traits>
bool regex_search(const std::basic_string<CharT, STraits, SAlloc> &s,
                  const std::basic_regex<CharT, Traits> &e,
                  std::regex_constants::match_flag_type flags =
                      std::regex_constants::match_default);
// (6) 	(C++11 起)
template <class STraits, class SAlloc, class Alloc, class CharT, class Traits>
bool regex_search(
    const std::basic_string<CharT, STraits, SAlloc> &&,
    std::match_results<
        typename std::basic_string<CharT, STraits, SAlloc>::const_iterator,
        Alloc> &,
    const std::basic_regex<CharT, Traits> &,
    std::regex_constants::match_flag_type flags =
        std::regex_constants::match_default) = delete;
// (7) 	(C++14 起)
```

> 后面的内容看得人脑壳痛，有需求再去查吧。