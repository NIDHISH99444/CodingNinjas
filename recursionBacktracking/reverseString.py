def reverseString(str):
    if len(str)==0:
        return
    reverseString(str[1:])
    print(str[0],end="")

def checkPallindrome(str,newString):

    if len(str)==0:
        return ""
    # temp=str[0]
    # val=checkPallindrome(str[1:],newString)
    # newString+=val+temp
    # return newString
    return checkPallindrome(str[1:],newString)+str[0]


strcheck="mtld"
newString=checkPallindrome(strcheck,"")
print(newString)
print(newString==strcheck)

print()
reverseString("abcd")

