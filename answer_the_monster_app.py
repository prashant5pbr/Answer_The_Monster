from widgets import AppWindow
from home_screen import Home

#Create a window object
root = AppWindow(1100, 660, "Answer The Monster")

#Create a Home class object
home = Home(root.root)
home.create_menu()              #Create menu

#Setup and run the window
root.start()