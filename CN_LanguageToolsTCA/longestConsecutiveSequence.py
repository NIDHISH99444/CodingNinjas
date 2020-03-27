def longestSequence(arr):
    newArr=arr
    arr=set(arr)
    store=-1
    maxI=-1
    while arr:
        first=last=arr.pop()
        while first-1 in arr:
            store=first
            first-=1
            arr.remove(first)
        while last+1 in arr:
            last+=1
            arr.remove(last)
        if last-first+1>maxI:
            maxFirst=first
            maxLast=last
            maxI=last-first+1
    final=[]
    for i in range(maxFirst,maxLast+1):
        final.append(i)
    if len(final)==1:
        return [newArr[0]]
    else:
        return final

n=int(input())
lst=list(map(int,input().split()))
final=longestSequence(lst)
#final=longestSequence([693 ,697, 299 ,662, 290, 288 ,925, 234, 257, 192, 687 ,144 ,142, 710, 66, 955, 321, 629, 989, 621])
for ele in final:
    print(ele)

#10
# 11 13 14 5 4 12 6 8 10 7

# 1
# 568
# 20
# 693 697 299 662 290 288 925 234 257 192 687 144 142 710 66 955 321 629 989 621
# 4
# 5
# 6
# 7
# 8
