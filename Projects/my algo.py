#my algo : 10 element array's, 1 input => output = 2 arrays : 1 for the first array's elements less than input, seconf for the first array's elements greater than input.

import numpy as np

li = [1,2,4,5,6,7,8,9,10]

less = []
greater = []

n = 0


for i in range(len(li)):
    x = li[n]
    n = n + 1

    if x > 5 :
        less = np.append(less, x)
    else:
        greater = np.append(greater, x)

print(greater)
print(less)


