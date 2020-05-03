from decimal import  Decimal

def maxPoints( A, B):
    maxCount = 0
    for i in range(len(A)):
        x1 = A[i]
        y1 = B[i]
        slopeCount = 0
        duplicate = 1
        currSlope = {}
        for j in range(i + 1, len(A)):
            x2 = A[j]
            y2 = B[j]
            if x1 == x2:
                if y1 == y2:
                    duplicate += 1
                    continue
                else:
                    slope = "inf"
            else:
                slope = Decimal(y2 - y1) / Decimal(x2 - x1)
            if slope not in currSlope:
                currSlope[slope] = 1
            else:
                currSlope[slope] += 1
        for slope in currSlope:
            slopeCount = max(slopeCount, currSlope[slope])
        maxCount = max(slopeCount + duplicate, maxCount)
    return maxCount
pnt=[[0,0],[94911151,94911150],[94911152,94911151]]
a,b=[],[]
for ele in range(len(pnt)):
    a.append(pnt[ele][0])
    b.append(pnt[ele][1])
print(a,b)
print(maxPoints(a,b))