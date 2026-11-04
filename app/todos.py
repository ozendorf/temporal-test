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
