from flask import Flask
import requests
import json


def test_user_update_to_be_200(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 200 STATUS CODE"""

        mock_request_headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE2Mjg4ODkwNzF9.t4esknNLn8ZbAelQ5wDpkUx2MGFZB_sRvULQxnl7p1k'
        }

        mock_request_data = {
            'username': 'lenda_do_tdd',
        }

        url = 'http://localhost:5000/users/4'

        response = requests.put(
            url,
            json=mock_request_data,
            headers=mock_request_headers
        )

        assert response.status_code == 200


def test_user_update_to_be_401(app: Flask):
    with app.app_context():

        """INVALID TOKEN"""

        mock_request_headers = {
            'authorization': 'Bearer'
            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
            '.eyJ1c2VyX2lkIjo0LCJleHAiOjE2Mjg4ODkwNzF9'
            '.t4esknNLn8ZbAelQ5wDpkUx2MGFZB_sRvULQxnl7p1k'
        }

        mock_request_data = {
            'username': 'rafaela'
        }

        url = 'http://localhost:5000/users/4'

        response = requests.put(
            url,
            json=mock_request_data,
            headers=mock_request_headers
        )

        assert response.status_code == 401


def test_user_update_to_be_404(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        BUT THIS SHOULD RETURN A 404 STATUS CODE,
        BECAUSE THE ID PROVIDED DOES NOT EXISTS"""

        mock_request_headers = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE2Mjg4ODkwNzF9.t4esknNLn8ZbAelQ5wDpkUx2MGFZB_sRvULQxnl7p1k'
        }

        mock_request_data = {
            'username': 'lenda_do_tdd',
        }

        url = 'http://localhost:5000/users/90'

        response = requests.put(
            url,
            json=mock_request_data,
            headers=mock_request_headers
        )

        assert response.status_code == 404
