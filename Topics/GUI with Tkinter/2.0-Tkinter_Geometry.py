# Reference
# http://tcl.tk/man/tcl8.5/TkCmd/contents.htm


# In tkinter, there are mainly 3 types of geometry, which is essentially specifying which function
# are used to arrange and position the widgets on display
# The 3 main ones are:
#       >   pack()
#       >   grid()
#       >   place()

# ====================
#       Pack
#=====================
# The pack() is the easiest to use, as we simply specifying the position relative to the parent widget.
# We have been using this geometry method so far. The arguments can be:
#
#   > expand (Bool) - Should it expand to consume extra space in master?
#   > fill (None,X,Y,Both) - Stretch slave vertically, horizontally or both to fill parcel
#   > side (left, right, top, bottom) - Which side of master the slave will be packed against
#   > ipadx, ipady (Amount) - Amount of internal padding (Pad in web terms)
#   > padx, pady (Amount) - Amount of external padding (Margin in web terms)


# ====================
#       Grid
#=====================
# As for grid, it gives you to arrange widgets in tabular form. See the arguments:
#
#   > column, row (N) - Put the widget at the Nth column/row
#   > columnspan, rowspan (N) - The widget will stretch across N rows/colums
#   > Sticky (N/S/E/W)+ - If the slave's cell is larger, determine how it positions (or stretch)
#                         Stretching is done when opposite direction is specified, like North and South
#   > ipadx, ipady (Amount) - Amount of internal padding (Pad in web terms)
#   > padx, pady (Amount) - Amount of external padding (Margin in web terms)


# ====================
#       Place
#=====================
# place() is like positioning absolute in web terms, relative to the container
#   > anchor (N/E/W/S/xy position) - Where the widget is positioned
#   > height/width (position) - Height and width in pixels
#   > relheight/relwidth (float [0,1]) - offset by how many percent relative to master container
#   > x/y (pixels) - Offset in pixels
#   > bordermode - The default value of the border type is INSIDE that refers to ignore the parent's inside the border.
#                   The other option is OUTSIDE.



import tkinter as tk


class MainApplication(tk.Frame):
    # Methods
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.stateWindow = None
        self.changeState(2)
        self.btnPane = SelectStateButton(self)
        self.btnPane.pack(side=tk.BOTTOM)
        self.pack(expand=True)

    def changeState(self, state):
        self.stateWindow.destroy() if self.stateWindow is not None else None

        if state == 1:
            self.stateWindow = PackWindow(self)
        elif state == 2:
            self.stateWindow = GridWindow(self)
        elif state == 3:
            self.stateWindow = None

        self.stateWindow.pack()




class SelectStateButton(tk.Frame):
    BTN_MARGIN = 10
    BTN_PADDING = 5

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.btns = (
            tk.Button(self, text='pack()', command=lambda: self.master.changeState(1) ),
            tk.Button(self, text='grid()', command=lambda: self.master.changeState(2) ),
            tk.Button(self, text='place()', command=lambda: self.master.changeState(3) ),
        )

        for btn in self.btns:
            btn.pack(side=tk.LEFT, padx=self.BTN_MARGIN,
                     pady=self.BTN_MARGIN, ipadx=self.BTN_PADDING)


# pack() Demonstration Window
class PackWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.left = tk.Label(self, text="LEFT", font=("Helvetica", "16", "bold"), fg='#27ae60' )
        self.right = tk.Label(self, text="RIGHT", font=("Helvetica", "16", "bold"), fg='#2980b9' )
        self.top = tk.Label(self, text="This is pack(), and this is TOP", font=("Helvetica", "30", "bold"),
                            fg='#8e44ad')
        self.bottom = tk.Label(self, text="BOTTOM", font=("Helvetica", "16", "bold"), fg='#f39c12' )

        self.left.pack(side=tk.LEFT)
        self.right.pack(side=tk.RIGHT)
        self.top.pack(side=tk.TOP, pady=(0, 100))
        self.bottom.pack(side=tk.BOTTOM)


# grid() Demonstration Window
class GridWindow(tk.Frame):
    BTN_PAD = 10

    class ToggleColorBtn(tk.Button):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.toggled = True
            self.toggle()
            self['command'] = self.toggle

        def toggle(self):
            self.toggled = not self.toggled
            if self.toggled:
                self['bg'] = '#e74c3c'
            else:
                self['bg'] = '#2ecc71'


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.buttons = [GridWindow.ToggleColorBtn(self) for i in range(25)]
        for i, b in enumerate(self.buttons):
            b.grid(column=i % 5, row=i // 5, ipadx=self.BTN_PAD, ipady=self.BTN_PAD)






root = tk.Tk()
root.title('Tkinter Geometry')
app = MainApplication(root)
root.mainloop()






