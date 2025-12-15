import tkinter as tk
import paths

#Class to create window
class AppWindow:
    #Class attribute to store the reference of the root
    main_window = None

    #Initialised the width, height and title for window
    def __init__(self, width, height, title):
        self.root = tk.Tk()              #Create the window as an attribute for object of the class

        self.width = width
        self.height = height
        self.title = title

        #Assign the Tk() object to the window handler
        AppWindow.main_window = self.root

        #Set the logo
        self.set_logo()

    #Setting the dimensions and title of the window
    def setup_window(self):
        self.root.minsize(self.width, self.height)
        self.root.title(self.title)

    #Running the window
    def start(self):
        self.setup_window()
        self.root.mainloop()            #Start the main event loop to make window appear and make it able to interact

    #Method to set the logo
    def set_logo(self):
        self.root.iconphoto(True, tk.PhotoImage(file = paths.LOGO_PATH))