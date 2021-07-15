import numpy as np
li = []
n = 4

l = 0

t = 0
x = 0
y = 1
for i in range(n):
    l = l + 1
    li = np.append(li, l)

for i in range(len(li)):
    t = li[x]
    x = x + 1
    y = x * y
print(y)
