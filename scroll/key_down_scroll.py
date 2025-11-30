#Function to make scrollbar scroll on key press (Scroll Down)
def v_scroll_down(event, scrollable_object):
    if not scrollable_object.winfo_exists():
        return
    
    scrollable_object.yview_scroll(1, "units")