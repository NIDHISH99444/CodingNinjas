import  sys
def flip(arr):
    sumA=sum(arr)
    n=len(arr)+1
    matrix=[[0 for i in range(sumA+1)]for j in range(n)]
    for i in range(sumA+1):
        matrix[0][i]=False
    for i in range(0,len(arr)+1):
        matrix[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,sumA+1):
            if arr[i-1]<=j:
                matrix[i][j]=matrix[i-1][j] or matrix[i-1][j-arr[i-1]]
            else:
                matrix[i][j]=matrix[i-1][j]
    res=[]
    res=(matrix[-1])

    mini=sys.maxsize
    for i in range(0,len(res)//2):
        if res[i]==True:
            if sumA-2*i<mini:
                mini=min(mini,sumA-2*i)
    return (mini)


def solve( A):
        sum_ = sum(A)
        sums = [None for i in range(sum_ + 1)]
        sums[sum_] = 0
        print(sums)
        for t in A:
            for i in range(len(sums)):
                n_flips = sums[i]
                new_sum = i - 2*t
                if n_flips is not None and new_sum >= 0:
                    if sums[new_sum] is None:
                        sums[new_sum] = n_flips + 1
                    else:
                        sums[new_sum] = min(sums[new_sum], n_flips + 1)

        if sums[0] is not None and sums[0] < len(A):
            return sums[0]

        for proper_sum in sums[1:]:
            if proper_sum is not None:
                return proper_sum

#print(solve([6,10,15]))
#print(flip([ 2,4,5,6,7,8 ]))


def bulbs(arr, n):
    # To keep track of switch presses so far
    count = 0


    for i in range(n):
       if arr[i]==1 and count%2==0:
           continue
       elif arr[i]==0 and count%2==1:
           continue
       elif arr[i]==0 and count%2==0:
           count+=1
       elif arr[i]==1 and count%2==1:
           count+=1
    return count

#print(bulbs([0,1,1,0,1],5))

def candies(arr):
    canSum=0
    left=[1]*len(arr)
    right=[1]*len(arr)
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            left[i]=left[i-1]+1
    for j in range(len(arr)-2,-1,-1):
        if arr[j]>arr[j+1]:
            right[j]=right[j+1]+1

    for i in range(len(arr)):
        canSum+=max(left[i],right[i])

    return canSum

#print(candies([1,5,2,1]))


def seats( A):
    lst=[]
    for i in range(len(A)):
        if A[i]=='x':
            lst.append(i)
    med=len(lst)//2
    lc,rc=0,0
    for i in range(med,-1,-1):
        lc+=lst[med]-lst[i]-(med-i)
    for j in range(med+1,len(lst)):
        rc+=lst[j]-lst[med]-(j-med)
    return lc+rc%10000003
#print(seats("...x..xx...x.x"))


def majorityEle(arr):
    majEle=-1
    cnt=0
    for i in range(len(arr)):
        if cnt==0:
            majEle=arr[i]
            cnt=1
        elif arr[i]==majEle:
            cnt+=1
        else:
            cnt-=1
    return majEle



arr=[1,2,1,2,2]
#print(majorityEle(arr))

def gasStation(gas,cost):
    sum,diff,newSum=0,0,0
    start=0
    for i in range(len(gas)):
        sum=gas[i]-cost[i]
        if sum<0:
            diff+=sum
            start=i+1
        else :
            newSum+=sum
        sum=0
    if newSum+diff>=0:
        return start
    else:
        return 1
A=[ 959, 329, 987, 951, 942, 410, 282, 376, 581, 507, 546, 299, 564, 114, 474, 163, 953, 481, 337, 395, 679, 21, 335, 846, 878, 961, 663, 413, 610, 937, 32, 831, 239, 899, 659, 718, 738, 7, 209 ]
B=[ 862, 783, 134, 441, 177, 416, 329, 43, 997, 920, 289, 117, 573, 672, 574, 797, 512, 887, 571, 657, 420, 686, 411, 817, 185, 326, 891, 122, 496, 905, 910, 810, 226, 462, 759, 637, 517, 237, 884 ]
#print(gasStation(A,B))


def assingMouseHole(mouse,hole):
    maxDiff=-1
    mouse.sort()
    hole.sort()
    for i in range(len(mouse)):
        maxDiff=max(abs(mouse[i]-hole[i]),maxDiff)
    return maxDiff

#print(assingMouseHole([-10, -79, -79, 67, 93, -85, -28, -94 ],[-2, 9, 69, 25, -31, 23, 50, 78]))

import heapq
def KthSmallestEle(arr,k):
    heap=[]
    for i in range(len(arr)):
        heapq.heappush(heap,-1*arr[i])
        if len(heap)>k:
            heapq.heappop(heap)
    print(-heapq.heappop(heap))

#KthSmallestEle([10,3,9,5,12,14],4)

def klargest(arr,k):
    heap=[]
    for i in range(len(arr)):
        heapq.heappush(heap,arr[i])
        if len(heap)>k:
            heapq.heappop(heap)
    while heap:
        print(heapq.heappop(heap))

#klargest([10,3,9,5,12,14],4)


def multiple(A):
    flag=True
    i=1
    validSet=set('01')

    while flag:
        num=A*i
        newFlag=True
        for ele in str(num):
            if ele not in validSet:
                newFlag=False
                break
        if newFlag==False:
            i+=1
        else:
            return num


# Driver code
n =12
print(multiple(n))



def multiple1(A):
    flag = False
    i = 1
    while (flag != True):

        # s = str(A)
        # print(s)
        # print(A)
        result = A * i

        # method returns smallest
        # multiple which has
        # binary digits
        allowed_chars = set('01')
        validationString = str(result)
        if set(validationString).issubset(allowed_chars):
            flag = True;
            break;
        else:
            i = i + 1

    return validationString


# Driver code
n = 54
print(multiple1(n))

# This code is contributed
# by HARDY_123



