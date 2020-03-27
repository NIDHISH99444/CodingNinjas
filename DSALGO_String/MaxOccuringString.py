ASCII_SIZE = 26
def getMaxOccuringChar(str): 
    count=[0]*26
    for i in range(len(str)):
        count[ord(str[i])-ord("a")]+=1
    max=-1
    c=""
    for i in str:
        if max<count[ord(i)-ord("a")]:
            max=count[ord(i)-ord("a")]
            c=i
    return c

str = "ravindraaa"
print(getMaxOccuringChar(str))


