def powerSet(str,index,curr):
    if len(str)==index:
        print(curr,end=" ")
        return
    powerSet(str,index+1,curr+str[index])
    powerSet(str, index + 1, curr)



powerSet("abc",0,"")

