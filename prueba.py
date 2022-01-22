from datetime import datetime 
import locale



i = 0
while i < 5:
    fechaHora = datetime.now()
    #print(datetime.time())
    locale.setlocale(locale.LC_ALL, 'es-ES') 

    print(fechaHora.strftime("%A %d %B %Y %I:%M"))
    print(fechaHora.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h

    i +=1