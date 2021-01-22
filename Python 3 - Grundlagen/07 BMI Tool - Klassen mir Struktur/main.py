#!/usr/bin/phyton

# import bmi
# benutzer=bmi.Benutzer()
# bmirechner=bmi.Bmirechner()

from bmi import Benutzer,Bmirechner

benutzer=Benutzer()
bmirechner=Bmirechner()

while True:
    try:
        bmi=bmirechner.rechnen(benutzer.groesse)
        if not bmi:
            break
    except ValueError:
        print('Gewicht falsch angegeben!')
        continue
    bmirechner.auswerten(bmi)
    bmirechner.hinzufuegen(benutzer.name,bmi)
bmirechner.ausgeben()

help(Benutzer)
input('ENDE')
