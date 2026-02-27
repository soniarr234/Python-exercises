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
  else:
    #devolver los elementos no comundes
    for i in range(len(array1)):
      for j in range (len(array2)):
        if array1[i] != array2[j]:
          if array2[j] not in not_common_num:
            not_common_num.append(array2[j])
  print (common_num)
  print (not_common_num)


array1 = [1, 2, 3, 3, 4]
array2 = [2, 2, 3, 3, 3, 4, 6]
bool = True
print (commonElements(array1, array2, bool))
