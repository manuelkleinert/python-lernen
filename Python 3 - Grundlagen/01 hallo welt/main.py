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

# BMI calculate
print(name,'dein BMI ist',round(float(gewicht)/(float(koerpergroesse)**2),2))

input('Press Enter to Exit...')
