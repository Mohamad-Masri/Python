import numpy as np
import matplotlib.pyplot as plt
import math

x1 = np.array([1]).reshape(-1,1)
y1 = np.array([6]).reshape(-1,1)

x2 = np.array([4]).reshape(-1,1)
y2 = np.array([3]).reshape(-1,1)

xtarget = np.array([2.5]).reshape(-1,1)
ytarget = np.array([5]).reshape(-1,1)

plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.scatter(xtarget, ytarget)

lengh1 = math.sqrt((x1[0] - xtarget[0])**2 + (y1[0] - ytarget[0])**2)
lengh2 = math.sqrt((x2[0] - xtarget[0])**2 + (y2[0] - ytarget[0])**2)

print(lengh1)
print(lengh2)

if lengh1 < lengh2 :
    print("classifier 1")
else :
    print("classifier 2")
#plt.plot(np.linspace(0,70,100).reshape(-1,1), model.predict(np.linspace(0,70,100).reshape(-1,1)), 'r')

#plt.ylim(0, 10)
plt.show()
