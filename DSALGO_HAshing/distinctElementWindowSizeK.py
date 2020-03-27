from collections import defaultdict
def findDistinctElementWindowK(arr,k):
    mp=defaultdict(lambda :0)
    dist_count=0
    for i in range(k):
        if mp[arr[i]]==0:
            dist_count+=1
        mp[arr[i]]+=1
    print(dist_count,end=" ")
    for i in range(k,len(arr)):
        if mp[arr[i-k]]==1:
            dist_count-=1
        mp[arr[i - k]]-=1
        if mp[arr[i]]==0:
            dist_count+=1
        mp[arr[i]]+=1
        print(dist_count,end=" ")

findDistinctElementWindowK([1, 2, 1, 3, 4, 2, 3],4)