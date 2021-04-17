# This is a Hello World Program in Tkinter.
# This gives a basic overview of how to program with Tkinter.
# Essentially, the steps can be broken down into these:
#   >   Import tkinter
#   >   Create a Main Application Window (Using Tk class. It should only be called ONCE)
#   >   (Optional) Create a Application class. Everything will be done inside that class
#   >   Add widgets, like menus, buttons, labels to your GUI window
#   >   Invoke the main event loop so the actions take place on user's screen
#
# Similarly, every widget that we add also follows the procedure:
#   >   Widget class inherits from base tkinter class (Skip this if you use tkinter class directly)
#   >   Invoke constructor with master passed in
#   >   Configure properties and implementation (Styles, Functions)
#   >   Geometry method, like pack(), place(), grid()...


import tkinter as tk


# The Top level application class (just below Tk() instance). Inherits Frame class
class HelloWorldApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)        # Since we inherit Frame class, we shall invoke parent constructor
        self.master = master
        self.pack()                     # Geometry method so this top level widget is drawn on screen

        self.create_widgets()

    def create_widgets(self):
        self.hi_btn = tk.Button(self)
        self.hi_btn['text'] = "Hello World\n(Click me)"
        self.hi_btn['command'] = self.say_hi
        self.hi_btn.pack(side='top')

        self.quit_btn = tk.Button(self, text='QUIT',
                              fg='red', command=self.master.destroy)
        self.quit_btn.pack(side='bottom')

    def say_hi(self):
        print("Hello Welcome to Tkinter")
        self.destroy()


root = tk.Tk()                      # Top level application window
app = HelloWorldApp(master=root)
app.mainloop()                      # Invoke the main event loop