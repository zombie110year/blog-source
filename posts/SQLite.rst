---
title: SQLite3
date: 2019-06-10 15:18:17
tags:
  - sql
categories: 教程
---

本文记录了 SQLite3 的命令行工具用法, 以及一些常用的 SQL 语句.

速查表
======

表的建立与删除:

.. code:: sql

   CREATE TABLE /* 表名 */
   (
       /* 列定义 */
   );
   DROP TABLE /* 表名 */;

数据的增查删改:

.. code:: sql

   INSERT INTO /* 表 */ (/* 列 */)
   VALUES
   (/* 值 */),
   (/* 多个值 */);

   SELECT /* 列 */ FROM /* 表 */
   WHERE /* 限定条件 */;

   DELETE FROM /* 表 */ WHERE /* 限定条件 */;

   UPDATE /* 表 */ SET /* 列=值 对 */ WHERE /* 限定条件 */;

.. raw:: html

   <!--more-->

数据库与表的概念
================

sqlite 以一个文件为一个数据库, 在一个数据库中, 可以创建多个表与索引.
它属于关系型数据库, 每一张表都是二维的. 在一张表中, 可以存储多个元组,
而每一个元组由多个属性构成. 如果将一个元组用一行来表示,
那么一种属性就是表的一列.

我们要开发一个关于文件查重的应用, 其基本思想就是计算文件的 md5 摘要值,
通过比对摘要来判断文件是否重复. 这就要存储文件的 *绝对路径*, *md5值*.
而在每一次更新数据库时,
可以通过判断文件的最后修改时间来判断是否需要重新计算 md5, 于是再存储一条
*最后修改时间* 数据.

这样, 在要创建的表(姑且命名为 ``fileinfo``)中就需要三条属性, 也就是三列:

::

   -- TABLE: fileinfo
   <path>          <md5>                               <mtime>
   /example.txt    d41d8cd98f00b204e9800998ecf8427e    1560151570.7963877

其中, ``path`` 和 ``md5`` 都用字符串存储, 在 SQLite3 中使用的类型名为
``TEXT``. ``md5`` 是 16 进制表示的, 一共 32 个字符. ``mtime`` 是一个 32
位浮点数, 使用类型名 ``REAL``.

sqlite 命令
===========

sqlite 提供了命令行工具 ``sqlite3`` 以进入 sqlite 命令环境.
在这个环境下可以运行 SQL 语句以及 sqlite3 的命令.
进入这个环境的特征就是命令行的提示符更换为 ``sqlite>``.

1. 配置选取数据的显示样式.
--------------------------

默认情况下, 使用 ``SELECT`` 语句选择的数据会以

::

   |/example.txt|d41d8cd98f00b204e9800998ecf8427e|1560151570.7963877|

的形式显示. 可以通过 sqlite3 命令 ``.mode`` 和 ``.headers`` 来进行配置.

::

   sqlite> .mode column            -- 以空白字符对齐成列显示
   sqlite> .headers on             -- 显示表头

如果要查看当前配置, 可以使用 ``.show`` 指令:

::

   sqlite> .show
           echo: off
            eqp: off
        explain: auto
        headers: on
           mode: column
      nullvalue: ""
         output: stdout
   colseparator: "\037"
   rowseparator: "\n"
          stats: off
          width:
       filename: :memory:

``.mode`` 指令可以接受几个参数, 可以使用 ``.help mode`` 指令来查看:

::

   sqlite> .help mode
   .mode MODE ?TABLE?       Set output mode
      MODE is one of:
        ascii    Columns/rows delimited by 0x1F and 0x1E
        csv      Comma-separated values
        column   Left-aligned columns.  (See .width)
        html     HTML <table> code
        insert   SQL insert statements for TABLE
        line     One value per line
        list     Values delimited by "|"
        quote    Escape answers as for SQL
        tabs     Tab-separated values
        tcl      TCL list elements

为了与其他程序交互, html 与 csv 格式是比较实用的. 但是在 sqlite3
命令环境中, 都是与人类交互, 如果要进行数据交互, 只能靠复制粘贴,
因此一般使用比较美观的 column 模式. 在与其他程序交互的过程中,
一般都是使用程序自身提供的数据库工具, 而不使用 sqlite3 命令环境.

