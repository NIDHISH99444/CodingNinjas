def lootHouse(arr):
    if len(arr)==1:
        return arr[0]
    elif len(arr)==2:
        return max(arr[0],arr[1])
    else:
        newArray[0]=arr[0]
        newArray[1]=max(newArray[0],newArray[1])
        for i in range(2,len(newArray)):
            newArray[i]=max(newArray[i-2]+arr[i],newArray[i-1])
    return newArray[-1]


n=int(input())
arr=list(map(int,input().split()))
#arr=[5,5,10,100,10,5]
newArray=[0]*(len(arr))
print(lootHouse(arr))