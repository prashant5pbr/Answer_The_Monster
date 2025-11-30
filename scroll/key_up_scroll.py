#Function to make scrollbar scroll on key press (Scroll Up)
def v_scroll_up(event, scrollable_object):
    if not scrollable_object.winfo_exists():
        return
    
    scrollable_object.yview_scroll(-1, "units")