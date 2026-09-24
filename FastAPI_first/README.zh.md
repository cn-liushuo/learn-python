# FastAPI 入门练习

**语言 / Language:** [English](./README.md) | 中文

本目录用于 FastAPI（高性能 Web 框架）入门学习。示例集中在 `main.py`，覆盖路由、参数校验、请求体（Request Body）、依赖注入（Dependency
Injection）、中间件（Middleware）、以及 SQLAlchemy 异步 ORM（Object-Relational Mapping，对象关系映射）。

## 环境要求

- Python 3.x
- MySQL（示例库名：`FastAPI_first`）
- 建议使用本目录下的虚拟环境（Virtual Environment）

| 包                   | 推荐版本      | 用途                                                       |
|---------------------|-----------|----------------------------------------------------------|
| `fastapi`           | `0.141.1` | Web API（应用程序接口）框架                                        |
| `uvicorn[standard]` | `0.21.1`  | ASGI（异步服务器网关接口）服务器；带 `standard` 额外依赖时 `--reload` 热重载稳定好用 |
| `pydantic`          | `2.13.5`  | 请求 / 响应数据校验                                              |
| `SQLAlchemy`        | `2.0.54`  | ORM 与异步会话（Async Session）                                 |
| `aiomysql`          | `0.3.2`   | MySQL 异步驱动                                               |

## 安装依赖

在 `FastAPI_first` 目录下执行（Windows PowerShell）：

```bash
# 1. 创建并激活虚拟环境（若已有 .venv 可跳过创建）
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. 安装 uvicorn[standard]（推荐固定 0.21.1，热重载好用）
pip uninstall uvicorn -y
pip install "uvicorn[standard]==0.21.1"
pip show uvicorn

# 3. 安装其余依赖（任选其一）
pip install -r requirements.txt
# 或手动安装：
# pip install fastapi==0.141.1 pydantic==2.13.5 SQLAlchemy==2.0.54 aiomysql==0.3.2
```

> 说明：必须使用 `uvicorn[standard]`（不要只装裸 `uvicorn`），才会带上热重载等常用额外依赖。`requirements.txt`
> 已写为 `uvicorn[standard]==0.21.1`。

## 启动服务

```bash
# 确保已激活 .venv
.\.venv\Scripts\Activate.ps1

# --reload：文件变更后自动重载（uvicorn[standard]==0.21.1 表现良好）
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

| 地址                            | 说明               |
|-------------------------------|------------------|
| `http://127.0.0.1:8000`       | 应用根地址            |
| `http://127.0.0.1:8000/docs`  | 交互文档（Swagger UI） |
| `http://127.0.0.1:8000/redoc` | 可选文档（ReDoc）      |

数据库连接在 `main.py` 的 `ASYNC_DATABASE_URL` 中配置。请使用本机账号，**勿把真实密码写入文档或提交到版本库**。占位格式：

```text
mysql+aiomysql://USER:PASSWORD@HOST:3306/FastAPI_first?charset=utf8
```

## 项目结构

```text
FastAPI_first/
├── README.md              # 英文说明
├── README.zh.md           # 本说明（中文）
├── requirements.txt       # 依赖版本锁定
├── main.py                # FastAPI 应用与学习示例
├── test_main.http         # HTTP 请求示例（IDE 可直接发送）
├── files/
│   └── photo.jpg          # /file 接口返回的静态图片
├── .vscode/               # VS Code 启动配置（可选）
└── .venv/                 # 本地虚拟环境（可不提交）
```

| 路径                 | 用途                   |
|--------------------|----------------------|
| `main.py`          | 全部路由、中间件、ORM 建表与查询示例 |
| `requirements.txt` | pip 依赖清单             |
| `test_main.http`   | 本地快速联调               |
| `files/`           | 静态文件示例               |

## 学习路径（与代码对应）

建议按下列章节阅读 `main.py` 中的注释与路由。部分备选写法以注释保留，**当前生效的是未注释的那一版**。

### 1. 基础路由

