# def lexicalOrder( n):
#     ans = [i for i in range(1, n + 1)]
#     ans.sort(key=lambda x: str(x))
#     return ans
#
# print(lexicalOrder(24))


def lexicalOrder(n) :
    res = []
    recursion(res, 1, 9, n)
    return res


def recursion( lst, start, end, limit):
    number = start
    while (number <= limit and number <= end):
        lst.append(number)
        recursion(lst, number * 10, number * 10 + 9, limit)
        number += 1
print(lexicalOrder(24))


