import tkinter as tk
from widgets import FrameWidget, TextWidget, EntryWidget, ButtonWidget
from options.manage_tables import Tables
from game import Chat, GamePlay
#Lazy import class Questioner

#Class to pack widgets in the bottom frame of game layout
class BottomFramePacker:
    #Class attribute to store the Text widget and Entry widget and to be accessed through other class
    text_handler = None
    entry_handler = None

    #Initialised the frame and Text widget as an instance attribute
    def __init__(self, frame):
        self.frame = frame
        self.text_object = None
        self.entry_object = None

    #Method to place widgets in the bottom frame
    def pack_bottom_frame(self):
        #Grid layout management for the frame
        self.frame.rowconfigure(0, weight = 1)
        self.frame.columnconfigure(0, weight = 1)
        self.frame.columnconfigure(1, minsize = 800)
        self.frame.columnconfigure(2, weight = 1)

        #Creating top left frame
        bottom_left_frame = FrameWidget(self.frame, borderwidth = 5, relief = "solid", row = 0, column = 0, sticky = "nsew")

        #Create table in the bottom left frame
        left_table = Tables(bottom_left_frame.frame)
        left_table.create()

        #Creating top mid frame
        bottom_mid_frame = FrameWidget(self.frame, borderwidth = 5,  relief = "solid", row = 0, column = 1, sticky = "nsew")

        #Grid layout management for bottom mid frame
        bottom_mid_frame.frame.rowconfigure(0, weight = 1)
        bottom_mid_frame.frame.rowconfigure(1, weight = 0)
        bottom_mid_frame.frame.rowconfigure(2, weight = 0)
        bottom_mid_frame.frame.columnconfigure(0, weight = 1)

        #Creating Text widget in bottom mid frame
        self.text_object = TextWidget(bottom_mid_frame.frame, font = ("Helvetica, 20"), width = 57, highlightthickness = 0, 
                                      row = 0, column = 0, sticky = "nsew")
        
        #Assigning Text widget to the class attribute
        BottomFramePacker.text_handler = self.text_object.text

        #Creating separator frame in the bottom mid frame
        FrameWidget(bottom_mid_frame.frame, height = 1, row = 1, column = 0)

        #Creating frame in the bottom mid frame 
        input_frame = FrameWidget(bottom_mid_frame.frame, row = 2, column = 0)

        #Grid layout management for the input frame
        input_frame.frame.rowconfigure(0, weight = 1)
        input_frame.frame.columnconfigure(0, weight = 1)
        input_frame.frame.columnconfigure(1, weight=0)

        #Creating entry widget in the input frame
        self.entry_object = EntryWidget(input_frame.frame, width = 57, font = ("Helvetica", 20), bd = 0, highlightthickness = 1, 
                            row = 0, column = 0, sticky = "nsew")
        
        #Assigning Text widget to the class attribute
        BottomFramePacker.entry_handler = self.entry_object.entry
    
        #Creating object of the class Chat to start conversation
        talk = Chat(self.text_object.text, self.entry_object.entry)
        talk.start()

        #Making text uneditable
        self.text_object.text.config(state = "disabled")

        #Method to be called when enter button is clicked
        def submit_enter():
            #Lazy import the class Questioner
            from game.questions_answers import Questioner

            #Create object of the class and insert the user replied answer in the Text widget
            if Questioner.answer_ready:
                games_answer = Questioner()
                games_answer.insert_answer()
            
            #Create object of the class and call the method to restart the game or go to home
            elif GamePlay.should_restart_game:
                #Create the object of given class
                game_play = GamePlay(BottomFramePacker.text_handler, BottomFramePacker.entry_handler)
                game_play.end_options()

            #Method for interaction before the game starts
            elif Chat.initial_response:
                talk.respond()

            else:
                BottomFramePacker.entry_handler.delete(0, tk.END)
                return
        
        #Create button widget in the input frame
        ButtonWidget(input_frame.frame, text = "Enter", font = ("Helvetica", 30), borderwidth = 0, highlightthickness = 0,
                              command = submit_enter, row = 0, column = 1)
        
        self.entry_object.entry.bind("<Return>", lambda event : submit_enter())

        #Creating top right frame
        bottom_right_frame = FrameWidget(self.frame, borderwidth = 5, relief = "solid", row = 0, column = 2, sticky = "nsew")

        #Create table in the bottom right frame
        right_table = Tables(bottom_right_frame.frame)
        right_table.create()