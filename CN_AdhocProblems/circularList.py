def Finallist(start,p):
        return (start+p)%12


n=int(input())
for i in range(n):
    start,p=list(map(int,input().split()))
    print(Finallist(start,p))
