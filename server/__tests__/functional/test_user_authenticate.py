from flask import Flask


def test_user_authenticate_to_be_201(app: Flask):
    with app.app_context():
        client = app.test_client()

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 201 STATUS CODE"""

        mock_request_data = {
            'email': 'josethomaz2003@gmail.com',
            'password': '1234567890'
        }

        url = '/users/auth'

        response = client.post(
            url,
            json=mock_request_data
        )
        assert response.status_code == 201


def test_user_authenticate_to_be_401(app: Flask):
    with app.app_context():
        client = app.test_client()

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 201 STATUS CODE"""

        mock_request_data = {
            'email': 'reidelasns@gmail.com',
            'password': 'br123456789'
        }

        url = '/users/auth'

        response = client.post(
            url,
            json=mock_request_data
        )
        assert response.status_code == 401
