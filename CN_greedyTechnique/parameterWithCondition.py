def parameter(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-2):
        s1=arr[i]
        s2=arr[i+1]
        s3=arr[i+2]
        if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
            print(s3,s2,s1)
            return
    else:
        print("-1")
n=int(input())
arr=list(map(int,input().split()))
parameter(arr)