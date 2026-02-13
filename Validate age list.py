"""
The user enters ages (integers) up to -1.
The program must determine if the list is valid according to these rules:
- All ages must be greater than or equal to 0
All ages must be less than or equal to 120
- There must be at least one age
"""

user_num = None
isok = True
numbers = []
while user_num != -1:
  user_num = int (input ("Enter a number"))
  if user_num >= 0 and user_num <= 120:
    numbers.append(user_num)
    isok = False

if len (numbers) > 0 and isok:
  print ("La lista es valida: ", numbers)
else:
  print ("La lista NO es valida:", numbers)
