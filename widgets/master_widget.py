#Class containing the common parameters for different widgets
class MasterWidget:
    #Initialised the different parameters as the instance attributes
    def __init__(self, master, **kwargs):
        self.master = master
        self.bg = kwargs.get("bg", None)
        self.fg = kwargs.get("fg", None)
        self.row = kwargs.get("row", None)
        self.rowspan = kwargs.get("rowspan", None)
        self.column = kwargs.get("column", None)
        self.columnspan = kwargs.get("columnspan", None)
        self.sticky = kwargs.get("sticky", None)
        self.padx = kwargs.get("padx", None)
        self.pady = kwargs.get("pady", None)