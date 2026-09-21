# 第二章节：Python 编程基础入门

**语言 / Language:** [English](./chapter-02-python-programming-basics.md) | 中文

本章笔记与 `code/`、`out/` 中的现有文件一一对应，建议边读边运行。

## 01 了解程序设计语言概述

> 什么是计算机程序  
> 计算机程序（Computer Program）是使用编程语言组织起来的一组计算机指令的集合，用于实现特定功能，是计算机执行操作的依据。

**生活实例类比**  
如同菜谱步骤：菜谱通过明确食材、用量、烹饪顺序指导做菜；程序通过指令序列指导计算机完成任务（如计算、数据处理）。

> 编程语言的定义  
> 编程语言（Programming Language）是人与计算机沟通的工具，用于编写计算机程序；其作用类似「翻译官」，将人类逻辑转换为计算机可识别的指令。

**编程语言的分类**

| 类型                        | 特点     | 说明                       |
|---------------------------|--------|--------------------------|
| 机器语言（Machine Language）    | 二进制指令  | 硬件直接执行，效率高，难写难读          |
| 汇编语言（Assembly Language）   | 助记符    | 需经汇编器（Assembler）转换，仍依赖硬件 |
| 高级语言（High-level Language） | 接近自然语言 | 如 Python、Java，需编译或解释后执行  |

**编译型与解释型**

> 编译型语言（Compiled Language）  
> 编译器（Compiler）先把整份源码翻译成机器码再运行。典型：C、C++、Go。

> 解释型语言（Interpreted Language）  
> 解释器（Interpreter）运行时逐行翻译并执行。典型：Python、JavaScript、PHP。

**静态语言与脚本语言（补充）**

- **静态语言（Static Language）**：多在编译期做类型检查，变量类型通常固定。代表：Java、C、C++、Go。
- **脚本语言（Scripting Language）**：侧重快速编写与解释执行，变量类型可随赋值变化。代表：Python、JavaScript、PHP、Ruby。

二者并不完全等同于「编译 / 解释」。Python 常被归为解释型脚本语言，同时支持类型提示（Type Hint）。

**适用场景**  
编译型偏重性能（如系统开发）；解释型偏重快速开发与跨平台（如数据分析、Web 脚本、小工具）。按项目需求选择即可。

## 02 初识 Python

**起源与名称**  
1989 年圣诞节，荷兰程序员 Guido van Rossum 开始开发 Python（作为 ABC 语言的替代）。名称来自喜剧《Monty Python's Flying
Circus》，并非「蟒蛇」。1991 年首个解释器正式发布。

**为什么选择 Python**  
语法简洁、易学；类库丰富；适用于爬虫、数据分析、Web、人工智能 / 机器学习、自动化、运维、游戏等。修改后可直接运行，开发效率高。

**第一个程序**  
对应脚本：[1.py](../code/1.py)

```python
print('hello world')
```

```bash
# Windows PowerShell（在 pythonProject111 根目录）
.\.venv\Scripts\Activate.ps1
python code/1.py
```

看到 `hello world` 即表示解释器可用。括号、引号请用英文输入法输入。

**开发工具**  
常用 IDE：PyCharm（自动补全、高亮、调试）。安装见第一章。

## 03 熟练应用 print 函数

对应脚本：[print函数.py](../code/print函数.py)  
运行后会写入：[1.txt](../out/1.txt)

> 作用  
> `print` 把内容输出到控制台，也可通过 `file` 写入文件。

**基础写法（与项目代码一致）**

```python
a = 10  # a 是变量，10 是值
b = 20  # b 是变量，20 是值
print(111)
print(a + b)  # 做运算
print('我爱中国 中国也爱我')
print(a, b, '好好学习，天天向上', 100)  # 多个内容，默认用空格分隔
```

**end：控制结尾字符**  
默认 `end='\n'`（换行）。项目中的写法：

```python
print('湖南', end='--->')
print('欢迎你')  # 输出：湖南--->欢迎你
```

**file：写入文件**  
项目中写入 `out/1.txt`：

