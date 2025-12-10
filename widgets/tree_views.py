from tkinter import ttk
from widgets.master_widget import MasterWidget

#Class to create Table widgets
class TreeViewWidget(MasterWidget):
    def __init__(self, master, height = None, show = None, **kwargs):
        #Calling the __init__ method of the parent class (MasterWidget)
        super().__init__(master, **kwargs)

        self.height = height
        self.show = show

        #Create and locate the table
        self.tree = ttk.Treeview(master = self.master, height = self.height, show = self.show)

        self.tree.grid(row = self.row, column = self.column, sticky = self.sticky, padx = self.padx, pady = self.pady)