import sqlite3
import os.path

'''
    Dokumentationen werden direkt under den Klassen oder Methoden definiert (Dockstring) diese können dann so über die help funktion abgefragt werden
    z.B. help(Benutzer)
'''

class Benutzer:
    ''' Repräsentiert einen BMI Benutzer '''
    def __init__(self):
        ''' Der Konstruktor eines Benutzers bei dem der Name und Körpergrösse abgefragt wird'''
        self.name=input('Name:')
        self.groesse=input('Körpergrösse:')

class Bmirechner:
    ''' Repräsentiert einen BMI Rechner '''
    def __init__(self):
        self.datenspeicher={}

        # Create DB
        if not os.path.exists('bmi.db'):
            connection=sqlite3.connect('bmi.db')
            cursor=connection.cursor()
            cursor.execute('''CREATE TABLE bmirechner(name Text, bmi REAL)''')
        else:
            connection=sqlite3.connect('bmi.db')
            cursor=connection.cursor()
            cursor.execute('''SELECT name,bmi FROM bmirechner''')
            rows=cursor.fetchall()

            for row in rows:
                name=row[0]
                bmi=row[1]
                if name in self.datenspeicher:
                    bmis=self.datenspeicher[name]
                else:
                    bmis=[]

                bmis.append(bmi)
                self.datenspeicher.update({name:bmis})

    def rechnen(self,gr):
        gewicht=input('Gewicht:')
        if not gewicht:
            return
        return round(float(gewicht)/(float(gr)**2),2)

    # Mit einem *b kann man einen Parameter optional deklarieren
    def auswerten(self,b):
        if b>=25:
            print('Sie sind leider Übergewichtig!')
        elif b<18.5:
            print('Sie sind leider Untergewichtig!')
        else:
            print('Normalgewicht')

    # Mit einem = kann man einen Parameter vordefinieren
    def hinzufuegen(self,n,b=0.0):
        if n in self.datenspeicher:
            bmis=self.datenspeicher[n]
        else:
            bmis=[]
        bmis.append(float(b))
        self.datenspeicher.update({n:bmis})

        # Save to db
        connection=sqlite3.connect('bmi.db')
        cursor=connection.cursor()
        cursor.execute('''INSERT INTO bmirechner VALUES(?,?)''',(n,b))
        connection.commit()
        connection.close()

    def ausgeben(self):
        for i in self.datenspeicher.items():
            print(i)
