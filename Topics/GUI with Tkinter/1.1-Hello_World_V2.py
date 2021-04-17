import tkinter as tk


class HelloWorldApplicationV2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.stateWindow = None
        self.switchState(1)
        self.pack()

    # State 1: Welcome screen. State 2: Home screen
    def switchState(self, state):
        self.stateWindow.destroy() if self.stateWindow is not None else None

        if state == 1:
            self.stateWindow = WelcomeScreen(self)
        elif state == 2:
            self.stateWindow = HomeScreen(self)

        self.stateWindow.pack()





class WelcomeScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.label = tk.Label(self, text="Welcome to Hello World Application!")
        self.button = tk.Button(self, text='Click to enter application', command = lambda: self.master.switchState(2) )
        self.label.pack()
        self.button.pack()


class HomeScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.label = tk.Label(self, text="Press Button Below for Hello World!", fg='Red')
        self.button = tk.Button(self, text="Hello!", command=HomeScreen.printHello )
        self.exit = tk.Button(self, text='Exit', command=root.quit)

        self.label.pack()
        self.button.pack()
        self.exit.pack()

    @staticmethod
    def printHello():
        print("Hello From Tkinter!")




root = tk.Tk()
main = HelloWorldApplicationV2(root)
main.mainloop()
