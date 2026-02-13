"""
Write a function that takes two strings as input and returns a string containing all the characters that appear in exactly one of the two strings, but not both.

Example:
strl = "hola"
str2 = "adios"
result = "hldis"
"""

strl = "hola"
str2 = "adios"
resultado = ""
encontrado = False

for i in str1:
    encontrado = False
        for j in str2:
            if i = j:
                encontrado = True
                break
    if not encontrado:
        resultado += i

for i in str2:
    encontrado = False
    for j in strl:
        if i = j:
            encontrado = True
            break
    if not encontrado:
        resultado += i

print (resultado, end = '')
