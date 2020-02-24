---
title: CMake 简单笔记
date: 2019-04-15 12:01:53
tags:
  - C/C++
  - cmake
categories: 笔记
---

> CMake 3.14.0

<!--more-->

# CMake 基本概念

- CMake 中的命令不区分大小写
- CMake 使用 `set` 命令设置变量
- CMake 使用 `${varname}` 的形式引用变量
- 对于多个元素, 可以使用空格分隔

# 必须命令

## `cmake_minimum_required`

`cmake_minimum_required` 命令用于设置 CMake 最低所需要的版本, 语法:

```cmake
cmake_minimum_required(VERSION <min>[...<max>])
```

- 设置最低版本

```cmake
cmake_minimum_required(VERSION 3.14.0)
```

- 设置在两个版本之间

```cmake
cmake_minimum_required(VERSION 3.0.0..3.14.0)
```

## `project`

[`project`](https://cmake.org/cmake/help/v3.14/command/project.html) 设置项目信息. 在顶层模块中, 这是必须的设置.

```cmake
project(<PROJECT-NAME>
        [VERSION <major>[.<minor>[.<patch>[.<tweak>]]]]
        [DESCRIPTION <project-description-string>]
        [HOMEPAGE_URL <url-string>]
        [LANGUAGES <language-name>...])
```

这会设置一个变量 `PROJECT_NAME`, 它的值也是参数 `<PROJECT_NAME>` 的值.
同时, 也会产生另外两个相关的变量:

- `<PROJECT_NAME>_SOURCE_DIR`
- `<PROJECT_NAME>_BINARY_DIR`

例如:

```
project(helloworld)
```

则会产生

```
${PROJECT_NAME} # helloworld
${helloworld_SOURCE_DIR}
${helloworld_BINARY_DIR}
```

对于顶层模块, 则有:

```
PROJECT_SOURCE_DIR = ${<PROJECT_NAME>_SOURCE_DIR}
PROJECT_BINARY_DIR = ${<PROJECT_NAME>_BINARY_DIR}
```

# 生成目标

## `add_executable`

[`add_executable`](https://cmake.org/cmake/help/v3.14/command/add_executable.html) 为项目添加一个可执行目标:

```cmake
add_executable(<name> [WIN32] [MACOSX_BUNDLE]
                [EXCLUDE_FROM_ALL]
                [source1] [source2 ...])
```

- `<name>` 设置为可执行文件的命名, 在 Windows 上, 会自动添加 `.exe` 后缀.
- `EXCLUDE_FROM_ALL` 设置是否在生成的 Makefile 中的 `all` 目标中将此目标排除. 如果设置了此变量, 则排除, 需要单独 `make <name>` 进行构建, 否则将被包含.
- `sources ...` 是一个源文件列表, 也可以使用变量来指定, 常用 `aux_sources_directory` 来将一个目录下的所有源文件设置到一个变量中.

这会创建一个与 `<name>` 同名的变量, 指向这个目标.

## `add_library`

[`add_library`](https://cmake.org/cmake/help/v3.14/command/add_library.html) 将对应的源代码设置为库目标:

```cmake
add_library(<name> [STATIC | SHARED | MODULE]
            [EXCLUDE_FROM_ALL]
            [source1] [source2 ...])
```

- `<name>` 是该生成目标的命名, 会自动添加相应的前缀/后缀名. 例如 `lib<name>.a`, `<name>.lib` 等.
- `STATIC | SHARED | MODULE` 三选一, 设置该目标的库类型 (静态链接库 | 动态链接库 | 未链接到其他目标的插件，但可以在运行时使用类似 `dlopen` 的函数动态加载)

这会创建一个与 `<name>` 同名的变量, 指向这个目标.

## `target_link_library`

[`target_link_library`](https://cmake.org/cmake/help/v3.14/command/target_link_libraries.html) 设置一个链接关系.

```cmake
target_link_libraries(<target> ... <item>... ...)
```

将 `<item>` 链接到 `<target>` 上. `<item>` 可以是一个空格分隔的列表.

# 模块化

## `add_subdirectory`

[`add_subdirectory`](https://cmake.org/cmake/help/v3.14/command/add_subdirectory.html) 将一个子目录添加进来.
典型的 CMake 构建项目将类似于一个树状结构, 顶部目录的 CMakeLists.txt 将作为 根, 而各级子目录中的 CMakeLists.txt 则作为 分支与叶, 最终构建整个项目.

```cmake
add_subdirectory(<source_dir> [<binary_dir>] [EXCLUDE_FROM_ALL])
```

子目录中的 CMakeLists.txt 将被立刻解析, 并 "嵌入" 到当前位置.

- `<source_dir>` 设置此模块的源码路径(即 CMakeLists.txt 所在路径), 可以是相对或绝对路径. 相对路径是相对于当前文件.
- `<binary_dir>` 设置此模块的二进制生成路径, 如果不进行设置, 则设置为 `<source_dir>`. 可以是相对或绝对路径.

# 编译选项

## `add_compile_options`

[`add_compile_options`](https://cmake.org/cmake/help/v3.14/command/add_compile_options.html) 添加编译器选项.

```cmake
add_compile_options(<option> ...)
```

例如

```cmake
if (MSVC)
    # warning level 4 and all warnings as errors
    add_compile_options(/W4 /WX)
else()
    # lots of warnings and all warnings as errors
    add_compile_options(-Wall -Wextra -pedantic -Werror)
endif()
```

## `add_link_options`

[`add_link_options`](https://cmake.org/cmake/help/v3.14/command/add_link_options.html) 添加链接器选项.

## `add_definitions`

[`add_definitions](https://cmake.org/cmake/help/v3.14/command/add_definitions.html) 添加宏定义.

```cmake
add_definitions(-DFOO -DBAR ...)
```

## `include_directoies`

添加头文件搜索路径.

## `link_directoies`

添加库文件搜索路径.

# 常用命令

## `aux_source_directory`

```cmake
aux_source_directory(<dir> <variable>)
```

将 `<dir>` 中的源文件扫描, 保存到变量 `<variable>` 中.

## `set`/`unset`

[`set`](https://cmake.org/cmake/help/v3.14/command/set.html) 设置变量.

常用的预定义变量有:

- `EXECUTABLE_OUTPUT_PATH`: 生成的可执行文件保存的路径
- `LIBRARY_OUTPUT_PATH`: 生成的库文件保存的路径
- [`CMAKE_BUILD_TYPE`](https://cmake.org/cmake/help/v3.14/variable/CMAKE_BUILD_TYPE.html): 构建类型, 有  `Debug`, `Release`, `MinSizeRel` 等级别.

也可以在生成构建脚本时, 使用 `-Dkey=value` 的形式在命令行中设置:

```sh
cmake -DCMAKE_BUILD_TYPE=Release ..
```
使用 `unset` 删除一个变量.

# 脚本语法

可以为 CMake 脚本添加一些逻辑功能: https://cmake.org/cmake/help/v3.14/manual/cmake-commands.7.html#scripting-commands

## if-else

https://cmake.org/cmake/help/v3.14/command/if.html

```cmake
if(<condition>)
  <commands>
elseif(<condition>) # optional block, can be repeated
  <commands>
else()              # optional block
  <commands>
endif()
```

# cmake 命令行选项

## 定义一个变量

```sh
cmake -D <key>=<value>
# or
cmake -D <key>:<type>=<value>
```

## 设置生成器

选择生成 Makefile, VS 工程, 或者其他构建系统的文件:

```sh
cmake -G "<Generators>"
```

## 仅预览

```sh
cmake -N
```

## 使用 graphviz 生成依赖关系图

```sh
cmake --graphviz=output.gv
```

得到 graphviz 标记语言文件, 可以继续使用 graphviz 工具得到图片.

https://cmake.org/cmake/help/v3.14/module/CMakeGraphVizOptions.html
