# Chapter 1: Installing Python and PyCharm

**Language / 语言:** English | [中文](./chapter-01-python-and-pycharm-installation.zh.md)

## 01 Python interpreter overview

> Definition  
> A Python interpreter is an application that interprets and runs Python code. It turns human-readable Python source into instructions the computer can execute.

> Core role  
> As the foundation of Python development, it parses program logic and executes it line by line. It bridges the developer and the machine so Python programs can run correctly.

## 02 Installing the Python interpreter

**Windows install steps**  
**Download from the official site**  
Visit the [Python](https://www.python.org/) website and download the Windows Python 3.14 installer (64-bit).

**Install now (defaults)**  
Double-click the installer and choose **Install Now**. The default path is typically under  
`C:\Users\<username>\AppData\Local\Programs\Python\Python314`.  
This includes IDLE, pip, and documentation; shortcuts and file associations are created automatically.

**Customize installation**  
Choose **Customize installation**. You can enable **Use admin privileges when installing py.exe**, set the install path under Advanced Options, add Python to `PATH` (recommended), install for all users, then click **Install**.

**Verify the install**

> Open Command Prompt  
> Press `Win + R`, type `cmd`, and press Enter.

> Run the check command  
> Type `python` and press Enter. If you see version text such as `Python 3.14.0 (...) on win32`, the interpreter is installed successfully.

## 03 Uninstalling the Python interpreter

**Windows uninstall steps**  
**Open Control Panel**  
Search for **Control Panel** in Windows Settings, open it, then choose **Uninstall a program**.

**Uninstall the Python interpreter**  
Find **Python 3.14.0 (64-bit)** in the list, select it, click **Uninstall**, and follow the prompts.

**Uninstall Python Launcher**  
Also find **Python Launcher**, select it, and click **Uninstall** so that component is fully removed.

## 04 Introduction to PyCharm

**Basic concepts of PyCharm**  
**What PyCharm is**  
PyCharm is an integrated development environment (IDE) developed by JetBrains specifically for Python, offering a complete set of tools for Python development.

**Community Edition features**  
Free and open source. Supports Python development only (editing, debugging, code inspection). Good for learning and small projects.

**Professional Edition features**  
Paid subscription. Adds Web development (Django / Flask), database tools, deeper Jupyter integration, remote development, and other advanced features for enterprise development, data analysis, and machine learning.

**PyCharm core features and use cases**  
**Core features**  
Smart code editing, powerful debugging tools, data-analysis-friendly features, version control integration, and a rich plugin ecosystem.

**Use case 1: Learning Python basics**  
The Community Edition provides the essential development features that beginners need for writing and debugging code, helping them learn Python syntax quickly.

**Use case 2: Data analysis**  
Deep Jupyter integration makes data processing, visualization, and model training easier, fitting data analysis and machine learning workflows.

**Use case 3: Web development and full-stack development**  
The Professional Edition supports Web frameworks such as Django, enabling front-end plus Python full-stack development for enterprise-grade Web projects.

## 05 Installing PyCharm

**PyCharm download channels**  
**01 Official download address**  
The PyCharm official download address is: https://www.jetbrains.com/zh-cn/pycharm/. You can get the latest installer from that page.

**02 Unified product trial policy**  
All users automatically receive a one-month free Pro trial. After the trial ends, you can subscribe to Pro or keep using the core features, including Jupyter support, for free.

**03 Version benefits**  
PyCharm Professional users are unaffected and keep full access to all Pro features in the unified product. The Community Edition is free and open source and supports basic Python development only.

## 06 Using PyCharm

**Initial setup and project creation**  
**User agreement and import settings**  
The first time you open PyCharm, you need to read and accept the **JETBRAINS USER AGREEMENT** (version effective September 22, 2021), then click Continue to confirm. Next comes the import settings window, where you can choose **Do not import settings** or import a previous configuration file.

**Creating a new project**  
On the welcome screen, choose **New Project** to create a local project from scratch, or use SSH, WSL, or Dev Containers for remote development. After you set the project location, the system automatically creates a `.venv` virtual environment to isolate project dependencies.

**Creating a file and writing code**  
Right-click in the project directory, choose **New** → **Python File**, and name it `1.py`. Type `print('hello world')` in the editor, right-click the file, and choose **Run** to see the output and complete a basic code test.

## 07 Uninstalling PyCharm

**Windows uninstall steps**  
**Open Control Panel**  
Search for **Control Panel** in Windows Settings and open it.

**Go to the program uninstall page**  
In Control Panel, click **Programs** → **Programs and Features** to open the uninstall or change a program page.

**Uninstall PyCharm**  
Find **PyCharm 2024.3.6** in the list (the actual version depends on what you installed), select it, click **Uninstall**, and follow the prompts.

## 08 Chapter summary

Downloading, installing, and uninstalling the Python interpreter

Downloading, installing, using, configuring, and uninstalling PyCharm
