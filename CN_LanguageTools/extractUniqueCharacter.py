from _collections import defaultdict
def ExtractUniquecharacters(arr):
        hs,res={},[]
        for i in range(len(arr)):
            if arr[i] not in hs:
                res.append(arr[i])
                hs[arr[i]]=1

        print("".join(res))


ExtractUniquecharacters("ababacd")
ExtractUniquecharacters("abcde")