#Function for behaviour of the scrollbar on horizontal mouse scroll
def on_mousewheel_side_scroll(event, scrollable_object):
    if not scrollable_object.winfo_exists():
        return
    
    threshold = 1
    if abs(event.delta) > threshold:
        if event.delta > 0:                         #Scroll Left
            scrollable_object.xview_scroll(-1, "units")

        elif event.delta < 0:                       #Scroll Right
            scrollable_object.xview_scroll(1, "units")