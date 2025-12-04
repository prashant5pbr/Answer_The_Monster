import tkinter as tk
from widgets.master_widget import MasterWidget

#Class to create Text Widget
class TextWidget(MasterWidget):
    ##Initialised the parameters specific to Text widgets
    def __init__(self, master, width = None, height = None, font = None, bg = None, fg = None, highlightthickness = None,
                  insertbackground = None, **kwargs):
        
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)
        
        self.width = width
        self.height = height
        self.font = font
        self.bg = bg
        self.fg = fg
        self.highlightthickness = highlightthickness
        self.insertbackground = insertbackground

        #Create and locate the Text widget
        self.text = tk.Text(master = self.master, width = self.width, height = self.height, font = self.font, bg = self.bg, 
                            fg = self.fg, highlightthickness = self.highlightthickness, insertbackground = self.insertbackground)
        
        self.text.grid(row = self.row, column = self.column, sticky = self.sticky, padx = self.padx, pady = self.pady)