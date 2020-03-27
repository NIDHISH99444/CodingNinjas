from _collections import deque
def firstNonRepeating(string):
    dict=[0]*26
    q=deque()
    for i in range(len(string)):
        dict[ord(string[i])-ord('a')]+=1
        if dict[ord(string[i]) - ord('a')]==1:
            q.append(string[i])

        if dict[ord(q[0])-ord('a')]>1:
            q.popleft()

    if len(q)==0:
        print("-1")
    else:
        print(q[0])

firstNonRepeating("aabc")
firstNonRepeating("aacc")
firstNonRepeating("aba")


