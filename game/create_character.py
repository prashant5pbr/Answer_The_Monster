#Class to create characters
class Character:
    #Defining system's name, initial points and the reference to the player as class attributes 
    system_name = "Monster"
    system_points = 50
    player_handler = None

    #Initialising the player's name and initial points as instance attributes
    def __init__(self, name, points = 50):
        self.name = name
        self.points = points
        Character.player_handler = self

    #Method to distribue points between the system and the player
    def adjust_points(self, answer = None):
        if answer.lower() == "correct":
            self.points += 5
            Character.system_points -= 5

        elif answer.lower() == "incorrect":
            self.points -= 5
            Character.system_points += 5