def MinimumWindowString(S,T):
    miss=[]
    indices={}
    for i in T :
        miss.append(i)
    for i in T :
        indices[i]=[]
    start=0
    end=len(S)-1
    for i in range(len(S)):
        if S[i] in T :
            if S[i] in miss:
                miss.remove(S[i])
                indices[S[i]].append(i)
            elif S[i] not in miss:
                indices[S[i]].pop(0)
                indices[S[i]].append(i)
        if miss==[]:
            maxVal= max(x[-1] for x in indices.values())
            minVal= min(x[0] for x in indices.values())
            if maxVal-minVal<end-start+1:
                start=minVal
                end=maxVal
    if miss!=[]:
        return -1
    return S[start:end+1]

print(MinimumWindowString("ADOBECODEBANC","ABC"))