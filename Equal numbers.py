"""
The user enters numbers until entering a 0.
The program should indicate if the user ever enters two identical numbers consecutively.
"""

num=None
numbers = []
iguales = False

while num != 0:
  num = int(input ("Introduce un número"))
  if num != 0:
    numbers.append(num)

for i in range (len (numbers)-1):
  if numbers [i] == numbers [i+1]:
    iguales = True
    break

if iguales:
  print ("Si hay iguales seguidos")
else:
  print ("No hay iguales seguidos")
