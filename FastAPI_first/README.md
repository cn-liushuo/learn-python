# FastAPI Getting Started

**Language / 语言:** English | [中文](./README.zh.md)

This folder is a hands-on FastAPI (high-performance web framework) practice project. Examples live in `main.py` and
cover routing, validation, Request Body, Dependency Injection, Middleware, and async SQLAlchemy ORM (Object-Relational
Mapping).

## Requirements

- Python 3.x
- MySQL (example database name: `FastAPI_first`)
- Prefer the local virtual environment under this directory

| Package             | Recommended version | Role                                                                      |
|---------------------|---------------------|---------------------------------------------------------------------------|
| `fastapi`           | `0.141.1`           | Web API framework                                                         |
| `uvicorn[standard]` | `0.21.1`            | ASGI server; with the `standard` extras, `--reload` hot reload works well |
| `pydantic`          | `2.13.5`            | Request / response validation                                             |
| `SQLAlchemy`        | `2.0.54`            | ORM and async sessions                                                    |
| `aiomysql`          | `0.3.2`             | Async MySQL driver                                                        |

## Install dependencies

From the `FastAPI_first` directory (Windows PowerShell):

```bash
# 1. Create and activate the virtual environment (skip create if .venv already exists)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install uvicorn[standard] (pin 0.21.1 — hot reload works well)
pip uninstall uvicorn -y
pip install "uvicorn[standard]==0.21.1"
pip show uvicorn

# 3. Install the rest (pick one)
pip install -r requirements.txt
# or manually:
# pip install fastapi==0.141.1 pydantic==2.13.5 SQLAlchemy==2.0.54 aiomysql==0.3.2
```

> Note: Use `uvicorn[standard]` (not bare `uvicorn`) so hot-reload extras are installed. `requirements.txt`
> pins `uvicorn[standard]==0.21.1`.

## Run the app

```bash
# Make sure .venv is active
.\.venv\Scripts\Activate.ps1

# --reload: auto-reload on file changes (works well with uvicorn[standard]==0.21.1)
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

| URL                           | Description                   |
|-------------------------------|-------------------------------|
| `http://127.0.0.1:8000`       | App root                      |
| `http://127.0.0.1:8000/docs`  | Interactive docs (Swagger UI) |
| `http://127.0.0.1:8000/redoc` | Alternative docs (ReDoc)      |

Database URL is configured in `main.py` as `ASYNC_DATABASE_URL`. Use your local credentials; **do not put real passwords
in docs or commit them**. Placeholder format:

```text
mysql+aiomysql://USER:PASSWORD@HOST:3306/FastAPI_first?charset=utf8
```

## Project layout

```text
FastAPI_first/
├── README.md              # This file (English)
├── README.zh.md           # Chinese README
├── requirements.txt       # Pinned dependencies
├── main.py                # FastAPI app and learning examples
├── test_main.http         # HTTP request snippets (send from IDE)
├── files/
│   └── photo.jpg          # Image returned by /file
├── .vscode/               # Optional VS Code launch config
└── .venv/                 # Local virtual environment (optional to commit)
```

| Path               | Purpose                                            |
|--------------------|----------------------------------------------------|
| `main.py`          | Routes, middleware, ORM table creation and queries |
| `requirements.txt` | pip dependency list                                |
| `test_main.http`   | Quick local HTTP checks                            |
| `files/`           | Static file sample                                 |

## Learning path (maps to code)

Read the comments and routes in `main.py` by chapter. Alternate styles remain as comments; **the active version is the
uncommented one**.

### 1. Basic routes

| Method | Path         | Description                                       |
|--------|--------------|---------------------------------------------------|
| GET    | `/`          | Returns `{"message": "Hello World"}`              |
| GET    | `/hello`     | Simple JSON: `{"msg": "你好 FastAPI"}`              |
| GET    | `/html`      | `HTMLResponse` with an HTML snippet               |
| GET    | `/file`      | `FileResponse` for `files/photo.jpg`              |
| GET    | `/news/{id}` | Only ids in [1, 6]; otherwise `HTTPException` 404 |

### 2. Path and Query parameters

Path params use `Path` for range / length checks. Pagination-related Query params are covered in sections 4 and 6.

| Method | Path             | Description                           |
|--------|------------------|---------------------------------------|
| GET    | `/book/{id}`     | `Path`: `id` in `(0, 101)` → [1, 100] |
| GET    | `/author/{name}` | `Path`: `name` length [2, 10]         |

### 3. Body (request body)

Validate the request body with a Pydantic `BaseModel` + `Field`.

| Method | Path        | Description                                              |
|--------|-------------|----------------------------------------------------------|
| POST   | `/register` | Body: `User` (`username`, `password` length constraints) |

| Field      | Constraint                     |
|------------|--------------------------------|
| `username` | Default `"张三"`, length [2, 10] |
| `password` | Length [3, 20]                 |

### 4. Depends and Middleware

**Depends**: reuse pagination params and the DB session.

| Method | Path              | Description                                       |
|--------|-------------------|---------------------------------------------------|
| GET    | `/news/news_list` | `Depends(common_parameters)` → `{skip, limit}`    |
| GET    | `/user/user_list` | Same pagination dependency                        |
| —      | `get_database`    | Async session dependency for `/book/*` ORM routes |

`common_parameters`: `skip >= 0`; `limit` defaults to 10 and is `<= 60`.

**Middleware**: `middleware1` and `middleware2` log before/after the request. Later-registered middleware runs first (
outside-in).

### 5. ORM

On startup (`@app.on_event("startup")`), `create_tables()` creates tables from the `Book` model.

| Model / component   | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| `Base`              | Shared fields: `create_time`, `update_time`                       |
| `Book`              | Table `book`: `id`, `book_name`, `author`, `price`, `publisher`   |
| `AsyncSessionLocal` | `async_sessionmaker` factory                                      |
| `get_database`      | `yield` session; commit on success, rollback on error, then close |

### 6. Queries (database operations)

Core pattern: `await db.execute(select(...))`; use `scalars()` / `scalar()` / `get()` for results.

| Method | Path                       | Active logic                                                                                             |
|--------|----------------------------|----------------------------------------------------------------------------------------------------------|
| GET    | `/book/books`              | `db.get(Book, 3)` by primary key                                                                         |
| GET    | `/book/get_book/{book_id}` | `where(Book.id == book_id)`, `scalar_one_or_none()`                                                      |
| GET    | `/book/search_book`        | `Book.id.in_([1, 3, 5, 7])`                                                                              |
| GET    | `/book/count`              | Aggregate `func.avg(Book.price)`                                                                         |
| GET    | `/books/get_books`         | Query: `page` (default 1), `page_size` (default 2); `offset=(page-1)*page_size` then `.limit(page_size)` |

Commented samples also cover `like`, logical `|`, and `count` / `max` / `sum` for comparison.

## How to verify

- Start `uvicorn`, open `/docs`, and try endpoints by chapter
- Or use `test_main.http` / a browser against the paths above

No automated unit tests; use manual checks and the interactive docs.
