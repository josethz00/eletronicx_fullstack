from flask import Flask


def test_invalid_url(app: Flask):
    client = app.test_client()
    url = '/invalid_url'
    assert client.get(url).status_code == 404
