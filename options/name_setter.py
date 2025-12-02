from tkinter import messagebox
#Lazy import for GameSetup

#Class to dynamically accept input on key press
class EnterName:
    #Initialised the class attributes
    x_pos = 10
    cursor_pos = 0          
    char_list = []              #List of characters of the name

    #Dicitonary storing characters as values to replace the given string names on key press
    to_replace = {"space" : " ", "underscore" : "_", "at" : "@", "dollar" : "$", "minus" : "-", "grave" : "`", 
                      "exclam" : "!", "ampersand" : "&", "apostrophe" : "'", "period" : ".", "slash" : "/"}

    #Initialised the window and canvas as instance attributes
    def __init__(self, window = None, canvas = None):
        self.root = window
        self.canvas = canvas

    #Method to set name
    def set_name(self, event):
        #Assign to the variable the symbolic name of the key press
        key = event.keysym

        modifier_keys = ["Caps_Lock", "Shift_L", "Shift_R", "Super_L", "Control_L", "Alt_L", "Alt_R", "Meta_L", "Meta_R", "Tab", 
                        "Up", "Down", "Escape"]

        invalid_keys = ["backslash", "bar", "braceleft", "braceright", "bracketleft", "bracketright", "parenleft", "parenright", 
                        "plus", "equal", "asterisk", "asciicircum", "percent", "numbersign", "asciitilde", "quotedbl", "colon", 
                        "semicolon", "comma", "less", "greater", "question"]

        if key in modifier_keys:
            return
        
        if key in invalid_keys:
            messagebox.showinfo(message = "Invalid character for name.", parent = self.root)
            return
        
        if key != "BackSpace":
            #Return if the length of name exceeds 20 characters
            if len(self.char_list) >= 20:
                messagebox.showinfo(message = "Length of name cannot exceed 20 characters.", parent = self.root)
                return
            
            #Embed the character in canvas
            if key in self.to_replace:
                replaced_key = self.to_replace.get(key, None)
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
            self.cursor_pos += 1                    #Increase the cursor position

            #Append the char with its width to the character list
            self.char_list.append((key, char, width))

        #If Backspace/delete is pressed, delete the character at cursor position
        elif key == "BackSpace":
            if not self.char_list:
                self.x_pos = 10
                return
            
            #Delete the character
            self.canvas.delete(self.char_list[self.cursor_pos-1][1])

            #Update the position
            self.x_pos -= self.char_list[self.cursor_pos-1][2]

            #Remove the deleted character from the list
            self.char_list.remove(self.char_list[self.cursor_pos-1])

            #Update the cursor position
            if self.x_pos == 10:
                self.cursor_pos = 0
                return

            self.cursor_pos -= 1

    #Method to convert all the entered characters to a single text
    def compile_name(self, setup = False):
        name = [item[0] for item in self.char_list]
        
        for index, char in enumerate(name):
            if char in self.to_replace:
                name[index] = self.to_replace.get(char, None)

        #Join all the elements of the list into a single name
        name = "".join(name)

        if name:
            if setup:
                #Lazy importing
                from options.game_setup import GameSetup

                game_setup = GameSetup(self.root)
                game_setup.layout()
            
            else:
                return word
            
        else:
            if setup:
                from options.game_setup import GameSetup
                obj = GameSetup(self.root)
                obj.layout()
            
            else:
                word = "Anonymous"
                return word