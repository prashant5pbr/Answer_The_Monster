from tkinter import messagebox
from widgets import AppWindow

#Function to exit the game
def exit_game():
    #Ask for confirmation before exiting
    confirmation = messagebox.askyesno(message = "Are you sure you want to exit?", parent = AppWindow.main_window)

    #Exit on positive response
    if confirmation:
        AppWindow.main_window.destroy()