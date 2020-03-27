def repeatingNames(arr):
    hs={}
    for ele in arr:
        if ele not in hs:
            hs[ele]=1
        else:
            hs[ele]+=1
    for ele in arr:
        if hs[ele] ==1 :
            del hs[ele]
    return (hs)

#
# n=[ele for ele in input().split()]
# repeatingNames(n)
# #Abhishek harshit Ayush harshit Ayush Iti Deepak Ayush Iti
names=input().strip().split()
m=repeatingNames(names)

if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)