def longestPrefixSuffixCode(str):
    i=1
    j=0
    lcs=[0]*len(str)
    while i<len(str):
        if str[i]==str[j]:
            lcs[i]=j+1
            i+=1
            j+=1
        elif j!=0:
            j=lcs[j-1]
        else:
            lcs[i]=0
            i+=1
    return lcs
def KMP(text,pattern,lcs):
    i,j=0,0
    while i<len(text) and j<len(pattern):
        if text[i]==pattern[j]:
            i+=1
            j+=1
        elif j!=0:
            j=lcs[j-1]
        else:
            i+=1
    if j==len(pattern):
        return True
    return False
lcs=longestPrefixSuffixCode("AABA")
print(KMP("AABAAC","AABA",lcs))