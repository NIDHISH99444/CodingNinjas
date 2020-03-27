def raiCoinBoxes(startIndex,endIndex,n,k):
    start=[0]*(n+1)
    end=[0]*(n+1)

    for i in range(k):
        start[startIndex[i]]+=1
    for j in range(k):
        end[endIndex[j]]+=1

    buffer=[0]*(n+1)
    buffer[1]=start[1]
    for i in range(2,n):
        buffer[i]=start[i]-end[i-1]+buffer[i-1]

    coin=[0]*(n+1)
    for i in range(1,n):
        coin[buffer[i]]+=1      

    for i in range(n-2,-1,-1):
        coin[i]+=coin[i+1]
    return coin
def returnCoins(coin,case):
    return coin[case]

n=int(input())
k=int(input())
startArray,endArray=[],[]
for i in range(k):
    start,end=list(map(int,input().split()))
    startArray.append(start)
    endArray.append(end)
coinArray=raiCoinBoxes(startArray,endArray,n,k)
print(coinArray)
testCases=int(input())
while testCases>0:
    case=int(input())
    print(returnCoins(coinArray,case))
    testCases-=1