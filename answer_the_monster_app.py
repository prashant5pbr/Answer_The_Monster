from widgets import AppWindow, FrameWidget, LabelWidget

#Create a window object
root = AppWindow(1100, 660, "Answer The Monster")

#Grid layout management for the root
for i in range(3):
    root.root.rowconfigure(i, weight = 1)
    root.root.columnconfigure(i, weight = 1)

#Create a frame
frame = FrameWidget(root.root, row = 1, column = 1, sticky = "nsew")

#Grid layout management for the frame
for i in range(4):
    frame.frame.rowconfigure(i, weight = 0)

frame.frame.columnconfigure(0, weight = 1)

#Creating labels inside frame
LabelWidget(frame.frame, text = "Answer The Monster", font = ("Bradley Hand", 80), fg = "red", 
            row = 0, column = 0, sticky = "w", padx = (100, 0), pady = 50)

new_game_option = LabelWidget(frame.frame, text = "New Game", font = ("Academy Engraved LET", 40), cursor = "hand2", fg = "red", 
                              row = 1, column = 0, sticky = "w", padx = (375, 0))

scores_option = LabelWidget(frame.frame, text = "Scores", font = ("Academy Engraved LET", 40), cursor = "hand2", fg = "red", 
                            row = 2, column = 0, sticky = "w", padx = (375, 0))

exit_option = LabelWidget(frame.frame, text = "Exit", font = ("Academy Engraved LET", 40), cursor = "hand2", fg = "red", 
                          row = 3, column = 0, sticky = "w", padx = (375, 0))

#Setup and run the window
root.start()