# Python program to print 
# duplicates from a list 
# of integers 
def Repeat(x): 
	_size = len(x) 
	repeated = [] 
	for i in range(_size): 
		k = i + 1
		for j in range(k, _size): 
			if x[i] == x[j] and x[i] not in repeated: 
				repeated.append(x[i]) 
	return repeated 

# Driver Code 
list1 = [10, 20, 30, 20, 20, 30, 40, 
		50, -20, 60, 60, -20, -20] 
print (Repeat(list1)) 
	
# This code is contributed 
# by Sandeep_anand 



#-------------------------------------------------

class Solution(object):
   def findDuplicate(self, nums):
      hare = nums[0]
      tortoise = nums[0]
      while True:
         hare = nums[nums[hare]]
         tortoise = nums[tortoise]
         if hare == tortoise:
            break
      ptr = nums[0]
      while ptr!=tortoise:
         ptr = nums[ptr]
         tortoise = nums[tortoise]
      return ptr
ob1 = Solution()
print(ob1.findDuplicate([3,1,3,4,2]))
