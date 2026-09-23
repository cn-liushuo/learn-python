# FastAPI 入门练习

**语言 / Language:** [English](./README.md) | 中文

本目录用于 FastAPI（高性能 Web 框架）入门学习。示例集中在 `main.py`，覆盖路由、参数校验、请求体（Request Body）、依赖注入（Dependency
Injection）、中间件（Middleware）、以及 SQLAlchemy 异步 ORM（Object-Relational Mapping，对象关系映射）。

## 环境要求

- Python 3.x
- MySQL（示例库名：`FastAPI_first`）
- 建议使用本目录下的虚拟环境（Virtual Environment，虚拟环境）

| 包            | 用途                       |
|--------------|--------------------------|
| `fastapi`    | Web API（应用程序接口）框架        |
| `uvicorn`    | ASGI（异步服务器网关接口）服务器       |
| `pydantic`   | 请求 / 响应数据校验              |
| `SQLAlchemy` | ORM 与异步会话（Async Session） |
| `aiomysql`   | MySQL 异步驱动               |

激活环境并启动：

```bash
# Windows PowerShell（在 FastAPI_first 目录执行）
.\.venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

| 地址                            | 说明               |
|-------------------------------|------------------|
| `http://127.0.0.1:8000`       | 应用根地址            |
| `http://127.0.0.1:8000/docs`  | 交互文档（Swagger UI） |
| `http://127.0.0.1:8000/redoc` | 可选文档（ReDoc）      |

数据库连接在 `main.py` 的 `ASYNC_DATABASE_URL` 中配置。请使用本机账号，**勿把真实密码写入文档或提交到版本库**。占位格式示例：

```text
mysql+aiomysql://USER:PASSWORD@HOST:3306/FastAPI_first?charset=utf8
```

## 项目结构

```text
FastAPI_first/
├── README.md              # 英文说明
├── README.zh.md           # 本说明（中文）
├── main.py                # FastAPI 应用与学习示例
├── test_main.http         # HTTP 请求示例（IDE 可直接发送）
├── files/
│   └── photo.jpg          # /file 接口返回的静态图片
├── .vscode/               # VS Code 启动配置（可选）
└── .venv/                 # 本地虚拟环境（可不提交）
```

| 路径               | 用途                   |
|------------------|----------------------|
| `main.py`        | 全部路由、中间件、ORM 建表与查询示例 |
| `test_main.http` | 本地快速联调               |
| `files/`         | 静态文件示例               |

## 学习路径（与代码对应）

建议按下列章节阅读 `main.py` 中的注释与路由。部分备选写法以注释保留，**当前生效的是未注释的那一版**。

---

### 1. 基础路由

最简单的 `GET` 响应，以及 HTML / 文件 / 异常示例。

| 方法  | 路径           | 说明                                     |
|-----|--------------|----------------------------------------|
| GET | `/`          | 返回 `{"message": "Hello World"}`        |
| GET | `/hello`     | 返回简单 JSON：`{"msg": "你好 FastAPI"}`      |
| GET | `/html`      | `HTMLResponse`，返回 HTML 片段              |
| GET | `/file`      | `FileResponse`，返回 `files/photo.jpg`    |
| GET | `/news/{id}` | 仅允许 id ∈ [1, 6]；否则 `HTTPException` 404 |

---

### 2. Path（路径参数）与 Query（查询参数）

路径参数用 `Path` 做范围 / 长度校验；分页相关 Query 见第 4、6 节。

| 方法  | 路径               | 说明                                     |
|-----|------------------|----------------------------------------|
| GET | `/book/{id}`     | `Path`：`id` 取值范围 `(0, 101)`，即 [1, 100] |
| GET | `/author/{name}` | `Path`：`name` 长度 [2, 10]               |

---

### 3. Body（请求体）

使用 Pydantic `BaseModel` + `Field` 校验请求体。

| 方法   | 路径          | 说明                                      |
|------|-------------|-----------------------------------------|
| POST | `/register` | Body：`User`（`username`、`password` 长度约束） |

示例字段约束（与代码一致）：

| 字段         | 约束                   |
|------------|----------------------|
| `username` | 默认 `"张三"`，长度 [2, 10] |
| `password` | 长度 [3, 20]           |

---

### 4. Depends（依赖注入）与 Middleware（中间件）

**Depends**：复用分页参数与数据库会话。

| 方法  | 路径                | 说明                                             |
|-----|-------------------|------------------------------------------------|
| GET | `/news/news_list` | `Depends(common_parameters)` → `{skip, limit}` |
| GET | `/user/user_list` | 复用同一分页依赖                                       |
| —   | `get_database`    | 异步会话依赖，注入到 `/book/*` 等 ORM 路由                  |

`common_parameters` 约束：`skip >= 0`；`limit` 默认 10，且 `<= 60`。

**Middleware**：两个 HTTP 中间件（`middleware1`、`middleware2`）打印请求前后日志。注册顺序靠后的先执行（由外向内）。

---

### 5. ORM（对象关系映射）

启动时（`@app.on_event("startup")`）调用 `create_tables()`，按 `Book` 模型建表。

| 模型 / 组件             | 说明                                                      |
|---------------------|---------------------------------------------------------|
| `Base`              | 公共字段：`create_time`、`update_time`                        |
| `Book`              | 表名 `book`：`id`、`book_name`、`author`、`price`、`publisher` |
| `AsyncSessionLocal` | `async_sessionmaker` 会话工厂                               |
| `get_database`      | `yield` 会话；成功提交，异常回滚，最后关闭                               |

---

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
