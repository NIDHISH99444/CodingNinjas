def warmReception(arrival,departure):
    arrival.sort()
    departure.sort()
    res=0
    i,j=1,0
    count=1
    while i<len(arrival) and j < len(departure):
        if arrival[i]<=departure[j]:
            count+=1
            i+=1
            res=max(res,count)
        else:
            count-=1
            j+=1
    return res




arrival=list(map(int,input().split()))
departure=list(map(int,input().split()))
print(warmReception(arrival,departure))

# 8
# 307 2007 1736 2314 2101 1719 435 2214
# 400 2100 1800 2359 2200 1800 500 2300
# 10
# 1700 1607 2212 605 605 1 1002 127 2304 1013
# 1900 1900 2300 1800 1700 500 1100 1000 2359 1100
# 9
# 1708 1607 2012 605 605 101 1002 127 2304
# 1900 1800 2300 1800 1700 1500 1200 1200 2359
# 10
# 1708 1607 2212 605 605 101 1002 127 2304 1013
# 1900 1900 2300 1800 1700 1500 1200 1200 2359 1200
# 2,4,5,6