```python
aa = open('../out/1.txt', 'w', encoding='utf-8')  # 写入文件
print('hello world 你好世界', file=aa)  # 输出内容到文件中
aa.close()  # 关闭文件
```

**扩展：sep 自定义分隔符**  
`sep` 默认空格。例如：`print('Hello', 'World', sep='-')` → `Hello-World`。

```bash
python code/print函数.py
```

## 04 熟练应用 input 函数

对应脚本：[input函数.py](../code/input函数.py)

> 作用  
> `input('提示')` 从键盘读入一行，**返回值类型始终是字符串（`str`）**。

**项目中的写法**

```python
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
print(f'我的姓名是{name}，我的年龄是{age}')  # f 格式化（f-string）
```

**关于 f-string**  
字符串前加 `f`，用 `{变量名}` 插入值。

**补充：需要数值运算时再转换**  
若要对年龄做加减，可写：`age = int(input('请输入年龄：'))`。项目示例本身未做转换。

```bash
python code/input函数.py
```

## 05 掌握注释与缩进

对应脚本：[注释.py](../code/注释.py) · [python缩进.py](../code/python缩进.py)

### 注释（见 `注释.py`）

注释不会被执行，用来说明代码含义。

**单行注释**：行首（或行尾）加 `#`。PyCharm 快捷键：`Ctrl + /`。

```python
# 单行注释   在注释内容的前面加一个 # 号   英文状态下 按住 shift + 3
# 快捷键 Ctrl + /
# print(1)
# print('hello world')
```

**多行注释**：用三个单引号 `'''` 或三个双引号 `"""` 包裹（项目中用的是 `'''`）。

```python
''' 多行注释的内容  """   """  单引号 双引号 三对'''

'''
print(100)
print('abcd')
print('你好')
'''
```

### 缩进（见 `python缩进.py`）

缩进表示代码的层次关系。类、函数、`for` 等语句行尾的冒号 `:`，加上下一行缩进，表示代码块开始。推荐 **4 个空格**；缩进不一致会报
`IndentationError`。

```python
# 正常情况下，直接写 没有缩进
print(1)
print(2)


class hhh:  # 定义类
    pass


def function():  # 定义函数
    pass


for i in range(5):  # for 循环 控制流程
    pass
```

## 06 本章练习题

对应脚本：[练习题.py](../code/练习题.py)  
第 1 题输出文件：[text.txt](../out/text.txt)

**练习 1：输出到文本文件**  
用 `print()` 将「好好学习，天天向上」写入 `out/text.txt`。

```python
fp = open('../out/text.txt', 'w', encoding='utf-8')  # 写入文件
print('好好学习，天天向上', file=fp)  # 输出内容到文件
fp.close()  # 关闭文件
```

**练习 2：输出个人爱好**  
用 `input()` 从键盘读取姓名、年龄、爱好，再用 `print()` 输出到控制台。

```python
name = input('请输入姓名：')
age = input('请输入年龄：')
hobby = input('请输入爱好：')
print('--------我的介绍：--------')
print(f'我是{name}，我今年{age}，我的爱好是{hobby}')
```

```bash
python code/练习题.py
```

## 07 本章总结

- 程序是指令集合；语言分机器 / 汇编 / 高级；另有编译型与解释型、静态与脚本等分类角度
- Python 是高级解释型语言，适合入门与快速开发
- `print(..., sep=..., end=..., file=...)` 负责输出；`input(...)` 负责输入（返回 `str`）
- `#` / 三引号做注释；缩进划分代码块（常用 4 空格）

**建议练习顺序（与仓库文件一致）**

1. [1.py](../code/1.py) — Hello World
2. [print函数.py](../code/print函数.py) — 控制台输出 → [1.txt](../out/1.txt)
3. [input函数.py](../code/input函数.py) — 输入与 f-string
4. [注释.py](../code/注释.py) — 单行 / 多行注释
5. [python缩进.py](../code/python缩进.py) — 缩进与代码块
6. [练习题.py](../code/练习题.py) — 综合练习 → [text.txt](../out/text.txt)  
