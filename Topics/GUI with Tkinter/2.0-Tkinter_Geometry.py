# Reference
# http://tcl.tk/man/tcl8.5/TkCmd/contents.htm


# Tkinter comes with a collection of widgets. Here goes some of them:
#       > Button
#       > Canvas
#       > Checkbutton
#       > Entry
#       > Frame
#       > Label
#       > Listbox
#       > Menubutton
#       > Menu
#       > Message
#       > Radiobutton
#       > Scale
#       > Scrollbar
#       > Text
#       > Toplevel
#       > Spinbox
#       > PanedWindow
#       > LabelFrame
#       > tkMessageBox


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
        self.pack()


    def changeState(self, state):
        self.stateWindow.destroy() if self.stateWindow is not None else None

        if state == 1:
            self.stateWindow = PackWindow(self)
        elif state == 2:
            self.stateWindow = GridWindow(self)
        elif state == 3:
            self.stateWindow = PlaceWindow(self)
        elif state == 4:
            self.stateWindow = ReliefWindow(self)

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
            tk.Button(self, text='Bonus: Relief Styles', command=lambda: self.master.changeState(4) )
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



# place() Demonstration Window
class PlaceWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['height'] = 200
        self['width'] = 200
        self['bg'] = '#34495e'
        self['relief'] = tk.GROOVE
        self['borderwidth'] = 4

        self.text1 = tk.Label(self, text="Henlo", font=("Helvetica", "16", "bold"), fg='#27ae60')
        self.text2 = tk.Label(self, text="Hooman", font=("Helvetica", "16", "bold"), fg='#2980b9')
        self.text3 = tk.Label(self, text=":3", font=("Helvetica", "26", "bold"), fg='#f39c12')
        self.text1.place(x=100)
        self.text2.place(x=60, y=50)
        self.text3.place(x=70, y=100)



# Bonus: Relief styles
# Relief style are simply simulated 3D border styles on the border
# of the widget. Note that the border must have non-zero width to see the relief effect
class ReliefWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.btns = [
            tk.Button(self, text='FLAT', relief=tk.FLAT, borderwidth=4),
            tk.Button(self, text='RAISED', relief=tk.RAISED, borderwidth=4),
            tk.Button(self, text='SUNKEN', relief=tk.SUNKEN, borderwidth=4),
            tk.Button(self, text='GROOVE', relief=tk.GROOVE, borderwidth=4),
            tk.Button(self, text='RIDGE', relief=tk.RIDGE, borderwidth=4),
        ]
        for btn in self.btns:
            btn.pack( ipadx=15, ipady=5, pady=5 )




root = tk.Tk()
root.title('Tkinter Geometry')
app = MainApplication(root)
root.mainloop()






