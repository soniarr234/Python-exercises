"""
Ask for a number and show its multiplication table from 1 to 10
"""
number =int (input ("Enter a number"))
result = 0
for x in range (1, 11):
  result = number * x
  print (number, "x", x, "=", result)
