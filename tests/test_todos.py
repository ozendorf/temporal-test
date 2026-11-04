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
