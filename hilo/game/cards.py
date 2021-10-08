import random

class cards:

    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    'a fucntion to get the current and next card randomly'
    def get_cards(self):
        first_card = random.choice(self.cards)
        
        return first_card
    def next_card(self, first_card):
        pass
  