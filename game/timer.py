import tkinter as tk
from game.create_character import Character
#Lazy imported classes TopFramePacker, BottomFramePacker and Tables

#Class to give countdown effect inside a Text widget
class CountDown:
    #Class attributes to determine if the timer has been stopped and if the time is up
    stop_timer = False
    time_up = False

    #Initialised the instance attribute with Text widget inside game layout's bottom frame
    def __init__(self):
        #Lazy import the class BottomFramePacker
        from options import BottomFramePacker

        self.text_object = BottomFramePacker.text_handler
        self.entry_object = BottomFramePacker.entry_handler

    #Method to start the timer
    def start(self):
        #Reset the flags everytime the timer starts
        CountDown.stop_timer = False
        CountDown.time_up = False

        #Lazy import the class TopFramePacker
        from options import TopFramePacker

        #Disable the command for each button of the game layout's botom frame
        for button in TopFramePacker.buttons_list:
                button.button.config(command = lambda : None) 
        
        #Fetch the current position of the cursor
        pos = self.text_object.index("insert")

        #Insert the given number in the current cursor position
        self.text_object.insert(pos, 10)

        #Fetch the end position of the line where the current cursor position is located
        end_pos = self.text_object.index(f"{pos} lineend")

        #Right align the text in the selected range
        self.text_object.tag_add("right", pos, end_pos)
        self.text_object.tag_configure("right", justify = "right")

        #Call the timer method after the delay of 1000 ms (1 second)
        self.text_object.after(1000, lambda : self.timer(10))

    #Method to continue the timer
    def timer(self, num):
        #Return if the timer has stopped
        if CountDown.stop_timer:
            return
        
        #Make the text field editable
        self.text_object.config(state="normal")

        #Always accept new line at the bottom of the text
        self.text_object.mark_set("insert", tk.END)

        #Fetch the start and end of the line where the number will be inserted
        line_start = self.text_object.index("insert linestart")
        line_end = self.text_object.index("insert lineend")

        #Delete the previous number
        self.text_object.delete(line_start, line_end)

        #Display time's up message
        if num == 1:
            #Change the state of the flags
            CountDown.stop_timer = True
            CountDown.time_up = True

            #Make the text field editable
            self.text_object.config(state="normal")

            #Insert the time up message in the Text widget
            self.text_object.insert(line_start, "Time's up ⏰!!!\n")

            #Scroll the view to the end of the Text widget
            self.text_object.see(tk.END)

            #Right align the text in the selected range
            self.text_object.tag_add("right", line_start, line_end)
            self.text_object.tag_configure("right", justify = "right")

            #Insert the message
            self.text_object.insert(f"{line_start} + 1 line", "\n❌ You could not answer in time.\nMonster gains your 5 points.\n")

            #Update the labels displaying points
            Character.player_handler.adjust_points(answer = "incorrect")

            #Lazy import the classes TopFramePacker and Tables
            from options import TopFramePacker, Tables

            #Update the labels displaying the points
            TopFramePacker.player_points.config(text = f"Current Points :\n{Character.player_handler.points}")
            TopFramePacker.monster_points.config(text = f"Current Points :\n{Character.system_points}")

            #Update the tables
            Tables.manage(answer = "incorrect")

            #Scroll the view to the end of the Text widget
            self.text_object.see(tk.END)

            #Make the text field uneditable
            self.text_object.config(state="disabled")

            #Enable the command for each button of the game layout's botom frame
            for button in TopFramePacker.buttons_list:
                button.button.config(command = TopFramePacker.buttons_commands[button.button]) 

            return
        
        #Insert the next number
        self.text_object.insert(line_start, num - 1)

        #Right align the text in the selected range
        self.text_object.tag_add("right", line_start, line_end)
        self.text_object.tag_configure("right", justify = "right")
        
        #Recursively call the timer method after the delay of 1000 ms (1 second)
        self.text_object.after(1000, lambda : self.timer(num - 1))

        #Make the text field uneditable
        self.text_object.config(state="disabled")