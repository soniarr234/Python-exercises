"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 - La función recibirá dos String y retornará un Int.
 - La diferencia en días será absoluta (no importa el orden de las fechas).
 - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

from datetime import datetime

def countDays(date1, date2):
  try:
    new_date1 = datetime.strptime(date1, "%d/%m/%Y")
    new_date2 = datetime.strptime(date2, "%d/%m/%Y")
    subtraction = new_date1 - new_date2
    days = abs(subtraction.days)
    return days
  except:
    raise
    

date1 = "26/05/2026"
date2 = "27/02/2026"
print(countDays(date1, date2))
