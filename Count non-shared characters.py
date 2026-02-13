"""
This function takes two strings and returns how many characters from strl are NOT in str2, and vice versa.
You don't need to return the values, just count them.
Example:
str1="banana"
str2 = "manzana"
resultado = (1,2) --> 1 letter from strl is not in str2, 2 letters from str2 are not in stri
"""

str1="banana"
str2="manzana"
resultado = []
encontrado = False

for i in strl:
  encontrado = False
  for j in str2:
    if i = j:
        encontrado = True
        break
    if not encontrado:
      resultado.append(i)

for i in str2:
  encontrado = False
  for j in strl:
    if i = j:
      encontrado = True
      break
    if not encontrado:
      resultado.append(i)

for result in resultado:
  print (resultado)
