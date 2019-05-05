import json
from unittest import TestCase
from test_helpers.helpers import wipe_database
from main import app
from infrastructure.redis import db


class TestRegister(TestCase):
    def setUp(self):
        wipe_database(db)

    def test_registration(self):
        # given
        data = {'email': 'email@wp.pl', 'password': '123'}
        # when
        request, response = app.test_client.post("/auth/register", data=json.dumps(data))

        # then
        assert response.status == 200

    def test_getting_me_data(self):
        data = {'email': 'email@wp.pl', 'password': '123'}
        # when
        request, response = app.test_client.post("/auth/register", data=json.dumps(data))
        token = response.json["jwt"]

        # sending without token should return 401
        request, response = app.test_client.get("/auth/me")
        assert response.status == 401

        # sending with header
        request, response = app.test_client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert response.status == 200
