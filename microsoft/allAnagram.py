from collections import Counter
def allAnagram(string,cmpString):
    newString=Counter(cmpString)
    print(newString)
    finalString=Counter(string[:len(cmpString)-1])
    print(finalString)
    res=[]
    for i in range(len(cmpString)-1,len(string)):
        if string[i] not in finalString:
            finalString[string[i]]=1
        else:
            finalString[string[i]]+=1
        if finalString==newString:
            res.append(i-len(newString)+1)
        finalString[string[i-len(cmpString)+1]]-=1
        if finalString[string[i-len(cmpString)+1]]==0:
            del finalString[string[i-len(cmpString)+1]]
    return  res

print(allAnagram("abab","ab"))