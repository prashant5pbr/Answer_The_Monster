import tkinter as tk
from widgets import FrameWidget, LabelWidget, CanvasWidget
from options.top_frame_widges import pack_top_frame
from options.name_setter import EnterName
from home_screen import Home

#Creating class to setup up the layout of frames for the game
class GameSetup:
    #Initialised the instance attribute
    def __init__(self, window):
        self.root = window

    #Method to clear the screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #Method to ask the name of the player
    def ask_name(self):
        #Clear the screen
        self.clear_screen()

        #Grid layout management for the root
        for i in range(3,5):
            self.root.rowconfigure(i, weight = 1)

        #Label to go back to the home screen
        go_back = LabelWidget(self.root, text = "\u21d0", font = ("Helvetica", 80), fg = "red", cursor = "hand2", 
                              row = 0, column = 0, sticky = "nw", padx = (25, 0), pady = (20, 0))
        
        #Create object of Home class
        home = Home(self.root)

        #Bind the given method to the given label
        go_back.label.bind("<Button-1>", lambda event : home.create_menu())
        self.root.bind("<Escape>", lambda event : home.create_menu())

        #Creating a frame
        frame = FrameWidget(self.root, row = 1, column = 1, sticky = "nsew")

        #Creating label asking for player name
        LabelWidget(frame.frame, text = "Enter player's name :", font = ("Academy Engraved LET", 50), fg = "red", 
                           row = 0, column = 0, sticky = "w", pady = (50, 0))
        
        #Creating canvas
        canvas = CanvasWidget(frame.frame, height = 10, width = 500, row = 0, column = 1, sticky = "nsew")

        #Creating a dashed line as placeholder for the name
        dash_line = canvas.canvas.create_text(5, 55, text = "_"*30, fill = "red", font = ("Academy Engraved LET", 50), anchor="nw")
        
        #Creating clickable label to create the layout
        start = LabelWidget(frame.frame, text = "Start", font = ("Academy Engraved LET", 50), fg = "red", cursor = "hand2", 
                            row = 1, column = 0, sticky = "w")
        
        #Bind the given method to the given label
        start.label.bind("<Button-1>", lambda event : self.layout())

        #Functions to change the cursor when over canvas item
        def on_text(event):
            canvas.canvas.config(cursor = "hand2")
        
        #Functions to change the cursor when out of canvas item
        def on_text_leave(event):
            canvas.canvas.config(cursor = "arrow")

        #Bind the given methods to the given canvas items
        canvas.canvas.tag_bind(dash_line, "<Enter>", on_text)
        canvas.canvas.tag_bind(start, "<Enter>", on_text)
        canvas.canvas.tag_bind(dash_line, "<Leave>", on_text_leave)
        canvas.canvas.tag_bind(start, "<Leave>", on_text_leave)

        #Enter name for the player
        name = EnterName(self.root, canvas.canvas)

        #Bind the given key press events to the root
        self.root.bind("<Key>", lambda e : name.set_name(e, self.root))
        self.root.bind("<Left>", lambda e : "break")
        self.root.bind("<Right>", lambda e : "break")

    #Method to create layout
    def layout(self):
        #Clear the screen
        self.clear_screen()

        #Reset the layout
        for i in range(5):
            self.root.rowconfigure(i, weight = 0)
            self.root.columnconfigure(i, weight = 0)

        #Handle pending GUI updates
        self.root.update_idletasks()

        #Grid layout management for the root
        self.root.rowconfigure(0, minsize = 175)
        self.root.rowconfigure(1, minsize = 5)
        self.root.rowconfigure(2, weight = 1)
        self.root.columnconfigure(0, weight = 1)

        #Create top frame inside the root
        top_frame = FrameWidget(self.root, row = 0, column = 0, sticky = "nsew")
        pack_top_frame(top_frame.frame)                     #Place widgets in top frame

        #Creating a separator
        FrameWidget(self.root, bg = "black", row = 1, column = 0, sticky = "nsew")

        #Create bottom frame inside the root
        bottom_frame = FrameWidget(self.root, bg = "white", row = 2, column = 0, sticky = "nsew")