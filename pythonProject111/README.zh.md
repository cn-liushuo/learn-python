# Python 零基础教程

**语言 / Language:** [English](./README.md) | 中文

本目录用于 Python（蟒蛇语言）入门学习：笔记放在 `markdown/`，练习脚本放在 `code/`，运行产生的输出放在 `out/`。

## 环境要求

- Python 3.x（本机练习版本可为 3.14）
- PyCharm（专业集成开发环境，可选）

建议在项目虚拟环境（Virtual Environment，虚拟环境）中运行示例：

```bash
# Windows PowerShell（在 pythonProject111 根目录执行）
.\.venv\Scripts\Activate.ps1
python code/1.py
```

## 项目结构

```text
pythonProject111/
├── README.md                 # 英文说明
├── README.zh.md              # 本说明（中文）
├── code/                     # 练习脚本（.py）
│   ├── 1.py                  # Hello World
│   ├── print函数.py          # print 练习
│   └── input函数.py          # input 练习
├── markdown/                 # 学习笔记（.md）
│   ├── chapter-01-python-and-pycharm-installation.md
│   └── chapter-01-python-and-pycharm-installation.zh.md
├── out/                      # 运行输出（脚本写入的文件）
│   └── 1.txt                 # print 写入文件的示例输出
└── .venv/                    # 本地虚拟环境（可不提交到版本库）
```

| 目录 | 用途 |
|------|------|
| `code/` | 可运行的 Python 练习代码 |
| `markdown/` | 章节笔记与安装说明 |
| `out/` | 程序运行后生成的输出文件 |

## 目录

### 第一章：环境搭建

| 内容 | 文件 |
|------|------|
| Python 解释器概述、安装与卸载；PyCharm 介绍、安装、使用与卸载 | [English](./markdown/chapter-01-python-and-pycharm-installation.md) · [中文](./markdown/chapter-01-python-and-pycharm-installation.zh.md) |

章节小节：

1. Python 解释器概述
2. Python 解释器的安装
3. Python 解释器的卸载
4. PyCharm 介绍
5. PyCharm 的安装
6. PyCharm 的使用
7. PyCharm 的卸载
8. 本章总结

### 第二章：输入与输出（练习中）

| 内容 | 文件 | 说明 |
|------|------|------|
| Hello World | [1.py](code/1.py) | 第一条 `print` 输出 |
| `print` 函数 | [print函数.py](code/print函数.py) | `sep` / `end` / `file` 参数；写入 [1.txt](out/1.txt) |
| `input` 函数 | [input函数.py](code/input函数.py) | 读取姓名与年龄，并用 f-string（格式化字符串）输出 |

## 建议学习顺序

1. 阅读 `markdown/` 中第一章安装笔记，完成本机 Python / PyCharm 环境准备  
2. 运行 `python code/1.py`，确认解释器可用  
3. 学习并运行 `python code/print函数.py`，理解控制台输出与写入 `out/`  
4. 学习并运行 `python code/input函数.py`，理解用户输入与 f-string  

## 后续计划

后续章节（变量、数据类型、运算符、流程控制等）可按同一约定追加：

- 笔记 → `markdown/`（英文 `*.md` 与中文 `*.zh.md` 成对）
- 练习脚本 → `code/`
- 运行输出 → `out/`

并在本 README 的「目录」中保持链接一致。
