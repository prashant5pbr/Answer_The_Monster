from widgets import FrameWidget, LabelWidget, ButtonWidget
from options.bottom_frame_widgets import BottomFramePacker
from options.name_setter import EnterName
from options.count_click import click_tracker
from options.put_canvas import place_canvas
from game import GamePlay, Character
from scroll import ScrollEnabler

#Class to pack widgets in the top frame of game layout
class TopFramePacker:
    #Defined the clas attributes
    buttons_list = []
    buttons_commands = {}
    player_points = None                #Attribute to store reference to the label displaying player's points
    monster_points = None               #Attribute to store reference to the label displaying monster's points

    #Initialised the frame as an instance attribute
    def __init__(self, frame):
        self.frame = frame

    #Method to pack the widgets in the top frame
    def pack_top_frame(self):
        #Grid layout management for the frame
        self.frame.rowconfigure(0, weight = 1)
        self.frame.columnconfigure(0, weight = 1)
        self.frame.columnconfigure(1, minsize = 800)
        self.frame.columnconfigure(2, weight = 1)

        #Creating top left frame
        top_left_frame = FrameWidget(self.frame, borderwidth = 5, relief = "solid", row = 0, column = 0, sticky = "nsew")

        #Creating canvas and inner frame inside the top left frame
        canvas1, i_frame1 = place_canvas(top_left_frame.frame)
        i_frame1.config(bg = "red")

        #Grid layout management for the inner frame inside top left frame
        for i in range(2):
            i_frame1.rowconfigure(i, weight = 1)

        #Fetch the name of the player
        player = Character(EnterName.name)
        player_name = player.name

        #Display the name of the player
        LabelWidget(i_frame1, text = f"Player (You):\n{player_name}", font = ("Helvetica", 30), justify = "left", 
                            bg = "red", fg = "white", row = 0, column = 0, sticky = "nw")
        
        #Display the points of the player
        player_points_label = LabelWidget(i_frame1, text = f"Current Points :\n{player.points}", font = ("Helvetica", 30), 
                                    justify = "left", bg = "red", fg = "white", row = 1, column = 0, sticky = "nw")
        
        #Assign the label to display the points of player as class attribute
        TopFramePacker.player_points = player_points_label.label

        #Enable horizontal scrolling in top left frame
        left_scroll_enabler = ScrollEnabler(canvas1)
        left_scroll_enabler.enable_scrolling()

        #Creating top mid frame
        top_mid_frame = FrameWidget(self.frame, borderwidth = 5, bg = "white",  relief = "solid", row = 0, column = 1, sticky = "nsew")

        #Grid layout management for the top mid frame
        top_mid_frame.frame.rowconfigure(0, weight = 1)
        top_mid_frame.frame.columnconfigure(0, weight = 1)
        top_mid_frame.frame.columnconfigure(1, weight = 1)
        top_mid_frame.frame.columnconfigure(2, weight = 1)

        #Function to be called when the buttons are clicked
        def on_click(label):
            #create the object for the class
            game_play = GamePlay(BottomFramePacker.text_handler, BottomFramePacker.entry_handler)

            #Fetch the click count and random number from the given function
            click_count, random_number = click_tracker()

            #Call the method to interact with game layout's bottom frame's Text widget
            game_play.click_reciever(label, click_count, random_number)

        #Creating buttons in the top mid frame
        for index, label in enumerate(["A", "B", "C"]):
            button = ButtonWidget(top_mid_frame.frame, text = f"Room-{label}", font = ("Helvetica", 40),  
                         command = lambda l=label : on_click(l), row = 0, column = index, sticky = "nsew")
            
            #Append the button to the list
            TopFramePacker.buttons_list.append(button)

            #Added the command for the button in the dictionary
            TopFramePacker.buttons_commands[button.button] = button.button.cget("command")

        #Creating top right frame
        top_right_frame = FrameWidget(self.frame, borderwidth = 5, relief = "solid", row = 0, column = 2, sticky = "nsew")

        #Creating canvas and inner frame inside the top left frame
        canvas2, i_frame2 = place_canvas(top_right_frame.frame)
        i_frame2.config(bg = "green")

        #Grid layout management for the inner frame
        for i in range(2):
            i_frame2.rowconfigure(i, weight = 1)
            i_frame2.columnconfigure(i, weight = 1)

        #Display the name of opponent (monster)
        LabelWidget(i_frame2, text = f"Player :\n{Character.system_name}", font = ("Helvetica", 30), justify = "right", 
                            bg = "green", fg = "white", row = 0, column = 1, sticky = "ne")
        
        #Display the points of the player
        monster_points_label = LabelWidget(i_frame2, text = f"Current Points :\n{Character.system_points}", font = ("Helvetica", 30), 
                                     justify = "right", bg = "green", fg = "white", row = 1, column = 1, sticky = "ne")
        
        #Assign the label to display the points of monster as class attribute
        TopFramePacker.monster_points = monster_points_label.label
        
        #Update the positions of the widgets
        canvas2.update_idletasks()
        
        #Enable horizontal scrolling in top right frame
        right_scroll_enabler = ScrollEnabler(canvas2)
        right_scroll_enabler.enable_scrolling()