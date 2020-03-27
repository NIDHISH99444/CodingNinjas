def alphaCode(input,size,output):
    output[0]=1
    output[1]=1
    for  i in range(2,size+1):
        if input[i-1]!=0:
            output[i]=output[i-1]
        if input[i-2]*10+input[i-1] <=26:
            output[i]+=output[i-2]
    return output[size]

#output(i)  -->checking i length ka input array

ipt=int(input())
while ipt!=0:


    string=str(ipt)
    size=len(string)
    output=[0]*(size+1)
    arr=[int(string[i]) for i in range(len(string))]
    print(alphaCode(arr,size,output))
    ipt=int(input())