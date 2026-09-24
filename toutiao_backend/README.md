# Toutiao Backend (toutiao_backend)

**Language / 语言:** English | [中文](./README.zh.md)

A FastAPI (high-performance web framework) practice project modeled after a Toutiao-style news backend. This is still a
scaffold: basic routes run, and the usual layered folders are reserved for later features.

For the prerequisite FastAPI exercises, see [FastAPI_first](../FastAPI_first) in the same repository.

## Requirements

- Python 3.x
- MySQL (for upcoming ORM work; current sample routes do not need a database)
- Prefer the local virtual environment under this directory

| Package             | Recommended version | Role                                                                      |
|---------------------|---------------------|---------------------------------------------------------------------------|
| `fastapi`           | `0.141.1`           | Web API framework                                                         |
| `uvicorn[standard]` | `0.21.1`            | ASGI server; with the `standard` extras, `--reload` hot reload works well |
| `pydantic`          | `2.13.5`            | Request / response validation                                             |
| `SQLAlchemy`        | `2.0.54`            | ORM and async sessions                                                    |
| `aiomysql`          | `0.3.2`             | Async MySQL driver                                                        |

## Install dependencies

From the `toutiao_backend` directory (Windows PowerShell):

```bash
# 1. Create and activate the virtual environment (skip create if .venv already exists)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt
```

> Note: `requirements.txt` pins `uvicorn[standard]==0.21.1`. Do not install bare `uvicorn` alone, or hot-reload extras
> may be missing.

## Run the app

```bash
# Make sure .venv is active
.\.venv\Scripts\Activate.ps1

# --reload: auto-reload on file changes
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

| URL                           | Description                   |
|-------------------------------|-------------------------------|
| `http://127.0.0.1:8000`       | App root                      |
| `http://127.0.0.1:8000/docs`  | Interactive docs (Swagger UI) |
| `http://127.0.0.1:8000/redoc` | Alternative docs (ReDoc)      |

## Project layout

```text
toutiao_backend/
├── README.md           # This file (English)
├── README.zh.md        # Chinese README
├── requirements.txt    # Pinned dependencies
├── main.py             # FastAPI app entry
├── test_main.http      # HTTP request snippets (send from IDE)
├── config/             # Configuration (reserved)
├── models/             # SQLAlchemy models (reserved)
├── schemas/            # Pydantic schemas (reserved)
├── crud/               # Database access helpers (reserved)
├── routers/            # Route modules (reserved)
├── utils/              # Utilities (reserved)
└── .venv/              # Local virtual environment (optional to commit)
```

| Path               | Purpose                                             |
|--------------------|-----------------------------------------------------|
| `main.py`          | App entry and current sample routes                 |
| `requirements.txt` | pip dependency list                                 |
| `test_main.http`   | Quick local HTTP checks                             |
| `config/`          | App / database settings (to be implemented)         |
| `models/`          | Table definitions (to be implemented)               |
| `schemas/`         | Request / response models (to be implemented)       |
| `crud/`            | Create / read / update / delete (to be implemented) |
| `routers/`         | Business API routers (to be implemented)            |
| `utils/`           | Shared helpers (to be implemented)                  |

## Current endpoints

| Method | Path            | Description                                        |
|--------|-----------------|----------------------------------------------------|
| GET    | `/`             | Returns `{"message": "Hello World"}`               |
| GET    | `/hello/{name}` | Path-param greeting: `{"message": "Hello {name}"}` |

## How to verify

- Start `uvicorn`, open `/docs`, and try the endpoints
- Or send requests from `test_main.http` in the IDE

No automated unit tests; use manual checks and the interactive docs.
