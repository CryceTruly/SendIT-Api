import unittest
from app.endpoints import app

class FlaskTestCase(unittest.TestCase):
    #Ensure that flask was setup correctly
    def test_set_up(self):
        tester=app.test_client(self)
        response=tester.get('/parcels',content_type="application/json")
        self.assertEqual(response.status_code,200)


if __name__=="__main__":
    unittest.main()