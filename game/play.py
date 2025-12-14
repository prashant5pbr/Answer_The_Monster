import time
import tkinter as tk
from home_screen import Home
from widgets import AppWindow
#Lazy imported classes TopFramePacker, Character, Questioner, Chat, Tables and Countdown
#Lazy import the function reset() from reset_attributes.py

#Class to proceed the conversation on positive reply from the user
class GamePlay:
    #Class attributes
    game_on = False
    should_restart_game = False
    start_time = None

    #Initialised the Text widget and Entry widget as an instance attribute
    def __init__(self, text_object, entry_object):
        self.text_object = text_object
        self.entry_object = entry_object

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

        #Set the timer and change the value of the flag to True
        GamePlay.start_time = time.time()
        GamePlay.game_on = True

    #Method to be called when the game layout's top frame's buttons are clicked
    def click_reciever(self, label, click_count, random_number):
        if not GamePlay.game_on:
            return
        
        #Flag to indicate to start the game
        GamePlay.game_on = True
        
        #Make the text field editable
        self.text_object.config(state = "normal")

        #Always accept new lines at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #Fetch the number of the line where the line will be inserted
        pos = self.text_object.index("insert + 1 line")

        #Inser the message in Text widget
        if click_count == random_number:
            self.text_object.insert(pos, f"\nYou cliked on {label} : MONSTER !!!\n")

            #Lazy import class Questioner
            from game.questions_answers import Questioner

            #Create object of the class
            game_questions = Questioner()

            #Insert the question in the Text widget
            game_questions.insert_question()

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

        #Make the text field uneditable
        self.text_object.config(state = "disabled")

    #Method to insert the last messages at the end of the game
    def game_end(self, status):
        #Calculate the duration of the game and convert it in HH:MM:SS format
        duration = time.time() - GamePlay.start_time
        duration = time.strftime("%H:%M:%S", time.gmtime(duration))

        #Lazy import the class Questioner
        from game.questions_answers import Questioner

        #Calculate the score
        score = (Questioner.correct_answers / Questioner.question_number) * 100
        score = f"{score:.3f}"

        #Insert the messages in the Text widget
        self.text_object.insert(self.text_object.index("insert"), "\n\n")
        self.text_object.insert(self.text_object.index("insert"), "-"*37)
        self.text_object.insert(self.text_object.index("insert"), "END OF GAME")
        self.text_object.insert(self.text_object.index("insert"), "-"*37)
        
        self.text_object.insert(self.text_object.index("insert"), f"\nYou {status}")
        self.text_object.insert(self.text_object.index("insert"), f"\nScore : {score}")
        self.text_object.insert(self.text_object.index("insert"), f"\nDuration : {duration}")

        self.text_object.insert(self.text_object.index("insert"), f"\n\nType Restart(R) to restart the game or Home(H) to go to home screen.")

        #Make the text field uneditable
        self.text_object.config(state = "disabled")

        #Flag to indicate the end of the game
        GamePlay.game_on = False
        GamePlay.should_restart_game = True

    #Method to restart the game or go to home page
    def end_options(self):
        #Fetch the response from the Entry widget
        response = self.entry_object.get().lower().strip()

        #Make the Text widget editable
        self.text_object.config(state = "normal")

        #Always accept new lines at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #No reply to input message
        if not response:
            return
        
        if response in ["r", "restart"]:
            #Insert the response in the Text widget
            self.text_object.insert(self.text_object.index("insert"), "\n\n")
            self.text_object.insert(self.text_object.index("insert"), response.capitalize())

            #Fetch the number of the line where the message will be inserted
            pos = self.text_object.index("insert + 1 line")
            self.text_object.insert(pos, "\n\nRestarting the game.\nStart clicking..\n")
            self.text_object.see(tk.END)

            #Fetch the end of the line where the output is inserted
            end_pos = self.text_object.index("insert lineend")

            #Right align the output by applying tag
            self.text_object.tag_add("right", pos, end_pos)
            self.text_object.tag_configure("right", justify = "right")

            #Lazy import the class Tables
            from options import Tables
            
            #Clear the tables
            for table in Tables.all_tables:
                for row in table.get_children():
                    table.delete(row)

            #Lazy import the classes Character and TopFramePacker and the function reset
            from game import Character
            from options import TopFramePacker
            from game.reset_attributes import reset

            #Reset the attributes
            reset()

            #Update the labels displaying the points
            TopFramePacker.player_points.config(text = f"Current Points :\n{Character.player_handler.points}")
            TopFramePacker.monster_points.config(text = f"Current Points :\n{Character.system_points}")

            #Change the value of the flag to True
            GamePlay.game_on = True

            #Clear the entry object
            self.entry_object.delete(0, tk.END)

            #Make the text field uneditable
            self.text_object.config(state = "disabled")

        elif response in ["h", "home"]:
            #Lazy import the class Chat, Tables and TopFramePacker and the function reset
            from game.conversation import Chat
            from options import Tables, TopFramePacker
            from game.reset_attributes import reset

            #Reset the flag to True
            Chat.initial_response = True

            #Reset the attributes
            reset()

            #Clear the lists/dictionary
            TopFramePacker.buttons_list.clear()
            TopFramePacker.buttons_commands.clear()
            Tables.all_tables.clear()

            #Create a Home class object
            home = Home(AppWindow.main_window)
            home.create_menu() 