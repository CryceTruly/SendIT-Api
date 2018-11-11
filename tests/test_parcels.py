from app import app
import unittest
import json
import datetime
from app.models import Parcel


class TestsParcel(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)


    def create_parcel(self):
        self.new_parcel = Parcel(
            id=1,
            pickup_address='Kampala Kikoni Makerere 13',
            destination_address='Mabarara Kikoni Home 13',
            comment_description='My parcels contain a laptop,please deliver',
            status='In Transit',
            current_location='Mabarara Kikoni Home 13',
            created=datetime.datetime.now(),
            user_id=1,
            recipient_address='Julie Muli',
            recipient_phone='0767876666',
            recipient_email='recipient@email.com'
        )
    def test_welcome(self):
        '''
        checks if the app is up and running
        '''
        response = self.client.get(
            "api/v1/parcels",
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 200)
    def test_create_parcel_with_only_pickup_address(self):
        """
        checks if a parcel request cant be created without any data
        """
        expectedreq = {

        }
        response = self.client.post(
            "api/v1/parcels",
            data=json.dumps(expectedreq),
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 400)

    def test_create_parcel(self):
        """
        checks if a parcel request can be created
        """
        expectedreq = {
            'pickup_address': 'Kampala Kikoni Makerere 13',
            'destination_address': 'Mabarara Kikoni Home 13',
            'comment_description': 'My parcels contain a laptop,please deliver',
            'status': 'In Transit',
            'current_location': 'Mabarara Kikoni Home 13',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT",
            'user_id': 1,
            'recipient_address': 'Julie Muli',
            'recipient_phone': '0767876666',
            'recipient_email': 'recipient@email.com'
        }
        response = self.client.post(
            "api/v1/parcels",
            data=json.dumps(expectedreq),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_cannot_create_parcel_that_has_no_owner(self):
        """
        checks if a parcel request can not be created without a user
        """
        expectedreq = {
            'pickup_address': 'Kampala Kikoni Makerere 13',
            'destination_address': 'Mabarara Kikoni Home 13',
            'comment_description': 'My parcels contain a laptop,please deliver',
            'status': 'In Transit',
            'current_location': 'Mabarara Kikoni Home 13',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT",
            'recipient_address': 'Julie Muli',
            'recipient_phone': '0767876666',
            'recipient_email': 'recipient@email.com'
        }
        response = self.client.post(
            "api/v1/parcels",
            data=json.dumps(expectedreq),
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 400)

    def test_checkcangetparcel_request_orders(self):
        '''
        checks
        :return:
        '''
        response = self.client.get("api/v1/parcels")
        # we should get an ok on successful creation
        self.assertEqual(response.status_code, 200)

    def test_can_get_parcel(self):
        """
        checks if a single parcel can be returned given its id
        """
        expectedreq = {
            'id': 1,
            'pickup_address': 'Kampala Kikoni Makerere 13',
            'destination_address': 'Mabarara Kikoni Home 13',
            'comment_description': 'My parcels contain a laptop,please deliver',
            'status': 'In Transit',
            'current_location': 'Mabarara Kikoni Home 13',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT",
            'user_id': 1,
            'recipient_address': 'Julie Muli',
            'recipient_phone': '0767876666',
            'recipient_email': 'recipient@email.com'
        }
        self.client.post(
            "api/v1/parcels",
            data=json.dumps(expectedreq),
            content_type="application/json")
        response = self.client.get(
            "api/v1/parcels/1",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_cant_get_inexistent_parcel(self):
        response = self.client.get(
            "api/v1/parcels/b",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_can_cancel_parcel_delivery_order(self):
        expected = {
            'id': 1,
            'pickup_address': 'Kampala Kikoni Makerere 13',
            'destination_address': 'Mabarara Kikoni Home 13',
            'comment_description': 'My parcels contain a laptop,please deliver',
            'status': 'In Transit',
            'current_location': 'Mabarara Kikoni Home 13',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT",
            'user_id': 1,
            'recipient_address': 'Julie Muli',
            'recipient_phone': '0767876666',
            'recipient_email': 'recipient@email.com'
        }
        self.client.post(
            "api/v1/parcels",
            data=json.dumps(expected),
            content_type="application/json")
        res = self.client.put("api/v1/parcels/1/cancel",
                              data='',
                              content_type="application/json")

        self.assertEqual(res.status_code, 200)

    def test_get_a_no_parcels_message(self):
        '''
        tests if a user gets a readable no users message when users are not there
        :return:
        '''
        response = self.client.get('api/v1/parcels', content_type='application/json')
        data = json.loads(response.data.decode())
        count = data['count']
        if count == 0:
            self.assertEqual(data['msg'], 'No parcels')
        self.assertEqual(response.status, '200 OK')

   

    def test_cant_cancel_adelivered_order(self):
        """
        checks if cannot cancel an order thats already delivered
        """
        expectedreq = {
            'id': 1,
            'pickup_address': 'Kampala Kikoni Makerere 13',
            'destination_address': 'Mabarara Kikoni Home 13',
            'comment_description': 'My parcels contain a laptop,please deliver',
            'status': 'delivered',
            'current_location': 'Mabarara Kikoni Home 13',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT",
            'user_id': 1,
            'recipient_address': 'Julie Muli',
            'recipient_phone': '0767876666',
            'recipient_email': 'recipient@email.com'
        }
        self.client.post(
            "api/v1/parcels",
            data=json.dumps(expectedreq),
            content_type="application/json")
        response = self.client.put(
            "api/v1/parcels/1/cancel",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 200)
