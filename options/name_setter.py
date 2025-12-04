from tkinter import messagebox

#Class to fetch the name from the entry field
class EnterName:
    #Defining class attributes
    name = None
    text_object = None

    #Initialised the root as instance attribute
    def __init__(self, window = None):
        self.root = window

    #Validation method
    def check_input(self, P):
        #Characters which are not acceptable for name
        invalid_char = "~#%^*()+=:;<>,?|\"\\{[]}"

        #Return if total characters exceed 20
        if len(P) > 20:
            messagebox.showinfo(message = "Length of name cannot exceed 20 characters.", parent = self.root)
            return False
        
        #Return if invalid character is entered
        elif set(invalid_char) & set(P):
            messagebox.showinfo(message = f"Name cannot contain any of these characters :\n{invalid_char}", parent = self.root)
            return False
        
        return True

    #Method to assign name defined as static method
    @staticmethod
    def get_name():
        if EnterName.text_object:
            EnterName.name = EnterName.text_object.get()
            
            if not EnterName.name:
                EnterName.name = "Anonymous"