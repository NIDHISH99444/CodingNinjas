def tellThePosition(lst):
    lst=sorted(lst, key=lambda x: (-x[1],x[2]))
    count=1
    for ele in lst:
        print(count,ele[0])
        count+=1


if __name__ == "__main__":
    n=int(input())
    res=[]
    for i in range(n):
        name,marks1,marks2,marks3=input().split()
        res.append([name,int(marks1)+int(marks2)+int(marks3),i])
    tellThePosition(res)

#
# Mohit 94 85 97
# Shubham 93 91 94
# Rishabh 95 81 99