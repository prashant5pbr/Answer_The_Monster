import tkinter as tk
from game.line_inserter import InsertText
from game.play import GamePlay
import re
#Lazy imported EnterName class

#Create class to display interaction between the user and the system in a chat form
class Chat:
    initial_response = True

    #Initialised the Text widget and Entry widgets as instance attributes
    def __init__(self, text_object = None, entry_object = None):
        self.text_object = text_object
        self.entry_object = entry_object

    #Method to start the converstation
    def start(self):
        #Lazy import the class EnterName
        from options import EnterName

        #Fetch the name of player
        name = EnterName.name

        #Initial messages
        messages = {
            "message1" : f"Hello {name}...", 
            "message2" : "Welcome to the game ANSWER THE MONSTER. Are you ready to play?",
            "message3" : "***",
            "message4" : "Rules of the game :",
            "message5" : "1. Given above are three rooms. You can visit them by clicking on it.",
            "message6" : "2. Keep on clicking on any of them randomly until a monster appears from one of them.",
            "message7" : "3. The monster will ask you a question. You will have to answer it within a given time.",
            "message8" : "4. Both you and the monster start at 50 points.",
            "message9" : "5. If you answer correctly, five of his points will be yours.",
            "message10" : "6. If you answer incorrectly, five of your points will be his.",
            "message11" : "7. Whoever's points first become zero loses.",
            "message12" : "***",
            "message13" : "Type yes(y) to start the game or no(n) to end"
        }

        #Make Text object editable
        self.text_object.config(state = "normal")

        #Insert the messages and align each message to right
        for line, message in enumerate(list(messages.values())):
            self.text_object.insert(f"{line+1}.0", f"{message}\n")

            #Assign tag to the text in given range
            self.text_object.tag_add("right", f"{line+1}.0", f"{line+1}.end")

            #Assign the behaviour to the tagged text
            self.text_object.tag_configure("right", justify = "right")

        #Make the Text object uneditable
        self.text_object.config(state = "disabled")

    #Method to invoke response on user input
    def respond(self):
        if not Chat.initial_response:
            #Clear the entry widget
            self.entry_object.delete(0, tk.END)
            return
        
        #Fetch the input from the entry
        response = self.entry_object.get().strip().capitalize()

        #Truncate all the unwanted spaces between the words to single space 
        clean_response = re.sub(r'\s+', ' ', response)
        clean_response_lower = clean_response.lower()
        
        #Make the text field editable
        self.text_object.config(state = "normal")

        #Always accept new lines at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #Create object of class
        text_inserter = InsertText(self.text_object, clean_response)

        #Based on the response insert the given lines in the text
        if clean_response_lower in ["ok", "y", "yes", "yeah", "sure", "let's go", "start", "i want to play."]:
            text_inserter.insert_line("Great. Let's start then.")

            Chat.initial_response = False

            #Create the object of given class
            game_play = GamePlay(self.text_object, self.entry_object)

            #Start the game
            game_play.start()

        elif clean_response_lower in ["hey", "hi", "hlo", "hello", "hey there"]:
            text_inserter.insert_line("Hello. Are you in?")

        elif clean_response_lower == "who are you?":
            text_inserter.insert_line("I am the monster with whom you'll play the game.")

        elif clean_response_lower in ["n", "no"]:
            text_inserter.insert_line("Fine. Good bye.....")

        elif clean_response_lower in ["later"]:
            text_inserter.insert_line("No problem. Take your time.")

        elif not clean_response_lower:
            return

        else:
            text_inserter.insert_line("What's that? Are you in or not?")
        
        #Make the Text uneditable 
        self.text_object.config(state = "disabled")

        #Clear the entry widget
        self.entry_object.delete(0, tk.END)