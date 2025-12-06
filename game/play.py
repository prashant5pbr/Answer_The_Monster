import tkinter as tk

#Class to proceed the conversation on positive reply from the user
class GamePlay:
    #Initialised the Text widget as an instance attribute
    def __init__(self, text_object):
        self.text_object = text_object

    #Method to display initial messages if user replies positively
    def start(self):
        #Initial messages
        message1 = "Start visiting the rooms."
        message2 = "From now on, anything apart from correct answer will be considered incorrect answer.\n"

        messages = [message1, message2]

        #Fetch the number of the line where the text will be inserted
        pos = self.text_object.index("insert + 1 line")

        #Insert the messages
        for num, message in enumerate(messages):
            #Fetch the current position
            current_pos = f"{pos} + {num} line"

            #Insert the message
            self.text_object.insert(current_pos, f"\n{message}")

            #Scroll the view to the end of the Text widget
            self.text_object.see(tk.END)

            #Fetch the end of the line where the output is inserted
            end_pos = self.text_object.index(f"{current_pos} lineend")

            #Right align the message by applying tag
            self.text_object.tag_add("right", current_pos, end_pos)
            self.text_object.tag_configure("right", justify = "right")