
MAX_CHAR = 26

def findFirstNonRepeating():
    inDll=[]
    stream="geeksforgeeksandgeeksquizfor"
    for i in range(len(stream)):
        x=stream[i]

        if x not in inDll:
            inDll.append(x)
        else:
            inDll.remove(x)
        if len(inDll)!=0:
            print(str(inDll[0]),end=" ")





findFirstNonRepeating()

