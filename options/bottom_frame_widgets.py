from widgets import FrameWidget, TextWidget, EntryWidget, ButtonWidget

#Function to pack widgets in game setup's top frame
def pack_bottom_frame(frame):
    #Grid layout management for the frame
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, minsize = 800)
    frame.columnconfigure(2, weight = 1)

    #Creating top left frame
    bottom_left_frame = FrameWidget(frame, borderwidth = 5, relief = "solid", row = 0, column = 0, sticky = "nsew")

    #Creating top mid frame
    bottom_mid_frame = FrameWidget(frame, borderwidth = 5,  relief = "solid", row = 0, column = 1, sticky = "nsew")

    #Grid layout management for bottom mid frame
    bottom_mid_frame.frame.rowconfigure(0, weight = 1)
    bottom_mid_frame.frame.rowconfigure(1, weight = 0)
    bottom_mid_frame.frame.rowconfigure(2, weight = 0)
    bottom_mid_frame.frame.columnconfigure(0, weight = 1)

    #Creating Text widget in bottom mid frame
    text = TextWidget(bottom_mid_frame.frame, width = 57, highlightthickness = 0, row = 0, column = 0, sticky = "nsew")

    #Making text uneditable
    text.text.config(state = "disabled")

    #Creating separator frame in the bottom mid frame
    FrameWidget(bottom_mid_frame.frame, height = 1, row = 1, column = 0)

    #Creating frame in the bottom mid frame 
    input_frame = FrameWidget(bottom_mid_frame.frame, row = 2, column = 0)

    #Grid layout management for the input frame
    input_frame.frame.rowconfigure(0, weight = 1)
    input_frame.frame.columnconfigure(0, weight = 1)
    input_frame.frame.columnconfigure(1, weight=0)

    #Creating entry widget in the input frame
    entry = EntryWidget(input_frame.frame, width = 57, font = ("Helvetica", 20), bd = 0, highlightthickness = 1, 
                        row = 0, column = 0, sticky = "nsew")
    
    #Create button widget in the input frame
    button = ButtonWidget(input_frame.frame, text = "Enter", font = ("Helvetica", 30), borderwidth = 0, highlightthickness = 0,
                          row = 0, column = 1)

    #Creating top right frame
    bottom_right_frame = FrameWidget(frame, borderwidth = 5, relief = "solid", row = 0, column = 2, sticky = "nsew")