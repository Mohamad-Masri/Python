from random import randint
print (3*"\t",'==========> Ghost game <==========')
brave = True
score = 0

while brave:

    ghost_door = randint(1,3)
    door = input('chose the correct door from 1 to 3 : ')
    door_num=int(door)
    if door_num == ghost_door:
        print (3*'\t','GHOOOOOOOST')
        brave = False
    else :
        print ('No Ghost , Good')
        print ('You enter to the next room')
        score = score+1

print('Run away Ghost behind you')
print ('Game Over! You scored :', score)