2. 显示 SQL 语句执行耗时
------------------------

在需要调试数据库性能时, 显示 SQL 语句的执行耗时是一项有用的功能. 通过
sqlite3 命令 ``.timer`` 进行控制:

::

   sqlite> .timer on   -- 开启
   sqlite> .timer off  -- 关闭

之后, 每次执行 SQL 语句, 都会显示诸如

::

   Run Time: real 0.004 user 0.000000 sys 0.000000

这样的信息了.

3. 读取与输出
-------------

读取 sqlite 命令或 sql 语句并执行:

::

   sqlite> .read path/to/scripts.sql

将 stdout 设置为目标文件. 这回让本应显示在屏幕上的输出被输出到目标文件.

::

   sqlite> .output output.txt

将当前数据库的 ``fileinfo`` 表以 SQL 语句的格式保存为文件:

::

   sqlite> .dump fileinfo

4. 在未知数据库中探索
---------------------

查看有哪些可以访问的数据库:

::

   sqlite> .databases

查看当前数据库中有哪些表:

::

   sqlite> .tables

创建数据库与表
--------------

sqlite3 以独立文件作为数据库的载体, 可以直接使用 ``sqlite3 filename.db``
来创建一个名为 ``filename.db`` 的数据库文件.
如果启动命令时没有指定文件名, 那么 sqlite3 会创建并连接入一个内存数据库.
当退出命令环境时, 内存数据库将被释放, 除非在命令环境中使用命令 ``.dump``
来将它保存为 sql 文件, 否则数据库中的信息将会消失.

这部分内容和 SQL 无关, 是 sqlite3 自己使用的命令, 一些常用的操作如下 (
``$`` 表示是系统控制台, ``sqlite>`` 表示是 sqlite3 命令环境):

::

   $ sqlite3 .fileinfo.db          # 创建名为 .fileinfo.db 的数据库文件
   # 之后, 进入命令环境
   sqlite> ▊

::

   $ sqlite3                       # 打开内存数据库, 然后进入命令环境
   sqlite> ▊

创建表以及之后的行为都使用 SQL 语句. SQL 语句的关键字不区分大小写,
为了与存储的数据相区分, 通常使用大写. 每一条 SQL 语句都需要以 ``;``
分号结尾.

.. code:: sql

   CREATE TABLE fileinfo (
       path    TEXT PRIMARY KEY,
       md5     TEXT,
       mtime   REAL
   );

在创建表的语句中, 使用这样的语法:

.. code:: sql

   CREATE TABLE /* 数据库名, 如果为 main 则可省略 */./* 表名 */ (
       /* 列名 */ /* 列的类型 */ /* 列的其他设置, 例如是否为主键之类, 可以留空 */,
       /* 另一列 */ /* 类型 */ /* 其他设置 */,
       ...
   );

要删除一个表, 使用 ``DROP`` 语句:

.. code:: sql

   DROP TABLE /* 数据库别名 */./* 表名 */;

附加与分离数据库
================

在一些使用情形下, 可能需要同时访问多个数据库中的部分表. 可以使用 SQL
语句种的 ATTACH 和 DETACH 进行连接与分离.

.. code:: sql

   ATTACH DATABASE /* 数据库名 */ AS /* 在当前会话中使用的别名 */;
   DETACH DATABASE /* 在当前会话中使用的别名 */;

对 sqlite3 来说, 第一个打开的数据库会得到 ``main`` 为别名.
而数据库本身的名字则是数据库文件的路径, 可以使用相对路径或绝对路径.

增查删改
========

在创建了数据库与表之后, 可以使用 INSERT, SELECT, DELETE 和 UPDATE
来实现数据的增查删改. 每一条数据都是以元组的性质参与操作的.

INSERT
------

INSERT 语句用于向表中增加数据, 它的语法为:

.. code:: sql

   INSERT INTO /* 数据库别名 */./* 表名 */ (/* 列 A */, /* 列 B */)
   VALUES (/* 值 A */, /* 值 B */),
   (/* 其他元组 */);

