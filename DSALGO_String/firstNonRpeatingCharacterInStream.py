from _collections import deque
def firstNonRepeating(string):
    dict=[0]*26
    q=deque()
    for i in range(len(string)):
        dict[ord(string[i])-ord('a')]+=1
        q.append(string[i])
        while len(q)!=0:
            if dict[ord(q[0])-ord('a')]>1:
                q.popleft()
            else:
                print(q[0],end=" ")
                break
        if len(q)==0:
            print("-1",end=" ")
    print()
firstNonRepeating("aabc")
firstNonRepeating("aac")


