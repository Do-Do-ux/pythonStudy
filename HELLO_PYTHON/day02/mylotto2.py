from random import random, randint

arr = []
for i in range(1,45+1):
    arr.append(i)
print(arr)
for i in range(10000):
    rand = randint(0,len(arr)-1)
    a = arr[0]
    arr[0] = arr[rand]
    arr[rand] = a
    
for i in range(0,6):
    print(arr[i],end=" ")
    
    
#print("Lotto:",arr[0],arr[1],arr[3],arr[4],arr[5],arr[6])





