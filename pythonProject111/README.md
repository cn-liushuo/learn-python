# Python Beginner Tutorial

**Language / 语言:** English | [中文](./README.zh.md)

This directory is for learning Python from scratch. Notes live in `markdown/`, practice scripts in `code/`, and runtime output in `out/`.

## Requirements

- Python 3.x (local practice may use 3.14)
- PyCharm (optional IDE)

Run examples inside the project virtual environment:

```bash
# Windows PowerShell (from the pythonProject111 root)
.\.venv\Scripts\Activate.ps1
python code/1.py
```

## Project layout

```text
pythonProject111/
├── README.md                 # This file (English)
├── README.zh.md              # Chinese README
├── code/                     # Practice scripts (.py)
│   ├── 1.py                  # Hello World
│   ├── print函数.py          # print practice
│   ├── input函数.py          # input practice
│   ├── 注释.py               # comments practice
│   ├── python缩进.py         # indentation practice
│   └── 练习题.py             # Chapter 2 exercises
├── markdown/                 # Study notes (.md)
│   ├── chapter-01-python-and-pycharm-installation.md
│   ├── chapter-01-python-and-pycharm-installation.zh.md
│   ├── chapter-02-python-programming-basics.md
│   └── chapter-02-python-programming-basics.zh.md
├── out/                      # Runtime output files
│   ├── 1.txt                 # written by print函数.py
│   └── text.txt              # written by 练习题.py
└── .venv/                    # Local virtual environment (optional to commit)
```

| Directory | Purpose |
|-----------|---------|
| `code/` | Runnable Python practice scripts |
| `markdown/` | Chapter notes and install guides |
| `out/` | Files produced when scripts run |

## Contents

### Chapter 1: Environment setup

| Topic | File |
|-------|------|
| Python interpreter overview, install, uninstall; PyCharm intro, install, usage, uninstall | [English](./markdown/chapter-01-python-and-pycharm-installation.md) · [中文](./markdown/chapter-01-python-and-pycharm-installation.zh.md) |

Section outline:

1. Python interpreter overview
2. Installing the Python interpreter
3. Uninstalling the Python interpreter
4. Introduction to PyCharm
5. Installing PyCharm
6. Using PyCharm
7. Uninstalling PyCharm
8. Chapter summary

### Chapter 2: Python Programming Basics

| Topic                                                                                           | File                                                                                                                        |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Language overview, first Python program, `print` / `input`, comments and indentation, exercises | [English](./markdown/chapter-02-python-programming-basics.md) · [中文](./markdown/chapter-02-python-programming-basics.zh.md) |

Section outline:

1. Overview of programming languages
2. First look at Python
3. Using the print function
4. Using the input function
5. Comments and indentation
6. Chapter exercises
7. Chapter summary

Scripts and outputs (matches the repo):

| Topic            | File                            | Notes                                                 |
|------------------|---------------------------------|-------------------------------------------------------|
| Hello World      | [1.py](code/1.py)               | First `print` output                                  |
| `print` function | [print函数.py](code/print函数.py)   | multi-arg / `end` / `file`; writes [1.txt](out/1.txt) |
| `input` function | [input函数.py](code/input函数.py)   | Read name and age; f-string                           |
| Comments         | [注释.py](code/注释.py)             | `#` and `'''`                                         |
| Indentation      | [python缩进.py](code/python缩进.py) | class / function / `for`                              |
| Exercises        | [练习题.py](code/练习题.py)           | write file + intro; writes [text.txt](out/text.txt)   |

## Suggested learning path

1. Read the Chapter 1 install notes under `markdown/`, then set up Python / PyCharm locally
2. Read the Chapter 2
   notes [chapter-02-python-programming-basics.md](./markdown/chapter-02-python-programming-basics.md)
3. Run `python code/1.py` to confirm the interpreter works
4. Run `python code/print函数.py` and check `out/1.txt`
5. Run `python code/input函数.py` for input and f-strings
6. Run `python code/注释.py` and `python code/python缩进.py`
7. Run `python code/练习题.py` and check `out/text.txt`

## Next steps

Later chapters (variables, data types, operators, control flow, etc.) can follow the same layout:

- Notes → `markdown/` (pair `*.md` English with `*.zh.md` Chinese)
- Practice scripts → `code/`
- Runtime output → `out/`

Keep links in this README in sync with those files.
