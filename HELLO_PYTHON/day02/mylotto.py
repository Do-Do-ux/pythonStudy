from random import random, randint

arr = [1,2,3,4,5]
for i in range(10000):
    rand = randint(0,len(arr)-1)
    a = arr[0]
    arr[0] = arr[rand]
    arr[rand] = a
print(arr[0],arr[1])