一次 INSERT 可以插入多个元组, 不同元组间使用 ``,`` 逗号分隔, 最后一个以
``;`` 分号结束. 在元组和属性列表中, 使用 ``,`` 逗号分隔各个元素.

如果操作的数据库为 main, 则别名可以省略.

SELECT
------

SELECT 语句用于从表中查询数据, 语法为:

.. code:: sql

   SELECT /* 属性列表 */ FROM /* 数据库别名 */./* 表名 */;

同样的, 数据库别名可以在为 main 时被省略. 可以使用通配符 ``*``
来从表中查询所有数据:

.. code:: sql

   SELECT * FROM fileinfo;

另外, 还可以使用 ``WHERE`` 条件表达式有条件地从数据库中查询数据:

.. code:: sql

   SELECT path, mtime FROM fileinfo
   WHERE md5="d41d8cd98f00b204e9800998ecf8427f";

DELETE
------

DELETE 语句用于从表中删除一个元组, 语法为:

.. code:: sql

   DELETE FROM /* 数据库别名 */./* 表名 */
   WHERE /* 条件 */;

DELETE 语句必须使用 WHERE 条件表达式. 凡是符合条件的元组都会被删除.
**由于删除是一项比较危险的操作, 因此在删除前推荐使用 SELECT
语句先查询确认一下.**

如果发生了误删, 可以尝试从日志文件中找到记录,
在生产环境中建议把日志打开. (生产环境中很少使用 sqlite3, 建议了解一下
Microsoft SQL Server, MySQL 等商业数据库, 或者 MariaDB 等开源数据库).

UPDATE
------

UPDATE 语句用于更改现存的元组, 语法为:

.. code:: sql

   UPDATE /* 数据库别名 */./* 表名 */ SET /* 列 A */=/* 值 A */, /* 列 B */=/* 值 B */
   WHERE /* 条件 */;

UPDATE 语句也必须使用条件表达式, 凡是符合条件的元组,
都会将其对应列修改为特定值. 大部分情况下应当一次修改一个元组.

更改同样是危险操作, 建议提前确认.

WHERE 条件表达式
----------------

WHERE 子句是经常在 SELECT, DELETE, UPDATE 语句中使用的条件判断语句.
在它之后可以接上一些条件表达式. 例如

============== =============================
条件表达式     含义
============== =============================
``col=value``  对应列的值等于 value 的元组
``col<value``  对应列的值小于 value 的元组
``col>value``  对应列的值大于 value 的元组
``col<=value`` 对应列的值不大于 value 的元组
``col>=value`` 对应列的值不小于 value 的元组
============== =============================

此外还有 ``LIKE``, ``GLOB``, ``NOT``, ``AND``, ``OR`` 操作符.

``LIKE`` 操作符用于比较两个字符串, 例如:

.. code:: sql

   SELECT * FROM fileinfo WHERE
   path LIKE "/home/zom%";

这会选择到所有 path 以 ``/home/zom`` 开头的元组.
它实际上是判断字符串与包含通配符的字符串是否匹配. ``%``
表示零个或多个字符, ``_`` 表示一个字符.

``GLOB`` 与 ``LIKE`` 类似, 但是对大小写敏感, 而且使用 ``*``, ``?``
作为通配符.

而 ``NOT``, ``AND``, ``OR`` 和大多数编程语言中的条件表达式连接符一样,
表示 “否”, “且”, “或” 关系.

子查询
------

通过 ``SELECT`` 语句查询到的内容可以被当作一张临时的表, 可以将它放在
``WHERE`` 语句中, 继续添加语句进行查询, 例如:

