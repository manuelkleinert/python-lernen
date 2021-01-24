from tkinter import *

master=Tk()

nameFrame=Frame(master)
nameFrame.pack()
nameLabel=Label(nameFrame,anchor=W,text='Name:',width=30)
nameLabel.pack(side='left')
nameEntry=Entry(nameFrame,width=30)
nameEntry.pack(side='right')

groesseFrame=Frame(master)
groesseFrame.pack()
groesseLabel=Label(groesseFrame,anchor=W,text='Körbergrösse:',width=30)
groesseLabel.pack(side='left')
groesseEntry=Entry(groesseFrame,width=30)
groesseEntry.pack(side='right')

buttonFrame=Frame(master)
buttonFrame.pack()
okButton=Button(buttonFrame,text='OK',width=20)
okButton.pack(side='left')

cancelButton=Button(buttonFrame,text='Abbrechen',width=20)
cancelButton.pack(side='right')

master.mainloop()
