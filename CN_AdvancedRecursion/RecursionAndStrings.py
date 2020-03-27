def removeCharacter(string,char):
    if len(string)==0:
        return string
    if string[0]!=char:
        return string[0]+removeCharacter(string[1:],char)
    else:
        return  removeCharacter(string[1:],char)
print(removeCharacter("xacxds","x"))

def replaceCharacter(string,old,new):
    if len(string)==0:
        return string
    if string[0]==old:
        return new+replaceCharacter(string[1:],old,new)
    else:
        return string[0] + replaceCharacter(string[1:], old, new)
print(replaceCharacter("nidhish","i","p"))

def removeDuplicates(string):
    if len(string)==0 or len(string)==1:
        return string
    if string[0]==string[1]:
        return removeDuplicates(string[1:])
    else:
        return string[0]+removeDuplicates(string[1:])

print(removeDuplicates("aabcdeeee"))


def lengthOfString(arr):
    if len(arr)==0:
        return 0
    return 1+lengthOfString(arr[1:])

print(lengthOfString("abcd"))
