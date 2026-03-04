"""
Crea una función que ordene y retorne una matriz de números.
  - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""
def orderList (list_nums, order):
  temp = 0
  for i in range(len(list_nums)):
    for j in range (i+1, len(list_nums)):
      if order == "Asc" and list_nums[i] > list_nums[j]:
        temp = list_nums[i]
        list_nums[i] = list_nums[j]
        list_nums[j] = temp
        #Esta forma de intercambiar valores de forma asincrona solo lo hace python
        #list_nums[i], list nums[i] = list_nums[i], list_nums[i]
      elif order == "Desc" and list_nums[i] < list_nums[j]:
        print()
        temp = list_nums[j]
		list_nums[j] = list_nums[i]
        list_nums[i] = temp
        # Esta forma de intercambiar valores de forma asincrona solo lo hace python
        #list_nums[il, list nums[i] = list_nums[i], list_nums[i]
  
  print(list_nums)


print (orderList([4, 2, 8, 6, 9], "Desc"))
