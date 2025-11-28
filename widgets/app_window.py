import tkinter as tk

#Class to create window
class AppWindow:
    #Initialised the width, height and title for window
    def __init__(self, width, height, title):
        self.root = tk.Tk()              #Create the window as an attribute for object of the class

        self.width = width
        self.height = height
        self.title = title

    #Setting the dimensions and title of the window
    def setup_window(self):
        self.root.minsize(self.width, self.height)
        self.root.title(self.title)

    #Running the window
    def start(self):
        self.setup_window()
        self.root.mainloop()            #Start the main event loop to make window appear and make it able to interact