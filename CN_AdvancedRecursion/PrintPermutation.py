def printPermutation(string):
    res=[]
    printPerm(string,res,[])
    return res

def printPerm(string,res,path):
    if len(string)==0:
        res.append("".join(path))
    for i in range(len(string)):
        printPerm(string[:i]+string[i+1:],res,path+[string[i]])


print(printPermutation("abc"))
