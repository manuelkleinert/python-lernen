from tkinter import *
from gesundheit.bmi import Benutzer,Bmirechner

class Rahmen(Frame):
    def __init__(self,master=None,labelText=''):
        Frame.__init__(self,master)
        self.pack()
        self.label=Label(self,anchor=W,text=labelText,width=30)
        self.label.pack(side='left')

        self.text=StringVar()
        # self.text.set('123')
        self.entry=Entry(self,width=30,textvariable=self.text)
        self.entry.pack(side='right')

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()

        self.nameFrame=Rahmen(master,'Name:')
        self.groesseFrame=Rahmen(master,'Körbergrösse:')
        self.gewichtFrame=Rahmen(master,'Gewicht:')

        self.buttonFrame=Frame(master)
        self.buttonFrame.pack()

        self.okButton=Button(self.buttonFrame,text='OK',width=20)
        self.okButton['command']=self.action
        self.okButton.pack(side='left')

        self.cancelButton=Button(
            self.buttonFrame,text='Abbrechen',width=20,command=root.destroy)
        self.cancelButton.pack(side='right')

        self.listbox=Listbox(master)
        self.listbox.pack(fill=BOTH)

    def action(self):
        benutzer=Benutzer(
            self.nameFrame.text.get(),
            self.groesseFrame.text.get())
        bmirechner=Bmirechner()
        bmi=bmirechner.rechnen(
            self.groesseFrame.text.get(),
            self.gewichtFrame.text.get())
        bmirechner.hinzufuegen(benutzer.name,bmi)

        self.listbox.delete(0,END)
        if benutzer.name in bmirechner.datenspeicher:
            bmis=bmirechner.datenspeicher[benutzer.name]
            for bmi in bmis:
                self.listbox.insert(
                END,
                benutzer.name+':'+
                str(bmi)+':'+
                bmirechner.auswerten(bmi))

root=Tk()
app=Application(master=root)
app.mainloop()
