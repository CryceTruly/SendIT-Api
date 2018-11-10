from app import app
import unittest
import json
import datetime
from app.models import Parcel
from tests import test_base


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
        response=self.client.get("api/v1/parcels")
        # we should get an ok on successful creation
        self.assertEqual(response.status_code, 200)
    
        

    if __name__ == "__main__":
        unittest.main()
