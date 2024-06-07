arr = [1,2,3]

for i in range(3):
    for j in range(3):
        if arr[i] < arr[j]:
            a = arr[i]
            arr[i] = arr[j]
            arr[j] = a
print(arr)