#Lazy import classes GamePlay and BottomFramePacker

#Class to create and manage characters
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

    #Method to check if the game has ended when any of the character's points become zero
    @staticmethod
    def check_points():
        #Lazy import the classes GamePlay and BottomFramePacker
        from game.play import GamePlay
        from options import BottomFramePacker

        #Check if system's point first became zero
        if Character.system_points == 0:
            status = "win 💪"

            #Create object and call method to insert last messages in the Text widget
            last_message_inserter = GamePlay(BottomFramePacker.text_handler, BottomFramePacker.entry_handler)
            last_message_inserter.game_end(status)

        #Check if system's point first became zero
        elif Character.player_handler.points == 0:
            status = "lose"

            #Create object and call method to insert last messages in the Text widget
            last_message_inserter = GamePlay(BottomFramePacker.text_handler, BottomFramePacker.entry_handler)
            last_message_inserter.game_end(status)