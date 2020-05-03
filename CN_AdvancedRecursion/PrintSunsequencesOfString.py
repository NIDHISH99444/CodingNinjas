def subsequences(arr):
    res=[]
    sub(arr,res,[])
    return res

def sub(arr,res,path):

    if len(arr)==0:
        res.append("".join(path))
        return
    sub(arr[1:],res,path)
    sub(arr[1:], res, path+[arr[0]])

arr="abc"
lst=list(arr)
print(subsequences(lst))