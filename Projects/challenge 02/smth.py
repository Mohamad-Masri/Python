members = int(input("input the number of members : "))
array1 = []
array2 = []
for i in range(members):
	team1 = int(input("enter weight of player " +"in first team : "))
	array1.append(team1)
	team2 = int(input("enter weight of player " +"in second team : "))
	array2.append(team2)
if str(sum(array1)) > str(sum(array2)) :
	print("Team 1 has an advantage")
else : print("Team 2 has an advantage")
print("total weight of the first team is " + str(sum(array1)))
print("total weight of the second team is " + str(sum(array2)))