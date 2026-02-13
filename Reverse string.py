"""
Create a program that reverses the order of a string of text
without using built-in language functions that do it automatically.
- If we pass it "Hello world", it would return "dlrow olleH"
"""

palabra = "Hello world"
resultado = ""

for letra in palabra:
    resultado = letra + resultado
print (resultado)
