def findPlatform(arr,dep):
    arr.sort()
    dep.sort()
    i,j=1,0
    platform=1
    n=len(arr)
    maxCount=0
    while i<n and j<n:
        if arr[i]<dep[j]:
            platform+=1
            i+=1
            if maxCount<platform:
                maxCount=platform
        else:
            platform-=1
            j+=1
    return maxCount





arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print("total no of platform ",findPlatform(arr,dep))