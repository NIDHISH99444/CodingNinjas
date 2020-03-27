def subsequences(arr):
    res=[]
    sub(arr,res,[])
    return res

def sub(arr,res,path):
    if len(arr)==0:
        res.append("".join(path))
        return
    sub(arr[1:],res,path+[arr[0]])
    sub(arr[1:], res, path)

arr="abc"
lst=list(arr)
print(subsequences(lst))