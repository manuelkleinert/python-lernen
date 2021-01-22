#!/usr/bin/phyton

def rechnen(gr):
    gewicht=input('Gewicht:')
    if not gewicht:
        return
    return round(float(gewicht)/(float(gr)**2),2)

# Mit einem * kann man einen Parameter optional deklarieren
def auswerten(*b):
    if b>=25:
        print('Sie sind leider Übergewichtig!')
    elif b<18.5:
        print('Sie sind leider Untergewichtig!')
    else:
        print('Normalgewicht')
        
# Mit einem = kann man einen Parameter vordefinieren
def hinzufuegen(n,b=0.0):
    if n in datenspeicher:
        bmis=datenspeicher[n]
    else:
        bmis=[]
    bmis.append(b)
    datenspeicher.update({n:b})

def ausgeben():
    for i in datenspeicher.items():
    print(i)


name=input('Name:')
print('Hallo',name,sep=' ')
groesse=input('Körpergrösse:')

datenspeicher={}

while True:
    try:
        bmi=rechnen(groesse)
        if not bmi:
            break

    except ValueError:
        print('Gewicht falsch angegeben!')
        continue

    # BMI calculate
    print(name,'dein BMI ist',bmi)

    auswerten(bmi)
    hinzufuegen(name,bmi)

ausgeben()

input('ENDE')
