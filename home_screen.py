from widgets import LabelWidget, FrameWidget
#Lazy imported class GameSetup and ScoreBoard
#Lazy imported the function exit_game() from end_game.py

#Class to creat home screen
class Home:
    #Initialised the app window and the options of custom in-app menu as the instance attributes
    def __init__(self, master, new_game_option = None, scores_option = None, exit_option = None):
        self.root = master
        self.new_game_option = new_game_option
        self.scores_option = scores_option
        self.exit_option = exit_option

    #Method to clear the screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #Method to create the menu
    def create_menu(self):
        #Clear the screen
        self.clear_screen()

        #Reset the grid layout
        for i in range(5):
            self.root.rowconfigure(i, weight = 0)
            self.root.columnconfigure(i, weight = 0)

        self.root.rowconfigure(0, minsize = 0)
        self.root.rowconfigure(1, minsize = 0)

        #Grid layout management for the root
        for i in range(3):
            self.root.rowconfigure(i, weight = 1)
            self.root.columnconfigure(i, weight = 1)

        #Create a frame
        frame = FrameWidget(self.root, row = 1, column = 1, sticky = "nsew")

        #Grid layout management for the frame
        for i in range(4):
            frame.frame.rowconfigure(i, weight = 0)

        frame.frame.columnconfigure(0, weight = 1)

        #Create main menu title
        LabelWidget(frame.frame, text = "Answer The Monster", font = ("Bradley Hand", 80), fg = "red", 
            row = 0, column = 0, sticky = "w", padx = (100, 0), pady = 50)
        
        #Create labels options for in-app menu which can be clicked
        self.new_game_option = LabelWidget(frame.frame, text = "New Game", font = ("Academy Engraved LET", 40), cursor = "hand2", 
                                           fg = "red", row = 1, column = 0, sticky = "w", padx = (375, 0))

        self.scores_option = LabelWidget(frame.frame, text = "Scores", font = ("Academy Engraved LET", 40), cursor = "hand2", 
                                         fg = "red", row = 2, column = 0, sticky = "w", padx = (375, 0))

        self.exit_option = LabelWidget(frame.frame, text = "Exit", font = ("Academy Engraved LET", 40), cursor = "hand2", 
                                       fg = "red", row = 3, column = 0, sticky = "w", padx = (375, 0))
        
        #Lazy importing the GameSetup and ScoreBoard Class
        from options import GameSetup
        from game import ScoreBoard

        #Create GameSetup object and bind the method to the label
        new_game_object = GameSetup(self.root)
        self.new_game_option.label.bind("<Button-1>", lambda event : new_game_object.ask_name())

        #Create ScoreBoard object and bind the method to the label
        score_object = ScoreBoard(self.root)
        self.scores_option.label.bind("<Button-1>", lambda event : score_object.display_scores())

        #Lazy import the function exit_game
        from game import exit_game

        #Bind the method to exit the game
        self.exit_option.label.bind("<Button-1>", lambda event : exit_game())