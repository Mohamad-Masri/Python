#pip install matplotlib

from matplotlib import pyplot as plt

player = ['John','Ronaldo','TripleH','Brock']

score = [51,87,45,67]

plt.var(players,score,color = 'green')

plt.title('score card')

plt.xlabel('Players')

plt.ylabel('Runs')

plt.show()
