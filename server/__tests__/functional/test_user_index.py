from flask import Flask


def test_category_index_to_be_500(app: Flask):
    client = app.test_client()

    mock_request_headers = {
        'authorization': 'Bearer '
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
        'eyJ1c2VyX2lkIjoyLCJleHAiOjE2Mjg4MTk3NTZ9.'
        'hZGPe1P2QSDhCNDyTifrsJrcAGiwqR8FmHvVsYfQ0z4'
    }

    """NOT SENDING THE USER_ID, SO THIS WILL FAIL ON THE ROLE_DECORATOR"""

    url = '/users'
    assert client.get(url, headers=mock_request_headers).status_code == 500


def test_category_index_to_be_200(app: Flask):
    client = app.test_client()

    mock_request_headers = {
        'authorization': 'Bearer '
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
        'eyJ1c2VyX2lkIjoyLCJleHAiOjE2Mjg4MTk3NTZ9.'
        'hZGPe1P2QSDhCNDyTifrsJrcAGiwqR8FmHvVsYfQ0z4',
        'user_id': 2
    }

    """SENDING THE USER_ID, SO THIS WILL NOT FAIL ON THE ROLE_DECORATOR"""

    url = '/users'
    assert client.get(url, headers=mock_request_headers).status_code == 200


def test_category_index_to_be_404(app: Flask):
    client = app.test_client()

    mock_request_headers = {
        'authorization': 'Bearer '
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
        'eyJ1c2VyX2lkIjoyLCJleHAiOjE2Mjg4MTk3NTZ9.'
        'hZGPe1P2QSDhCNDyTifrsJrcAGiwqR8FmHvVsYfQ0z4',
        'user_id': 90
    }

    """SENDING THE AN NONEXISTENT USER_ID,
    SO THIS WILL FAIL ON THE ROLE_DECORATOR, RETURNING A 404 CODE"""

    url = '/users'
    assert client.get(url, headers=mock_request_headers).status_code == 404
