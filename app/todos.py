"""In-memory todo store."""
from __future__ import annotations

_TODOS: list[dict] = []


def reset() -> None:
    _TODOS.clear()


def list_todos() -> list[dict]:
    return list(_TODOS)


def create_todo(body: dict) -> tuple[int, dict]:
    title = str(body.get("title", "")).strip()
    if not title:
        return 400, {"error": "title is required"}
    todo = {"id": len(_TODOS) + 1, "title": title, "done": False}
    _TODOS.append(todo)
    return 201, todo


def mark_done(todo_id: str) -> tuple[int, dict]:
    # isascii() guards against non-ASCII digits (e.g. "²") that isdigit() accepts but int() rejects.
    if not (todo_id.isascii() and todo_id.isdigit()):
        return 404, {"error": "todo not found"}
    n = int(todo_id)
    for todo in _TODOS:
        if todo["id"] == n:
            todo["done"] = True
            return 200, todo
    return 404, {"error": "todo not found"}
