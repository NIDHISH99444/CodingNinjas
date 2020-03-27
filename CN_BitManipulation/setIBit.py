def setIthBit(num,i):

    val=1<<i
    return val | num

def unsetBit(n,k):
    # val=1<<i
    # return  num & ~val
    return (~(1 << k) & n)

def checkPowerOf2(num):
    return num&(num-1)==0

def findFiderstSetBit(num):
    INT_SIZE,i=32,1
    for j in range(INT_SIZE):
        if num & i:
            return i
        else:
            i=i<<1
    return i
def turnOffFirstSetBit(num):
    INT_SIZE,i=32,1
    for j in range(INT_SIZE):
        if num & i:
            return num & ~i
        else:
            i=i<<1
    return i

print(setIthBit(4,1))
print(unsetBit(7,2))
print(checkPowerOf2(16))
print(checkPowerOf2(12))
print(findFirstSetBit(7))
print(turnOffFirstSetBit(12))