def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0
    i = 1
    res=[]
    while i <= n:

        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == sum:
            res=[arr[start],arr[i-1]]
            return [res,"true"]

        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    return "false"


n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))
res,output=subArraySum(lst, n, m)
if output=="true":
    print(output)
    for ele in res:
        print(ele,end=" ")
else:
    print(output)



