import sqlite3
import os.path

'''
    Dokumentationen werden direkt under den Klassen oder Methoden definiert (Dockstring) diese können dann so über die help funktion abgefragt werden
    z.B. help(Benutzer)
'''

class Benutzer:
    ''' Repräsentiert einen BMI Benutzer '''
    def __init__(self,name,groesse):
        ''' Der Konstruktor eines Benutzers bei dem der Name und Körpergrösse abgefragt wird'''
        self.name=name
        self.groesse=groesse

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

    def rechnen(self,gr,ge):
        return round(float(ge)/(float(gr)**2),2)

    # Mit einem *b kann man einen Parameter optional deklarieren
    def auswerten(self,b):
        if b>=25:
            return 'Sie sind leider Übergewichtig!'
        elif b<18.5:
            return 'Sie sind leider Untergewichtig!'
        else:
            return 'Normalgewicht'

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
