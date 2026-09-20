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
│   └── input函数.py          # input practice
├── markdown/                 # Study notes (.md)
│   ├── chapter-01-python-and-pycharm-installation.md
│   └── chapter-01-python-and-pycharm-installation.zh.md
├── out/                      # Runtime output files
│   └── 1.txt                 # Sample file written by print
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

### Chapter 2: Input and output (in progress)

| Topic | File | Notes |
|-------|------|-------|
| Hello World | [1.py](code/1.py) | First `print` output |
| `print` function | [print函数.py](code/print函数.py) | `sep` / `end` / `file`; writes [1.txt](out/1.txt) |
| `input` function | [input函数.py](code/input函数.py) | Read name and age; print with f-string |

## Suggested learning path

1. Read the Chapter 1 install notes under `markdown/`, then set up Python / PyCharm locally
2. Run `python code/1.py` to confirm the interpreter works
3. Study and run `python code/print函数.py` for console output and writing to `out/`
4. Study and run `python code/input函数.py` for user input and f-strings

## Next steps

Later chapters (variables, data types, operators, control flow, etc.) can follow the same layout:

- Notes → `markdown/` (pair `*.md` English with `*.zh.md` Chinese)
- Practice scripts → `code/`
- Runtime output → `out/`

Keep links in this README in sync with those files.
