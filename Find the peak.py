"""
The user enters numbers until entering 0. The program must determine if there is a peak in the sequence.
A peak is a number that is:
- Greater than the previous number
- And greater than the next number
Example:
1,3,2,4,0 --> Hay pico (3)
5,4,3,2,0 --> No hay pico
1,2,3,2,1,0 --> Hay pico (3)
"""
num = None
numbers = []
pico = False
valor_pico = None
while num != 0:
  num int (input ("Introduce un número"))
  if num != 0:
    numbers.append(num)
    
for i in range (1, len (numbers) -1):
  if numbers [i] > numbers [i-1] and numbers [i] > numbers [i+1]:
    valor_pico = numbers [i]
    pico = True
    break
if pico:
  print ("Hay pico (", valor_pico, ")")
else:
  print ("No hay pico")
