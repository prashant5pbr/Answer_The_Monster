import tkinter as tk
from widgets.master_widget import MasterWidget

#Class to create Button widgets
class ButtonWidget(MasterWidget):
    #Initialised the parameters specific to button widgets
    def __init__(self, master, text = None, command = None, font = None, width = None, borderwidth = None, 
               highlightthickness = None, relief = None, **kwargs):
        
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)

        self.text = text
        self.command = command
        self.font = font
        self.width = width
        self.borderwidth = borderwidth
        self.highlightthickness = highlightthickness
        self.relief = relief

        #Create and locate the button
        self.button = tk.Button(master = self.master, text = self.text, command = self.command, font = self.font, width = self.width, 
                                borderwidth = self.borderwidth, highlightthickness = self.highlightthickness, relief = self.relief)
        
        self.button.grid(row = self.row, column = self.column, sticky = self.sticky, padx = self.padx, pady = self.pady)