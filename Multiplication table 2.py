"""
Write the multiplication tables from 1 to 10
"""
multiplication = None
for i in range (1, 11):
  for j in range (1, 11):
    multiplication = i * j
    print (i, "x", j, "=", multiplication)
  print ("-----------------------")
