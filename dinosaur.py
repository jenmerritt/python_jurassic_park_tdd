class Dinosaur:
    def __init__(self, species, diet, daily_visitors):
        self.species = species 
        self.diet = diet 
        self.daily_visitors = daily_visitors
    
    def get_species(self):
        return self.species
    
    def get_diet(self):
        return self.diet

    def get_daily_visitors(self):
        return self.daily_visitors