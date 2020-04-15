from diet_data import *

class Park:
    def __init__(self, name, ticket_price):
        self.name = name 
        self.ticket_price = ticket_price
        self.dinosaurs = []
    
    def get_name(self):
        return self.name

    def get_ticket_price(self):
        return self.ticket_price
    
    def get_number_of_dinosaurs(self):
        return len(self.dinosaurs)
    
    def add_dinosaur(self, dinosaur):
        self.dinosaurs.append(dinosaur)
    
    def remove_dinosaur(self, dinosaur):
        if len(self.dinosaurs) > 0:
            self.dinosaurs.remove(dinosaur)
    
    def get_most_popular_dinosaur(self):
        if len(self.dinosaurs) > 0:
            most_number_of_visitors = 0
            most_popular_dinosaur = ""
            for dinosaur in self.dinosaurs:
                if dinosaur.get_daily_visitors() > most_number_of_visitors:
                    most_number_of_visitors = dinosaur.get_daily_visitors()
                    most_popular_dinosaur = dinosaur
            return most_popular_dinosaur
        
    def get_dinosaurs_by_species(self, species):
        if len(self.dinosaurs) > 0:
            species_list = [dinosaur for dinosaur in self.dinosaurs if dinosaur.species == species]
            return species_list
        else:
            return []
    
    def get_total_daily_visitors(self):
        total = 0
        for dinosaur in self.dinosaurs:
            total += dinosaur.get_daily_visitors()
        return total
    
    def get_annual_visitors(self):
        return self.get_total_daily_visitors() * 365
    
    def get_annual_ticket_revenue(self):
        return self.get_annual_visitors() * self.get_ticket_price()
    
    def remove_dinosaurs_by_species(self, species):
        self.dinosaurs = [dinosaur for dinosaur in self.dinosaurs if dinosaur.species is not species]
    
    def number_of_a_species(self, species):
        return len(self.get_dinosaurs_by_species(species))
    
    def get_dinosaurs_by_diet(self, diet):
        if len(self.dinosaurs) > 0:
            diet_list = [dinosaur for dinosaur in self.dinosaurs if dinosaur.diet == diet]
            return diet_list
        else:
            return []

    def get_number_of_a_diet_type(self, diet):
        return len(self.get_dinosaurs_by_diet(diet))
    
    def get_snapshot_of_diet_data(self, date):
        number_of_carnivores = self.get_number_of_a_diet_type("Carnivore")
        number_of_herbivores = self.get_number_of_a_diet_type("Herbivore")
        number_of_omnivores = self.get_number_of_a_diet_type("Omnivore")
        return Diet_Data(date, number_of_carnivores, number_of_herbivores, number_of_omnivores)
            