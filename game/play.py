import tkinter as tk
#Lazy imported CountDown Class

#Class to proceed the conversation on positive reply from the user
class GamePlay:
    #Class attribute to determine the game has started
    game_on = False

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

        #Change the value of the flag to True
        GamePlay.game_on = True

    #Method to be called when the game layout's top frame's buttons are clicked
    def click_reciever(self, label, click_count, random_number):
        if not GamePlay.game_on:
            return
        
        #Make the text field editable
        self.text_object.config(state = "normal")

        #Always accept new lines at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #Fetch the number of the line where the line will be inserted
        pos = self.text_object.index("insert + 1 line")

        #Inser the message in Text widget
        if click_count == random_number:
            self.text_object.insert(pos, f"\nYou cliked on {label} : MONSTER !!!\n")

            #Lazy import the CountDown class
            from game.timer import CountDown

            #Create object and call the method to start the timer
            timer = CountDown()
            timer.start()

        else:
            self.text_object.insert(pos, f"\nYou cliked on {label} : Empty room!!!\n")

        #Scroll the view to the end of the Text widget
        self.text_object.see(tk.END)

        #Fetch the end of the line where the output is inserted
        end_pos = self.text_object.index(f"{pos} lineend")

        #Right align the output by apply tag
        self.text_object.tag_add("right", pos, end_pos)
        self.text_object.tag_configure("right", justify = "right")

        #Make the text field editable
        self.text_object.config(state = "disabled")