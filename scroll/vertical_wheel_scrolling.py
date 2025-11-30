#Function for behaviour of the scrollbar on vertical mouse scroll
def on_mousewheel_scroll(event, scrollable_object):
    if not scrollable_object.winfo_exists():
        return
        
    threshold = 1
    if abs(event.delta) > threshold:
        if event.delta > 0:                         #Scroll up
            scrollable_object.yview_scroll(-1, "units")

        elif event.delta < 0:                       #Scroll down
            scrollable_object.yview_scroll(1, "units")