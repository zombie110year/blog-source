---
title:  SQL 语言
date:   2018-11-06 18:36:36
comment: true
mathjax:  false
tags:
    - SQL
categories:
    - DataBase
---

SQL (Standard Query Language) 结构化查询语言, 是为了同一各数据库操作而建立的语言. 对于不同的数据库, 都有相近的语法.

SQL 对大小写不敏感, 并且可以在任意一个关键字处换行. 使用 `--` 单行注释, `/*  */` 区块注释.

SQL 语言是解释性语言, 需要在连接上 SQL 服务器后, 在提供的命令行或解释器下编辑执行.

本文介绍 MS SQL Server 的 T-SQL 语言.

# create

create 意为 "创建", 可以被创建的对象有 `database` 数据库, `table` 表, 以及 `index` 索引.

`table` 是关系型数据库中的基本单元, 所有关系都是通过一张二维表来存储的.

`index` 是

分别使用 `create database ...` 和 `create table ...` `create index` 等语句.

## 创建数据库

创建数据库可以使用数据库管理程序提供的 GUI, 也可以使用以下语句:

```sql
create database <数据库名>
on primary -- 将文件放入主文件组
(
    name=<数据库别名>
    filename=<数据库文件存储路径> -- 例如 "D:\database\testdb.mdf"
    size=<数据库文件初始大小> -- 为一个整数, 单位是 MB 兆字节
    maxsize=<数据库文件最大大小> -- 可以用 整数MB 指定, 也可以设为 unlimited 不限制
    filegrowth=<数据库文件递增大小> -- 每一次数据库满了之后增长的大小
)
```

### 创建日志文件

日志文件应当和 database 一起建立, 在 `create database` 语句后面跟上:

```sql
create database <数据库名>
(...) -- 创建数据库文件的部分
log on
(
    name=<日志名>
    filename=<日志文件路径>
    size=<日志文件初始大小>
    maxsize=<日志文件最大大小>
    filegrowth=<日志文件增长率> -- 日志文件每次写满既定大小后增长的比率, 使用 10% 等百分数指定.
)
```

## 创建表

```sql
create table <表名>
(
    <列名> <数据类型> <列级完整性约束条件>,
    <列名> <数据类型> <列级完整性约束条件>,
    <列名> <数据类型> <列级完整性约束条件>,
    ...
    <表级完整性约束条件>
) -- 指定多个不同的列
```

### 列级完整性约束条件

- `null` 该属性可以为空值.
- `not null` 该属性不可以为空值.

### 表级完整性约束条件

```sql
primary key <pk_主键> -- 指定主键
```

# 约束

创建约束的条件语句只能使用本表数据标量表达式或常数, 不能检查数据与另一个表中数据的关系, 除非将其作为外键引入该表.

要在输入数据时检查合法性, 例如插入一门课程的成绩时检查成绩不能高于学分, 要么将 "成绩" 这条数据设计成百分比, 要么在外部程序输入时先查询课程表获取学分, 再检查成绩. 总之无法在 SQL 语言中跨表检查.
