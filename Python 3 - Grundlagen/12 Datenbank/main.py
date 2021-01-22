import sqlite3

connection = sqlite3.connect('bmi.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE bmirechner(name Text, bmi REAL)''')
cursor.execute('''INSERT INTO bmirechner VALUES(?,?)''',('Manuel',1.8))
cursor.execute('''INSERT INTO bmirechner VALUES(?,?)''',('Pinki',0.6))
cursor.execute('''INSERT INTO bmirechner VALUES(?,?)''',('Pinki',0.6))

cursor.execute('''SELECT name,bmi FROM bmirechner''')
rows=cursor.fetchall()

print(rows)
cursor.close()

input('end')
