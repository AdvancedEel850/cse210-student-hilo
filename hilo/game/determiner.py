import random
 
class Determiner:
    
    def __init__(self) -> None:
        
        self.card_number = []
        self.next_card_number = []
        self.num_tries = 0
 
    def can_draw(self):
 
        pass
 
    def get_points(self):
 
        pass
 
    def card_draw(self):
 
        self.card_number.clear()
        result = random.randint(1, 14)
        self.card_number.append(result)
 
    def next_card_draw(self):
 
        self.next_card_number.clear()
        result = random.randint(1, 14)
        self.next_card_number.append(result)
        self.num_tries += 1