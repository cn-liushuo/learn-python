# 第一章节：Python 和 PyCharm 软件的安装

**语言 / Language:** [English](./chapter-01-python-and-pycharm-installation.md) | 中文

## 01 Python 解释器概述

> Python 解释器的定义  
> Python 解释器是一款用于解释、执行 Python 代码的应用程序，能够将人类可读的 Python 源代码转为计算机可执行的指令。

> Python 解释器的核心作用  
> 作为 Python 开发的基础工具，其核心作用是解析代码逻辑并逐行执行，是连接开发者与计算机硬件的关键桥梁，确保 Python 程序能够正常运行。

## 02 Python 解释器的安装

**Windows 系统安装步骤：**  
**官网下载 Python 安装包**  
访问 [Python](https://www.python.org/) 官方网站，下载适用于 Windows 系统的 Python 3.14 版本安装包（64-bit）。

**立即安装（默认设置）**  
双击安装包窗口，选择 **Install Now**，默认安装路径一般为  
`C:\Users\<用户名>\AppData\Local\Programs\Python\Python314`，  
包含 IDLE、pip 及文档，并自动创建快捷方式、关联文件。

**自定义安装选项**  
选择 **Customize installation**，可勾选 **Use admin privileges when installing py.exe**，在高级选项中设置安装路径、添加 Python 到环境变量（建议勾选）、为所有用户安装等，完成后点击 **Install**。

**安装完成校验方法**

> 打开命令提示符窗口  
> 按下 `Win + R` 打开「运行」窗口，输入 `cmd` 并回车，启动命令提示符。

> 输入验证命令  
> 在命令行中输入 `python` 并回车，若显示 `Python 3.14.0(...) on win32` 等版本信息，表明 Python 解释器安装成功。

## 03 Python 解释器的卸载

**Windows 系统卸载步骤**  
**打开控制面板**  
在 Windows 设置中搜索「控制面板」，点击进入后选择「卸载程序」。

**卸载 Python 解释器**  
在程序列表中找到 **Python 3.14.0 (64-bit)**，选中后点击「卸载」，按提示完成卸载。

**卸载 Python Launcher**  
继续在程序列表中找到 **Python Launcher**，选中并点击「卸载」，确保该组件被彻底移除。

## 04 PyCharm 介绍

**PyCharm 的基本概念**  
**PyCharm 的定义**  
PyCharm 是由 JetBrains 公司开发的一款专为 Python 设计的集成开发环境（IDE），提供全面的 Python 开发支持工具。

**社区版的特点**  
免费开源，仅支持 Python 开发（编辑、调试、代码检查），适合学习和小型项目。

**专业版的特点**  
需付费订阅，额外支持 Web 开发（Django / Flask）、数据库工具、Jupyter 深度集成、远程开发等高级功能，适配企业开发 / 数据分析 / 机器学习等场景。

**PyCharm 核心功能与适用场景**  
**核心功能**  
智能代码编写、强大的调试工具、数据分析友好特性、版本控制集成、插件生态丰富。

**适用场景一：Python 基础学习**  
社区版提供基础开发功能，满足初级学者代码编写、调试需求，助力快速掌握 Python 语法。

**适用场景二：数据分析**  
支持 Jupyter 深度集成，便于数据处理、可视化及模型训练，适配数据分析与机器学习工作流。

**适用场景三：Web 开发与全栈开发**  
专业版支持 Django 等 Web 框架，可实现前端 + Python 全栈开发，满足企业级 Web 项目需求。

## 05 PyCharm 的安装

**PyCharm 下载渠道**  
**01 官方下载地址**  
PyCharm 官网下载地址为：https://www.jetbrains.com/zh-cn/pycharm/，用户可通过该地址获取最新版本安装程序。

**02 统一产品试用政策**  
所有用户自动获得为期一个月的免费 Pro 试用，试用期结束后可选择订阅 Pro 版本或继续免费使用包含 Jupyter 支持的核心功能。

**03 版本权益说明**  
PyCharm Professional 用户不受影响，可继续享受统一产品中所有 Pro 功能的完全使用权限；社区版为免费开源，仅支持基础 Python 开发。

## 06 PyCharm 的使用

**PyCharm 初始设置与项目创建**  
**用户协议与导入设置**  
首次打开 PyCharm 需阅读并勾选《JETBRAINS USER AGREEMENT》（2021年9月22日生效版本），点击“继续”完成协议确认；随后进入导入设置窗口，可选择“不导入设置”或者导入之前的配置文件。

**新项目创建步骤**
在欢迎界面选择“新建项目”，可从头创建本地项目，或通过 SSH、WSL、Dev Container 进行远程开发；设置项目存放路径后，系统自动生成 .venv 虚拟环境文件，用于隔离项目依赖。

**新建文件与代码书写**
在项目目录右键选择“新建” → “Python 文件”，命名为 1.py；在编辑区输入代码print('hello world')，右键文件选择“运行”即可输出结果，完成基础代码测试。

## 07 PyCharm 的卸载

**Windows系统卸载方法**  
**打开控制面板**  
在 Windows 设置中搜索“控制面板”，点击进入控制面板界面。

**进入程序卸载页面**  
在控制面板中依次点击“程序” → “程序和功能”，进入卸载或更改程序页面。

**卸载 Python 程序**  
在程序列表中找到“PyCharm2024.3.6”（具体版本以实际安装为准），选中后点击“卸载”，按照提示完成卸载流程。


## 08 本章总结

Python 解释器的下载，安装，卸载

PyCharm 的下载，安装，使用，设置，卸载
