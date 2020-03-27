def create(num):
    if num==0:
        return
    create(num-1)
    x=num
    flag=1
    while x :
        val=x%10
        if val!=2 and val!=5:
            flag=0
            break
        x=x//10
    if flag==1:
        print(num)

create(25)