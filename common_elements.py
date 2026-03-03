"""
/*
Crea una función que reciba dos array, un booleano y retorne un array.
  - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
  - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
  - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def commonElements(array1, array2, bool):
  common_num = []
  not_common_num = []
  if bool:
    #devolver los elementos comunes
    for i in range(len(array1)):
      for j in range (len (array2)):
        if array1[i] == array2[j]:
          if array2[j] not in common_num:
            common_num.append(array2[j])
    return common_num
  else:
    #devolver los elementos no comundes
    for i in array1:
      if i not in array2:
        not_common_num.append(i)

    for i in array2:
      if i not in array1:
        not_common_num.append(i)
    return not_common_num

array1 = [1, 2, 3, 3, 4]
array2 = [2, 2, 3, 3, 3, 4, 6]
bool = True
print (commonElements(array1, array2, bool))
