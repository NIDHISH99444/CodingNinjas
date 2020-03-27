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




