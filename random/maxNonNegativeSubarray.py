def maxNonnegative(arr):
    cs,ms=[],[]
    css,mss=0,0
    for i in range(len(arr)):
        if arr[i] < 0 and css>=mss:
            mss = css
            ms = cs
            cs = []
            css = 0
        elif arr[i]>=0:
            cs.append(arr[i])
            css+=arr[i]
        else:
            cs=[]
            css=0
    if css>mss:
        mss=css
        ms=cs


    return ms


print(maxNonnegative([10, -1, 2, 3, -4, 100]))

