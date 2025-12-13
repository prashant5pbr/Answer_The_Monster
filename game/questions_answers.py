import random
import copy
import tkinter as tk
from game.create_character import Character
from game.timer import CountDown
from game.all_questions import questions_data
#Lazy import classes Gameplayy, TopFramePacker, BottomFramePacker and Tables

#Class to insert questions and answers in the Text widget
class Questioner:
    #Class attributes
    questions = None
    question_number = 0
    current_question = None
    current_answer = None
    answer_ready = False
    reset_questions = False

    #Initialised the instance attribute with Text widget and Entry widget inside game layout's bottom frame
    def __init__(self):
        #Lazy import class BottomFramePacker
        from options import BottomFramePacker

        self.text_object = BottomFramePacker.text_handler
        self.entry_object = BottomFramePacker.entry_handler

    #Method to selected questions to be asked
    def ask_questions(self):
        if Questioner.questions is None or Questioner.reset_questions:
            Questioner.questions = copy.deepcopy(questions_data)

        #Create a list of questions only
        questions_list = list(Questioner.questions)
        
        #Randomly fetch a question
        Questioner.current_question = random.choice(questions_list)

        #Fetch the answer of the selected questions
        Questioner.current_answer = Questioner.questions[Questioner.current_question]

        #Delete the question from the dataset
        del Questioner.questions[Questioner.current_question]

        #Reset the flag to False
        Questioner.reset_questions = False

    #Method to insert questions in the Text widget
    def insert_question(self):
        #Call the method to ask questions
        self.ask_questions()

        #Update the question number
        Questioner.question_number += 1

        #Fetch the randomly selected question
        selected_question = Questioner.current_question

        #Always accept new line at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #Fetch the cursor position to insert the line
        pos = self.text_object.index("insert")

        #Insert the question in the Text widget
        self.text_object.insert(pos, f"What's {selected_question.lower()}?\n")

        #Fetch the end of the line where the output is inserted
        end_pos = self.text_object.index(f"{pos} lineend")

        #Right align the output by apply tag
        self.text_object.tag_add("right", pos, end_pos)
        self.text_object.tag_configure("right", justify = "right")

        #Ready to fetch and insert the answer
        Questioner.answer_ready = True

    #Method to insert answers in the Text widget
    def insert_answer(self):
        #Fetch the response from the Entry widget
        response = self.entry_object.get().lower().strip()

        #Make the Text widget editable
        self.text_object.config(state = "normal")

        #Always accept new line at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #Fetch the cursor position to insert the line
        pos = self.text_object.index("insert linestart")

        #Delete the content of the given line
        self.text_object.delete(pos, f"{pos} lineend")

        #Lazy import class TopFramePacker and Tables
        from options import TopFramePacker, Tables
        
        #No reply to input message
        if not response:
            return
        
        #Return if the time is up
        if CountDown.time_up:
            #Don't accept the answer after time is up
            Questioner.answer_ready = False
            return
        
        #Message for correct answer
        elif response == Questioner.current_answer:
            #Update the flags
            CountDown.stop_timer = True
            CountDown.time_up = False

            #Update the points of the player and the monster
            Character.player_handler.adjust_points(answer = "correct")

            #Update the labels displaying the points
            TopFramePacker.player_points.config(text = f"Current Points :\n{Character.player_handler.points}")
            TopFramePacker.monster_points.config(text = f"Current Points :\n{Character.system_points}")

            #Message to be inserted
            message = f"You entered : {response}.\n✅ That's correct.\nYou gain Monster's 5 points."

            #Update the tables
            Tables.manage(answer="correct")

            #Don't accept the answer after time is up
            Questioner.answer_ready = False

        #Message for incorrect answer
        else:
            #Update the flags
            CountDown.stop_timer = True
            CountDown.time_up = False

            #Update the points of the player and the monster
            Character.player_handler.adjust_points(answer = "incorrect")

            #Update the labels displaying the points
            TopFramePacker.player_points.config(text = f"Current Points :\n{Character.player_handler.points}")
            TopFramePacker.monster_points.config(text = f"Current Points :\n{Character.system_points}")

            #Message to be inserted
            message = f"You entered : {response}.\n❌ That's incorrect.\nMonster gains your 5 points."

            #Update the tables
            Tables.manage(answer="incorrect")

            #Don't accept the answer after time is up
            Questioner.answer_ready = False

        #Insert the message in the Text widget
        self.text_object.insert(self.text_object.index("insert"), f"\n{message}\n")

        #Check if any character's points has become zero
        Character.check_points()

        #Scroll the view to the end of the Text widget
        self.text_object.see(tk.END)

        #Delete the content of the given line
        self.entry_object.delete(0, tk.END)

        #Make the text widfet uneditable
        self.text_object.config(state = "disabled")

        #Enable the command for each button of the game layout's botom frame
        for button in TopFramePacker.buttons_list:
            button.button.config(command = TopFramePacker.buttons_commands[button.button])