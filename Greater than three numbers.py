"""
Ask the user for three numbers and display which is the largest.
"""

'''
numbers = []
for x in range (3):
  number = input ("Enter a number")
  number = int (number)
  numbers.append(number)
  if numbers [0] > numbers [1] and numbers [0] > numbers [2]:
    print ("El número", numbers [0], " es el mayor")
  elif numbers [1] > numbers [0] and numbers [1] > numbers [2]:
    print ("El número", numbers [1], "es el mayor")
  else:
    print ("El número", numbers [2],"es el mayor")
'''    
#---------------------------------------------------------------

numbers = []
for x in range (3):
  number = input ("Enter a number")
  number = int (number)
  numbers.append(number)
  mayor = numbers [0]

for number in numbers [1:]:
  if mayor < number:
    mayor = number

print (mayor, "es el mayor")
I
