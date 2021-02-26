from flask import Flask
import requests
import json


def test_user_store_to_be_201(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 201 STATUS CODE"""

        mock_request_data = {
            'username': 'pietra',
            'email': 'pietra@gmail.com',
            'role': 'client',
            'password': 'br123456789',
            'password_confirmation': 'br123456789'
        }

        url = 'http://localhost:5000/users'

        response = requests.post(
            url,
            json=mock_request_data
        )

        assert response.status_code == 201


def test_user_store_to_be_401(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, BUT WITH INCORRRECT VALUES,
        THIS SHOULD RETURN A 401 STATUS CODE,
        BECAUSE THE PASSWORD AND THE CONFIRMATION DO NOT MATCH"""

        mock_request_data = {
            'username': 'rafaela',
            'email': 'rafinha@gmail.com',
            'role': 'client',
            'password': 'br123456789',
            'password_confirmation': 'br123'
        }

        url = 'http://localhost:5000/users'

        response = requests.post(
            url,
            json=mock_request_data
        )

        assert response.status_code == 401


def test_user_store_to_be_500(app: Flask):
    with app.app_context():

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES, BUT
        THIS SHOULD RETURN A 500 STATUS CODE,
        BECAUSE CONTAINS NON-UNIQUE EMAIL AND USERNAME"""

        mock_request_data = {
            'username': 'pietra',
            'email': 'pietra@gmail.com',
            'role': 'client',
            'password': 'br123456789',
            'password_confirmation': 'br123456789'
        }

        url = 'http://localhost:5000/users'

        response = requests.post(
            url,
            json=mock_request_data
        )

        assert response.status_code == 500
