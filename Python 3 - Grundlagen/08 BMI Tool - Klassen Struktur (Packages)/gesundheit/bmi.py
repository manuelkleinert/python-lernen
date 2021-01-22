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

    def ausgeben(self):
        for i in self.datenspeicher.items():
            print(i)
