def knows(a,b):
    return matrix[a][b]
def celebrity(n):
    a=0
    b=n-1
    while a<b :
        if knows(a,b):
            a+=1
        else:
            b-=1
    for i in range(n):
        if i!=a and (knows(a,i) or not knows(i,a)):
            return -1
    return a





matrix=[[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
print(celebrity(len(matrix)))