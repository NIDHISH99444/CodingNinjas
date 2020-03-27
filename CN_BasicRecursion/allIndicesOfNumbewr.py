def allIndexes(arr,x,res=[],count=0):
    if len(arr)==0:
        return

    if arr[0]==x:
        res.append(count)
    #count+=1
    allIndexes(arr[1:],x,res,count+1)
    return res
n=int(input())
inputArray=list(map(int,input().split()))
eleToSearch=int(input())
res=allIndexes(inputArray,eleToSearch)
for ele in res:
    print(ele,end=" ")