from tkinter import messagebox

#Class to dynamically accept input on key press
class EnterName:
    #Initial position as the class attribute
    x_pos = 8

    #Initialised the window and canvas as instance attributes
    def __init__(self, window, canvas):
        self.root = window
        self.canvas = canvas
        self.word_list = []

    #Method to set name
    def set_name(self, event, window):
        #Assign to the variable the symbolic name of the keypresses
        key = event.keysym

        modifier_keys = ["Caps_Lock", "Shift_L", "Shift_R", "Super_L", "Control_L", "Alt_L", "Alt_R", "Meta_L", "Meta_R", "Tab", 
                        "Up", "Down", "Escape"]

        invalid_keys = ["backslash", "bar", "braceleft", "braceright", "bracketleft", "bracketright", "parenleft", "parenright", 
                        "plus", "equal", "asterisk", "asciicircum", "percent", "numbersign", "asciitilde", "quotedbl", "colon", 
                        "semicolon", "comma", "less", "greater", "question"]
        
        to_replace = {"space" : " ", "underscore" : "_", "at" : "@", "dollar" : "$", "minus" : "-", "grave" : "`", 
                      "exclam" : "!", "ampersand" : "&", "apostrophe" : "'", "period" : ".", "slash" : "/"}

        if key in modifier_keys:
            return
        
        if key in invalid_keys:
            messagebox.showinfo(message = "Invalid character for name.", parent = window)
            return
        
        if key != "BackSpace":
            #Embed the character in canvas
            if key in to_replace:
                replaced_key = to_replace.get(key, None)
                char = self.canvas.create_text(self.x_pos, 65, text = replaced_key, font = ("Academy Engraved LET", 30), 
                                           fill = "red", anchor = "nw")
                
            else:
                char = self.canvas.create_text(self.x_pos, 65, text = key, font = ("Academy Engraved LET", 30), 
                                           fill = "red", anchor = "nw")

            #Coordinates of smallest bounding rectangle containing canvas items
            bbox = self.canvas.bbox(char)
            width = bbox[2] - bbox[0]

            #Increase the position for the other character
            self.x_pos += width

            #Append the char with its width to the word list
            self.word_list.append((char, width))

        #If Backspace/delete is pressed, delete the right most character
        elif key == "BackSpace":
            if not self.word_list:
                self.x_pos = 8
                return
            
            #Delete the right most character
            self.canvas.delete(self.word_list[-1][0])

            #Update the position
            self.x_pos -= self.word_list[-1][1]

            #Remove the deleted character from the list
            self.word_list.pop()