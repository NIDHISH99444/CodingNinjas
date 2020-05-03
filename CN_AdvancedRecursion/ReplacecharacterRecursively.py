
#Given an input string S and two characters c1 and c2, you need to replace every occurrence of character c1 with character c2 in the given string.
# Do this recursively.
# Input Format :
# Line 1 : Input String S
# Line 2 : Character c1 and c2 (separated by space)
# Output Format :
# Updated string
# Constraints :
# 1 <= Length of String S <= 10^6
# Sample Input :
# abacd
# a x
# Sample Output :
# xbxcd

# def replaceChar(inval, old, new):
#     if inval=='':
#         return ''
#     if inval[0] == old:
#         return new + replaceChar(inval[1:], old, new)
#     return inval[0] + replaceChar(inval[1:], old, new)

def replaceChar(string, old, new):
    if len(string)==0:
      return string
    if string[0]==old:
      return new+replaceChar(string[1:],old,new)
    else:
      return string[0]+replaceChar(string[1:],old,new)

res=replaceChar("nid","i","p")
print(res)




