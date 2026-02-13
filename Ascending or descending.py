"""
Ask the user for numbers until they enter 0.
Store the numbers in a list and determine if:
The list is sorted in ascending order
- The list is sorted in descending order
- The list is not sorted
Do not use sort (), sorted(), min (), or max()
"""

num = None
numbers = = []
ascendente = True
descendente = True

while num != 0:
  num = int(input ("Introduce un numero"))
  if num != 0: I
    numbers.append(num)

for i in range (len (numbers)-1):
  if numbers [i] < numbers [i+1]:
    descendente = False
  elif numbers [i] > numbers [i+1]:
    ascendente = False

if descendente:
  print ("Es descendente")
elif ascendente:
  print ("Es ascendente")
else:
  print ("Esta desordenada")
