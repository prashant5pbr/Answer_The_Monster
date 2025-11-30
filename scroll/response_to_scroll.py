from scroll.vertical_wheel_scrolling import on_mousewheel_scroll
from scroll.key_up_scroll import v_scroll_up
from scroll.key_down_scroll import v_scroll_down
from scroll.horizontal_wheel_scrolling import on_mousewheel_side_scroll
from scroll.key_left_scroll import h_scroll_left
from scroll.key_right_scroll import h_scroll_right

#Class to make widgets respond to the events of mouse scroll and key press
class ScrollEnabler:
    #Initialised the scrollable object and the direction of scrolling (vertical/horizontal) as instance attributes
    def __init__(self, scrollable_object, vertical = False, horizontal = False):
        self.scrollable_object = scrollable_object
        self.vertical = vertical
        self.horizontal = horizontal

    #Method to bind the events to the scrollable object when mouse cursor is over it
    def on_enter(self, event):
        if self.vertical:
            self.scrollable_object.bind_all("<MouseWheel>", lambda e : on_mousewheel_scroll(e, self.scrollable_object))
            self.scrollable_object.bind_all("<Up>", lambda e : v_scroll_up(e, self.scrollable_object))
            self.scrollable_object.bind_all("<Down>", lambda e : v_scroll_down(e, self.scrollable_object))
        
        if self.horizontal:
            self.scrollable_object.bind_all("<Shift-MouseWheel>", lambda e : on_mousewheel_side_scroll(e, self.scrollable_object))
            self.scrollable_object.bind_all("<Left>", lambda e : h_scroll_left(e, self.scrollable_object))
            self.scrollable_object.bind_all("<Right>", lambda e : h_scroll_right(e, self.scrollable_object))

    #Method to unbind the events from the scrollable object when mouse cursor is not over it
    def on_leave(self, event):
        self.scrollable_object.unbind_all("<MouseWheel>")
        self.scrollable_object.unbind_all("<Up>")
        self.scrollable_object.unbind_all("<Down>")
        self.scrollable_object.unbind_all("<Shift-MouseWheel>")
        self.scrollable_object.unbind_all("<Left>")
        self.scrollable_object.unbind_all("<Right>")
    
    #Method to bind the given events to the given functions
    def enable_scrolling(self):
        self.scrollable_object.bind("<Enter>", self.on_enter)
        self.scrollable_object.bind("<Leave>", self.on_leave)