"""
Enter numbers up to 0.
Store them in a list and say whether the order is ascending or not.
"""
num_user = None
numbers = []
ordenada = True
while num_user != 0:
  num user = int (input ("Introduce un numero"))
  if num_user != 0:
    numbers.append (num_user)

for i in range (len (numbers)-1):
  if numbers [i] > numbers [i+1]:
    ordenada = False
    print ("No es ascendente")
    break
