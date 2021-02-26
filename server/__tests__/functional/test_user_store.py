from flask import Flask


def test_user_store_to_be_201(app: Flask):
    with app.app_context():
        client = app.test_client()

        """SENDING ALL NEEDED DATA, WITH CORRRECT VALUES,
        THIS SHOULD RETURN A 201 STATUS CODE"""

        mock_request_data = {
            'username': 'joaoozinn_reidelas',
            'email': 'reidelasns@gmail.com',
            'role': 'client',
            'password': 'br123456789',
            'password_confirmation': 'br123456789'
        }

        url = '/users'

        response = client.post(
            url,
            json=mock_request_data
        )
        assert response.status_code == 201
