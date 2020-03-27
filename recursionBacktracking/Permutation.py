def permuteNumber(lst):
    res=[]
    dfs(lst,res,[])
    return res


def dfs(lst,res,path):
    if len(lst)==0:
        res.append(path)
    for i in range(len(lst)):
        dfs(lst[:i]+lst[i+1:],res,path+[lst[i]])

def permuteString(str):
    res=[]
    dfsString(str,res,"")
    return res
def dfsString(str,res,path):
    if len(str)==0:
        res.append(path)
    for i in range(len(str)):
        dfsString(str[:i]+str[i+1:],res,path+str[i])



print(permuteNumber([1,2,3]))

print(permuteString("abc"))
