from flask import Flask
import requests


def test_user_authenticate_to_be_201(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 201 STATUS CODE"""

        mock_request_data = {
            'email': 'reidelasns@gmail.com',
            'password': 'br123456789'
        }

        url = 'http://localhost:5000/users/auth'

        response = requests.post(
            url,
            json=mock_request_data
        )

        assert response.status_code == 201


def test_user_authenticate_to_be_401(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH INCORRECT PASSWORD,
        THIS SHOULD RETURN A 401 STATUS CODE"""

        mock_request_data = {
            'email': 'reidelasns@gmail.com',
            'password': '12345678'
        }

        url = 'http://localhost:5000/users/auth'

        response = requests.post(
            url,
            json=mock_request_data
        )
        assert response.status_code == 401
