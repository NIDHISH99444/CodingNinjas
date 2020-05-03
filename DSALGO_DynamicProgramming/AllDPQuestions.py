import sys
def maxSumSubarray(arr):
    meh=0
    msf=-sys.maxsize
    for i in range(len(arr)):
        meh+=arr[i]
        if msf<meh:
            msf=meh
        if meh<0:
            meh=0
    return msf

def maximumSumIncreasingSubsequence(arr):
    summ=[]
    for i in range(len(arr)):
        summ.append(arr[i])
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j] and summ[i]<arr[j]+summ[i]:
                summ[i]=summ[i]+arr[j]
    print(max(summ))

def maximumSubsequenceConsecutive(arr):
    maxLen=0
    s=set(arr)
    while len(s)!=0:
        first=last=s.pop()
        while first-1  in s:
            first=first-1
            s.remove(first)
        while last+1  in s:
            last+=1
            s.remove(last)
        maxLen=max(maxLen,last-first+1)
    return maxLen

def maximumSqaureMatrix(matrix):
    newMatrix=[[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]

    for i in range(len(matrix)):
        newMatrix[i][0]=matrix[i][0]
    for j in range(len(matrix[0])):
        newMatrix[0][j]=matrix[0][j]

    for i in range(1,len(newMatrix)):
        for j in range(1,len(newMatrix[0])):
            if matrix[i][j]!=0:
                newMatrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1

    maxVale=0
    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            maxVale=max(maxVale,newMatrix[i][j])
    print(maxVale)

def longestIncreasingSubsequence(arr):
    dp=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp

def longestDecreasingSubsequence(arr):
    dp=[1]*len(arr)
    for i in range(len(arr)-2,-1,-1):
        for j in range(len(arr)-1,i,-1):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp

def longestBitonicSequence(lis,lds):
    maxLen=-1
    for i in range(len(lis)):
        maxLen=max(maxLen,lis[i]+lds[i]-1)
    return maxLen

def editDistance(str1,str2):
    str1=list(str1)
    str2=list(str2)
    matrix=[[0 for i in range(len(str1)+1)]for j in range(len(str2)+1)]
    for i in range(len(str2)+1):
        matrix[i][0]=i
    for j in range(len(str1)+1):
        matrix[0][j]=j

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if str2[i-1]==str1[j-1]:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
    return matrix[-1][-1]

def countNonZeros(n):
    fib=[0]*(n+1)
    fib[0]=0
    fib[1]=2
    fib[2]=3
    for i in range(3,n+1):
        fib[i]=fib[i-1]+fib[i-2]

    print( fib[n])

def reachTopStair(n):
    fib=[0]*(n+1)
    fib[1]=1
    fib[2]=2
    for i in range(3,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    print(fib[n])

def minimumcostPath(matrix):
    n=len(matrix)
    newMatrix=[[0 for i in range(n)]for j in range(n)]
    newMatrix[0][0]=matrix[0][0]
    for i in range(1,n):
        newMatrix[i][0]=matrix[i][0]+newMatrix[i-1][0]
        newMatrix[0][i]=matrix[0][i]+newMatrix[0][i-1]
    for i in range(1,n):
        for j in range(1,n):
            newMatrix[i][j]=min(newMatrix[i-1][j],newMatrix[i][j-1],newMatrix[i-1][j-1])+matrix[i][j]

    print(newMatrix[-1][-1])

def longestCommonSubstring(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    matrix = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for i in range(len(str2) + 1):
        matrix[i][0] = 0
    for j in range(len(str1) + 1):
        matrix[0][j] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if str2[i - 1] == str1[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]+1
            else:
                matrix[i][j] = 0
    print(max([max(rows) for rows in matrix]))

def subsetSum(arr,sum):
    matrix=[[0 for i in range(sum+1)]for j in range(len(arr)+1)]
    for i in range(sum+1):
        matrix[0][i]=False
    for j in range(len(arr)+1):
        matrix[j][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if arr[i-1]>j :
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i-1][j] or matrix[i-1][j-arr[i-1]]
    return matrix[-1][-1]

def countScore(score):
    arr=[0]*(score//2+1)
    arr[0]=1
    arr[1]=1
    arr[2]=2
    for i in range(3,len(arr)):
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3]

    print(arr[-1])

def weightedJobScheduling(intervals):
    intervals=sorted(intervals,key=lambda x:x[1])
    newarr=[0]*len(intervals)
    for i in range(len(newarr)):
        newarr[i]=intervals[i][2]

    for i in range(1,len(intervals)):
        for j in range(i):
            if intervals[j][1]<=intervals[i][0]:
                newarr[i]=max(newarr[i],newarr[j]+intervals[i][2])
    print(max(newarr))

def cuttingRod(price):
    n=len(price)
    matrix=[[0 for i in range(n+2)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+2):
            if i>j :
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-i]+price[i-1])
    print(matrix[-1][-1])

def longestRepeatedSubstring(str):
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
             for y in range(n + 1)]
    res = ""
    res_length = 0
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (str[i - 1] == str[j - 1] and LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1

                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
            else:
                LCSRe[i][j] = 0
    if (res_length > 0):
        for i in range(index - res_length + 1,
                       index + 1):
            res = res + str[i - 1]
    return res

def minimalDeletionCostString(a,b,DeletingCostA,DeletionCostB):
    str1=list(a)
    str2=list(b)
    matrix=[[0 for i in range(len(str2)+1)]for j in range(len(str1)+1)]
    for i in range(len(str1)+1):
        matrix[i][0]=i*DeletingCostA
    for j in range(len(str2)+1):
        matrix[0][j]=j*DeletionCostB
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str1[i-1]!=str2[j-1]:
                matrix[i][j]=min(DeletingCostA+matrix[i-1][j],DeletionCostB+matrix[i][j-1])
            else:
                matrix[i][j]=matrix[i-1][j-1]

    print(matrix[-1][-1])


def countSubsequences(str1,str2):
    str1=list(str1)
    str2=list(str2)
    matrix=[[0 for i in range(len(str2)+1)]for j in range(len(str1)+1)]
    for i in range(len(str1)+1):
        matrix[i][0]=1
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]!=str2[j-1]:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]
    print(matrix[-1][-1])

