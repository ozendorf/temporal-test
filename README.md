# temporal-test

A tiny stdlib-only JSON API, used as a playground for the agentic platform.

- `GET /todos` lists todos.
- `POST /todos` with `{"title": "..."}` creates a todo.
- `PATCH /todos/<id>` marks the todo as done (`"done": true`) and returns it; returns 404 `{"error": "todo not found"}` for unknown or non-numeric ids.

Run: `python -m app.server` · Test: `python -m pytest`
