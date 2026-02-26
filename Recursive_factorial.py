"""
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""
def recursiveFactorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * recursiveFactorial(num-1)


print(recursiveFactorial(5))
