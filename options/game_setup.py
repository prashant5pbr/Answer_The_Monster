from widgets import FrameWidget, LabelWidget, CanvasWidget, EntryWidget
from options.top_frame_widgets import TopFramePacker
from options.bottom_frame_widgets import BottomFramePacker
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
        canvas = CanvasWidget(frame.frame, height = 10, width = 800, highlightthickness = 0, row = 0, column = 1, sticky = "nsew")

        #Store the object of the Entername class as the attribute
        self.name = EnterName(self.root)

        #Register the validate command with the window
        vcmd = (self.root.register(self.name.check_input), "%P")

        #Create entry field that accepts player's name
        name_field = EntryWidget(canvas.canvas, validate = "key", validatecommand = vcmd, font = ("Academy Engraved LET", 40), 
                                 width = 22, bd = 0, highlightthickness = 0, bg = "systemWindowBackgroundColor", fg = "red", 
                                 insertbackground = "red", selectbackground = "red")
        
        canvas.canvas.create_window(15, 60, window = name_field.entry, anchor = "nw")

        #Assigning the entry object to the attribute of EnterName class
        EnterName.text_object = name_field.entry

        #Creating a dashed line as placeholder for the name
        canvas.canvas.create_text(5, 70, text = "_"*23, fill = "red", font = ("Academy Engraved LET", 50), anchor="nw")
        
        #Creating clickable label to create the layout
        start = LabelWidget(frame.frame, text = "Start", font = ("Academy Engraved LET", 50), fg = "red", cursor = "hand2", 
                            row = 1, column = 0, sticky = "w")
        
        #Bind the given method to the given label and entry object
        start.label.bind("<Button-1>", lambda event : self.layout())
        name_field.entry.bind("<Return>", lambda event : self.layout())

    #Method to create layout
    def layout(self):
        #Fetch the name of the player
        self.name.get_name()
        
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

        #Create object of the class TopFramePacker
        top_packer = TopFramePacker(top_frame.frame)
        top_packer.pack_top_frame()                             #Place widgets in top frame

        #Creating a separator
        FrameWidget(self.root, bg = "black", row = 1, column = 0, sticky = "nsew")

        #Create bottom frame inside the root
        bottom_frame = FrameWidget(self.root, bg = "white", row = 2, column = 0, sticky = "nsew")

        #Create object of the class TopFramePacker
        bottom_packer = BottomFramePacker(bottom_frame.frame)
        bottom_packer.pack_bottom_frame()                     #Place widgets in bottom frame