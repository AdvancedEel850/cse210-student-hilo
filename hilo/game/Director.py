from game.determiner import Determiner
 
class Director:
    """This class it the director of the game, It will start the game, and end the game.
    
    Modules:
    __init__
    start_game
    get_score
    do_ouptus
    get_input"""
 
    def __init__(self) -> None:
 
        """this class is used to define our variables used in this class of the game.
        args:
        self(Director):an instance of director"""
 
        self.score = 300
        self.card = 0
        self.keep_playing = True
        self.determiner = Determiner()
    
    def start_game(self):
 
        """This module is used to keep the game going as long as keep_playing is true.
        
        Args:
        Self(Director): an instance of the class Director"""
        while self.keep_playing:
            self.get_input()
            self.do_outputs()
 
    def get_input(self):
 
        """This module calls the file and class that will find the card and the next card.
 
        Args:
        Self(Director): an instance of the class Director"""
 
        self.determiner.card_draw() 
        self.determiner.next_card_draw()
        
        #fill in classname with classname, and findcardfun with the function to find the cards

 
    def do_outputs(self):
 
        """This module will output the card, ask the player for higher or lower, and see if they want to keep playing
        
        Args:
        Self(Director): an instance of the class Director"""
 
        print(f"\nThe card is: {self.determiner.card_number}") #classname = classname and card = the card they start with
        highlow = input("Higher or Lower: [h/l]")
        points = self.determiner.get_points(highlow) #classname = classname and higherorlowerfun = finding if the card is higher or lower.
        self.score += points 
        print(f"The next card was: {self.determiner.next_card_number}") #classname = classname and nextcard is the next card.
        print(f"Your score is: {self.score}")
        if self.determiner.can_draw(self.score): #classname = classname and camplay = the function checking if they can play again
           choice = input("Keep Playing? [y/n] ")
           self.keep_playing = (choice == 'y')
        else:
            self.keep_playing = False