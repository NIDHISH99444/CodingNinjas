#You are given a string of 0’s and 1’s you have to find the number of substrings in the string which starts and end with a 1.


def count(n):
    cnt=0
    for i in range(len(n)):
        if n[i]=='1':
            cnt+=1
    return ((cnt)*(cnt-1))//2


s="100101"
print(count(s))