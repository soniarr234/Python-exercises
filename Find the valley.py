"""
The user enters numbers until entering a 0.
The program should indicate if there is a flat zone.
A flat zone occurs when there are three consecutive identical numbers.
"""

num = None
numbers = []
zona_plana = False

while num != 0:
  num = int(input ("Introduce un número"))
  if num != 0:
    numbers.append(num)

for i in range (1, len (numbers)-1):
  if numbers [i] == numbers [i-1] and numbers [i] == numbers [i+1]:
    zona_plana = True
    break

if zona_plana:
  print ("Hay una zona plana")
else:
  print ("No hay una zona plana")
