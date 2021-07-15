def func(first, last):
  floor = last - first + 1
  array = []
  for i in range(floor):
  	tryy = last * last * 1
  	last = last - 1
  	array.append(tryy)
  print("The volume of the plinth is : " + str(sum(array)))
func(3,5)