.. code:: sql



   # 索引, 视图

   视图和索引是为了方便 SQL 的查询而引入的.
   索引由数据库自动使用, 大多数数据库都会自动为表的主键建立索引, 也可以手动为特定的列建立索引.
   视图可以当作一个只读的表, 它可以参与除了修改之外的表操作.

   ## 索引

   建立索引的 SQL 语句:

   ```sql
   CREATE INDEX /* 索引名 */ ON /* 数据库别名 */./* 表名 */
   (/* 列名 */);

为表的特定列建立索引. 可以为多个列建立索引.

另外, 还可以建立 *非重复* 索引, 使用关键字 ``UNIQUE``.
这将导致表中无法插入已索引列重复的元组:

.. code:: sql

   CREATE UNIQUE INDEX /* 索引名 */ ON /* 数据库别名 */./* 表名 */
   (/* 列名 */);

要删除索引, 使用 ``DROP`` 语句:

.. code:: sql

   DROP INDEX /* 索引名 */;

在一些情况下不适合使用索引:

1. 频繁写操作的列
2. 含大量空值的列

视图
----

视图的使用场景可以为:

1. 限制数据访问, 让特定用户只能获取允许的数据.
2. 汇总数据库中的数据, 以便生成报告.
3. 方便在特定场景下的数据查找.

需要注意的是, **表的更新不会导致视图更新**.

建立视图:

.. code:: sql

   CREATE VIEW /* 视图名 */ AS /* 选择的数据 */;

在 *选择的数据* 中, 使用 ``SELECT``
语句从已有的表或视图中选择需要的数据:

.. code:: sql

   CREATE VIEW md5_path AS
   SELECT md5, path FROM fileinfo;

也可以使用 ``WHERE`` 语句附加一些条件.

删除视图:

.. code:: sql

   DROP VIEW /* 视图名 */;

.. raw:: html

   <!-- # 日志 -->

SQL 安全
========

在实际使用情况下, 用户可能会提交 SQL 语句作为查询条件, 例如,
在一个网页中, 用户需要查询一个昵称对应的账号, 后台使用的 SQL 模板如下:

.. code:: sql

   SELECT id FROM users WHERE nickname=/* 输入 */;

如果用户给出 ``null'; DROP TABLE users;'`` 作为输入,
那么后台就会执行语句:

.. code:: sql

   SELECT id FROM users WHERE nickname='null'; DROP TABLE users;'';

这就执行了三条语句, 一个查询了无关紧要的值, 一个删除了表,
最后一个语法错误. 这就是 SQL 注入的一个案例.

要防止这种攻击, 可以在提交输入之前, 检查输入的类型.
大多数解决方法是使用正则表达式, 只有符合的输入才会被提交.

Python 访问 SQLite3 数据库
==========================

Python 可以使用标准库 ``sqlite3`` 来访问 sqlite3 , 常用的方法如下,
其他的建议参考官方文档:

.. code:: python

   session = sqlite3.connect(database)     # 打开 database 数据库
   cursor  = session.cursor()              # 创建一个
   result = cursor.execute(sql)            # 执行一条 SQL 语句
   result = cursor.executescript(sql)      # 执行 SQL 脚本, 由多个 SQL 语句组成, 每条语句用 ; 分隔
   session.commit()                        # 提交执行, 有写操作的语句之后提交后才会实际执行
   session.rollback()                      # 回滚至上一次提交
   session.close()                         # 终止会话, 注意, 不会自动 commit

``cursor.execute`` 的结果是一个可迭代对象, 可以直接使用 ``for``
语句迭代或者通过 ``list``, ``tuple`` 等函数将查询结果转化为 Python 对象.

.. code:: python

   >>> import sqlite3
   >>> session = sqlite3.connect(".fileinfo.db")
   >>> cursor = session.cursor()
   >>> result = cursor.execute("SELECT * FROM fileinfo")
   >>> list(result)
   [('/1.txt', 'd41d8cd98f00b204e9800998ecf8427e', 1.0),
    ('/2.txt', 'd41d8cd98f00b204e9800998ecf8427e', 2.0),
    ('/3.txt', 'd41d8cd98f00b204e9800998ecf8427e', 3.0),
    ('/4.txt', 'd41d8cd98f00b204e9800998ecf8427e', 4.0),
    ('/5.txt', 'd41d8cd98f00b204e9800998ecf8427e', 5.0),
    ('/6.txt', 'd41d8cd98f00b204e9800998ecf8427f', 6.0)]

.. raw:: html

   <!-- # SQLite3 嵌入 C/C++ 程序 -->

