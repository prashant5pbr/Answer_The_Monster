import tkinter as tk
from widgets.master_widget import MasterWidget

#Class to create label widgets
class LabelWidget(MasterWidget):
    #Initialised the parameters specific to label widgets
    def __init__(self, master, text, font, cursor = None, justify = None, **kwargs):
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)

        self.text = text
        self.font = font
        self.cursor = cursor
        self.justify = justify

        #Create and locate the label
        self.label = tk.Label(master = self.master, text = self.text, font = self.font, bg = self.bg, fg = self.fg, cursor = self.cursor, 
                            justify = self.justify)
        
        self.label.grid(row = self.row, column = self.column, sticky = self.sticky, padx = self.padx, pady = self.pady)