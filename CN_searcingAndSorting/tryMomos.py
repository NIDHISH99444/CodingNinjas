# 6
# 3 3 2 8 5 8
# 4
# 4
# 2
# 25
# 17
import sys
n=int(input())
numbers = [int(x) for x in sys.stdin.read().split()]
list1=numbers[0:n]
print("lsit",list1)
q=numbers[n]
print("q",q)
for i in range(q):
    s=int(input())
    print(s)
