def test_health_empty_store(client):
    assert client("GET", "/health") == (200, {"status": "ok", "todos": 0})


def test_health_after_one_todo(client):
    assert client("POST", "/todos", {"title": "write tests"})[0] == 201
    assert client("GET", "/health") == (200, {"status": "ok", "todos": 1})
