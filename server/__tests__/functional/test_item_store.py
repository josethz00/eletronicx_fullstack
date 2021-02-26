from flask import Flask, jsonify
import json


def test_item_store_to_be_201(app: Flask):
    with app.app_context():
        client = app.test_client()

        mock_request_headers = {
            'authorization': 'Bearer '
            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
            'eyJ1c2VyX2lkIjoyLCJleHAiOjE2Mjg4MTk3NTZ9.'
            'hZGPe1P2QSDhCNDyTifrsJrcAGiwqR8FmHvVsYfQ0z4',
            'user_id': 1
        }

        mock_request_data = {
            'name': 'Rádio AM',
            'price': 90.99,
            'quantity': 20,
            'category_id': 1
        }

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 201 STATUS CODE"""

        url = '/items'

        response = client.post(
            url,
            data=mock_request_data,
            headers=mock_request_headers
        )
        assert response.status_code == 201


def test_item_store_to_be_401(app: Flask):
    with app.app_context():
        client = app.test_client()

        mock_request_headers = {
            'user_id': 1
        }

        mock_request_data = {
            'name': 'Rádio AM',
            'price': 90.99,
            'quantity': 20,
            'category_id': 1
        }

        """NOT SENDING HEADERS OF AUTHORIZATION"""

        url = '/items'

        response = client.post(
            url,
            json=mock_request_data,
            headers=mock_request_headers
        )
        assert response.status_code == 401
