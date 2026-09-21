# Python Beginner Tutorial

**Language / 语言:** English | [中文](./README.zh.md)

Learn Python from scratch, one chapter per directory: each chapter keeps its own notes (`README.md` English /
`README.zh.md` Chinese) together with that chapter's practice scripts, and runtime output is collected in the shared
`out/` directory.

## Requirements

- Python 3.x (local practice may use 3.14)
- PyCharm (optional IDE)

Activate the project virtual environment once, then run a chapter's scripts from that chapter's directory:

```bash
# Windows PowerShell (from the pythonProject111 root)
.\.venv\Scripts\Activate.ps1
cd chapter-02-python-programming-basics
python 1.py
```

Scripts that write files use paths such as `../out/1.txt`, so they expect the chapter directory as the working
directory — which is also PyCharm's default when you run a script — and they write into the shared
`pythonProject111/out/` directory.

## Project layout

```text
pythonProject111/
├── README.md                                       # This file (English)
├── README.zh.md                                    # Chinese README
├── chapter-01-python-and-pycharm-installation/
│   ├── README.md                                   # Notes (English)
│   └── README.zh.md                                # Notes (Chinese)
├── chapter-02-python-programming-basics/
│   ├── README.md                                   # Notes (English)
│   ├── README.zh.md                                # Notes (Chinese)
│   ├── 1.py                                        # Hello World
│   ├── print函数.py                                # print practice
│   ├── input函数.py                                # input practice
│   ├── 注释.py                                     # comments practice
│   ├── python缩进.py                               # indentation practice
│   └── 练习题.py                                   # Chapter 2 exercises
├── chapter-03-python-data-types-and-operators/
│   ├── README.md                                   # Notes (English)
│   └── README.zh.md                                # Notes (Chinese)
├── out/                                            # Shared runtime output (git-ignored)
│   ├── 1.txt                                       # written by print函数.py
│   └── text.txt                                    # written by 练习题.py
└── .venv/                                          # Local virtual environment (optional to commit)
```

| Path | Purpose |
|------|---------|
| `chapter-XX-<topic>/` | One directory per chapter: notes plus that chapter's practice scripts |
| `chapter-XX-<topic>/README.md`, `README.zh.md` | Chapter notes, English / Chinese pair |
| `chapter-XX-<topic>/*.py` | Runnable Python practice scripts |
| `out/` | Shared output directory written by the scripts (ignored by git) |

## Contents

### Chapter 1: Installing Python and PyCharm

`chapter-01-python-and-pycharm-installation/`

| Topic | Files |
|-------|-------|
| Python interpreter overview, install, uninstall; PyCharm intro, install, usage, uninstall | [English](./chapter-01-python-and-pycharm-installation/README.md) · [中文](./chapter-01-python-and-pycharm-installation/README.zh.md) |

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

`chapter-02-python-programming-basics/`

| Topic | Files |
|-------|-------|
| Language overview, first Python program, `print` / `input`, comments and indentation, exercises | [English](./chapter-02-python-programming-basics/README.md) · [中文](./chapter-02-python-programming-basics/README.zh.md) |

Section outline:

1. Overview of programming languages
2. First look at Python
3. Using the print function
4. Using the input function
5. Comments and indentation
6. Chapter exercises
7. Chapter summary

Scripts and outputs (matches the repo):

| Topic            | File                                                              | Notes                                                                            |
|------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Hello World      | [1.py](chapter-01-python-and-pycharm-installation/1.py)                  | First `print` output                                                              |
| `print` function | [print函数.py](chapter-02-python-programming-basics/print函数.py)    | multi-arg / `end` / `file`; writes [1.txt](out/1.txt)                              |
| `input` function | [input函数.py](chapter-02-python-programming-basics/input函数.py)    | Read name and age; f-string                                                       |
| Comments         | [注释.py](chapter-02-python-programming-basics/注释.py)              | `#` and `'''`                                                                     |
| Indentation      | [python缩进.py](chapter-02-python-programming-basics/python缩进.py)  | class / function / `for`                                                          |
| Exercises        | [练习题.py](chapter-02-python-programming-basics/练习题.py)          | write file + intro; writes [text.txt](out/text.txt)                                |

### Chapter 3: Python Data Types and Operators

`chapter-03-python-data-types-and-operators/`

| Topic | Files |
|-------|-------|
| Keywords, variables, basic data types, type conversion, `eval()`, operators, operator precedence | [English](./chapter-03-python-data-types-and-operators/README.md) · [中文](./chapter-03-python-data-types-and-operators/README.zh.md) |

Section outline:

1. Getting to know Python keywords — written
2. Defining and using variables — to be added
3. Python basic data types — to be added
4. Converting between data types — to be added
5. The `eval()` function — to be added
6. Python operators — to be added
7. Operator precedence — to be added

## Suggested learning path

1. Read the Chapter 1 install notes, then set up Python / PyCharm locally
2. Read the [Chapter 2 notes](./chapter-02-python-programming-basics/README.md)
3. From `chapter-02-python-programming-basics`, run `python 1.py` to confirm the interpreter works
4. Run `python print函数.py` and check `out/1.txt`
5. Run `python input函数.py` for input and f-strings
6. Run `python 注释.py` and `python python缩进.py`
7. Run `python 练习题.py` and check `out/text.txt`
8. Read the [Chapter 3 notes](./chapter-03-python-data-types-and-operators/README.md) on keywords, data types and
   operators

## Next steps

Later chapters (control flow, functions, modules, etc.) follow the same convention:

- Create `chapter-XX-<topic>/`
- Add notes as `README.md` (English) paired with `README.zh.md` (Chinese)
- Add practice scripts next to those notes; runtime output lands in the shared `out/`
- Keep the links in this README in sync with those files
