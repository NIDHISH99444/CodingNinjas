def TwoSetDisjoint(a,b):
    set1=set()
    for i in range(len(a)):
        set1.add(a[i])
    for j in range(len(b)):
        if b[j] in set1:
            return False
    return True


print(TwoSetDisjoint([10, 5, 3, 4, 6],[8, 7, 9]))