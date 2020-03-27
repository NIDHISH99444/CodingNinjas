
def removeDuplicates(string):
    i,dict,j=0,{},0
    string=list(string)
    while i<len(string):
        if string[i] not in dict:
            dict[string[i]]=1
            string[j]=string[i]
            j+=1
            i+=1
        else:
            i+=1
    return "".join(string[:j])

print(removeDuplicates("gangaprasad"))