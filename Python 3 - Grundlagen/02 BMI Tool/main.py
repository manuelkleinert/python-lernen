#!/usr/bin/phyton

'''
First project
Multiline comments
'''

#  single line comments

name=input('Name:')
print('Hallo',name,sep=' ')
koerpergroesse=input('Körpergrösse:')

bmi=0
bmis=[]
datenspeicher={}


# for i in range(1,11):
# while bmi<=18.5 or bmi>=25:
while True:
    gewicht=input('Gewicht:')

    if not gewicht:
        break
        # continue

    try:
        bmi=round(float(gewicht)/(float(koerpergroesse)**2),2)
    except ValueError:
        print('Gewicht falsch angegeben!')
        continue

    # BMI calculate
    print(name,'dein BMI ist',bmi)

    if bmi>=25:
        print('Sie sind leider Übergewichtig!')
    elif bmi<18.5:
        print('Sie sind leider Untergewichtig!')
    else:
        print('Normalgewicht')

    bmis.append(bmi)
    datenspeicher.update({name:bmis})

print(bmis)
print(datenspeicher)

for bmi in bmis:
    print('Errechnete BMI',bmi)

for i in datenspeicher.items():
    print(i)

input('ENDE')
