def reverseWord(string):
    res,word="",[]
    for i in range(len(string)):
        if string[i]!=' ':
            res+=string[i]
        else:
            if len(res)>0:
                word.append(res)
                res=""
    if len(res)>0:
        word.append(res)
    return " ".join(word[::-1])

def reverse(word):
    return word[::-1]
print(reverseWord("the sky is blue "))
print(reverse(["h","e","l","l","o"]))