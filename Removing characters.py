"""
Create a function that takes two strings as parameters (strl, str2) and prints two other strings as output (out1, out2).
- outl will contain all the characters present in strl but NOT present in str2.
- out2 will contain all the characters present in str2 but NOT present in strl.
print (j, end=' ')
"""

strl = "hola"
str2 = "adios"
out1=""
out2=""

#Camino facil
for i in str1:
    if i not in str2:
        out1 = out1 + i
print (out1)

#Camino dificil
encontrado = False

for i in str1:
    encontrado = False
    for j in str2:
        if i == j:
            encontrado = True
            break
    if not encontrado:
        outl += i

print (out1)
