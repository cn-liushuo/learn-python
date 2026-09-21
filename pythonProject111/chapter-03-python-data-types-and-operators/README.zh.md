# 第三章：Python 数据类型与运算符详解

**语言 / Language:** [English](./README.md) | 中文

本章 01 节笔记已完成，02–07 节为占位小节，后续补充（配套脚本将与本章笔记放在同一目录）。

## 01 了解 Python 中的关键字

**关键字的定义与作用**  
**关键字的定义**  
关键字是Python中被赋予特定意义的单词，这些单词在Python语言中有固定的语法功能和使用场景。

**关键字的核心作用**  
关键字是Python语法规则的重要组成部分，用于实现条件判断、循环控制、函数定义、类声明等核心编程逻辑。

**使用限制**  
在开发程序时，不可将关键字作为变量、函数、类、模块和其他对象的名称使用，否则会导致语法错误。

**关键字分类及列表**

| 类别        | 关键字列表                              | 说明                                     |
|-----------|------------------------------------|----------------------------------------|
| 逻辑/布尔     | `True`、`False`、`None`、`and`、`or`、`not` | `True`/`False` 是布尔值，`None` 是空值，`and`/`or`/`not` 是逻辑运算符 |
| 条件判断      | `if`、`elif`、`else`                  | `else` 也用于循环和异常处理                      |
| 模式匹配（3.10+） | `match`、`case`                      | 软关键字，仅在 `match` 语句中生效                   |
| 循环控制      | `for`、`while`、`break`、`continue`     | `break` 结束循环，`continue` 跳过本次循环          |
| 异常处理      | `try`、`except`、`finally`、`raise`、`assert` | `assert` 用于断言，`raise` 用于主动抛出异常          |
| 函数与类      | `def`、`class`、`lambda`、`return`、`yield` | `yield` 用于生成器函数                        |
| 作用域与命名    | `global`、`nonlocal`、`del`            | `global`/`nonlocal` 声明变量的作用域，`del` 删除对象引用  |
| 模块与别名     | `import`、`from`、`as`                 | `as` 既可给模块起别名，也可用于 `with ... as ...`     |
| 上下文管理     | `with`                              | 用于自动管理资源（如文件）的打开与关闭                    |
| 异步编程（3.5+） | `async`、`await`                     | `async def` 定义协程，`await` 等待协程执行         |
| 成员与同一性判断  | `in`、`is`                           | `in` 判断成员是否存在，`is` 判断是否为同一个对象           |
| 占位语句      | `pass`                              | 空语句，用于占据语法位置而不执行任何操作                   |

**全部关键字（共 35 个）**  
`False`、`None`、`True`、`and`、`as`、`assert`、`async`、`await`、`break`、`class`、`continue`、`def`、`del`、`elif`、`else`、`except`、`finally`、`for`、`from`、`global`、`if`、`import`、`in`、`is`、`lambda`、`nonlocal`、`not`、`or`、`pass`、`raise`、`return`、`try`、`while`、`with`、`yield`

**软关键字（共 4 个）**  
`_`、`case`、`match`、`type`  
软关键字只有在特定语法场景下才具有关键字含义，因此仍可以作为变量名、函数名等标识符使用。

**关键字的查看方法**  
**使用`keyword`模块**  
Python提供内置模块keyword，可用于查看当前版本的关键字列表及相关信息，是学习和验证关键字的重要工具。

**查看关键字列表**  
通过代码`import keyword;print(keyword.kwlist)`可输出Python所有关键字，例如Python 3.x版本包含35个关键字（具体数量因版本略有差异）。

**获取关键字个数**  
使用`print(len(keyword.kwlist))`可获取关键字的总数量， 帮助了解关键字体系规模。

**大小写敏感性**  
关键字严格区分大小写，例如True是关键字，而true是普通变量名；None是关键字，none不是。

## 02 熟练掌握 python 中变量的定义及使用

> 待补充：本节笔记尚未整理。

## 03 掌握 python 中的基本数据类型

> 待补充：本节笔记尚未整理。

## 04 掌握数据类型之间的相互转换

> 待补充：本节笔记尚未整理。

## 05 eval() 函数

> 待补充：本节笔记尚未整理。

## 06 掌握 Python 中的运算符

> 待补充：本节笔记尚未整理。

## 07 运算符优先级

> 待补充：本节笔记尚未整理。

