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
