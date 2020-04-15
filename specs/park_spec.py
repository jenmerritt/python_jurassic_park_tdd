import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from park import *
from dinosaur import *

class TestPark(unittest.TestCase):

    def setUp(self):
        self.park = Park("Jurassic Park", 50)

    def test_park_has_name(self):
        self.assertEqual("Jurassic Park", self.park.get_name())

    def test_park_has_ticket_price(self):
        self.assertEqual(50, self.park.get_ticket_price())

    def test_park_created_with_no_dinosaurs(self):
        self.assertEqual(0, self.park.get_number_of_dinosaurs())
    
    def test_can_add_dinosaur_to_park(self):
        dinosaur = Dinosaur("Raptor", "Omnivore", 300)
        self.park.add_dinosaur(dinosaur)
        self.assertEqual(1, self.park.get_number_of_dinosaurs())
    
    def test_can_remove_dinosaur_from_park(self):
        dinosaur = Dinosaur("Pterosaur", "Carnivore", 250)
        self.park.add_dinosaur(dinosaur)
        self.park.add_dinosaur(dinosaur)
        self.park.remove_dinosaur(dinosaur)
        self.assertEqual(1, self.park.get_number_of_dinosaurs())
    
    def test_can_find_most_popular_dinosaur(self):
        self.pterosaur = Dinosaur("Pterosaur", "Carnivore", 200)
        self.raptor = Dinosaur("Raptor", "Omnivore", 300)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)
        self.park.add_dinosaur(self.pterosaur)
        self.park.add_dinosaur(self.bronty)
        self.park.add_dinosaur(self.raptor)
        self.assertEqual(self.raptor, self.park.get_most_popular_dinosaur())
    
    def test_can_get_all_dinosaurs_of_a_species(self):
        self.pterosaur = Dinosaur("Pterosaur", "Carnivore", 200)
        self.raptor1 = Dinosaur("Raptor", "Omnivore", 300)
        self.raptor2 = Dinosaur("Raptor", "Omnivore", 350)
        self.raptor3 = Dinosaur("Raptor", "Omnivore", 290)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)
        self.park.add_dinosaur(self.pterosaur)
        self.park.add_dinosaur(self.bronty)
        self.park.add_dinosaur(self.raptor1)
        self.park.add_dinosaur(self.raptor2)
        self.park.add_dinosaur(self.raptor3)
        actual = len(self.park.get_dinosaurs_by_species("Raptor"))
        self.assertEqual(3, actual)
    
    def test_can_get_total_number_of_daily_vistors(self):
        self.pterosaur = Dinosaur("Pterosaur", "Carnivore", 200)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)
        self.park.add_dinosaur(self.pterosaur)
        self.park.add_dinosaur(self.bronty)
        self.assertEqual(450, self.park.get_total_daily_visitors())
    
    def test_can_get_annual_visitors(self):
        self.pterosaur = Dinosaur("Pterosaur", "Carnivore", 200)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)
        self.park.add_dinosaur(self.pterosaur)
        self.park.add_dinosaur(self.bronty)
        self.assertEqual(164250, self.park.get_annual_visitors())
    
    def test_can_get_annual_ticket_revenue(self):
        self.pterosaur = Dinosaur("Pterosaur", "Carnivore", 200)
        self.park.add_dinosaur(self.pterosaur)
        self.assertEqual(3650000, self.park.get_annual_ticket_revenue())
    
    def test_can_remove_dinosaurs_by_species(self):
        self.pterosaur = Dinosaur("Pterosaur", "Carnivore", 200)
        self.raptor1 = Dinosaur("Raptor", "Omnivore", 300)
        self.raptor2 = Dinosaur("Raptor", "Omnivore", 350)
        self.raptor3 = Dinosaur("Raptor", "Omnivore", 290)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)
        self.bronty = Dinosaur("Brontosaurus", "Herbivore", 250)
        self.park.add_dinosaur(self.pterosaur)
        self.park.add_dinosaur(self.bronty)
        self.park.add_dinosaur(self.bronty)
        self.park.add_dinosaur(self.raptor1)
        self.park.add_dinosaur(self.raptor2)
        self.park.add_dinosaur(self.raptor3)
        self.park.remove_dinosaurs_by_species("Brontosaurus")
        self.assertEqual(3, len(self.park.get_dinosaurs_by_species("Raptor")))
        self.assertEqual(0, len(self.park.get_dinosaurs_by_species("Brontosaurus")))
        self.assertEqual(1, len(self.park.get_dinosaurs_by_species("Pterosaur")))


if __name__ == "__main__":
    unittest.main() 