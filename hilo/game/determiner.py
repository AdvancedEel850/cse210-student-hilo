import random
 
class Determiner:
    
    def __init__(self) -> None:
        
        self.card_number = []
        self.next_card_number = []
        self.num_tries = 0
 
    def can_draw(self, points):
 
        if points <= 0:
            return False
        else:
            return True
 
    def get_points(self, highlow):
 
        if highlow == 'h' and self.card_number[0] < self.next_card_number[0]:
            return 100
        elif highlow == 'l' and self.card_number[0] > self.next_card_number[0]:
            return 100
        else:
            return -75 
 
    def card_draw(self):
 
        self.card_number.clear()
        result = random.randint(1, 14)
        self.card_number.append(result)
 
    def next_card_draw(self):
 
        self.next_card_number.clear()
        result = random.randint(1, 14)
        self.next_card_number.append(result)
        self.num_tries += 1