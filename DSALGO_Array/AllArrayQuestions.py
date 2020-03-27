#39 sort nearly sorted array
#36 Find the largest sub array with equal number of 0's and 1's Apprach-2 copy from Ravindra on Vimeo
#28 Find the largest multiple of 3 from Ravindra on Vimeo
#27 Implementation of count number of smaller elements on right of each element in an array from Ravindra on Vimeo

def rearrangeArray_63(arr):
    n=len(arr)
    for i in range(len(arr)):
        arr[i]=arr[i]+((arr[arr[i]])%n)*n

    for i in range(len(arr)):
        arr[i]=arr[i]//n

    print(arr)
def possibleTraingels(arr):
    arr.sort()

    n=len(arr)
    sum=0
    for i in range(0,n-2):
        k=i+2
        for j in range(i+1,n-1):
            while k < n and arr[i]+arr[j]>arr[k]:
                k+=1
            sum+=k-j-1
    return  sum

def nextGreaterNumber(arr):
    arr=list(arr)
    n=len(arr)
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>arr[i-1]:
            break
    if i==0:
        print("not posible")
    val=arr[i-1]
    small=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[small] and arr[j]>val:
            small=j
    arr[i-1],arr[small]=arr[small],arr[i-1]
    x=0
    for j in range(i):
        x=x*10+int(arr[j])
    arr=sorted(arr[i:])
    for j in range(n-i):
        x = x * 10 + int(arr[j])
    print(x)


def waveForm(arr):
    for i in range(0,len(arr),2):
        if i>0 and arr[i]<arr[i-1]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
        if i<len(arr)-1 and arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

    print(arr)

def find2repatingNumber(arr):
    res=[]
    for i in range(len(arr)):
        if arr[abs(arr[i])-1]<0:
            res.append(abs(arr[i]))
        else:
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
    print(res)

def findSubarraywithGivenSum(arr,val):
    hs,sum={},0
    for i in range(len(arr)):
        sum+=arr[i]

        if (sum-val) in hs:
            return arr[hs[sum-val]+1:i+1]
        hs[sum] = i
    return -1


def IfSubArraySum0(arr):
    sum=0
    set1=set()
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==0 or sum in set1:
            return True
        set1.add(sum)
    return False

def EquilibriumIndex(arr):
    rightSum,leftSum=0,0
    for i in range(len(arr)):
        rightSum+=arr[i]
    for i in range(len(arr)):
        rightSum-=arr[i]
        if leftSum==rightSum:
            return i
        leftSum+=arr[i]
    return -1

def sumClosestToZero(arr):
    arr.sort()
    closestSum=100
    lindex=0
    rindex=len(arr)-1
    while lindex<rindex:
        currSum=arr[lindex]+arr[rindex]
        if abs(currSum)<abs(closestSum):
            closestSum=currSum
            finalLindex=lindex
            finalRindex=rindex
        if currSum<0:
            lindex+=1
        else:
            rindex-=1
    return [arr[finalLindex],arr[finalRindex]]

def seperate0and1(arr):
    lft=0
    rgt=len(arr)-1
    while lft<rgt:
        while arr[lft]==0 and lft<rgt:
            lft+=1
        while arr[rgt]==1 and lft<rgt:
            rgt-=1
        arr[lft],arr[rgt]=arr[rgt],arr[lft]
    print(arr)

def  maximumDifference(arr):
    minEle=arr[0]
    maxDiff=arr[1]-arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minEle:
            minEle=arr[i]
        else:
            diff=arr[i]-minEle
            if diff>maxDiff:
                maxDiff=diff
    return maxDiff

def findCandidate(arr):
    majEle=arr[0]
    count=1
    for i in range(1,len(arr)):
        if count==0:
            majEle=arr[i]
            count=1
        elif arr[i]==majEle:
            count+=1
        else:
            count-=1
    return majEle
def majority(arr):
    count=0
    cand=findCandidate(arr)
    for i in range(len(arr)):
        if arr[i]==cand:
            count+=1
    if count>=len(arr)//2:
        return cand
    else:
        return -1
print("08 Implementation of finding the majority element in the given  array ")
print(majority([1, 3, 3, 1,2,3,3]))
print("12 Implementation of maximum difference bw two elements in an array such that larger element has higher index than smaller element")
print(maximumDifference([4,3,10,2,9,1,6]))
print("17 separate 0 and 1 in an array ")
seperate0and1([0,1,0,1,0,0,0,1,1])
print("19 implementation for find the pair in the given array whose sum is closed to zero ")
print(sumClosestToZero([-9,-79,0,69,59,84]))
print("22 Find the equilibrium index in an array")
print(EquilibriumIndex([7,2,1,4,6,4,0]))
print("31 Find a subarray with given sum")
print(findSubarraywithGivenSum([8,5,-2,3,5,-5,7],10))
print(findSubarraywithGivenSum([9,1,2,3,4,5,5,16,17,19],10))
print("33 Find a subarray with given sum is equal to zero ")
print(IfSubArraySum0([4,2,-3,1,6]))
print("46 Find the two repeating elements in a given array ")
print(find2repatingNumber([4, 2, 4, 5, 2, 3, 1]))

print("53 Implementation of sort an array in wave form")
waveForm([20, 10, 8, 6, 4, 2])
print("56 Implementation of next greater number with same set of digits ")
nextGreaterNumber("268765")
print("60 Algorithm for number of possible triangles ")
print(possibleTraingels([7,8,6,10,12,50,14]))
print("63 Rearrange the array so that a[i] becomes a[a[i]] ")
rearrangeArray_63([3, 2, 0, 1])