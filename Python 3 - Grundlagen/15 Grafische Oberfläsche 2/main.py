from tkinter import *

master=Tk()

nameLabel=Label(master,text='Name:')
# nameLabel.place(x=10,y=10)
nameLabel.pack(side='left') # Automatische anordnung

nameEntry=Entry(master)
# nameEntry.place(x=100,y=10)
nameEntry.pack(side='right')  # Automatische anordnung

master.mainloop()
