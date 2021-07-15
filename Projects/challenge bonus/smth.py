num = int(input("enter the number of letters : "))
array = []
for i in range(num) :
	letter = input("enter a letter : ")
	array.append(letter)

def Repeat(x): 
	_size = len(x) 
	repeated = [] 
	for i in range(_size): 
		k = i + 1
		for j in range(k, _size): 
			if x[i] == x[j] and x[i] not in repeated: 
				repeated.append(x[i]) 
	return repeated 
print("")
print ("The repeated letters are : ", Repeat(array))