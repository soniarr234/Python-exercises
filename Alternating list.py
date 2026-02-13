"""
Ask the user for numbers until they enter 0. Store these numbers in a list and determine if the list is alternating.
*An alternating list is: An even number followed by an odd number, then an even number, and so on... or vice versa
"""

number = None
numbers = []
alternante = True

while number != 0:
  number = int(input ("Enter a number"))
  if number != 0:
    numbers.append(number)

for i in range (len (numbers)-1):
  print (numbers)
  if numbers [i]%2==0 and numbers [i+1] 82 = 1 or numbers [i]%2== 1 and numbers [i+1] 82 = 0:
    print ("Son alternantes")
  else:
    alternante = False
    print ("No son alternantes")
    break
