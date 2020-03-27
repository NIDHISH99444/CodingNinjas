def minimumBracketReversal(str):
    stack=[]
    for i in range(len(str)):
       if stack and str[i]=='}':
           if stack[-1]=='{':
               stack.pop()
           else:
               stack.append('}')
       else:
           stack.append(str[i])
    print("final stack",stack)
    unbalanced=len(stack)
    cnt=0
    while stack and stack[-1]=='{':
        cnt+=1
        stack.pop()
    return  unbalanced//2 + cnt%2
print(minimumBracketReversal("}}{{}}{{{}"))
print(minimumBracketReversal("}}}{{}}{{{{}"))