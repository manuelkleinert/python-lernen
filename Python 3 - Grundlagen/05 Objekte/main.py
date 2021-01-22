class Benutzer:
    name=''
    groesse=0.0

    # Magische Methoden (kennzeichnung __) init wird auch als Construktor verwendet
    def __init__(self,name,groesse):
        self.name = name
        self.groesse = groesse
        print('init')

    # Methode mit einem verweis auf sich selbst (self)
    def anmelden(self):
        print('Anmeldung Benutzer:', self.name)

    # Magische Methode die beim löschen aufgerufen wird
    def __del__(self):
        print('ich werde gelöscht')

    # Magische Methode die definiert was ausgegeben wir wenn das Objekt als Print ausgegeben wird
    def __str__(self):
        return 'Benutzer: ' + self.name

# Klasse die alle eigenschaften von Benutzer erbt
class Administrator(Benutzer):
    kennwort=''
    def __init__(self,name,groesse,kennwort):
        self.name = name
        self.groesse = groesse
        self.kennwort = kennwort
        print('init')
    def __str__(self):
        return 'Benutzer: ' + self.name + ' hat das Kennwort ' + self.kennwort

benutzer1=Benutzer('Manuel', 1.80)
benutzer1.anmelden()
print(benutzer1)
del benutzer1

benutzer2=Administrator('Pinki',1.75,'123TestPw')
print(benutzer2)
