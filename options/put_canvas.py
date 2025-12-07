from widgets import CanvasWidget, FrameWidget

#Function to place canvas along with inner frame inside a main frame and make it scrollable
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

    return canvas.canvas, inner_frame.frame