# 头条后端（toutiao_backend）

**语言 / Language:** [English](./README.md) | 中文

基于 FastAPI（高性能 Web 框架）的头条类后端练习项目。当前为脚手架阶段：可启动基础路由，目录已按常见分层预留，便于后续扩展业务。

前置练习可参考同仓库 [FastAPI_first](../FastAPI_first)。

## 环境要求

- Python 3.x
- MySQL（后续接入 ORM 时使用；当前示例接口不依赖数据库）
- 建议使用本目录下的虚拟环境（Virtual Environment）

| 包                   | 推荐版本      | 用途                                                       |
|---------------------|-----------|----------------------------------------------------------|
| `fastapi`           | `0.141.1` | Web API（应用程序接口）框架                                        |
| `uvicorn[standard]` | `0.21.1`  | ASGI（异步服务器网关接口）服务器；带 `standard` 额外依赖时 `--reload` 热重载稳定好用 |
| `pydantic`          | `2.13.5`  | 请求 / 响应数据校验                                              |
| `SQLAlchemy`        | `2.0.54`  | ORM（Object-Relational Mapping，对象关系映射）与异步会话               |
| `aiomysql`          | `0.3.2`   | MySQL 异步驱动                                               |

## 安装依赖

在 `toutiao_backend` 目录下执行（Windows PowerShell）：

```bash
# 1. 创建并激活虚拟环境（若已有 .venv 可跳过创建）
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. 安装依赖
pip install -r requirements.txt
```

> 说明：`requirements.txt` 已锁定 `uvicorn[standard]==0.21.1`，请勿只装裸 `uvicorn`，否则热重载等额外能力可能缺失。

## 启动服务

```bash
# 确保已激活 .venv
.\.venv\Scripts\Activate.ps1

# --reload：文件变更后自动重载
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

| 地址                            | 说明               |
|-------------------------------|------------------|
| `http://127.0.0.1:8000`       | 应用根地址            |
| `http://127.0.0.1:8000/docs`  | 交互文档（Swagger UI） |
| `http://127.0.0.1:8000/redoc` | 可选文档（ReDoc）      |

## 项目结构

```text
toutiao_backend/
├── README.md           # 英文说明
├── README.zh.md        # 本说明（中文）
├── requirements.txt    # 依赖版本锁定
├── main.py             # FastAPI 应用入口
├── test_main.http      # HTTP 请求示例（IDE 可直接发送）
├── config/             # 配置（预留）
├── models/             # SQLAlchemy 模型（预留）
├── schemas/            # Pydantic Schema（预留）
├── crud/               # 数据库读写封装（预留）
├── routers/            # 路由模块（预留）
├── utils/              # 工具函数（预留）
└── .venv/              # 本地虚拟环境（可不提交）
```

| 路径                 | 用途                        |
|--------------------|---------------------------|
| `main.py`          | 应用入口与当前示例路由               |
| `requirements.txt` | pip 依赖清单                  |
| `test_main.http`   | 本地快速联调                    |
| `config/`          | 数据库、应用配置等（待实现）            |
| `models/`          | 表结构定义（待实现）                |
| `schemas/`         | 请求 / 响应模型（待实现）            |
| `crud/`            | 增删改查逻辑（待实现）               |
| `routers/`         | 按业务拆分的 API（应用程序接口）路由（待实现） |
| `utils/`           | 公共工具（待实现）                 |

## 当前接口

| 方法  | 路径              | 说明                                      |
|-----|-----------------|-----------------------------------------|
| GET | `/`             | 返回 `{"message": "Hello World"}`         |
| GET | `/hello/{name}` | 路径参数问候，返回 `{"message": "Hello {name}"}` |

## 如何验证

- 启动 `uvicorn` 后打开 `/docs`，在交互文档中试调接口
- 或在 IDE 中打开 `test_main.http` 直接发送请求

不使用自动化单元测试（Unit Test）；以手工联调与交互文档验证为准。
