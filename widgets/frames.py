import tkinter as tk
from widgets.master_widget import MasterWidget

#Class to create frame widgets
class FrameWidget(MasterWidget):
    def __init__(self, master, width = None, height = None, relief = None, columnspan = None, borderwidth = None, 
                 highlightthickness = None, highlightbackground = None, **kwargs):
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)

        self.width = width
        self.height = height
        self.relief = relief
        self.columnspan = columnspan
        self.borderwidth = borderwidth
        self.highlightthickness = highlightthickness
        self.highlightbackground = highlightbackground

        #Create and locate the frame
        self.frame = tk.Frame(master = self.master, width = self.width, height = self.height, bg = self.bg, fg = self.fg, 
                              relief = self.relief, borderwidth = self.borderwidth, highlightthickness = self.highlightthickness, 
                              highlightbackground = self.highlightbackground)
        
        self.frame.grid(row = self.row, column = self.column, columnspan = self.columnspan, sticky = self.sticky, padx = self.padx, pady = self.pady)