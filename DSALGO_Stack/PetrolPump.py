def petrolPump(fuel,distance):
    sum,difference=0,0
    start=0
    for i in range(len(fuel)):
        sum+=fuel[i]-distance[i]
        if sum<0:
            difference+=sum
            sum=0
            start+=1
    if sum+difference>=0:
        return start
    return -1
print(petrolPump([1,2,3,4,5],[3,4,5,1,2]))
print(petrolPump([2,3,4],[3,4,3]))