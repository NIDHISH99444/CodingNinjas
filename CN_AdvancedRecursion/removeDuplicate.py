# Given a string S, remove consecutive duplicates from it recursively.
# Input Format :
# String S
# Output Format :
# Output string
# Constraints :
# 1 <= Length of String S <= 10^3
# Sample Input :
# aabccba
# Sample Output :
# abcba

def removeConsecutiveDuplicates(string):
    if len(string)==0 or len(string)==1:
      return string
    if string[0]==string[1]:
      return removeConsecutiveDuplicates(string[1:])
    else:
      return string[0]+removeConsecutiveDuplicates(string[1:])



print(removeConsecutiveDuplicates("aabccba"))

