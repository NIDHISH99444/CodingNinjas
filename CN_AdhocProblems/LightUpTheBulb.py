def lightUpBulb(arr, x, y):
    brk = 0
    if arr[0]==0:
        brk=1
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            brk+=1
    if brk==0:
        return 0
    operation=(brk-1)
    return operation*min(x,y)+y



#totalSize, x, y = list(map(int, input().split()))
#str = input()

str="1001011"
lst = [int(str[i]) for i in range(len(str))]

print(lightUpBulb(lst, 9, 10))