| 方法  | 路径           | 说明                                     |
|-----|--------------|----------------------------------------|
| GET | `/`          | 返回 `{"message": "Hello World"}`        |
| GET | `/hello`     | 返回简单 JSON：`{"msg": "你好 FastAPI"}`      |
| GET | `/html`      | `HTMLResponse`，返回 HTML 片段              |
| GET | `/file`      | `FileResponse`，返回 `files/photo.jpg`    |
| GET | `/news/{id}` | 仅允许 id ∈ [1, 6]；否则 `HTTPException` 404 |

### 2. Path（路径参数）与 Query（查询参数）

路径参数用 `Path` 做范围 / 长度校验；分页相关 Query 见第 4、6 节。

| 方法  | 路径               | 说明                                     |
|-----|------------------|----------------------------------------|
| GET | `/book/{id}`     | `Path`：`id` 取值范围 `(0, 101)`，即 [1, 100] |
| GET | `/author/{name}` | `Path`：`name` 长度 [2, 10]               |

### 3. Body（请求体）

使用 Pydantic `BaseModel` + `Field` 校验请求体。

| 方法   | 路径          | 说明                                      |
|------|-------------|-----------------------------------------|
| POST | `/register` | Body：`User`（`username`、`password` 长度约束） |

| 字段         | 约束                   |
|------------|----------------------|
| `username` | 默认 `"张三"`，长度 [2, 10] |
| `password` | 长度 [3, 20]           |

### 4. Depends（依赖注入）与 Middleware（中间件）

**Depends**：复用分页参数与数据库会话。

| 方法  | 路径                | 说明                                             |
|-----|-------------------|------------------------------------------------|
| GET | `/news/news_list` | `Depends(common_parameters)` → `{skip, limit}` |
| GET | `/user/user_list` | 复用同一分页依赖                                       |
| —   | `get_database`    | 异步会话依赖，注入到 `/book/*` 等 ORM 路由                  |

`common_parameters`：`skip >= 0`；`limit` 默认 10，且 `<= 60`。

**Middleware**：`middleware1`、`middleware2` 打印请求前后日志；注册顺序靠后的先执行（由外向内）。

### 5. ORM（对象关系映射）

启动时（`@app.on_event("startup")`）调用 `create_tables()`，按 `Book` 模型建表。

| 模型 / 组件             | 说明                                                      |
|---------------------|---------------------------------------------------------|
| `Base`              | 公共字段：`create_time`、`update_time`                        |
| `Book`              | 表名 `book`：`id`、`book_name`、`author`、`price`、`publisher` |
| `AsyncSessionLocal` | `async_sessionmaker` 会话工厂                               |
| `get_database`      | `yield` 会话；成功提交，异常回滚，最后关闭                               |

### 6. 查询（数据库操作）

核心写法：`await db.execute(select(...))`；标量用 `scalars()` / `scalar()` / `get()`。

| 方法  | 路径                         | 当前生效逻辑                                                                                 |
|-----|----------------------------|----------------------------------------------------------------------------------------|
| GET | `/book/books`              | `db.get(Book, 3)` 按主键取一条                                                               |
| GET | `/book/get_book/{book_id}` | `where(Book.id == book_id)`，`scalar_one_or_none()`                                     |
| GET | `/book/search_book`        | `Book.id.in_([1, 3, 5, 7])`                                                            |
| GET | `/book/count`              | `func.avg(Book.price)` 聚合                                                              |
| GET | `/books/get_books`         | Query：`page`（默认 1）、`page_size`（默认 2）；`offset=(page-1)*page_size` 后 `.limit(page_size)` |

源码注释中还保留了 `like`、逻辑或 `|`、`count` / `max` / `sum` 等写法，便于对照学习。

## 验证方式

- 启动 `uvicorn` 后访问 `/docs`，按章节逐个试调
- 或使用 `test_main.http` / 浏览器访问上述路径

未提供自动化单元测试（Unit Test）；以手工联调与交互文档为准。
