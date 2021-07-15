a = int(input("input a : "))
b = int(input("input b : "))
c = int(input("input c : "))

delta = b * b - 4 * a * c

print(delta)

if delta < 0 :
	print("no result")
if delta == 0 :
	x = -b * 2 * a
	print(x)
if delta > 0 :
	x1 = (-b + delta)/2*a
	x2 = (-b - delta)/2*a

	print(x1)
	print(x2)