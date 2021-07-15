maxX = 0
maxY = 0
minX = float('inf')
minY = float('inf')

numberOfHouse = int(input("Enter the number of houses : "))

for i in range(numberOfHouse) :

	inputX = int(input("Input the X position of the next house : "))
	inputY = int(input("Input the Y position of the next house : "))

	if inputX < minX :
		minX = inputX
	if inputY < minY :
	 	minY = inputY
		 	
	if inputX > maxX :
		maxX = inputX
	if inputY > maxY :
		maxY = inputY

height = maxY - minY
width = maxX - minX
perimeter = 2 * height + 2 * width

print(perimeter)