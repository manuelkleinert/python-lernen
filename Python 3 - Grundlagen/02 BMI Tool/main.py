#!/usr/bin/phyton

'''
First project
Multiline comments
'''

#  single line comments

name=input('Name:')
print('Hallo',name,sep=' ')

gewicht=input('Gewicht:')
koerpergroesse=input('Körpergrösse:')
bmi=round(float(gewicht)/(float(koerpergroesse)**2),2)

# BMI calculate
print(name,'dein BMI ist',bmi)

if bmi>=25:
    print('Sie sind leider Übergewichtig!')
elif bmi<18.5:
    print('Sie sind leider Untergewichtig!')
else:
    print('Normalgewicht')

input('Press Enter to Exit...')
