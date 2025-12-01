import tkinter as tk
from widgets.master_widget import MasterWidget

#Class to create canvas widgets
class CanvasWidget(MasterWidget):
    #Initialised the parameters specific to label widgets
    def __init__(self, master, width = None, height = None, bg = None, highlightthickness = None, **kwargs):
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)

        self.width = width
        self.height = height
        self.bg = bg
        self.highlightthickness = highlightthickness

        #Creating and locating the canvas
        self.canvas = tk.Canvas(master = self.master, width = self.width, height = self.height, bg = self.bg, 
                                highlightthickness = self.highlightthickness)
        
        self.canvas.grid(row = self.row,column = self.column, sticky = self.sticky, padx = self.padx, pady = self.pady)