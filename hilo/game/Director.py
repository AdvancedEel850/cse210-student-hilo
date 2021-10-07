#imports

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
    
    def start_game(self):

        """This module is used to keep the game going as long as keep_playing is true.
        
        Args:
        Self(Director): an instance of the class Director"""
        while self.keep_playing:
            self.get_input()
            self.get_score()
            self.do_outputs()

    def get_input(self):

        """This moduel calls the file and class that will, find the card, and the next card

        Args:
        Self(Director): an instance of the class Director"""

        self.classname.findcardfun() #fill in classname with classname, and findcardfun with the function to find the cards

    def get_score(self):

        """This moduel will takes the points from the file and class that will determine if the player was right, and how many points the player wins or loses
        
        Args:
        Self(Director): an instance of the class Director"""

        points = self.classname.fun() #fill in classname with classname, and fun with the function to get points
        self.score += points

    def do_outputs(self):

        """This module will output the card, ask the player for higher or lower, and see if they want to keep playing
        
        Args:
        Self(Director): an instance of the class Director"""

        print(f"\nThe card is: {self.classname.card}") #classname = classname and card = the card they start with
        higlow = input("Higher or Lower: [h/l]")
        self.classname.higherorlowerfun(higlow) #classname = classname and higherorlowerfun = finding if the card is higher or lower.
        print(f"\nThe next card was: {self.classname.nextcard}") #classname = classname and nextcard is the next card.
        print(f"Your score is: {self.score}")
        if self.classname.canplay(): #classname = classname and camplay = the function checking if they can play again
           choice = input("Keep Playing? [y/n] ")
           self.keep_playing = (choice == 'y')
        else:
            self.keep_playing = False
