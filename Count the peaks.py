"""
The user enters numbers until they enter 0.
The program must determine how many peaks there are in the sequence.
A peak is a number that is:
- Greater than the previous number
- And greater than the next number
Example:
1, 5, 2, 6, 3, 4, 0 --> There are 2 peaks (5, 6)
5, 4, 3, 2, 0 --> There is no peak
1, 2, 3, 2, 1, 0 There is 1 peak (3)
"""
num = None
numbers = [ ]
valor_pico = []
num_picos = 0

while num != 0:
  num int (input ("Introduce un número"))
  if num != 0:
    numbers.append(num)

for i in range (1, len (numbers)-1):
  if numbers [i] > numbers [i-1] and numbers [i] > numbers [i+1]:
    valor_pico.append(numbers [i])
    num picos += 1

if num_picos > 0:
  if num_picos = 1:
    print ("Hay", num_picos, "pico (", valor_pico, ")")
  else:
    print ("Hay", num_picos, "picos (", valor_pico, ")")
else:
  print ("No hay picos")
