#!/usr/bin/phyton

# String
name='Manuel'

# Int
zahl=12

# float
dezimalzahl=12.57568

# Tuples (faster, unchangeable, unmutable)
gewichte1=(76,76.5,80)
gewichte2=(65,64)
gewichte=(gewichte1,gewichte2)

# Arrays (list, changeable, mutable)
gewichte1=[76,76.5,80]
gewichte2=[65,64]

# Verschachteln
gewichte=[gewichte1,gewichte2]

# Kombinieren
gewichte=gewichte1+gewichte2

# Löschen
del gewichte[2]

# Ergänzen an position 0
gewichte.insert(0,75.8)

# löschen
gewichte.remove(76)

# Ergänzen
gewichte.append(76.5)

print(gewichte[1])

for gewicht in gewichte:
    print(gewicht)

# String
gruss='Hallo Wells'
print(gruss[2])
print(gruss[1:4])

if 'a' in gruss:
    print('gefunden')

print(len(gruss))
print(max(gruss))

print(gruss.count('l'))
print(gruss.index('W'))

gruss_neu=gruss.replace('l','n')
print(gruss_neu)

# String mit Platzhalter
str1 = "Das ist der Kurs '{0}' von {1}".format("Fortgeschrittene Python-Techniken", "Joe Marini und Ralph Steyer")
print(str1)

# String mit Platzhalter Templates (Sicherer)
from string import Template
templ = Template("Das ist der Kurs '${title}' von ${authors}")
str2 = templ.substitute(title='Fortgeschrittene Python-Techniken', authors="Joe Marini und Ralph Steyer")
print(str2)

# String mit Platzhalter Templates mit einem Liste (Sicherer)
data={
    "authors":"Joe Marini und Ralph Steyer",
    "title":"Fortgeschrittene Python-Techniken"
}
    
str3 = templ.substitute(data)
print(str3)


# Dictionary
datenspeicher={}
datenspeicher={'Alex':23.45,'Pinki':32.54}

print('Alex' in datenspeicher)

del datenspeicher['Alex']

datenspeicher.update({'Alex':25.45})
print(datenspeicher)

for i in datenspeicher.items():
    print(i)

for i in datenspeicher.values():
    print(i)

for i in datenspeicher.keys():
    print(i)

input('END')

# Set
s=set()
s.add(1)
s.add(2)
s.add(2)

print(s)
print(len(s))

s={1,2,3,4,5}
s.remove(3)
print(s)
s.clear()
print(s)

s2=s.copy()

s1={1,2,3,4}
s2={3,4,5,6}

# Schnittmänge
print(s1&s2)

# Vereinigungsmänge
print(s1|s2)

# ohne s2
print(s1-s2)

# Frozenset (faster, unchangeable, unmutable)
s=frozenset({1,2,3,4,5})
