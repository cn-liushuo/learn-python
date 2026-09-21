# Python 零基础教程

**语言 / Language:** [English](./README.md) | 中文

按章节学习 Python：每一章单独一个目录，章内同时放着笔记（`README.md` 英文 / `README.zh.md` 中文）与该章的练习脚本，所有运行输出统一放在项目共享的 `out/` 目录。

## 环境要求

- Python 3.x（本机练习版本可为 3.14）
- PyCharm（专业集成开发环境，可选）

先在项目根目录激活一次虚拟环境，然后在「某一章的目录」下运行脚本：

```bash
# Windows PowerShell（在 pythonProject111 根目录执行）
.\.venv\Scripts\Activate.ps1
cd chapter-02-python-programming-basics
python 1.py
```

写文件的脚本使用 `../out/1.txt` 这类相对路径，因此约定以「章节目录」为工作目录运行（PyCharm 运行脚本时默认也是如此），输出会写入共享的 `pythonProject111/out/`。

## 项目结构

```text
pythonProject111/
├── README.md                                       # 英文说明
├── README.zh.md                                    # 本说明（中文）
├── chapter-01-python-and-pycharm-installation/
│   ├── README.md                                   # 笔记（英文）
│   └── README.zh.md                                # 笔记（中文）
├── chapter-02-python-programming-basics/
│   ├── README.md                                   # 笔记（英文）
│   ├── README.zh.md                                # 笔记（中文）
│   ├── 1.py                                        # Hello World
│   ├── print函数.py                                # print 练习
│   ├── input函数.py                                # input 练习
│   ├── 注释.py                                     # 注释练习
│   ├── python缩进.py                               # 缩进练习
│   └── 练习题.py                                   # 第二章综合练习
├── chapter-03-python-data-types-and-operators/
│   ├── README.md                                   # 笔记（英文）
│   └── README.zh.md                                # 笔记（中文）
├── out/                                            # 共享运行输出（不提交到版本库）
│   ├── 1.txt                                       # print函数.py 写入
│   └── text.txt                                    # 练习题.py 写入
└── .venv/                                          # 本地虚拟环境（可不提交到版本库）
```

| 路径 | 用途 |
|------|------|
| `chapter-XX-<主题>/` | 每一章一个目录：笔记 + 该章练习脚本 |
| `chapter-XX-<主题>/README.md`、`README.zh.md` | 章节笔记，英文 / 中文成对 |
| `chapter-XX-<主题>/*.py` | 可运行的 Python 练习脚本 |
| `out/` | 脚本运行后写入的共享输出目录（已被 git 忽略） |

## 目录

### 第一章：Python 和 PyCharm 软件的安装

`chapter-01-python-and-pycharm-installation/`

| 内容 | 文件 |
|------|------|
| Python 解释器概述、安装与卸载；PyCharm 介绍、安装、使用与卸载 | [English](./chapter-01-python-and-pycharm-installation/README.md) · [中文](./chapter-01-python-and-pycharm-installation/README.zh.md) |

章节小节：

1. Python 解释器概述
2. Python 解释器的安装
3. Python 解释器的卸载
4. PyCharm 介绍
5. PyCharm 的安装
6. PyCharm 的使用
7. PyCharm 的卸载
8. 本章总结

### 第二章：Python 编程基础入门

`chapter-02-python-programming-basics/`

| 内容 | 文件 |
|------|------|
| 程序与语言概述、初识 Python、`print` / `input`、注释与缩进、综合练习 | [English](./chapter-02-python-programming-basics/README.md) · [中文](./chapter-02-python-programming-basics/README.zh.md) |

章节小节：

1. 了解程序设计语言概述
2. 初识 Python
3. 熟练应用 print 函数
4. 熟练应用 input 函数
5. 掌握注释与缩进
6. 本章练习题
7. 本章总结

配套脚本与输出（与仓库文件一致）：

| 内容          | 文件                                                            | 说明                                                                     |
|-------------|---------------------------------------------------------------|------------------------------------------------------------------------|
| Hello World | [1.py](chapter-01-python-and-pycharm-installation/1.py)              | 第一条 `print` 输出                                                        |
| `print` 函数  | [print函数.py](chapter-02-python-programming-basics/print函数.py) | 多参数 / `end` / `file`；写入 [1.txt](out/1.txt)                            |
| `input` 函数  | [input函数.py](chapter-02-python-programming-basics/input函数.py) | 读取姓名与年龄，f-string 输出                                                    |
| 注释          | [注释.py](chapter-02-python-programming-basics/注释.py)           | 单行 `#` / 多行 `'''`                                                      |
| 缩进          | [python缩进.py](chapter-02-python-programming-basics/python缩进.py) | 类 / 函数 / `for` 缩进示例                                                    |
| 综合练习        | [练习题.py](chapter-02-python-programming-basics/练习题.py)       | 写文件 + 个人介绍；写入 [text.txt](out/text.txt)                               |

### 第三章：Python 数据类型与运算符详解

`chapter-03-python-data-types-and-operators/`

| 内容 | 文件 |
|------|------|
| 关键字、变量、基本数据类型、类型转换、`eval()`、运算符与优先级 | [English](./chapter-03-python-data-types-and-operators/README.md) · [中文](./chapter-03-python-data-types-and-operators/README.zh.md) |

章节小节：

1. 了解 Python 中的关键字 —— 已完成
2. 熟练掌握 Python 中变量的定义及使用 —— 待补充
3. 掌握 Python 中的基本数据类型 —— 待补充
4. 掌握数据类型之间的相互转换 —— 待补充
5. `eval()` 函数 —— 待补充
6. 掌握 Python 中的运算符 —— 待补充
7. 运算符优先级 —— 待补充

## 建议学习顺序

1. 阅读第一章安装笔记，完成本机 Python / PyCharm 环境准备
2. 阅读[第二章笔记](./chapter-02-python-programming-basics/README.zh.md)
3. 在 `chapter-02-python-programming-basics` 目录下运行 `python 1.py`，确认解释器可用
4. 运行 `python print函数.py`，查看控制台与 `out/1.txt`
5. 运行 `python input函数.py`，练习输入与 f-string
6. 运行 `python 注释.py` 与 `python python缩进.py`
7. 运行 `python 练习题.py`，完成综合练习并查看 `out/text.txt`
8. 阅读[第三章笔记](./chapter-03-python-data-types-and-operators/README.zh.md)，学习关键字、数据类型与运算符

## 后续计划

后续章节（流程控制、函数、模块等）按同一约定追加：

- 新建 `chapter-XX-<主题>/`
- 笔记写成 `README.md`（英文）与 `README.zh.md`（中文）成对
- 练习脚本直接放在该章目录下，运行输出落在共享的 `out/`
- 并在本 README 的「目录」中保持链接一致
