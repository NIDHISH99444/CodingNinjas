# Python program to find longest contiguous subsequence




def longestSequence(arr):
    n = len(arr)
    s = set()
    ans = 0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)

    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

        # if current element is the starting
        # element of a sequence
        if (arr[i] - 1) not in s:

            # Then check for next elements in the
            # sequence
            j = arr[i]
            while (j in s):
                j += 1

            # update optimal length if this length
            # is more
            ans = max(ans, j - arr[i])
    return ans


# Contributed by: Harshit Sidhwa

n = int(input())
lst = list(map(int, input().split()))
# final=longestSequence([693 ,697, 299 ,662, 290, 288 ,925, 234, 257, 192, 687 ,144 ,142, 710, 66, 955, 321, 629, 989, 621])
final = longestSequence(lst)
print(final)