"""A tiny JSON HTTP API built on the standard library (no dependencies)."""
from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Callable

from . import todos

Handler = Callable[[dict | None], tuple[int, object]]

# (method, path) -> handler. Add new endpoints here.
ROUTES: dict[tuple[str, str], Handler] = {
    ("GET", "/todos"): lambda _body: (200, todos.list_todos()),
    ("POST", "/todos"): lambda body: todos.create_todo(body or {}),
}


class RequestHandler(BaseHTTPRequestHandler):
    def _dispatch(self, method: str) -> None:
        handler = ROUTES.get((method, self.path))
        if handler is None:
            return self._send(404, {"error": "not found"})
        body = None
        length = int(self.headers.get("Content-Length") or 0)
        if length:
            try:
                body = json.loads(self.rfile.read(length))
            except json.JSONDecodeError:
                return self._send(400, {"error": "invalid JSON"})
        status, payload = handler(body)
        self._send(status, payload)

    def do_GET(self) -> None:  # noqa: N802
        self._dispatch("GET")

    def do_POST(self) -> None:  # noqa: N802
        self._dispatch("POST")

    def _send(self, status: int, payload: object) -> None:
        data = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args: object) -> None:  # keep test output quiet
        pass


def make_server(port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(("127.0.0.1", port), RequestHandler)


if __name__ == "__main__":
    srv = make_server()
    print("listening on http://127.0.0.1:8000")
    srv.serve_forever()
