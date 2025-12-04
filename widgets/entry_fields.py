import tkinter as tk
from widgets.master_widget import MasterWidget

#Class to create entry weidgets
class EntryWidget(MasterWidget):
    #Initialised the parameters specific to entry widgets
    def __init__(self, master, textvariable = None, validate = None, validatecommand = None, font = None, width = None, 
                 bd = None, highlightthickness = None, insertbackground = None, selectbackground = None, **kwargs):
        
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)

        self.textvariable = textvariable
        self.validate = validate
        self.validatecommand = validatecommand
        self.font = font
        self.width = width
        self.bd = bd
        self.highlightthickness = highlightthickness
        self.insertbackground = insertbackground
        self.selectbackground = selectbackground

        #Create and locate entry widget
        self.entry = tk.Entry(master = self.master, textvariable = self.textvariable, validate = self.validate, 
                              validatecommand = self.validatecommand, font = self.font, width = self.width, bd = self.bd, 
                              highlightthickness = self.highlightthickness, bg = self.bg, fg = self.fg, 
                              insertbackground = self.insertbackground, selectbackground = self.selectbackground)
        
        self.entry.grid(row = self.row, column = self.column, sticky = self.sticky, padx = self.padx, pady = self.pady)