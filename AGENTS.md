# 102V_fastAPI

## Quick start

```bash
uv sync              # install dependencies (uses uv.lock)
uv sync --group dev  # include dev deps (ruff)
```

## Commands

```bash
ruff check .         # lint (E, F, I rules, line-length 100)
uv run python -m uvicorn main:app --reload  # dev server
```

## Structure

- `main.py` — FastAPI app entrypoint, `app = FastAPI()`
- `models/` — SQLModel ORM models (`users.py`, `posts.py`)
- No tests, no CI, no Docker yet

## Stack

- Python >=3.10, managed via `uv`
- FastAPI 0.139.2 (standard extras), SQLModel 0.0.39
- `uv.lock` is committed
