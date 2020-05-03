def minWindowsub(s,t):
    miss=[]
    dict={}
    start=0
    end=len(S)-1
    for i in t:
        miss.append(i)
    for j in t:
        dict[j]=[]
    for v,i in enumerate(S):
        if i in t:
            if i in miss:
                miss.remove(i)
                dict[i].append(v)
            elif i not in miss:
                dict[i].pop(0)
                dict[i].append(v)
        if miss==[]:
            minV=min(ele[0] for ele in dict.values())
            maxV=max(ele[-1] for ele in dict.values())
            if maxV-minV<end-start:
                end=maxV
                start=minV
    if miss!=[]:
        return ""
    return s[start:end+1]






S = "ADOBECODEBANCA"
T = "AABC"
print(minWindowsub(S,T))