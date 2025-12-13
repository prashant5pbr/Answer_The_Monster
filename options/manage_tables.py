from tkinter import ttk
from widgets import TreeViewWidget
from game import Character
#Lazy import class Questioner

#Class to create and manage the tables
class Tables:
    #Defined the list to store all the created tables as class attribute
    all_tables = []

    #Initialised the class with the frame containing table as instance attribute
    def __init__(self, frame):
        self.frame = frame

    #Method to create table
    def create(self):
        #Grid layout management for the frame
        self.frame.rowconfigure(0, weight = 1)
        self.frame.columnconfigure(0, weight = 1)

        #Style configuration for the table and its heading
        style = ttk.Style()
        style.configure("Treeview", rowheight = 35)
        style.configure("Treeview.Heading", font = ("Helvetica", 15, "bold"))

        #Create a table
        self.table = TreeViewWidget(self.frame, show = "headings", row = 0, column = 0, sticky = "nsew")

        #Append the table to the list of all tables
        Tables.all_tables.append(self.table.tree)

        #Create placeholder in the table for the columns
        columns_place = ["A", "B", "C"]
        self.table.tree["columns"] = columns_place

        #Headers of the columns
        columns_names = ["No.", "+/-", "Points"]

        #Creating column headers for the table
        for i, j in zip(columns_place, columns_names):
            self.table.tree.heading(i, text = j)
            self.table.tree.column(i, anchor = "center", width = 50)

    #Method to insert data in the table
    @staticmethod
    def manage(answer = None):
        #Lazy import the class Questioner
        from game import Questioner

        #Fetch which number of question was asked
        q_no = Questioner.question_number

        #Fetch the table in which player's data will be inserted
        player_table = Tables.all_tables[0]

        #Fetch the updated points of the player
        p_updated_point = Character.player_handler.points

        #Fetch the table in which monster's data will be inserted
        monster_table = Tables.all_tables[1]

        #Fetch the updated points of the monster
        m_updated_point = Character.system_points

        #Points increment/decrement for the player and monster based on correct/incorrect answer
        if answer.lower() == "correct":
            p_point = "+5"
            m_point = "-5"

        elif answer.lower() == "incorrect":
            p_point = "-5"
            m_point = "+5"

        #Insert the data in the given tables
        player_table.insert("", "end", values = (q_no, p_point, p_updated_point))
        monster_table.insert("", "end", values = (q_no, m_point, m_updated_point))

        #Scroll the view to the end of the tables
        player_table.yview_moveto(1)
        monster_table.yview_moveto(1)