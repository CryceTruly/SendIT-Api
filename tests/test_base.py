from app import app
import unittest
import json


class TestsStart(unittest.TestCase):

    def setUp(self):
         self.app = app.test_client()
        
       
    
    def test_if_can_get_users(self):

        response = self.app.get('api/v1/users')
        self.assertEqual(response.status_code, 200)


    def test_if_can_get_parcels(self):
        response = self.app.get('api/v1/parcels')
        self.assertEqual(response.status_code, 200)

    def test_request_not_json(self):
        """ Test order content to be posted not in json format """
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
        result = self.app.post(
            '/api/v1/parcels',
            content_type = 'text/html',
            data=json.dumps(expectedreq)
        )
        self.assertEqual(result.status_code,401)
        self.assertIn('Content-type must be application/json',str(result.data))

if __name__ == "__main__":
    unittest.main()