def coinChange(coins,sum):
    matrix=[sum+1]*(sum+1)
    matrix[0]=0
    for i in range(1,sum+1):
        for c in coins:
            if i>=c:
                matrix[i]=min(matrix[i],matrix[i-c]+1)
    print(matrix[-1])

def longestPallindromicSubsequence(string):
    str=list(string)
    matrix=[[0 for i in range(len(str))]for j in range(len(str))]
    for i in range(len(str)):
        matrix[i][i]=1
    for ls in range(2,len(str)+1):
        for i in range(len(str)-ls+1):
            j=i+ls-1
            if str[i]==str[j]:
                matrix[i][j]=2+matrix[i+1][j-1]
            else:
                matrix[i][j]=max(matrix[i][j-1],matrix[i+1][j])
    print(matrix[0][len(str)-1])

def checkPallindromeMatrix(str):

    str = list(str)
    matrix = [[True for i in range(len(str))] for j in range(len(str))]

    for i in range(len(str)):
        matrix[i][i] = True
    for ls in range(2, len(str) + 1):
        for i in range(len(str) - ls + 1):
            j = i + ls - 1
            if str[i] == str[j]:
                matrix[i][j] = matrix[i + 1][j - 1]
            else:
                matrix[i][j] = False

    return matrix

def CountAllPallindromeSubstring(matrix,str):
    n=len(matrix)
    countMatrix = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(str)):
        countMatrix[i][i] = 1
    for ls in range(2, len(str) + 1):
        for i in range(len(str) - ls + 1):
            j = i + ls - 1
            if matrix[i][j]==True:
                countMatrix[i][j]=1+countMatrix[i][j-1]+countMatrix[i+1][j]-countMatrix[i+1][j-1]
            else:
                countMatrix[i][j] =  countMatrix[i][j-1] + countMatrix[i + 1][j] - countMatrix[i + 1][j - 1]
    print(countMatrix[0][len(str)-1])

def countDistintPallindrome(matrix,str):

    s=set()
    for ls in range(1, len(str) + 1):
        for i in range(len(str) - ls + 1):
            j = i + ls - 1
            if matrix[i][j]==True:
                s.add("".join(str[i:j+1]))
    print(s)

print("Find the maximum sum sub array")
print(maxSumSubarray([-4,-2,-3]))
print("Maximum sum increasing subsequence")
maximumSumIncreasingSubsequence([1, 101, 2, 3, 100, 4, 5])
print("Find the longest subsequence in an array, such that elements in subsequence are consecutive ")
print(maximumSubsequenceConsecutive([1, 9, 3, 10, 4, 20, 2]))
print("Given a Binary matrix, find the largest square sub matrix with all 1's ")
matrix= [[0, 1, 1,], [1, 1, 1], [0, 0, 1]]
maximumSqaureMatrix(matrix)
print("Longest Increasing Subsequence ")
lis=longestIncreasingSubsequence([2,10,11,5,3,4,12,10])
print (max(lis))
print("Longest Decreasing Subsequence")
lds=longestDecreasingSubsequence([2,10,11,5,3,4,12,1])
print(max(lds))
print("Longest Bitonic Susequence")
print(longestBitonicSequence(lis,lds))
print("Edit distance")
print(editDistance("abcdef","azced"))
print("find the number of n-bit integers which don't have any two consequent zeros")
countNonZeros(5)
print("number of ways to reach the top of n-stairs")
reachTopStair(5)
print("Minimum Cost Path ")
matrix=[[1,2,3,4],[4,5,8,3],[1,5,9,2],[6,2,4,3]]
minimumcostPath(matrix)
print("Longest common substring")
longestCommonSubstring("abcdaf","zbcdf")
print("Subset Sum Problem/Partion sum prob(you have check if half sum is there in subset)")
print(subsetSum([2,3,7,8,10],11))
print("Count the number of ways to reach a given score in a game using 2 or 4 or 6 ")
countScore(12)
print("Weighted job scheduling")
weightedJobScheduling([[1,3,5],[2,5,6],[4,6,5],[6,7,4],[7,9,2],[5,8,11]])
print("cutting a rod ")
cuttingRod([2,5,7,8])
print("Longest non-overlapping repeating sub string")
print(longestRepeatedSubstring("aaaaa"))
print("Minimum cost identical string,deleting string with deletion cost x and y")
minimalDeletionCostString("ravi","aibc",1,2)
print("Count the number of times a string occured as a subsequence of other string")
countSubsequences("abbab","ab")
print("coin change ")
coinChange([1,5,6,8],11)
print("Implementation of Longest palindromic subsequence")
longestPallindromicSubsequence("raudar")
print("Count all palindromic substrings in a string")
#https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
#watch above geeksforgeeks video for understanding
str="esass"
x=checkPallindromeMatrix(str)
CountAllPallindromeSubstring(x,str)
print("Count distinct Pallindrome")
countDistintPallindrome(x,str)
print("k pallindrome ")
#kPallindrome(str)
