import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from park import *

class TestPark(unittest.TestCase):

    def setUp(self):
        self.park = Park("Jurassic Park", 50)
    
    def test_park_has_name(self):
        self.assertEqual("Jurassic Park", self.park.get_name())

    def test_park_has_ticket_price(self):
        self.assertEqual(50, self.park.get_ticket_price())

    def test_park_created_with_no_dinosaurs(self):
        self.assertEqual(0, self.park.get_number_of_dinosaurs())


if __name__ == "__main__":
    unittest.main() 