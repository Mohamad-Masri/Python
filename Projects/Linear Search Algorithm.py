import random

def linearSearch(li, element):
  for x in range (len(li)):
    if li[x] == element:
      return x
  return -1

def randList(n):
  li = []
  for x in range(n):
    li.append(random.randrange(0, n))

  return li

li = randList(100)
print(linearSearch(li, 43))
print(li)
