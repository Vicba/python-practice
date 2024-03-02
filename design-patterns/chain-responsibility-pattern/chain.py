class Event: 
    def __init__(self, name): 
        self.name = name 

    def __str__(self): 
        return self.name 

# Define a Widget class, a base class for handling events
class Widget: 
    def __init__(self, parent=None): 
        self.parent = parent 

    # Method to handle an event
    def handle(self, event): 
        # Create a handler string based on the event name
        handler = f'handle_{event}' 
        
        # Check if the current object has a method corresponding to the handler
        if hasattr(self, handler): 
            # If the method exists, get it and call it with the event
            method = getattr(self, handler) 
            method(event) 
        # If the current object does not have a corresponding method
        # and there is a parent object, delegate the handling to the parent
        elif self.parent is not None: 
            self.parent.handle(event) 
        # If there is no parent and there is a default handler, use it
        elif hasattr(self, 'handle_default'): 
            self.handle_default(event) 


class MainWindow(Widget): 
    # Method to handle a 'close' event
    def handle_close(self, event): 
        print(f'MainWindow: {event}') 

    # Default handler for unhandled events
    def handle_default(self, event): 
        print(f'MainWindow Default: {event}') 


class SendDialog(Widget): 
    # Method to handle a 'paint' event
    def handle_paint(self, event): 
        print(f'SendDialog: {event}') 


class MsgText(Widget): 
    # Method to handle a 'down' event
    def handle_down(self, event): 
        print(f'MsgText: {event}') 


def main(): 
    mw = MainWindow() 
    sd = SendDialog(mw) 
    msg = MsgText(sd) 

    for e in ('down', 'paint', 'unhandled', 'close'): 
        evt = Event(e) 

        print(f'Sending event -{evt}- to MainWindow') 
        mw.handle(evt) 

        print(f'Sending event -{evt}- to SendDialog') 
        sd.handle(evt) 

        print(f'Sending event -{evt}- to MsgText') 
        msg.handle(evt)


if __name__ == '__main__': 
    main()
