# Chapter 2: Python Programming Basics

**Language / 语言:** English | [中文](./README.zh.md)

This chapter maps one-to-one to the scripts beside this file; their results go to the shared [../out/](../out)
directory. Read and run them together.

## 00 How to run the examples

```bash
# From the pythonProject111 root — activate the virtual environment once
.\.venv\Scripts\Activate.ps1

# Then run the scripts from this chapter's own directory
# (scripts write to ../out, i.e. the shared pythonProject111/out directory)
cd chapter-02-python-programming-basics
python 1.py
```

## 01 Overview of programming languages

> What is a computer program  
> A computer program is a set of instructions written in a programming language to perform a specific task.

**Everyday analogy**  
A recipe lists ingredients and steps. A program lists instructions so the computer can calculate, process data, and
more.

> What is a programming language  
> A programming language is how people communicate with computers — like a translator from human logic into machine
> instructions.

**Kinds of programming languages**

| Kind                | Trait                 | Notes                                    |
|---------------------|-----------------------|------------------------------------------|
| Machine language    | Binary                | Hardware runs it directly; hard to write |
| Assembly language   | Mnemonics             | Needs an assembler; still hardware-tied  |
| High-level language | Near natural language | e.g. Python, Java; compile or interpret  |

**Compiled vs interpreted**

> Compiled language  
> A compiler translates the whole source into machine code first. Examples: C, C++, Go.

> Interpreted language  
> An interpreter runs source line by line. Examples: Python, JavaScript, PHP.

**Static vs scripting (extra)**  
Static languages often check types early; scripting languages favor quick writing and interpretation. These axes are not
identical to compiled/interpreted. Python is commonly treated as an interpreted scripting language and also supports
type hints.

**When to use which**  
Compiled fits performance-heavy work. Interpreted fits rapid, cross-platform scripts (data analysis, web scripts, small
tools).

## 02 First look at Python

**Origin**  
Guido van Rossum started Python in 1989 (as an ABC alternative). The name comes from *Monty Python's Flying Circus*, not
the snake. First interpreter: 1991.

**Why Python**  
Clear syntax, rich libraries, wide use (crawlers, data analysis, web, AI/ML, automation, ops, games). Edit and run
quickly.

**First program**  
Script: [1.py](../chapter-01-python-and-pycharm-installation/1.py)

```python
print('hello world')
```

```bash
cd chapter-02-python-programming-basics
python 1.py
```

You should see `hello world`. Use English punctuation in code. PyCharm setup is in Chapter 1.

## 03 Using the print function

Script: [print函数.py](./print函数.py)  
Writes: [1.txt](../out/1.txt)

> What `print` does  
> Writes text/data to the console, or to a file via `file`.

**As in the project**

```python
a = 10  # a is the variable, 10 is the value
b = 20
print(111)
print(a + b)
print('我爱中国 中国也爱我')
print(a, b, '好好学习，天天向上', 100)  # multiple values, space-separated by default
```

**`end`**

```python
print('湖南', end='--->')
print('欢迎你')  # 湖南--->欢迎你
```

**`file`**

```python
aa = open('.../out/1.txt', 'w', encoding='utf-8')
print('hello world 你好世界', file=aa)
aa.close()
```

**Extra: `sep`**  
e.g. `print('Hello', 'World', sep='-')` → `Hello-World`.

```bash
python print函数.py
```

## 04 Using the input function

Script: [input函数.py](./input函数.py)

> What `input` does  
> Reads a line from the keyboard and always returns a `str`.

**As in the project**

```python
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
print(f'我的姓名是{name}，我的年龄是{age}')  # f-string
```

**f-strings**  
Prefix with `f` and put `{name}` where values go.

**Optional**  
For numeric math: `age = int(input('请输入年龄：'))`. The project demo does not convert.

```bash
python input函数.py
```

## 05 Comments and indentation

Scripts: [注释.py](./注释.py) · [python缩进.py](./python缩进.py)

### Comments (`注释.py`)

Comments are ignored by the interpreter.

**Single-line:** `#` (PyCharm: `Ctrl + /`)

```python
# single-line comment — type # in English input mode
# print(1)
# print('hello world')
```

**Multi-line:** triple quotes `'''` or `"""` (this project uses `'''`)

```python
''' multi-line comment note '''

'''
print(100)
print('abcd')
print('你好')
'''
```

### Indentation (`python缩进.py`)

Indentation marks code blocks. After `:`, the next lines indent. Prefer **4 spaces**. Bad indent → `IndentationError`.

```python
# top-level: no indent
print(1)
print(2)


class hhh:  # class body indented
    pass


def function():  # function body indented
    pass


for i in range(5):  # loop body indented
    pass
```

## 06 Chapter exercises

Script: [练习题.py](./练习题.py)  
Exercise 1 output: [text.txt](../out/text.txt)

**Exercise 1 — write to a text file**  
Use `print()` to write `好好学习，天天向上` into `out/text.txt`.

```python
fp = open('.../out/text.txt', 'w', encoding='utf-8')
print('好好学习，天天向上', file=fp)
fp.close()
```

**Exercise 2 — personal intro**  
Use `input()` for name, age, hobby; print them with `print()`.

```python
name = input('请输入姓名：')
age = input('请输入年龄：')
hobby = input('请输入爱好：')
print('--------我的介绍：--------')
print(f'我是{name}，我今年{age}，我的爱好是{hobby}')
```

```bash
python 练习题.py
```

## 07 Chapter summary

- Programs are instruction sets; languages: machine / assembly / high-level; also compiled vs interpreted, static vs
  scripting
- Python is a high-level interpreted language
- `print(..., sep=..., end=..., file=...)` for output; `input(...)` for input (returns `str`)
- `#` / triple quotes for comments; indentation defines blocks (usually 4 spaces)

**Suggested practice order (matches the repo)**

1. [1.py](../chapter-01-python-and-pycharm-installation/1.py) — Hello World
2. [print函数.py](./print函数.py) — console + [1.txt](../out/1.txt)
3. [input函数.py](./input函数.py) — input and f-strings
4. [注释.py](./注释.py) — comments
5. [python缩进.py](./python缩进.py) — indentation
6. [练习题.py](./练习题.py) — exercises → [text.txt](../out/text.txt)  
