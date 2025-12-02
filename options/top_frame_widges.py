from widgets import FrameWidget, LabelWidget, CanvasWidget
from scroll import ScrollEnabler
from options.name_setter import EnterName

#Function to place the canvas inside a frame and make it scrollable
def place_canvas(frame):
    #Grid layout management for the frame
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1)

    #Creating canvas
    canvas = CanvasWidget(frame, highlightthickness = 0, row = 0, column = 0, sticky = "nsew")

    #Creating inner frame inside canvas
    inner_frame = FrameWidget(canvas.canvas)
    canvas_window = canvas.canvas.create_window(0, 0, window = inner_frame.frame, anchor = "nw")

    #Function to expand the inner frame inside the canvas
    def on_resize(event):
        canvas.canvas.itemconfig(canvas_window, width = event.width, height = event.height)
    
    #Bind the function to the canvas
    canvas.canvas.bind("<Configure>", on_resize)

    #Function to dynamically update scroll region
    def update_scroll_region(event = None):
        # Get the required width of the inner frame and canvas
        frame_width = inner_frame.frame.winfo_reqwidth()
        canvas_width = canvas.canvas.winfo_width()
        
        # Set window width to max of canvas width or content width
        canvas.canvas.itemconfig(canvas_window, width=max(canvas_width, frame_width))

        #Coordinates of smallest bounding rectangle containing canvas items
        bbox = canvas.canvas.bbox("all")

        if bbox:
            x, y = bbox[2:]

            #Assign scroll region
            canvas.canvas.config(scrollregion = (0, 0, max(x, canvas_width), max(y, canvas.canvas.winfo_height())))

    #Bind the method to update scroll region to inner_frame
    inner_frame.frame.bind("<Configure>", update_scroll_region)

    return canvas, inner_frame

#Function to pack widgets in game setup's top frame
def pack_top_frame(frame):
    #Grid layout management for the frame
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1)
    frame.columnconfigure(1, minsize = 800)
    frame.columnconfigure(2, weight = 1)

    #Creating top left frame
    top_left_frame = FrameWidget(frame, borderwidth = 5, relief = "solid", row = 0, column = 0, sticky = "nsew")

    #Creating canvas and inner frame inside the top left frame
    canvas1, i_frame1 = place_canvas(top_left_frame.frame)
    i_frame1.frame.config(bg = "red")

    #Grid layout management for the inner frame inside top left frame
    for i in range(2):
        i_frame1.frame.rowconfigure(i, weight = 1)

    #Fetch the name of the player
    name = EnterName()
    player_name = name.compile_word(setup=False)

    #Display the name of the player
    LabelWidget(i_frame1.frame, text = f"Player (You):\n{player_name}", font = ("Helvetica", 30), justify = "left", 
                         bg = "red", fg = "white", row = 0, column = 0, sticky = "nw")

    #Enable horizontal scrolling in top left frame
    scroll_enabler = ScrollEnabler(canvas1.canvas, horizontal = True)
    scroll_enabler.enable_scrolling()

    #Creating top mid frame
    top_mid_frame = FrameWidget(frame, borderwidth = 5, bg = "white",  relief = "solid", row = 0, column = 1, sticky = "nsew")

    #Creating top right frame
    top_right_frame = FrameWidget(frame, borderwidth = 5, relief = "solid", row = 0, column = 2, sticky = "nsew")

    #Creating canvas and inner frame inside the top left frame
    canvas2, i_frame2 = place_canvas(top_right_frame.frame)
    i_frame2.frame.config(bg = "green")

    #Grid layout management for the inner frame
    i_frame2.frame.columnconfigure(0, weight = 0)
    i_frame2.frame.columnconfigure(1, weight = 1)

    #Display the name of opponent (monster)
    LabelWidget(i_frame2.frame, text = f"Player :\nMonster", font = ("Helvetica", 30), justify = "right", 
                         bg = "green", fg = "white", row = 0, column = 1, sticky = "ne")
    
    #Update the positions of the widgets
    canvas2.canvas.update_idletasks()
    
    #Enable horizontal scrolling in top right frame
    scroll_enabler2 = ScrollEnabler(canvas2.canvas, horizontal = True)
    scroll_enabler2.enable_scrolling()