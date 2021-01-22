import time
import datetime

# Time
print(time.time())
print(time.asctime())

# struct time
t=time.localtime()
print(t)

print(t.tm_mday)

# Format Date
print("{0:02d}.{1:02d}.{2:02d}".format(t.tm_mday,t.tm_mon,t.tm_year))

# Datetime
# Aktuelles Datum
datum = datetime.date.today()
print(str(datum.day)+'.'+str(datum.month)+'.'+str(datum.year))

# Datum manuell erfassen
datum2 = datetime.date(2015,1,15)
print(str(datum2.day)+'.'+str(datum2.month)+'.'+str(datum2.year))

# Monat überschreiben
datum3 = datum2.replace(month=5)
print(str(datum3.day)+'.'+str(datum3.month)+'.'+str(datum3.year))

time = datetime.time(10,20,0)
print(time)
time2 = time.replace(hour=15)
print(time2)

zeitstempel1 = datetime.datetime(2015,1,15,10,20,0)
print(zeitstempel1)

zeitstempel2 = datetime.datetime.now()
print(zeitstempel2)

# Differenz
print(zeitstempel2-zeitstempel1)

input('END')
