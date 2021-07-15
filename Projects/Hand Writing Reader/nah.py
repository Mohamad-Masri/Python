from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('database/0.jpeg'))
hash1 = imagehash.average_hash(Image.open('database/1.jpeg')) 
hash2 = imagehash.average_hash(Image.open('database/2.jpeg')) 
hash3 = imagehash.average_hash(Image.open('database/3.jpeg')) 
hash4 = imagehash.average_hash(Image.open('database/4.jpeg')) 
hash5 = imagehash.average_hash(Image.open('database/5.jpeg')) 
hash6 = imagehash.average_hash(Image.open('database/6.jpeg')) 
hash7 = imagehash.average_hash(Image.open('database/7.jpeg')) 
hash8 = imagehash.average_hash(Image.open('database/8.jpeg')) 
hash9 = imagehash.average_hash(Image.open('database/9.jpeg')) 
test = imagehash.average_hash(Image.open('test.png'))
cutoff = 10

if hash0 - test < cutoff:
  print('number is 0')
elif hash1 - test < cutoff:
  print('number is 1')
elif hash2 - test < cutoff:
  print('number is 2')
elif hash3 - test < cutoff:
  print('number is 3')
elif hash4 - test < cutoff:
  print('number is 4')
elif hash5 - test < cutoff:
  print('number is 5')
elif hash6 - test < cutoff:
  print('number is 6')
elif hash7 - test < cutoff:
  print('number is 7')
elif hash8 - test < cutoff:
  print('number is 8')
elif hash9 - test < cutoff:
  print('number is 9')
else:
	print("please write a clear number")