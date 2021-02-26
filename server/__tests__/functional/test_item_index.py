from flask import Flask


def test_item_index_to_be_401(app: Flask):
    client = app.test_client()

    mock_request_headers = {
        'authorization': 'Bearer ghssgshs'
    }

    """NOT SENDING A VALID TOKEN, SO THIS WILL FAIL ON THE AUTH DECORATOR"""

    url = '/items'
    assert client.get(url, headers=mock_request_headers).status_code == 401


def test_item_index_to_be_200(app: Flask):
    client = app.test_client()

    mock_request_headers = {
        'authorization': 'Bearer '
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
        'eyJ1c2VyX2lkIjoyLCJleHAiOjE2Mjg4MTk3NTZ9.'
        'hZGPe1P2QSDhCNDyTifrsJrcAGiwqR8FmHvVsYfQ0z4',
    }

    """SENDING THE CORRECT TOKEN,
    SO THIS WILL NOT FAIL ON THE AUTH DECORATOR"""

    url = '/items'
    assert client.get(url, headers=mock_request_headers).status_code == 200


def test_item_index_to_be_404(app: Flask):
    client = app.test_client()

    mock_request_headers = {
        'authorization': 'Bearer '
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
        'eyJ1c2VyX2lkIjoyLCJleHAiOjE2Mjg4MTk3NTZ9.'
        'hZGPe1P2QSDhCNDyTifrsJrcAGiwqR8FmHvVsYfQ0z4',
        'user_id': 1
    }

    """SENDING AN INVALID URL"""

    url = '/itemss'
    assert client.get(url, headers=mock_request_headers).status_code == 404
