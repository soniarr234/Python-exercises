"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
num = 5
isPrimeNumber = True

if num <= 1:
    isPrimeNumber = False

for i in range(2, num):
    if num % i = 0:
        isPrimeNumber = False

if isPrimeNumber:
    print("It is a prime number")
else:
    print("It is not a prime number")
