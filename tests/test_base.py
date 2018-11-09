from app.endpoints import app
import unittest

class TestsStart(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_if_can_get_users(self):
        response = self.app.get('/parcels')
        self.assertEquals(response.status_code,200)
    def test_if_can_get_parcels(self):
        response = self.app.get('/parcels')
        self.assertEquals(response.status_code,200)


if __name__ =="__main__":
    unittest.main()