import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-=_+"

all = lower + upper + numbers
lenght = 10
for i in range(10000000):
	password = "".join(random.sample(all,lenght))
	print(password)