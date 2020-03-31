def patternMatch(s,p):
    n=len(s)
    m=len(p)
    for i in range(n-m+1):
        isFound=True
        for j in range(m):
            if s[i+j]!=p[j]:
                isFound=False
                break
        if isFound==True:
            return True
    return False



#time complexity -->O(n*m)

print(patternMatch("bcdcbc","bcd"))