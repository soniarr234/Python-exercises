"""
The user enters numbers until entering a 0.
The program must indicate if the sequence ever goes down and then goes back up.
5,4,3,6,2,0 --> Yes
5,4,3,2,0 --> No
1,3,2,4,0 --> Yes
"""
num = None
numbers = []
direccion_anterior = None
direccion actual = ""
cambio = False

while num != 0:
  num =int (input ("Introduce un número"))
  if num != 0:
    numbers.append(num)

for i in range (len (numbers)-1):
  if numbers [i] < numbers [i+1]:
    direccion_actual = "sube"
  elif numbers [i] > numbers [i+1]:
    direccion_actual = "baja"
  else:
    continue #igual, no importan
  
  if direccion_anterior is None:
    direccion_anterior = direccion_actual
  if direccion_anterior != direccion actual:
    cambio = True
    break
if cambio:
  print ("La secuencia baja y luego sube, o al revés")
else:
  print ("La secuencia no cambia de dirección")
