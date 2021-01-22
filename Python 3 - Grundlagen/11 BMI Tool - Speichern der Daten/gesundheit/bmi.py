import os.path
from ast import literal_eval

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

        # Daten einlesen
        if os.path.exists('D:/bmi.txt'):
            datei=open('D:/bmi.txt')
            for zeile in datei:
                parts=zeile.split(':')
                name=parts[0]
                bmis=literal_eval(parts[1])
                self.datenspeicher.update({name:bmis})
            datei.close()

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

        # Save data to file
        datei=open('D:/bmi.txt', 'w')
        for name in self.datenspeicher.keys():
            datei.write(name+':[')
            bmis = self.datenspeicher[name]
            first=True
            for bmi in bmis:
                if not first:
                    datei.write(',')
                datei.write(str(bmi))
                first=False
        datei.write(']\n')
        datei.close()

    def ausgeben(self):
        for i in self.datenspeicher.items():
            print(i)
