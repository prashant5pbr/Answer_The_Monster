import tkinter as tk

#Class to insert lines in the the Text widget based on user response
class InsertText:
    #Initialise the Text widget and user response as the instance attributes
    def __init__(self, text_object, user_input):
        self.text_object = text_object
        self.user_input = user_input

    #Method to enter lines in the Text widget
    def insert_line(self, system_output):
        #Insert the user response in the most recent cursor position
        self.text_object.insert(self.text_object.index("insert"), f"\n{self.user_input}\n")
        
        #Scroll the view to the end of the Text widget
        self.text_object.see(tk.END)

        #Fetch the number of the line where the line will be inserted
        pos = self.text_object.index("insert + 1 line")

        #Insert the output in the Text
        self.text_object.insert(pos, f"\n{system_output}\n")

        #Scroll the view to the end of the Text widget
        self.text_object.see(tk.END)

        #Fetch the end of the line where the output is inserted
        end_pos = self.text_object.index(f"{pos} lineend")

        #Right align the output by apply tag
        self.text_object.tag_add("right", pos, end_pos)
        self.text_object.tag_configure("right", justify = "right")