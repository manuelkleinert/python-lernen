import os.path
import time
import shutil

p='D:/demo.txt'
kopie='D:/demo-kopie.txt'
verschoben='D:/demo-verschoben.txt'

# Create Fole
datei=open(p,'w')
datei.write('Pinki')
datei.close()

# Read File
datei=open(p)
zeile=datei.readlines()
print(zeile)
datei.close()

# Datem prüfen
if os.path.exists(p):
    print('File existiert')

    if os.path.isfile(p):
        print('File ist auch eine Datei')
        print('Grösse:',os.path.getsize(p))
        print('Editdate:',time.ctime(os.path.getmtime(p)))

# Datei kopieren und verschieben
shutil.copy(p,kopie)

if os.path.exists(kopie):
    print('Kopie wurde erstellt')
else:
    print('Kopie wurde nicht erstellt!')

# Datei verschieben
if os.path.exists(kopie):
    shutil.move(kopie,verschoben)

input('end')
