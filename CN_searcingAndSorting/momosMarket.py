def momosMarket(arr,amount):
    str=0
    end=len(arr)-1
    while str<=end:
        mid=(str+end)//2
        if arr[mid]<=amount:
            if mid+1<len(arr) and arr[mid]<=amount<=arr[mid+1]:

                print(mid+1,amount-arr[mid])
                return
            elif mid+1==len(arr):
                print(mid+1,amount-arr[mid])
                return
            else:
                str=mid+1
        else:
            end=mid-1
    print(0,amount)

def modifiedArray(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr

n=int(input())
priceMomosEverDay=list(map(int,input().split()))
noOfQueries=int(input())
newArray=modifiedArray(priceMomosEverDay)
for i in range(noOfQueries):
    amountSheHas=int(input())
    momosMarket(newArray,amountSheHas)
# newArray=modifiedArray([3, 3 ,2 ,8 ,5, 8])
# momosMarket(newArray,2)
# 6
# 3 3 2 8 5 8
# 4
# 4
# 2
# 25
# 17