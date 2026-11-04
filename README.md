# temporal-test

A tiny stdlib-only JSON API, used as a playground for the agentic platform.

- `GET /todos` lists todos.
- `POST /todos` with `{"title": "..."}` creates a todo.
- `GET /health` returns `{"status": "ok", "todos": <count>}`.

Run: `python -m app.server` · Test: `python -m pytest`
