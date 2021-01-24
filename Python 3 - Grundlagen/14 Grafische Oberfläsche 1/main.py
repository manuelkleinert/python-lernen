from tkinter import *

master=Tk()

halloLabel=Label(
    master,
    bg='#998899', # Background "background"
    borderwidth=1, # Border Size
    cursor='hand1', # Cursor https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm
    font='Verdana 12', # Font type and size
    foreground='#000055', # Foreground color for the widget. This can also be represented as fg foreground
    relief=SOLID,
    text='Hallo Welt')

halloLabel.place(x=10,y=10)

halloEntry=Entry(
    master,
    bg='#998899', # Background "background"
    borderwidth=1, # Border Size
    cursor='hand1', # Cursor https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm
    font='Verdana 12', # Font type and size
    foreground='#000055', # Foreground color for the widget. This can also be represented as fg foreground
    relief=SOLID)

halloEntry.place(x=10,y=100)

master.mainloop()
