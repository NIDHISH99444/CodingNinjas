

def removeConsecutiveDuplicates(string):
    if len(string)==0 or len(string)==1:
      return string
    if string[0]==string[1]:
      smallout=removeConsecutiveDuplicates(string[1:])
      return smallout
    else:

      smallout=removeConsecutiveDuplicates(string[1:])
      return string[0]+smallout


print(removeConsecutiveDuplicates("aabccba"))

