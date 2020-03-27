def Slowlcs(str1,str2):
    if len(str1)==0 or len(str2)==0:
        return 0
    if str1[0]==str2[0]:
        return 1+Slowlcs(str1[1:],str2[1:])
    else:
        return max(Slowlcs(str1[1:],str2),Slowlcs(str1,str2[1:]))


def lcsI(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    print(dp)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[m][n]
#print(Slowlcs("abcd","123"))

string1=input()
string2=input()
print(lcsI(string1,string2))
