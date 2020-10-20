def intersection (a, b):
    return list(set(a) & set (b))

list1 = []
list2 = []

numOfElements1 = int(input('enter nombre of elements List1 :'))
for i in range(0,numOfElements1):
    element = int(input('enter element' + str(i+1) + ' :'))
    list1.append(element)
numOfElements2 = int(input('enter nombre of elements List2 :'))
for i in range(0,numOfElements2):
    element = int(input('enter element' + str(i + 1) + ' :'))
    list2.append(element)

print ('intersection is :' , intersection (list1, list2))