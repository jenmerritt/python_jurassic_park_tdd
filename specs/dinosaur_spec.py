import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from dinosaur import *

class TestDinosaur(unittest.TestCase):

    def setUp(self):
        self.raptor = Dinosaur("Raptor", "Omnivore", 300)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)

    def test_dinosaur_has_species(self):
        self.assertEqual("Raptor", self.raptor.get_species())

    def test_dinosaur_has_diet(self):
        self.assertEqual("Omnivore", self.raptor.get_diet())

    def test_dinosaur_has_average_daily_visitors(self):
        self.assertEqual(300, self.raptor.get_daily_visitors())

if __name__ == "__main__":
    unittest.main() 
