"""
Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
 - Utiliza el menor número de líneas para resolver el ejercicio.
"""

from datetime import datetime

def leapYears():
  actual_year = datetime.now().year
  list_year = []
  for i in range(actual_year, actual_year + 31):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
      list_year.append(i)
  return list_year

print(leapYears())
