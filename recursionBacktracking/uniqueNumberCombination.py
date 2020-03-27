
def printArray(p, n):
    for i in range(0, n):
        print(p[i], end=" ")
    print()


def printAllUniqueParts(n):
    p = [0] * n  # An array to store a partition
    k = 0  # Index of last element in a partition
    p[k] = n  # Initialize first partition
    # as number itself

    while True:

        printArray(p, k + 1)


        rem_val = 0
        while k >= 0 and p[k] == 1:
            rem_val += p[k]
            k -= 1


        if k < 0:
            print()
            return


        p[k] -= 1
        rem_val += 1
        while rem_val > p[k]:
            p[k + 1] = p[k]
            rem_val = rem_val - p[k]
            k += 1

        p[k + 1] = rem_val
        k += 1



print('All Unique Partitions of 3')
printAllUniqueParts(3)


