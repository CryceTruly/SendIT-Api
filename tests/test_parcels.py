from app.endpoints import app
import unittest

class TestsParcel(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_creating_a_parcel(self):
        """
        Test that a user can add a parcel
        :return:
        """




if __name__ =="__main__":
    unittest.main()