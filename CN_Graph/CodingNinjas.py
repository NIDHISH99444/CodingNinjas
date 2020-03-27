def codingNinjas(matrix,i,j,word,count):
    if count==len(word):
        return True
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]!=word[count]:
        return False
    temp=matrix[i][j]
    matrix[i][j]='#'
    found=codingNinjas(matrix,i-1   , j-1  ,word,count+1)  \
    or codingNinjas(matrix, i - 1, j    , word, count + 1) \
    or codingNinjas(matrix, i - 1, j + 1, word, count + 1) \
    or codingNinjas(matrix, i    , j + 1, word, count + 1) \
    or codingNinjas(matrix, i + 1, j + 1, word, count + 1) \
    or codingNinjas(matrix, i + 1, j    , word, count + 1) \
    or codingNinjas(matrix, i + 1, j - 1, word, count + 1) \
    or codingNinjas(matrix, i    , j - 1, word, count + 1)
    matrix[i][j]=temp
    return found







matrix=[]
n,m=list(map(int,input().split()))
for i in range(n):
    m=input()
    lst=[char for char in m]
    matrix.append(lst)
word="CODINGNINJA"
#matrix=[['C', 'X', 'D', 'X', 'N', 'X', 'N', 'X', 'N', 'X', 'A'], ['X', 'O', 'X', 'I', 'X', 'G', 'X', 'I', 'X', 'J', 'X']]

def checkString(word,matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==word[0]:
                if codingNinjas(matrix,i,j,word,0):
                    return 1
    return 0


print(checkString(word,matrix))
