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