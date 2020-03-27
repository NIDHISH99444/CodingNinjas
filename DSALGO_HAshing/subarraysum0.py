def subarraySumZero(arr):
    set1=set()
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==0 or sum in set1:
            return True
        set1.add(sum)
    return False

print(subarraySumZero([4, 2, -3, 1, 6]))
