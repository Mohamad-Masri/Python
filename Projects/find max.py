li = [1,2,2,5,9,8]
n = 0

t = 0

for i in range(len(li)):
  
  x = li[n]
  n = n + 1

  if x > t :
     t = x
     print(t)