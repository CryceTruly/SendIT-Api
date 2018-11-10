from app import app
import unittest
import json
import datetime
from app.models import Parcel
from tests import test_base


class TestsParcel(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_create_user(self):
        """
        checks if a user can be created
        """
        expecteduser_obj = {
            "fullname": "John terry",
            "username": "jdoe",
            "phone_number": "0756544544",
            "email": "email@test.com",
            "password": "passwod="

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(
            data['success'], True)
        self.assertEqual(response.status_code, 201)

    def test_cannot_create_a_user_without_email(self):
        """
        checks if cannot create a user who has no email
        """
        expecteduser_obj = {
            "fullname": "John terry",
            "username": "jdoe",
            "phone_number": "0756544544",
            "password": "passwod="

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        # we should get this when a user has no email
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], False)
        self.assertEqual(data['msg'], "Bad request")

    def test_user_cannot_have_someones_email(self):
        users = []
        expecteduser_obj = {
            "fullname": "John terry",
            "username": "jdoe",
            "phone_number": "0756544544",
            "email": "email@test.com",
            "password": "passwod="

        }
        users.append(expecteduser_obj)
        user_obj = {
            "fullname": "John terry",
            "username": "j90e",
            "phone_number": "0756544544",
            "email": "email@test.com",
            "password": "passwod="

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'Email is already taken')
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_user_cannot_have_someones_user_name(self):
        users = []
        expecteduser_obj = {
            "fullname": "John terry",
            "username": "jdoe",
            "phone_number": "0756544544",
            "email": "email@test.com",
            "password": "passwod="

        }
        users.append(expecteduser_obj)
        user_obj = {
            "fullname": "John terry",
            "username": "jdoe",
            "phone_number": "0756544544",
            "email": "fred@test.com",
            "password": "yestpass"

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'Username is already taken')
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)


    def test_user_cannot_have_an_invalid_email(self):
      """
      tests if user supplies a valid email
      """
      user_obj = {
             "fullname":"John terry",
            "username":"jdoe",
            "phone_number": "0756544544",
            "email":"est.com",
            "password":"passwod="

        }
      response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
      data = json.loads(response.data.decode())
      self.assertEqual(data['msg'],'Email is badly formatted')
      self.assertEqual(data['success'],False)
      self.assertEqual(response.status_code, 401)



    def test_get_user_parcels(self):
        """
        checks if a user can get their own parcel request orders
        """
        response = self.client.get(
        "api/v1/users/1/parcels",
        content_type="application/json")
        # we should get an ok
        self.assertEqual(response.status_code, 200)
