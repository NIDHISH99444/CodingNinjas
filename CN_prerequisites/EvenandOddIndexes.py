def calculatesum(m):
    even,odd=0,0
    for i in range(len(m)):
        if i%2==0 and m[i]%2==0:
            even+=m[i]
        elif i%2!=0 and m[i]%2!=0:
            odd+=m[i]
    return [even,odd]
n=int(input())
m=list(map(int,input().split()))
e,o=calculatesum(m)
print(e,o)

