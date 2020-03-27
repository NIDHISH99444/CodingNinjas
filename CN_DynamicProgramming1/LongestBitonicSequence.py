def longestBitonicSequence(arr):
        #calculating longest increasing sequence
        newArr = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    newArr[i] = max(newArr[i], newArr[j] + 1)
        #calculating longest decreasing sequence
        newArr1 = [1] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            for j in range(len(arr) - 1, i, -1):
                if arr[i] > arr[j]:
                    newArr1[i] = max(newArr1[i], newArr1[j] + 1)

        maxVal=0
        for i in range(len(newArr)):
            maxVal=max(maxVal,newArr[i]+newArr1[i]-1)
        return maxVal


n=int(input())
lst=list(map(int,input().split()))
print(longestBitonicSequence(lst))