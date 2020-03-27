def subStringSum(arr):
    total=arr[0]
    last=arr[0]
    for i in range(1,len(arr)):
        last=last*10+arr[i]*(i+1)
        total+=last
    return total


#formula = (last)*10+(value at i)*(index+1)
string="123"

arr=[int(ele) for ele in string]
print(subStringSum(arr))