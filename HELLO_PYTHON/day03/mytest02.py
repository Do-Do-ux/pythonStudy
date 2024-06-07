#야구 
#com 327
#숫자를 맞춰보세요 321
#321 - 2S0B
#327 - 3S0B
#271 - 0S2B



from random import randint
arr = []
for i in range(1,9+1) :
    arr.append(i)


for i in range(10000):
    rand = randint(0,len(arr)-1)
    a = arr[0]
    arr[0] = arr[rand]
    arr[rand] = a

arr2 = [arr[0],arr[1],arr[2]]
#print(arr2)

while True:
    strike = 0
    ball = 0
    human = input("숫자를 맞춰보세요")
    words = list(human)
    list_a = [int (i) for i in words]
    if arr2[0] == list_a[0]:
        strike += 1
    if arr2[1] == list_a[1]:
        strike += 1
    if arr2[2] == list_a[2]:
        strike += 1
    if arr2[0] == list_a[1] or arr2[0] == list_a[2] :
        ball += 1
    if arr2[1] == list_a[0] or arr2[1] == list_a[2] :
        ball += 1
    if arr2[2] == list_a[1] or arr2[2] == list_a[0] :
        ball += 1
        
    print("{} - {}S{}B".format(human,strike,ball))
    
    if strike == 3:
        print("스트라이크! OUT!")
        break
        

    
    