def test_list_starts_empty(client):
    assert client("GET", "/todos") == (200, [])


def test_create_and_list(client):
    status, todo = client("POST", "/todos", {"title": "write tests"})
    assert status == 201 and todo == {"id": 1, "title": "write tests", "done": False}
    assert client("GET", "/todos") == (200, [todo])


def test_create_requires_title(client):
    assert client("POST", "/todos", {"title": " "}) == (400, {"error": "title is required"})


def test_unknown_route(client):
    assert client("GET", "/nope")[0] == 404


def test_mark_done(client):
    client("POST", "/todos", {"title": "a"})
    assert client("PATCH", "/todos/1") == (200, {"id": 1, "title": "a", "done": True})
    assert client("GET", "/todos") == (200, [{"id": 1, "title": "a", "done": True}])


def test_mark_done_unknown_id(client):
    assert client("PATCH", "/todos/99") == (404, {"error": "todo not found"})


def test_mark_done_non_numeric_id(client):
    assert client("PATCH", "/todos/abc") == (404, {"error": "todo not found"})
