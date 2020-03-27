mp= {0: 1, 2: 1, 3: 0}
mp1={1:0}
def printPath(mp,start,end):
    flag=0
    for key,val in mp.items():
        if val==start:
            flag=1
            break
    if flag==1:
        print(end, end=" ")
        while end!=start:
            print(mp[end],end=" ")
            end=mp[end]

start=1
end=3

printPath(mp1,start,end)