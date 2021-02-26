from flask import Flask
import requests
import json


def test_item_update_to_be_200(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 200 STATUS CODE"""

        mock_request_headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE2Mjg4ODkwNzF9.t4esknNLn8ZbAelQ5wDpkUx2MGFZB_sRvULQxnl7p1k',
            'user_id': '4'
        }

        mock_request_data = {
            'name': 'Categoria nova',
            'price': 99,
            'quantity': 12
        }

        url = 'http://localhost:5000/items/1'

        response = requests.put(
            url,
            json=mock_request_data,
            headers=mock_request_headers
        )

        assert response.status_code == 200


def test_item_update_to_be_401(app: Flask):
    with app.app_context():

        """INVALID TOKEN"""

        mock_request_headers = {
            'authorization': 'Bearer'
            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
            '.eyJ1c2VyX2lkIjo0LCJleHAiOjE2Mjg4ODkwNzF9'
            '.t4esknNLn8ZbAelQ5wDpkUx2MGFZB_sRvULQxnl7p1k',
            'user_id': '4'
        }

        mock_request_data = {
            'name': 'Categoria nova',
            'price': 99,
            'quantity': 12
        }

        url = 'http://localhost:5000/items/1'

        response = requests.put(
            url,
            json=mock_request_data,
            headers=mock_request_headers
        )

        assert response.status_code == 401
