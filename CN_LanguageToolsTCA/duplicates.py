def duplicates(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])+1]<0:
            return abs(arr[i])
        else:
            arr[abs(arr[i] )+1]=-arr[abs(arr[i])+1]

print(duplicates([0, 7, 2 ,5 ,4 ,7 ,1, 3 ,6]))