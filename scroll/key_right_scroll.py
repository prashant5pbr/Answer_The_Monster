#Function to make scrollbar scroll on key press (Scroll Right)
def h_scroll_right(event, scrollable_object):
    if not scrollable_object.winfo_exists():
        return
    
    scrollable_object.xview_scroll(1, "units")