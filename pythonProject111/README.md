# Python 零基础教程

本目录用于 Python（蟒蛇语言）入门学习，包含环境安装笔记与基础语法练习。

## 环境要求

- Python 3.x（本机练习版本可为 3.14）
- PyCharm（专业集成开发环境，可选）

建议在项目虚拟环境（Virtual Environment，虚拟环境）中运行示例：

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
python 1.py
```

## 目录

### 第一章：环境搭建

| 内容 | 文件 |
|------|------|
| Python 解释器概述、安装与卸载；PyCharm 介绍、安装、使用与卸载 | [第一章节：Python 和 PyCHarn 软件的安装.md](./第一章节：Python%20和%20PyCHarn%20软件的安装.md) |

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
| Hello World | [1.py](./1.py) | 第一条 `print` 输出 |
| `print` 函数 | [print函数.py](./print函数.py) | `sep` / `end` / `file` 参数；写入 [1.txt](./1.txt) |
| `input` 函数 | [input函数.py](./input函数.py) | 读取姓名与年龄，并用 f-string（格式化字符串）输出 |

## 项目结构

```text
pythonProject111/
├── README.md                          # 本说明
├── 第一章节：Python 和 PyCHarn 软件的安装.md
├── 1.py                               # Hello World
├── print函数.py                       # print 练习
├── input函数.py                       # input 练习
├── 1.txt                              # print 写入文件的示例输出
└── .venv/                             # 本地虚拟环境（勿提交到版本库亦可）
```

## 建议学习顺序

1. 阅读第一章安装笔记，完成本机 Python / PyCharm 环境准备  
2. 运行 `1.py`，确认解释器可用  
3. 学习并运行 `print函数.py`，理解控制台输出与写入文件  
4. 学习并运行 `input函数.py`，理解用户输入与 f-string  

## 后续计划

后续章节（变量、数据类型、运算符、流程控制等）可在本 README 的「目录」中继续追加，并与对应 `.py` / `.md` 文件保持链接一致。
