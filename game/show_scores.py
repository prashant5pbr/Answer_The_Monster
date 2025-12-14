import os
import sqlite3
from tkinter import ttk
from widgets import LabelWidget, TreeViewWidget
from home_screen import Home
import paths

#Class to display scores
class ScoreBoard:
    #Initialised the root as the instance attribute
    def __init__(self, window):
        self.root = window

    #Method to clear the screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #Method to display the scores
    def display_scores(self):
        #Clear the screen
        self.clear_screen()

        #Reset the grid layout
        for i in range(5):
            self.root.rowconfigure(i, weight = 0)
            self.root.columnconfigure(i, weight = 0)

        #Grid layout management for the root
        self.root.rowconfigure(0, minsize = 1)
        self.root.rowconfigure(1, weight = 1)
        self.root.columnconfigure(0, weight = 1)

        #Label to go back to the home screen
        go_back = LabelWidget(self.root, text = "\u21d0", font = ("Helvetica", 80), fg = "red", cursor = "hand2", 
                              row = 0, column = 0, sticky = "nw", padx = (25, 0), pady = (20, 0))
        
        #Create object of Home class
        home = Home(self.root)

        #Bind the given method to the given label
        go_back.label.bind("<Button-1>", lambda event : home.create_menu())
        self.root.bind("<Escape>", lambda event : home.create_menu())

        #Style configuration for the table and its heading
        style = ttk.Style()

        style.configure("Treeview", rowheight = 50, font = ("Academy Engraved LET", 20), 
                        background = "systemWindowBackgroundColor", fieldbackground = "systemWindowBackgroundColor", 
                         foreground = "red")
        
        style.configure("Treeview.Heading", font = ("Academy Engraved LET", 35), foreground = "red", 
                        background = "systemWindowBackgroundColor")
        
        #Create a table
        score_table = TreeViewWidget(self.root, show = "headings", row = 1, column = 0, sticky = "nsew", pady = (30, 0))

        #Check if the path to the database exists
        if os.path.exists(paths.DATA_PATH):
            #If the path exists, connect to the database
            with sqlite3.connect(paths.DATA_PATH) as connection:
                #Create cursor object
                cursor = connection.cursor()

                #Fetch the names of the columns
                columns_data = cursor.execute("pragma table_info(game_records)").fetchall()
                columns_names = [item[1] for item in columns_data]

                columns_names = [name.replace("_", " ") for name in columns_names]

                #Create placeholder for the columns
                columns_place = [f"Column-{i}" for i in range(len(columns_names))]
                score_table.tree["columns"] = columns_place

                #Create header row for the table
                for i, j in zip(columns_place, columns_names):
                    score_table.tree.heading(i, text = j)
                    score_table.tree.column(i, anchor="center", width = 250)

                #Fetch the data
                cursor.execute("select * from game_records")
                records = cursor.fetchall()

                #Insert the data
                for data in records:
                    score_table.tree.insert("", "end", values = data)

        #Function to disable the clicks or selection of rows in the table
        def block_selection(event):
            score_table.tree.selection_remove(score_table.tree.selection())

        #Bind the event to the function
        score_table.tree.bind("<<TreeviewSelect>>", block_selection)