def loveForChar(arr):
    hs={}
    for char in ["a","s","p"]:
        hs[char]=0
    for i in range(len(arr)):
        if arr[i] in hs:
            hs[arr[i]]+=1
    for ele in hs.values():
        print(ele,end=" ")
n=int(input())
p=input()
loveForChar(p)

#18
#owbdmvoechwwgunmrt
#6
#vfefgk
#36
#yndatfuqmzctvbyttrsfafmhkavwgqeuyoxo
#3 1 0
